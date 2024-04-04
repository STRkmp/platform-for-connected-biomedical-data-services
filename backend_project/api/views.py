from common.dto.RequestForServiceMessage import RequestForServiceMessage
from common.publisher.publisher import publish_message
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import ProcessingService, DiagnosisRequest
from .serializers import DiagnosisRequestSerializer, ProcessingServiceSerializer
from .upload import upload_file
import uuid


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_diagnosis_request(request):
    try:
        # Получение пользователя из запроса
        user = request.user

        # Получение service_id из header
        service_id = request.headers.get('Service-id')

        # Получение объекта ProcessingService по service_id
        service = ProcessingService.objects.get(id=service_id)

        # Получение файла из запроса
        file = request.data.get('file')

        uploaded_file = upload_file(file, user.id)

        serializer = DiagnosisRequestSerializer(data={
            'user': user.id,
            'status': 'created',
            'service': service.id,
            'uploaded_file': uploaded_file.id
        })

        if serializer.is_valid():
            instance = serializer.save()
            request_id = instance.id

            message = RequestForServiceMessage(request_id, uploaded_file.full_path)
            publish_message(message, service.name)

            return Response({'status': 'success'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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