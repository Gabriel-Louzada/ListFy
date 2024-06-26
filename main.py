from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from repo.categoria import *
from repo.denuncia import *
from repo.itens_lista import *
from repo.lista import *
from repo.produto import *
from repo.promocao import *
from repo.usuario import *
from routes import produto_routes,categoria_routes,lista_routes,main_router,usuario_routes,itens_lista_routes,promocao_routes,denuncia_routes
from util.auth import middleware_autenticacao
from util.exceptions import configurar_excecoes

criar_tabela_usuario()
criar_tabela_produto()
criar_tabela_categoria()
criar_tabela_lista()
criar_tabela_promocao()
criar_tabela_itens_lista()
criar_tabela_denuncia()

app = FastAPI()

templates = Jinja2Templates(directory = "templates")

app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
app.middleware(middleware_type="http")(middleware_autenticacao)
configurar_excecoes(app)
app.include_router(produto_routes.router)
app.include_router(categoria_routes.router)
app.include_router(lista_routes.router)
app.include_router(main_router.router)
app.include_router(usuario_routes.router)
app.include_router(itens_lista_routes.router)
app.include_router(promocao_routes.router)
app.include_router(denuncia_routes.router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)

#iniciar o servidor com o essa descrição a baixo no terminal
#uvicorn main:app --host 0.0.0.0 --port 8003