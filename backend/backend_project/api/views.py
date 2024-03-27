from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpRequest
from .publish_utils.publisher import publishMessage
from .common_dto.RequestForServiceMessage import RequestForServiceMessage


def send_diagnosis_request(request):
    message = RequestForServiceMessage("a", "a", "a", "a")

    print("отправляю в реббит")
    publishMessage(message)
    print("Отправил в реббит")

    return JsonResponse({"status": "success"})
