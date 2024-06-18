from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from models.usuario import Usuario
from repo.usuario import inserir_usuario, obter_um_usuario


router = APIRouter(prefix="/usuario")
templates = Jinja2Templates(directory = "templates")

@router.get("/entrar",response_class=HTMLResponse)
async def get_entrar(request: Request):
    return templates.TemplateResponse("/usuario/login.html",{"request":request})

@router.get("/cadastrar",response_class=HTMLResponse)
async def get_cadastrar(request: Request):
    return templates.TemplateResponse("/usuario/cadastrar_usuario.html",{"request":request})

@router.post("/post_entrar",response_model_include=RedirectResponse)
async def post_entrar_usuario( email: str = Form(),senha: str = Form()):
    usuario = obter_um_usuario(senha,email)
    return templates.TemplateResponse("/lista")


@router.post("/post_cadastrar_usuario",response_class=RedirectResponse)
async def post_cad_usuario(
    nome: str = Form(),
    email: str = Form(),
    senha: str = Form()):
    usuario = Usuario(0,nome,email,senha)
    inserir_usuario(usuario)
    return RedirectResponse("/usuario/entrar")
