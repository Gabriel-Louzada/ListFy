from fastapi import APIRouter, Form, Request,status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from repo.categoria import *
from repo.produto import *


router = APIRouter(prefix="/produto")
templates = Jinja2Templates(directory = "templates")

@router.get("/", response_class=HTMLResponse)
async def get_produtos(request: Request):
    produtos = obter_todos_produtos()
    return templates.TemplateResponse("/produto/listar_produtos.html", {"request": request, "produtos": produtos})

@router.get("/um_produto", response_class=HTMLResponse)
async def get_produtos(request: Request, nome_produto: str = ''):
    produto = obter_um_produto_nome(nome_produto)
    return templates.TemplateResponse("/produto/um_produto.html", {"request": request, "produto": produto})

@router.get("/categoria/{id_categoria}", response_class=HTMLResponse)
async def get_produtos(request: Request, id_categoria: int = 0):
    produtos = obter_produtos_categoria(id_categoria)
    return templates.TemplateResponse("/produto/listar_produtos_categoria.html", {"request": request, "produtos": produtos})

@router.get("/cadastrar_produto", response_class=HTMLResponse)
async def get_cadastrar(request: Request):
    categoria = obter_todas_categorias()
    return templates.TemplateResponse("/produto/cadastro_produto.html",{"request":request, "categoria":categoria})

@router.post("/post_cadastrar", response_class=RedirectResponse)
async def post_cadastrar(
    nome_produto: str = Form(),
    id_categoria: int = Form(),
    valor_produto: float = Form()):
    produto = Produto(0, nome_produto, id_categoria, valor_produto)
    inserir_produtos(produto)
    return RedirectResponse("/produto",status_code=status.HTTP_303_SEE_OTHER)

@router.get("/alterar_produto/{id:int}",)
async def get_alterar_produto(request: Request, id: int=0):
    produto = obter_um_produto(id)
    categoria = obter_todas_categorias()
    return templates.TemplateResponse("/produto/alterar_produto.html",{"request":request, "produto":produto, "categoria":categoria})

@router.post("/post_alterar_produto", response_class=RedirectResponse)
async def post_alterar_produto(
    id_produto: int = Form(),
    nome_produto: str = Form(),
    id_categoria: int = Form(),
    valor_produto: float = Form()):
    produto = Produto(id_produto, nome_produto, id_categoria, valor_produto)
    alterar_produtos(produto)
    return RedirectResponse("/produto", status_code=status.HTTP_303_SEE_OTHER)