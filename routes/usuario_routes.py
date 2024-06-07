from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from models.usuario import Usuario
from repo.usuario import inserir_usuario


router = APIRouter(prefix="/usuario")
templates = Jinja2Templates(directory = "templates")

@router.get("/entrar",response_class=HTMLResponse)
async def get_cadastrar_usuario(request: Request):
    return templates.TemplateResponse("/usuario/cadastro_usuario.html",{"request":request})

@router.post("/post_cadastrar_usuario",response_class=RedirectResponse)
async def post_cad_usuario(
    nome: str = Form(),
    email: str = Form(),
    senha: str = Form()):
    usuario = Usuario(0,nome,email,senha)
    inserir_usuario(usuario)
    return RedirectResponse("/usuario/entrar")
