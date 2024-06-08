from fastapi import APIRouter, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from repo.categoria import *
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

@router.get("/categorias/{id_lista:int}/{id_categoria:int}", response_class=HTMLResponse)
async def get_produtos(request: Request, id_categoria: int = 0, id_lista: int = 0):
    produtos = obter_produtos_categoria(id_categoria)
    return templates.TemplateResponse("/itens_lista/listar_produtos.html", {"request": request, "produtos": produtos, "id_lista":id_lista, "id_categoria":id_categoria})

@router.get("/um_produto", response_class=HTMLResponse)
async def get_um_produto(request: Request, nome_produto: str = ''):
    produtos = obter_um_produto_nome(nome_produto)
    return templates.TemplateResponse("/itens_lista/um_produto.html", {"request": request, "produtos": produtos})

@router.get("/categorias/{id_lista:int}", response_class=HTMLResponse)
async def get_listar_categoria(request: Request,id_lista: int = 0):
    categoria = obter_todas_categorias()
    return templates.TemplateResponse("/itens_lista/itens_lista_categorias.html",{"request":request, "categoria":categoria, "id_lista":id_lista})
