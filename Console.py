import time
import datetime

class Console:
	def __init__(self):
		pass
		
	def output(self, message):
		print("[" + datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S') + "] " + message)
		
	def request(self, path, user, port):
		self.output(user + ":" + str(port) + " >> GET: " + path)
	
	def unknown(self, args, user, port):
		message = user + ":" + str(port) + " >> ERROR: Unknown request\n"
		count = 0
		for arg in args:
			message = message + "Arg " + str(count) + ": " + str(arg) + "\n"
		self.output(message)