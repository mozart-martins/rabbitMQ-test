import pika, sys, os

def main():
    # Conectando-se ao RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()


    # Criando uma fila/queue chamada hello
    # Essa chamada é idempotente: significa que pode ser chamada várias vezes que
    # somente uma fila será criada.
    channel.queue_declare(queue='hello')


    # Função que será chamada quando recebermos uma mensagem
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")


    # Informando que as mensagens recebidas da queue hello serão tratadas pelo callback chamado callback (a função)
    channel.basic_consume(queue='hello',
                        auto_ack=True,
                        on_message_callback=callback)


    # Loop que espera por mensagens
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)