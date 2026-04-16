import time
from common.rabbitmq import publish

while True:
    publish("processor", "processed data")
    time.sleep(5)
