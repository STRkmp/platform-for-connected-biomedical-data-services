from django.http import HttpResponse
from common.dto.RequestForServiceMessage import RequestForServiceMessage
from common.utils.minio_utils import get_object_from_minio
from common.publisher.publisher import publish_message
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import ProcessingService, DiagnosisRequest, UploadedFile
from .serializers import DiagnosisRequestSerializer, ProcessingServiceSerializer, FeedbackSerializer
from .upload import upload_file
from django.http import FileResponse

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_diagnosis_request(request):
        print(request)
        # Получение пользователя из запроса
        user = request.user

        # Получение service_id из header
        service_id = request.headers.get('Service-id')

        # Получение объекта ProcessingService по service_id
        service = ProcessingService.objects.get(id=service_id)

        # Получение файла из запроса
        file = request.data.get('file')

        # Получение пациента и жалоб из запроса
        patient_id = request.data.get('patient_id')
        complaints = request.data.get('complaints')

        uploaded_file = upload_file(file, user.id)

        serializer = DiagnosisRequestSerializer(data={
            'user': user.id,
            'status': 'created',
            'service': service.id,
            'uploaded_file': uploaded_file.id,
            'patient': patient_id,
            'complaints': complaints
        })

        if serializer.is_valid():
            instance = serializer.save()
            request_id = instance.id

            message = RequestForServiceMessage(request_id, uploaded_file.full_path)
            publish_message(message, service.name)

            return Response({'status': 'success'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_processing_services(request):
    try:
        services = ProcessingService.objects.all()
        serializer = ProcessingServiceSerializer(services, many=True)
        data = serializer.data
        # Удаляем поле 'health_check_url' из каждого объекта

        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_requests(request):
    try:
        # Получение пользователя из запроса
        user = request.user

        # Фильтрация запросов по пользователю
        user_requests = DiagnosisRequest.objects.filter(user=user)

        # Получение service_id из header
        service_id = request.headers.get('Service-id')
        if service_id is not None:
            user_requests = user_requests.filter(service_id=service_id)

        # Сериализация результатов
        serializer = DiagnosisRequestSerializer(user_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_file(request):
    try:
        # Получение пользователя из запроса
        user = request.user

        file_id = request.headers.get('File-id')
        request_id = request.headers.get('Request-id')

        request_from_db = None

        if file_id:
            request_from_db = DiagnosisRequest.objects.get(result_file=file_id, user=user)
        elif request_id:
            request_from_db = DiagnosisRequest.objects.get(id=request_id, user=user)

        if not request_from_db:
            raise Exception('No diagnosis requested')

        if not request_from_db.result_file or request_from_db.status == 'error' or request_from_db.status == 'created':
            raise Exception('No diagnosis requested or result is not ready')

        file = UploadedFile.objects.get(id=request_from_db.result_file.id)

        file_from_minio = get_object_from_minio(file.full_path)

        response = HttpResponse(file_from_minio, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{file.name}"'
        response["Access-Control-Expose-Headers"] = "Content-Disposition"

        return response
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_report(request):
        print(request)
        # Получение пользователя из запроса
        user = request.user

        # Получение service_id из header
        request_id = request.headers.get('Request-id')

        # Получение объекта ProcessingService по service_id
        request_from_db = DiagnosisRequest.objects.get(id=request_id, user=user)

        if (request_from_db.status == 'created'):
            return Response({'status': 'error', 'error': "Запрос ещё не обработался."}, status=status.HTTP_400_BAD_REQUEST)

        # Получение пациента и жалоб из запроса
        comment = request.data.get('comment')

        serializer = FeedbackSerializer(data={
            'request': request_from_db.id,
            'comment': comment
        })

        if serializer.is_valid():
            instance = serializer.save()
            request_id = instance.id

            return Response({'status': 'success', 'request_id': request_id}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)