from django.contrib import admin
from .models import ProcessingService, UploadedFile, DiagnosisRequest

# Register your models here.


admin.site.register(ProcessingService)
admin.site.register(UploadedFile)
admin.site.register(DiagnosisRequest)
