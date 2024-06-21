import secrets
from typing import Optional
import bcrypt
from fastapi import HTTPException, Request, status
from models.usuario import Usuario
from repo.usuario import obter_por_token


NOME_COOKIE_AUTH = "token"


async def obter_usuario_logado(request: Request) -> Optional[Usuario]:
    try:
        token = request.cookies[NOME_COOKIE_AUTH]
        if token.strip() == "":
            return None
        usuario = obter_por_token(token)
        print(usuario)
        return usuario
    except KeyError:
        return None


def obter_hash_senha(senha: str) -> str:
    try:
        hashed = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
        return hashed.decode()
    except ValueError:
        return ""


def conferir_senha(senha: str, hash_senha: str) -> bool:
    try:
        return bcrypt.checkpw(senha.encode(), hash_senha.encode())
    except ValueError:
        return False


def gerar_token(length: int = 32) -> str:
    try:
        return secrets.token_hex(length)
    except ValueError:
        return ""


def adicionar_cookie_autenticacao(response, token):
    response.set_cookie(
        key=NOME_COOKIE_AUTH,
        value=token,
        max_age=1800,
        httponly=True,
        samesite="Lax",
    )
    return response


def excluir_cookie_autenticacao(response):
    response.set_cookie(
        key=NOME_COOKIE_AUTH,
        value=" ",
        httponly=True,
        expires=0,
    )
    return response


async def middleware_autenticacao(request: Request, call_next):
    usuario = await obter_usuario_logado(request)
    request.state.usuario = usuario #desta forma eu pego o usuario que esta no corpo do requisição
    response = await call_next(request)
    if response.status_code == status.HTTP_303_SEE_OTHER:
        return response
    if usuario:
        token = request.cookies[NOME_COOKIE_AUTH]
        adicionar_cookie_autenticacao(response, token)
    return response


def checar_autorizacao(request: Request):
    if not request.state.usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)