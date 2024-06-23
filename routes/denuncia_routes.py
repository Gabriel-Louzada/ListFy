from fastapi import APIRouter, Form, Request,status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from repo.denuncia import *
from repo.promocao import *


router = APIRouter(prefix="/denuncia")
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def get_denuncias(request: Request):
    denuncias = obter_todas_denuncias()
    return templates.TemplateResponse("/denuncias/listar_denuncias.html",{"request":request, "denuncias":denuncias})

@router.get("/cadastrar/{id_usuario:int}", response_class=HTMLResponse)
async def get_cadastrar_denuncias(request: Request):
    return templates.TemplateResponse("/denuncias/cadastrar_denuncia.html",{"request":request})

@router.get("/promocao/{id_lista:int}/{id_produto:int}/{nome_produto:str}/{estabelecimento:str}", response_class=HTMLResponse)
async def get_cadastrar_denuncias(request: Request, id_lista: int=0, id_produto:int=0, nome_produto:str='', estabelecimento:str=''):
    promocao = Promocao(id_produto,0,id_lista,estabelecimento,nome_produto)
    return templates.TemplateResponse("/denuncias/cadastrar_denuncia_promocao.html",{"request":request, "promocao":promocao})

@router.get("/ver/{id_denuncia:int}", response_class=HTMLResponse)
async def get_ver_denuncia(request: Request, id_denuncia:int=0):
    denuncia = obter_denuncia_por_id(id_denuncia)
    return templates.TemplateResponse("/denuncias/ver_denuncia.html",{"request":request, "denuncia":denuncia})

@router.post("/post_cadastrar_denuncia", response_class=RedirectResponse)
async def post_cadastrar_denuncia(
    id_usuario: int=Form(),
    assunto: str=Form(),
    descricao: str=Form()):
    denuncia = Denuncia(0,id_usuario,assunto, descricao)
    inserir_denuncia(denuncia)
    return RedirectResponse("/denuncia", status_code=status.HTTP_303_SEE_OTHER)
