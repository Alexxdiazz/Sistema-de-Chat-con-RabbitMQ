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

def main():
    connection = connect_to_rabbitmq()
    channel = connection.channel()
    channel.queue_declare(queue='chat_queue', durable=True)
    
    print("Bienvenido al productor de mensajes!")
    print("Escribe tus mensajes. Presiona Ctrl+C para salir.")
    
    try:
        while True:
            message = input("Mensaje: ")
            if message.lower() == 'exit':
                break
                
            channel.basic_publish(
                exchange='',
                routing_key='chat_queue',
                body=message,
                properties=pika.BasicProperties(
                    delivery_mode=2,
                ))
            print(f" [x] Mensaje enviado: '{message}'")
    except KeyboardInterrupt:
        print("\nSaliendo...")
    finally:
        connection.close()

if __name__ == '__main__':
    main()
