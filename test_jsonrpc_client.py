import requests
import json

def main():
    url = "http://localhost:4000/jsonrcp"
    headers={"content-type":"application/json"}

    payload = {
        "method":"hello",
        "params":[],
        "jsonrpc":"2.0",
        "id":0
    }
    req_post = requests.post(url, data=json.dumps(payload),headers=headers)
    response = req_post.json()

    print("debug: req_post",req_post)
    print("debug: response",response)
    print(response["result"])


if __name__ == "__main__":
    main()