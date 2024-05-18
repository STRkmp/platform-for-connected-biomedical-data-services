from django.db import models
from django.conf import settings


class DiagnosisRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    request_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    service = models.ForeignKey('ProcessingService', on_delete=models.DO_NOTHING, related_name='diagnosis_request')
    uploaded_file = models.OneToOneField('UploadedFile', on_delete=models.DO_NOTHING, related_name='uploaded_file_diagnosis_request')
    result_file = models.OneToOneField('UploadedFile', on_delete=models.DO_NOTHING, related_name='result_file_diagnosis_request',  null=True)
    patient = models.ForeignKey('Patient', on_delete=models.DO_NOTHING, null=True)
    complaints = models.TextField(null=True)


class UploadedFile(models.Model):
    name = models.CharField(max_length=255)  # Имя файла
    full_path = models.TextField()  # Путь к файлу в Minio
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Дата и время загрузки файла


class ProcessingService(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500, default='Without description :(')
    health_check_url = models.URLField(null=True)
    is_available = models.BooleanField(default=True)

class Patient(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, null=True)
    birth_date = models.DateField()

class Feedback(models.Model):
    request = models.ForeignKey('DiagnosisRequest', on_delete=models.DO_NOTHING,
                                         related_name='request_diagnosis_request')
    comment = models.TextField()