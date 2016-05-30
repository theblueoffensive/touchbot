import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
import os
import string
from time import sleep
from datetime import datetime
import hashlib
import json
import urllib
try:
    import simplejson as json
except ImportError:
    import json

from tornado.options import define, options

define("port", default=8001, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self)	:
        self.write("Hello, world")

class LoginHandler(tornado.web.RequestHandler):
    def post(self):
	data = json.loads(urllib.unquote_plus(self.request.body))
	print data['payload']
	try:
	    json.loads(self.request.body)
	except:
	    json.loads(urllib.unquote_plus(self.request.body))
        

        if data['payload']=="0":
            response = {
		"text": "Hi , How are you feeling today?",
			"actions": [
   			{
  			"type": "postback",
   			"text": "Very good!",
     			"payload": "0#1"
  			 },
 			  {
  			   "type": "postback",
   			  "text": "Alright",
   			  "payload": "0#2"
   				},
  			 {
  			   "type": "postback",
    			   "text": "Unhappy",
    			   "payload": "0#3"
  				 }
 				]
		}
		
	elif data['payload']=="0#1":
            response = {
		"text": "So nice to hear that, what would you like to do?",
		"actions": [
   			{
  			"type": "postback",
   			"text": "Nothing more, Thanks for the help",
     			"payload": "##"
  			 },
 			  {
  			   "type": "postback",
   			  "text": "Thats it for Now",
   			  "payload": "##"
   				},
  			 {
  			   "type": "postback",
    			   "text": "I wish to see the Counsellor",
    			   "payload": "#"
  				 }
 				]
		}	
	elif data['payload']=="0#2":
            response = {
		"text": "Should i help?",
		"actions": [
   			{
  			"type": "postback",
   			"text": "Thanks ",
     			"payload": "##"
  			 },
 			  {
  			   "type": "postback",
   			  "text": "Thats it !",
   			  "payload": "##"
   				},
  			 {
  			   "type": "postback",
    			   "text": "I wish to see the Counsellor",
    			   "payload": "#"
  				 }]
  				 			}
	elif data['payload']=="0#3":
            response = {
		"text": "I will help you, please tell me your problem?",
		"actions": [
   			{
  			"type": "postback",
   			"text": "No thanks, I think I got it ",
     			"payload": "##"
  			 },
 			  {
  			   "type": "postback",
   			  "text": "I am Fine!",
   			  "payload": "##"
   				},
  			 {
  			   "type": "postback",
    			   "text": "I wish to see the Counsellor",
    			   "payload": "#"
  				 }
  				 ]
		}
	
        else:
            response = {
		"text": "Please Repeat, something is Wrong",
				'payload': "0"
				}

        self.write(response)


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/login", LoginHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()

