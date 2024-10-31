from fastapi import FastAPI , Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from typing import Optional


app = FastAPI()
app.mount("/static",StaticFiles(directory="static"), name = "static")

templates = Jinja2Templates(directory= "templates")

@app.get('/')
def main(request: Request):
    return templates.TemplateResponse(
        "sudoku.html",
        {
            "request": request,
        }
    )