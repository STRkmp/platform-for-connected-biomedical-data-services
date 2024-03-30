from qmanager.qmanager_factory import QueueManagerFactory
from pydantic import BaseSettings
from .config import Settings, Workers
from threading import Thread


class ThreadedConsumer(Thread):
    def __init__(self, settings: BaseSettings):
        Thread.__init__(self)
        self.qmanager = QueueManagerFactory(settings).get_instance(callback_func=self.process_request)

    def run(self):
        print(f'{self.name} Consuming...')
        self.qmanager.consume()

    def process_request(self, data: bytes, headers: dict = None) -> None:
        print(f'{self.name} RECEIVED {headers}\n{type(data)}\n{data}')
        #Добавить логику обновления ответа на запросы от пользователей. Может возвращать как-то по вебсокету.


def start_consumer():
    for instance in range(Workers):
        print("запустил консьюмера {}".format(instance))
        ThreadedConsumer(Settings).start()
