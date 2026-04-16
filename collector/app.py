import time
from common.rabbitmq import publish

while True:
    publish("collector", "collector data")
    time.sleep(5)
