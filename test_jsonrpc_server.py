from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher

#@dispatcher.add_method
#def
def hello():
    print("hello")
    return "Ok"

@Request.application
def application(request):
    dispatcher["hello"]=hello
    dispatcher["add"]=lambda a,b: a+b

    print("debug " + request.data)
    response = JSONRPCResponseManager.handle(request.data, dispatcher)
    print("debug " + response.json)
    return Response(response.json, mimetype="application/ json")

if __name__ == "__main__":
    run_simple("localhost", 4000, application)