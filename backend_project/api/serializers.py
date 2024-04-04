from rest_framework import serializers
from .models import DiagnosisRequest, UploadedFile, ProcessingService


class DiagnosisRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosisRequest
        fields = ['id', 'user', 'request_time', 'status', 'service', 'uploaded_file', 'result_file']


class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['id', 'name', 'full_path', 'uploaded_at']

class ProcessingServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessingService
        fields = ['id', 'name', 'description', 'is_available']

