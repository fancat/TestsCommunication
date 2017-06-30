import Pyro4

objet_partage = Pyro4.Proxy("PYRONAME:class_a_partager")
print(objet_partage.hello())