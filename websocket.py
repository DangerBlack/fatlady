#sudo pip install tornado
#sudo pip install SpeechRecognition
#sudo apt-get install python-pyaudio python3-pyaudio
'''
$ sudo apt-get install git
$ sudo git clone http://people.csail.mit.edu/hubert/git/pyaudio.git
$ sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
$ sudo apt-get install python-dev
$ cd pyaudio
$ sudo python setup.py install
'''

#sudo apt-get install swig
#pip install --upgrade pocketsphinx

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import thread
import time
import speech_recognition as sr
from brainSentence import BrainSentence
from api import *

r = sr.Recognizer()

class MyWebSocketServer(tornado.websocket.WebSocketHandler):
    def listenThePeople(self):
        with sr.Microphone() as source:
            print("Say something!")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            print(API);
            message= r.recognize_google(audio)# key=''
            #message = r.recognize_sphinx(audio)
            bs = BrainSentence(message)
            output_message=bs.deduce()
            if(output_message!=[]):
                self.write_message(str(output_message).replace('\'','"'),False)
            print("Sphinx thinks you said " + message )
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))

        thread.start_new_thread(self.listenThePeople, ())

    def open(self):
        # metodo eseguito all'apertura della connessione
        print 'Nuova connessione'
        thread.start_new_thread(self.listenThePeople, ())

    def on_message(self, message):
        # metodo eseguito alla ricezione di un messaggio
        # la stringa 'message' rappresenta il messaggio
        print 'Messaggio ricevuto: %s' % message

    def on_close(self):
        # metodo eseguito alla chiusura della connessione
        print 'Connessione chiusa'

    def check_origin(self, origin):
        return True

application = tornado.web.Application([
    (r'/websocketserver', MyWebSocketServer),
])


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8000)

    tornado.ioloop.IOLoop.instance().start()

    application.write_message('hello there',False)
