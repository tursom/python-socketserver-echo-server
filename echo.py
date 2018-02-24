from socketserver import BaseRequestHandler, ThreadingTCPServer


class EchoHandler(BaseRequestHandler):
	def handle(self):
		print('Got connection from', self.client_address)
		msg = self.request.recv(2048).decode()
		if (msg == "close"):
			serv.server_close()
			serv.shutdown()
			return
		print('recved message:', msg)
		self.request.send(msg.encode())

def getServer(addr,handler,DEBUG):
	if DEBUG:
		serv = ThreadingTCPServer(addr, handler, bind_and_activate=False)
		serv.allow_reuse_address = True
		serv.daemon_threads = True
		serv.server_bind()
		serv.server_activate()
	else:
		serv = ThreadingTCPServer(addr, handler)
	return serv

serv = getServer(('', 22222), EchoHandler, True)
print('server started')
serv.serve_forever()
print('server closed')
