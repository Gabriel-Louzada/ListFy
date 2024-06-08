from fastapi import APIRouter, Form, Request,status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from repo.categoria import *

router = APIRouter(prefix="/categorias")
templates = Jinja2Templates(directory = "templates")


@router.get("/", response_class=HTMLResponse)
async def get_listar_categoria(request: Request):
    categoria = obter_todas_categorias()
    return templates.TemplateResponse("/categoria/categorias.html",{"request":request, "categoria":categoria})

@router.get("/cadastrar_categoria", response_class=HTMLResponse)
async def get_cadastrar_categoria(request: Request):
    return templates.TemplateResponse("/categoria/cadastro_categoria.html",{"request":request})


@router.post("/post_cadastrar_categoria", response_class=RedirectResponse)
async def post_cad_categoria(
    nome_categoria: str = Form()):
    categoria = Categoria(0,nome_categoria)
    inserir_categoria(categoria)
    return RedirectResponse("/categorias", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/alterar_categoria/{id:int}",)
async def get_alterar_produto(request: Request, id: int=0):
    categoria = obter_uma_categoria(id)
    return templates.TemplateResponse("/categoria/alterar_categoria.html",{"request":request, "categoria":categoria})

@router.post("/post_alterar_categoria{id:int}", response_class=RedirectResponse)
async def post_cad_categoria(
    id_categoria: int = Form(),
    nome_categoria: str = Form()):
    categoria = Categoria(id_categoria,nome_categoria)
    inserir_categoria(categoria)
    return RedirectResponse("/categorias", status_code=status.HTTP_303_SEE_OTHER)