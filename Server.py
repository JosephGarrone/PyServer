from Webservice import Webservice
from Console import Console
from Constants import Constants
import http.server
import time
import datetime

class Server:
	def __init__(self):
		self.webservice = Webservice
		self.console = Console()
		self.constants = Constants()
		self.started = False
		self.menu()
		
	def menu(self):
		while self.started == False:
			self.process(input("[" + datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S') + "] " + ">>: "))
			
	def process(self, cmd):
		cmds = cmd.split()
		action = cmds[0]
		parameter = -1
		if len(cmds) > 1:
			parameter = cmds[1]
		if action == "start":
			self.started = True
			self.start()
		elif parameter != -1:
			if action == "port":
				self.constants.port = int(parameter)
				self.console.output("Port set to: " + str(self.constants.port))
			elif action == "root":
				self.constants.root = str(parameter)
				self.console.output("Root directory set to: " + self.constants.root)
			elif action == "address":
				self.constants.address = str(parameter)
				self.console.output("Address set to: " + self.constants.address)
		else:
			self.console.output("Unknown command")
	
	def start(self):
		try:
			self.server = CustomHTTPServer(("127.0.0.1", self.constants.port), self.webservice, self.constants, self.console)
			self.console.output("Server started. Ctrl + C to stop.")
			self.console.output("Port: " + str(self.server.server_port))
			self.console.output("Address: " + self.constants.address)
			self.console.output("Root: " + self.constants.root)
			self.server.serve_forever()
		except KeyboardInterrupt:
			self.console.output("Server has stopped")
			self.menu()
		
class CustomHTTPServer(http.server.HTTPServer):
	def __init__(self, serverAddress, requestHandlerClass, constants, console):
		http.server.HTTPServer.__init__(self, serverAddress, requestHandlerClass)
		self.constants = constants
		self.console = console

if __name__ == "__main__":
	server = Server()