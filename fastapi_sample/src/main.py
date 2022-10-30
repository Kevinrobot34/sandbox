from datetime import datetime

import pandas as pd
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

@app.get('/',response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request, 'title': 'sample'}
    return templates.TemplateResponse('index.html', context=context)
