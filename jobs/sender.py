import pika
import json

from app.utils.logger import logger

def convert_to_json_serializable(info):
    if isinstance(info, set):
        return list(info)

def sent_to_queue(infos: list):
  credentials = pika.PlainCredentials('mtu','mtutp')

  connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq', credentials=credentials)
  )
  channel = connection.channel()

  channel.queue_declare(queue='mtu')

  for info in infos:
    message = json.dumps(info, default=convert_to_json_serializable)

    channel.basic_publish(
      exchange='', 
      routing_key='mtu', 
      body=message
    )

    logger.info(f"[x] Sent message do queue")
  connection.close()