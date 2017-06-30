# -*- coding:utf-8 -*-
import Pyro4


@Pyro4.expose
class Class_a_partager(object):
    def hello(self):
        print("hello")
        return "Ok"


deamon = Pyro4.Daemon()
uri = deamon.register(Class_a_partager)  # Uri généré, inconnu pour le client
ns = Pyro4.locateNS()  # Serveur de noms, pour que le client n'ait pas à connaitre l'uri
ns.register("class_a_partager", uri)

deamon.requestLoop()

#Pour faire tourner le serveur de nom, écrire dans une console:
#$ pyro4-ns