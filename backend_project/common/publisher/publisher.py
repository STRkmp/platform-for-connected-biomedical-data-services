from .config import qmanager
import jsonpickle


def publish_message(data: bytes, queue_name: str = None, headers: dict = None):
    message = jsonpickle.encode(data, unpicklable=False)
    if queue_name is None:
        queue_name = data.__class__.__name__
    qmanager.publish(data=message, queue_name=queue_name, headers=headers)
