import datetime
from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib

def hello():
    print("hello")
    return "Ok"

def today():
    date = datetime.datetime.today()
    return xmlrpclib.DateTime(date)

def nom(objet_user):
    return objet_user["nom"]

def user(nom,age):
    objet_user = {"nom":nom, "age":age}
    return objet_user

server = SimpleXMLRPCServer(("localhost",8000))
print("Listening on port 8000...")
server.register_function(hello,"hello")
server.register_function(today,"toooday")
server.register_function(nom,"nom")
server.register_function(user,"user")
server.serve_forever()