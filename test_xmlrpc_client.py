import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:8000")
print(proxy.hello())
print(proxy.toooday())
user = proxy.user("Toto",20)
print(user)
print(proxy.nom(user))