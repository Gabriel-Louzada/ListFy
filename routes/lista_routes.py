from fastapi import APIRouter, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from models.lista import Lista
from repo.lista import *

router = APIRouter(prefix="/lista")
templates = Jinja2Templates(directory = "templates")


@router.get("/", response_class=HTMLResponse)
async def get_listas(request: Request):
    listas = obter_todos_lista()
    return templates.TemplateResponse("/lista/listas.html", {"request": request, "listas": listas})

@router.get("/cadastrar_lista",response_class=HTMLResponse)
async def get_cadastrar_lista(request: Request):
    return templates.TemplateResponse("/lista/cadastro_lista.html", {"request":request})

@router.post("/post_cadastrar_lista",response_class=RedirectResponse)
async def post_cad_lista(
    estabelecimento: str = Form(),
    id_user: int = Form(),
    status_lista: int = Form()):
    lista = Lista(0,estabelecimento,id_user,status_lista)
    inserir_lista(lista)
    return RedirectResponse("/lista", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/alterar_lista/{id_lista:int}",response_class=HTMLResponse)
async def get_alterar_lista(request: Request):
    return templates.TemplateResponse("/lista/alterar_lista.html", {"request":request})

@router.post("/post_alterar_lista",response_class=RedirectResponse)
async def post_cad_lista(
    id_lista: int = Form(),
    estabelecimento: str = Form(),
    id_user: int = Form(),
    status_lista: int = Form()):
    lista = Lista(id_lista,estabelecimento,id_user,status_lista)
    inserir_lista(lista)
    return RedirectResponse("/lista", status_code=status.HTTP_303_SEE_OTHER)