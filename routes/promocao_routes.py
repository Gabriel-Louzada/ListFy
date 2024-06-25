from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from models.promocao import *
from repo.promocao import *

router = APIRouter(prefix="/promocao")
templates = Jinja2Templates(directory = "templates")

@router.get("/", response_class=HTMLResponse)
async def get_listar(request: Request):
    promocao = obter_todas_promocoes()
    return templates.TemplateResponse("/promocao/promocao.html", {"request": request, "promocao":promocao})