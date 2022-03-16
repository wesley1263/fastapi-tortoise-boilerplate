import json
import ssl
from app.config.settings import get_settings
from kafka import KafkaProducer

setting = get_settings()

context = ssl.create_default_context()
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)

producer = KafkaProducer(bootstrap_servers=setting.KAFKA_BOOTSTRAP_SERVERS,
                         sasl_mechanism="PLAIN",
                         ssl_context=context,
                         security_protocol='SASL_SSL',
                         sasl_plain_username=setting.KAFKA_USERNAME,
                         sasl_plain_password=setting.KAFKA_PASSWORD
                         )
