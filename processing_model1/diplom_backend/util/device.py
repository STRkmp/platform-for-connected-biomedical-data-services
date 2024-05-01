import torch

class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Device(metaclass=SingletonMeta):
    def __init__(self):
        print(torch.cuda.is_available())
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    def get_device(self):
        return self.device