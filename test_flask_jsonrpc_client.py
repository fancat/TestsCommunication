from flask_jsonrpc.proxy import ServiceProxy
server = ServiceProxy("http://localhost:5000/api")

print(server.hello())
print(server.livre("Harry Potter"))