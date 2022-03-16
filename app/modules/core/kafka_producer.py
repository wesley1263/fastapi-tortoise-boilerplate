import json

from app.config.kafka import producer
from app.config.settings import get_settings

settings = get_settings()


def set_message(message):
    message = json.dumps(message).encode("utf-8")
    producer.send(settings.KAFKA_TOPIC, message)
