from django.contrib import admin
from .models import ProcessingService, UploadedFile, DiagnosisRequest, Feedback

# Register your models here.


admin.site.register(ProcessingService)
admin.site.register(UploadedFile)
admin.site.register(DiagnosisRequest)
admin.site.register(Feedback)