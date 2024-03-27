from .config import qmanager
import json


def publishMessage(data: bytes, queue_name: str = None, headers: dict = None):
    message = json.dumps(data)
    queue_name = data.__class__.__name__
    qmanager.publish(data= message, queue_name= queue_name, headers= headers)