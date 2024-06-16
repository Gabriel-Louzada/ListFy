from fastapi import APIRouter, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from models.lista import Lista
from repo.lista import *
from repo.itens_lista import * 

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

@router.get("/abrir/{id_lista:int}",response_class=HTMLResponse)
async def get_abrir_lista(request:Request, id_lista: int=0 ):
    itens_lista = obter_itens_lista_nomes(id_lista)
    lista = obter_uma_lista(id_lista)
    return templates.TemplateResponse("/lista/listar_produtos.html", {"request":request, "itens_lista":itens_lista, "lista":lista})

@router.get("/remover_itens_lista/{id_lista:int}",response_class=HTMLResponse)
async def get_remover_itens_lista(request: Request, id_lista: int = 0):
    itens_lista = obter_itens_lista_nomes(id_lista)
    lista = obter_uma_lista(id_lista)
    return templates.TemplateResponse("/lista/remover_produtos.html", {"request":request, "itens_lista":itens_lista, "lista":lista})

@router.get("/alterar_lista/{id_lista:int}",response_class=HTMLResponse)
async def get_alterar_lista(request: Request, id_lista: int = 0):
    lista = obter_uma_lista(id_lista)
    return templates.TemplateResponse("/lista/alterar_lista.html", {"request":request, "lista":lista})

@router.get("/excluir/{id_lista:int}",response_class=RedirectResponse)
async def post_delete_lista(request: Request,id_lista: int=0):
    lista = obter_uma_lista(id_lista)
    return(templates.TemplateResponse("/lista/deletar_lista.html", {"request":request, "lista":lista}))

@router.post("/post_excluir_lista",response_class=RedirectResponse)
async def post_delete_lista(id_lista: int = Form()):
    print(f"Estou deletando a lista com ID={id_lista}")
    excluir_lista(id_lista)
    return RedirectResponse("/lista", status_code=status.HTTP_303_SEE_OTHER)


################ REVER
@router.get("/fechar_lista", response_class=HTMLResponse)
async def get_fechar_lista(request: Request, id_lista: int = 0):
    lista = obter_uma_lista(id_lista)
    return templates.TemplateResponse("/listar/fecha_lista.html", {"request":request, "lista":lista})

######### REVER
@router.post("/post_fechar_lista",response_class=RedirectResponse)
async def post_fechar_lista(id_lista: int = Form()):
    print(f"Estou FECHANDO a lista com ID={id_lista}")
    fechar_lista(id_lista)
    return RedirectResponse("/lista", status_code=status.HTTP_303_SEE_OTHER)

@router.post("/post_alterar_lista",response_class=RedirectResponse)
async def post_alterar_lista(
    id_lista: int = Form(),
    estabelecimento: str = Form(),
    id_user: int = Form(),
    status_lista: int = Form()):
    lista = Lista(id_lista,estabelecimento,id_user,status_lista)
    alterar_lista(lista)
    print(f"Estou alterando a {lista}")
    return RedirectResponse("/lista", status_code=status.HTTP_303_SEE_OTHER)
