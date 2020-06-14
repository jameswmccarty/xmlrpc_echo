""" Simple RPC Server """

import sys
from xmlrpc.server import SimpleXMLRPCServer

class DemoNonce:
	def __init__(self):
		self.val = -1

	def getNonce(self):
		self.val += 1
		return self.val

def echo_function(string):
	return string

def applyRot(ascii, key):
	output = ''
	for i,byte in enumerate(ascii):
		if ord(byte) < 65 or (ord(byte) > 90 and ord(byte) < 97) or ord(byte) > 122:
			output += byte
		elif ord(byte) < 91:
			output += chr(65+(((ord(byte)-65)+key)%26))
		else:
			output += chr(97+(((ord(byte)-97)+key)%26))
	return output

def rotN(string, num=13):
	try:
		num = int(num) % 26
		string = str(string)
		return applyRot(string, num)
	except:
		return "!!! Error: Invalid input. !!!"

# Create server
with SimpleXMLRPCServer(('localhost', 8000)) as server:
	server.register_introspection_functions()

	# Register a function under a different name
	server.register_function(echo_function, 'echo')

	server.register_function(rotN)

	#server.register_instance(DemoNonce(), allow_dotted_names=False)

	Nonce1 = DemoNonce()
	Nonce2 = DemoNonce()

	server.register_function(Nonce1.getNonce, 'next')
	server.register_function(Nonce2.getNonce, 'next1')

	# Run the server's main loop
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		print("\nKeyboard interrupt received, exiting.")
		sys.exit(0)

