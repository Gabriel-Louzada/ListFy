from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
import uvicorn

from repo.categoria import *
from repo.itens_lista import criar_tabela_itens_lista
from repo.lista import *
from repo.produto import *
from repo.promocao import criar_tabela_promocao
from repo.usuario import *
from routes import produto_routes,categoria_routes,lista_routes,main_router,usuario_routes

criar_tabela_usuario()
criar_tabela_produto()
criar_tabela_categoria()
criar_tabela_lista()
criar_tabela_promocao()
criar_tabela_itens_lista()

app = FastAPI()

#Esse objeto representa os arquivos HTML da pasta templates
templates = Jinja2Templates(directory = "templates")

app.include_router(produto_routes.router)
app.include_router(categoria_routes.router)
app.include_router(lista_routes.router)
app.include_router(main_router.router)
app.include_router(usuario_routes.router)

def obter_usuario_logado():
    return Usuario("Gabriel Louzada", False)

# roda o programa sem necessidade de abrir terminal
if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)