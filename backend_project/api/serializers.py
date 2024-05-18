from rest_framework import serializers
from .models import DiagnosisRequest, UploadedFile, ProcessingService, Patient, Feedback


class DiagnosisRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosisRequest
        fields = ['id', 'user', 'request_time', 'status', 'service', 'uploaded_file', 'result_file', 'patient', 'complaints']


class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['id', 'name', 'full_path', 'uploaded_at']

class ProcessingServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessingService
        fields = ['id', 'name', 'description', 'is_available']


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'lastname', 'surname', 'birth_date']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'request', 'comment']
