from abc import ABC

import pika
import tornado.ioloop
import tornado.web

import settings


class MessageHandler(tornado.web.RequestHandler, ABC):

    def get(self):
        msg = self.get_query_argument("msg")
        self.write("You send message " + msg)

        url = 'amqp://{0}:{1}@{2}:{3}/%2F'
        parameters = pika.URLParameters(url.format(
            settings.RABBIT_USER, settings.RABBIT_PASS,
            settings.RABBIT_HOST, settings.RABBIT_PORT)
        )

        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue='msg-queue')

        channel.basic_publish(exchange='',
                              routing_key='msg-queue',
                              body=msg)
        print(" [x] Sent message to msg-que!'")
        connection.close()


app = tornado.web.Application([
    (r"/send", MessageHandler),

])

app.listen(8000)
tornado.ioloop.IOLoop.instance().start()
