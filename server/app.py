import uvicorn
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# the_content = "LOLJK"

# hosts content from docker volume at /images endpoint
@app.get("/images")
def give_content():
    # f = open("../data/persistent/content.txt", 'r')
    f = open("/data/content.txt", 'r')
    content = f.read()
    f.close()
    return content

# receives content and saves in docker volume
@app.post("/", response_class=HTMLResponse)
async def get_form(request: Request, content: str = Form(...)):
    # the_content=content
    # f = open("../data/persistent/content.txt", 'w')
    f = open("/data/content.txt", 'w+')
    f.write(content)
    f.close()
    return templates.TemplateResponse('hello.html', {"request": request, "submitted": "you sent: "+content})

# home page as a form for receiving text
@app.get("/", response_class=HTMLResponse)
def hello(request: Request):
    return templates.TemplateResponse('hello.html', {"request": request, "submitted": "type something and press send"})