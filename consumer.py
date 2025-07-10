import pika
import time
import os

def connect_to_rabbitmq():
    while True:
        try:
            credentials = pika.PlainCredentials('admin', 'admin')
            parameters = pika.ConnectionParameters(
                host='rabbitmq',
                credentials=credentials,
                heartbeat=600,
                blocked_connection_timeout=300
            )
            connection = pika.BlockingConnection(parameters)
            return connection
        except pika.exceptions.AMQPConnectionError as e:
            print("Failed to connect to RabbitMQ. Retrying in 5 seconds...")
            time.sleep(5)

def callback(ch, method, properties, body):
    print(f" [x] Mensaje recibido: {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    connection = connect_to_rabbitmq()
    channel = connection.channel()

    channel.queue_declare(queue='chat_queue', durable=True)
    channel.basic_qos(prefetch_count=1)
    
    print(' [*] Esperando mensajes. Presiona Ctrl+C para salir')
    channel.basic_consume(queue='chat_queue', on_message_callback=callback)
    
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("\nSaliendo...")
    finally:
        connection.close()

if __name__ == '__main__':
    main()
