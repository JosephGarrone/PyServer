from Console import Console
from Constants import Constants
import http.server
import os
import os.path

class Webservice(http.server.BaseHTTPRequestHandler):
	def __init__(self, *args, **kwargs):
		super(Webservice, self).__init__(*args, **kwargs)

	def do_GET(self):
		if os.path.isfile(os.getcwd() + self.server.constants.root + self.path):
			ending = self.path.split(".")[-1]
			type = "text/html"
			if ending == "html":
				type = "text/html"
			elif ending == "js":
				type = "text/javascript"
			elif ending == "css":
				type = "text/css"
			f = open(os.getcwd() + self.server.constants.root + self.path, 'rb')
			self.send_response(200)
			self.send_header('Content-Type', type)
			self.end_headers()
			self.wfile.write(f.read())
		else:
			self.send_response(404)
			self.send_header('Content-Type', 'text/html')
			self.end_headers()
			self.wfile.write(bytes('<html><head><title>404 - Not Found</title></head><body><h1>404 - Page Not Found</h1></body></html>', 'UTF-8'))
		
	def log_message(self, format, *args):
		if self.command == "GET":
			self.server.console.request(self.path, self.client_address[0], self.client_address[1])
		else:
			self.server.console.unknown(args, self.client_address[0], self.client_address[1])