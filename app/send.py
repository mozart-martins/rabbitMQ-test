import pika


# Conectando-se ao RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


# Criando uma fila/queue chamada hello
channel.queue_declare(queue='hello')

# Enviando a mensagem Hello World!
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

# Feedback para o usuário
print(" [x] Sent 'Hello World!'")

# Fechando a conexão
connection.close()