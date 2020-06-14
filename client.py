""" Simple RPC Client """

import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')

# Print list of available methods
print(s.system.listMethods())
print(s.echo("Hello World!"))
print(s.rotN("Hello World!"))
print(s.rotN(s.rotN("Hello World!")))
print(s.rotN("Hello World!", 14)) #Vszzc Kcfzr!
for x in range(10):
	print(s.next())
for x in range(10):
	print(s.next1())

