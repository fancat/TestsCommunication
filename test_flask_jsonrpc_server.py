from flask import Flask
from flask_jsonrpc import JSONRPC

app = Flask(__name__)
jsonrpc = JSONRPC(app, "/api")

@jsonrpc.method("hello")
def hello():
    return "Hello"

@jsonrpc.method("livre")
def get_livre(titre):
    livre = {"titre":titre, "auteur":"Anonymous"}
    return livre

if __name__ == "__main__":
    app.run()
