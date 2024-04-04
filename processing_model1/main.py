from config import Settings, Workers
from consumer import ThreadedConsumer


if __name__ == '__main__':
    for instance in range(Workers):
        ThreadedConsumer(Settings).start()
