import time
from common.rabbitmq import publish

while True:
    publish("assets", "asset data")
    time.sleep(5)
