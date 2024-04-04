from qmanager.qmanager_factory import QueueManagerFactory
from pydantic import BaseSettings
from threading import Thread
import jsonpickle
from dto.ResultFromServiceMessage import ResultFromServiceMessage
from dto.RequestForServiceMessage import RequestForServiceMessage

class ThreadedConsumer(Thread):
    def __init__(self, settings: BaseSettings):
        Thread.__init__(self)
        self.qmanager = QueueManagerFactory(settings).get_instance(callback_func=self.process_request)

    def run(self):
        print(f'{self.name} Consuming...')
        self.qmanager.consume()

    # Необходимо переназначить этот метод
    def process_request(self, data: bytes, headers: dict = None) -> None:
        request = jsonpickle.loads(data)
        print(f'{self.name} RECEIVED {headers}\n{type(data)}\n{data}')




