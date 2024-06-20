from fastapi import APIRouter, Form, Request,status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from models.usuario import Usuario
from repo.usuario import *
from util.auth import *
from util.cookies import adicionar_cookie_mensagem


router = APIRouter(prefix="/usuario")
templates = Jinja2Templates(directory = "templates")

@router.get("/entrar",response_class=HTMLResponse)
async def get_entrar(request: Request):
    return templates.TemplateResponse("/usuario/login.html",{"request":request})

@router.get("/cadastrar",response_class=HTMLResponse)
async def get_cadastrar(request: Request):
    return templates.TemplateResponse("/usuario/cadastrar_usuario.html",{"request":request})

@router.post("/post_entrar",response_model_include=RedirectResponse)
async def post_entrar_usuario(email: str = Form(),senha: str = Form()):
    usuario = obter_por_email(email)
    if not conferir_senha(senha, usuario.senha):
        response = RedirectResponse("/usuario/entrar", status_code=status.HTTP_302_FOUND)
        adicionar_cookie_mensagem(response, "Credenciais inválidas. Tente novamente.")
        return response
    
    token = gerar_token()
    alterar_token(usuario.id_usuario, token)
    response = RedirectResponse("/lista", status_code=status.HTTP_302_FOUND)
    adicionar_cookie_mensagem(response, f"Seja Bem vindo(a) a ListFy <b>{usuario.nome}</b>")
    adicionar_cookie_autenticacao(response, token)
    return response

@router.post("/post_cadastrar_usuario")
async def post_cad_usuario(
    nome: str = Form(),
    email: str = Form(),
    senha: str = Form(),
    conf_senha: str = Form()):

    #Condicional se senha é igual a senha 
    if senha != conf_senha:
        response = RedirectResponse("/usuario/cadastrar", status_code=status.HTTP_302_FOUND)
        adicionar_cookie_mensagem(response, f"A Senhas não conferem",)
        return response
    
    #transformo a senha em uma criptografada (hash)
    senha_hash = obter_hash_senha(senha)
    #crio um objeto usuario
    usuario = Usuario(0, nome, email, senha_hash, "")

    #para esta parte funcionar é necessario que o usuario retorne algo, nesse caso ele me retorna o usuario ou None
    if inserir_usuario(usuario):
        response = RedirectResponse("/usuario/entrar", status_code=status.HTTP_302_FOUND)
        adicionar_cookie_mensagem(response, f"Usuário <b>{nome}</b> cadastrado com sucesso! Use suas credenciais para entrar.",)
        return response
    else:
        response = RedirectResponse("/usuario/cadastrar", status_code=status.HTTP_302_FOUND)
        adicionar_cookie_mensagem(response, f"Não foi possivel realizar o cadastro.",)
        return response
