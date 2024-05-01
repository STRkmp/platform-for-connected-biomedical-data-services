from django.urls import path
from .views import send_diagnosis_request, get_processing_services, get_user_requests, get_file

urlpatterns = [
    path('processing_services/', get_processing_services, name='processing_services'),
    path('requests/', get_user_requests, name='requests'),
    path('request/', send_diagnosis_request, name='request'),
    path('file/', get_file, name='file')
]