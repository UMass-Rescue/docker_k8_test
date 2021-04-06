import time
import uvicorn
from fastapi import FastAPI
import requests

app = FastAPI()

# collects content by requesting from server
def get_content():
    while True:
        try:
            # f = open("../data/content.txt", 'r')
            # content = f.read()
            # f.close()
            # content = requests.get("http://server.default:5000/images")
            print("HI")
            content = requests.get("http://host.docker.internal:5000/images")
            return content.text.strip("\"")
        except Exception as exc:
            return(exc)

# home page just prints content from server
@app.get('/')
def hello():
    content = get_content()
    return 'you sent me '+content