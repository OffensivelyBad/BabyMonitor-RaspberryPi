import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler
import RPi.GPIO as GPIO

def lightsOn():
        print "lights are on"
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18,GPIO.OUT)
        GPIO.output(18,GPIO.HIGH)

def lightsOff():
        print "lights are off"
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18,GPIO.OUT)
        GPIO.output(18,GPIO.LOW)

class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
                if self.path == '/lightsOn':
                        lightsOn()
                if self.path == '/lightsOff':
                        lightsOff()

                self.send_response(200)

httpd = SocketServer.TCPServer(("", 8080), Handler)
httpd.serve_forever()
