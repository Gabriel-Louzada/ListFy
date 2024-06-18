from dataclasses import dataclass
from typing import Optional


@dataclass
class Promocao():
    id_produto: Optional[int] = None
    valor_promocao: Optional[float] = None
    id_lista: Optional[int] = None
    estabelecimento: Optional[str] = None
    nome_produto: Optional[str] = None