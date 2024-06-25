from fastapi import APIRouter, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from repo.categoria import *
from repo.lista import *
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

#OBTER OS PRODUTOS DE APENAS UMA CATEGORIA 
@router.get("/categorias/{id_lista:int}/{id_categoria:int}", response_class=HTMLResponse)
async def get_produtos(request: Request, id_categoria: int = 0, id_lista: int = 0):
    produtos = obter_produtos_categoria(id_categoria)
    categoria = obter_uma_categoria(id_categoria)
    lista = obter_uma_lista(id_lista)
    return templates.TemplateResponse("/itens_lista/listar_produtos.html", {"request": request, 
                                                                            "produtos": produtos, 
                                                                            "id_lista":id_lista, 
                                                                            "id_categoria":id_categoria,
                                                                            "categoria":categoria,
                                                                            "lista":lista})
    
#ROTA PARA INSERÇÃO DE PRODUTOS A LISTA 
@router.post("/post_itens_lista/{id_lista:int}", response_class=RedirectResponse)
async def post_itens_lista(
    id_lista: int = 0,
    id_produto: int = Form(),
    quantidade: int = Form(),
    valor_produto: float = Form()):
    itens_lista = Itens_lista(id_produto,id_lista,quantidade,valor_produto)
    inserir_itens_lista(itens_lista)
    return RedirectResponse("/lista", status_code=status.HTTP_303_SEE_OTHER)

#ROTA PARA ALTERAÇÃO DE PRODUTOS DA LISTA
@router.post("/post_alterar_itens_lista",response_class=RedirectResponse)
async def post_alterar_itens_lista(
    id_lista: int = Form(),
    id_produto: int = Form(),
    quantidade: int = Form(),
    valor_produto: float = Form()):
    itens_lista = Itens_lista(id_produto,id_lista,quantidade,valor_produto)
    alterar_itens_lista(itens_lista)
    return RedirectResponse(f"/lista/abrir/{id_lista}", status_code=status.HTTP_303_SEE_OTHER)

#ROTA QUE OBTEM OS PRODUTOS DENTRO DE UMA LISTA COM SEUS RESPECTIVOS NOMES
@router.get("/um_produto", response_class=HTMLResponse)
async def get_um_produto(request: Request, nome_produto: str = ''):
    produtos = obter_um_produto_nome(nome_produto)
    return templates.TemplateResponse("/itens_lista/um_produto.html", {"request": request, "produtos": produtos})

#A FUNCAO QUE OBTEM OS PRODUTOS COM NOME. FAZ UM JOIN NA TABELA PRODUTO PARA PEGAR O NOME 
@router.get("/categorias/{id_lista:int}", response_class=HTMLResponse)
async def get_listar_categoria(request: Request,id_lista: int = 0):
    categoria = obter_todas_categorias()
    return templates.TemplateResponse("/itens_lista/itens_lista_categorias.html",{"request":request, "categoria":categoria, "id_lista":id_lista})

@router.post("/post_remover_item_lista",response_class=RedirectResponse)
async def post_remover_item_lista(
    id_lista: int = Form(),
    id_produto: int = Form()):
    excluir_itens_lista(id_lista,id_produto)
    return RedirectResponse("/lista", status_code=status.HTTP_303_SEE_OTHER)