from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from repo.categoria import *
from repo.itens_lista import criar_tabela_itens_lista
from repo.lista import *
from repo.produto import *
from repo.promocao import criar_tabela_promocao
from repo.usuario import *
from routes import produto_routes,categoria_routes,lista_routes,main_router,usuario_routes,itens_lista_routes

criar_tabela_usuario()
criar_tabela_produto()
criar_tabela_categoria()
criar_tabela_lista()
criar_tabela_promocao()
criar_tabela_itens_lista()

app = FastAPI()

templates = Jinja2Templates(directory = "templates")

app.mount(path="/static", app=StaticFiles(directory="static"), name="static")

app.include_router(produto_routes.router)
app.include_router(categoria_routes.router)
app.include_router(lista_routes.router)
app.include_router(main_router.router)
app.include_router(usuario_routes.router)
app.include_router(itens_lista_routes.router)

def obter_usuario_logado():
    return Usuario("Gabriel Louzada", False)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)

#iniciar o servidor com o essa descrição a baixo no terminal
#uvicorn main:app --host 0.0.0.0 --port 8003