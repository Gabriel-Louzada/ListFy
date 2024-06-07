from fastapi import APIRouter, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from repo.itens_lista import *
from models.itens_lista import *
from repo.produto import *

router  = APIRouter(prefix="/itens_lista")
templates = Jinja2Templates(directory = "templates")

@router.get("/", response_class=HTMLResponse)
async def get_itens_lista(request: Request):
    return templates.TemplateResponse("/itens_lista/itens_lista.html", {"request": request})

@router.get("/produtos", response_class=HTMLResponse)
async def get_produtos(request: Request):
    produtos = obter_todos_produtos()
    return templates.TemplateResponse("/itens_lista/listar_produtos.html", {"request": request, "produtos": produtos})

@router.get("/um_produto", response_class=HTMLResponse)
async def get_produtos(request: Request, nome_produto: str = ''):
    produto = obter_um_produto_nome(nome_produto)
    return templates.TemplateResponse("/itens_lista/um_produto.html", {"request": request, "produto": produto})