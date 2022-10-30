import base64
from datetime import datetime
from io import BytesIO

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates/")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    context = {"request": request, "title": "sample"}
    return templates.TemplateResponse("index.html", context=context)


@app.post("/")
def form_post(
    request: Request,
    form1: int = Form(None),
):
    input_data = f"{form1=}"
    print(input_data)
    result = "result"

    img = draw_graph(form1)

    context = {
        "request": request,
        "input_data": input_data,
        "result": result,
        "title": "sample after form_post",
        "img": img,
    }
    return templates.TemplateResponse("index.html", context=context)


def draw_graph(point_num):
    bytes_io = BytesIO()

    # 乱数を生成
    x = np.random.rand(point_num)
    y = np.random.rand(point_num)

    # 散布図を描画
    plt.scatter(x, y)
    plt.savefig(bytes_io, format="png")
    plt.close()
    bytes_io.seek(0)

    plot_url = base64.b64encode(bytes_io.getvalue()).decode()
    graph = f"data:image/png;base64,{plot_url}"
    return graph
