from fastapi import Response

def adicionar_cookie_mensagem(reponse: Response, mensagem: str):
    reponse.set_cookie(
        key="mensagem",
        value=mensagem,
        max_age=1,
        httponly=True,
        samesite="lax"
    )