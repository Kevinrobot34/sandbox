from datetime import datetime

import lightgbm as lgb
import pandas as pd
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

model = lgb.Booster(model_file="./model/model_fold4.txt")  # init model

@app.get('/',response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request, 'title': 'sample'}
    return templates.TemplateResponse('form.html', context=context)


@app.post("/")
def form_post(
    request: Request,
    weight: int = Form(None),
    distance: int = Form(None),
    loaddate: datetime = Form(None),
    destdate: datetime = Form(None),
    loadpref: int = Form(None),
    destpref: int = Form(None),
):
    input_data = f"{weight=} {distance=} {loaddate=} {destdate=} {loadpref=} {destpref=}"
    print(input_data)
    result = prediction(weight, distance, loadpref, loaddate, destpref, destdate)
    print(result)

    context = {"request": request, "input_data": input_data, "result": result, "title": "sample after form_post"}
    return templates.TemplateResponse("form.html", context=context)

def prediction(
    weight: float,
    distance: float,
    loadpref: int,
    loaddate: datetime,
    destpref: int,
    destdate: datetime,
) -> float:

    input_data = {
        "Use_diff_DestLoaddate": (destdate - loaddate).total_seconds(),
        "Use_Loaddate_month": loaddate.month,
        "Use_Loaddate_day": loaddate.day,
        "Use_Loaddate_hour": loaddate.hour,
        "Use_Destdate_month": destdate.month,
        "Use_Destdate_day": destdate.day,
        "Use_Destdate_hour": destdate.hour,
        "Use_LoadPrefecture": loadpref,
        "Use_DestPrefecture": destpref,
        "Goods_LOAD_DEST_distance": distance,
        "Use_Weight": weight,
    }
    print(pd.Series(input_data))

    pred = [1.00]
    print(pred)
    return round(pred[0])
