#rota Raiz do Site
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory = "templates")

@router.get("/", response_class=HTMLResponse)
async def get_raiz(request: Request):
    # request: objeto com dados da requisição do cliente
    # retorna o arquivo index.html
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/contato", response_class=HTMLResponse)
async def get_contato(request: Request):
    return templates.TemplateResponse("contato.html", {"request": request})