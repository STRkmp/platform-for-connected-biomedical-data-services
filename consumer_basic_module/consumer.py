from qmanager.qmanager_factory import QueueManagerFactory
from pydantic import BaseSettings
from config import Settings, Workers
from threading import Thread
from common_dto.ResultFromServiceMessage import ResultFromServiceMessage
from common_dto.RequestForServiceMessage import RequestForServiceMessage

class ThreadedConsumer(Thread):
    def __init__(self, settings: BaseSettings):
        Thread.__init__(self)
        self.qmanager = QueueManagerFactory(settings).get_instance(callback_func=self.process_request)

    def run(self):
        print(f'{self.name} Consuming...')
        self.qmanager.consume()

    def process_request(self, data: RequestForServiceMessage, headers: dict = None) -> None:
        print(f'{self.name} RECEIVED {headers}\n{type(data)}\n{data}')
        # SomeLogic
        message = ResultFromServiceMessage(data.user_id, data.service_id, data.path_to_image,
                                           "Ну жестко ты придумал чел. Держи ответочку")
        self.qmanager.publish(data)

if __name__ == '__main__':
    for instance in range(Workers):
        ThreadedConsumer(Settings).start()
