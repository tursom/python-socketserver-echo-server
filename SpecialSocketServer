from socketserver import ThreadingTCPServer


class Server:
	def __init__(self, port, handler, debug=True):
		self.port = port
		self.handler = handler
		self.DEBUG = debug
		self.serv = self.get_server(addr=('', port), handler=handler, debug=debug)
	
	@staticmethod
	def get_server(addr, handler, debug=False):
		if debug:
			serv = ThreadingTCPServer(addr, handler, bind_and_activate=False)
			serv.allow_reuse_address = True
			serv.daemon_threads = True
			serv.server_bind()
			serv.server_activate()
		else:
			serv = ThreadingTCPServer(addr, handler)
		return serv
	
	def start(self):
		self.serv.serve_forever()
