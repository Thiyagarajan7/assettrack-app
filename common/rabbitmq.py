import pika, os

def publish(queue, msg):
    conn = pika.BlockingConnection(
        pika.ConnectionParameters(host=os.getenv("RABBITMQ_HOST", "rabbitmq"))
    )
    ch = conn.channel()
    ch.queue_declare(queue=queue)
    ch.basic_publish(exchange='', routing_key=queue, body=msg)
    conn.close()
