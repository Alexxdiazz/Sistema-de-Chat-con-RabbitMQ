# Sistema-de-Chat-con-RabbitMQ

El sistema está compuesto por dos scripts escritos en Python:

producer.py: permite al usuario enviar mensajes que se colocan en una cola de mensajes.
consumer.py: se mantiene escuchando la cola y muestra en consola los mensajes recibidos.
Ambos scripts se comunican a través de chat_queue, utilizando RabbitMQ como sistema de mensajería.
para ejecutar, descargar: librería de Python "pika" , pip install pika en cdm
 y Docker para correr RabbitMQ.
Para levantar Docker con Rabbitmq: en cdm:
 docker run -d --hostname rabbit --name rabbitmq \
  -e RABBITMQ_DEFAULT_USER=admin \
  -e RABBITMQ_DEFAULT_PASS=admin \
  -p 5672:5672 -p 15672:15672 \
  rabbitmq:3-management
  y finalmente; ejecutar el programa, en la terminal  utilizando el comando, docker-compose up --build.
  En la terminal para iniciar el consumidor:python consumer.py, y para el productor, python producer.py

Profe, me costó bastante por mi computadora, no funcionó del todo con Docker.

