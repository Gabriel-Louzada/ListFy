from dataclasses import dataclass
from typing import Optional


@dataclass
class Promocao():
    id_promocao: Optional[int] = None
    id_produto: Optional[int] = None
    valor_promocao: Optional[float] = None
    estabelecimento: Optional[str] = None
    nome_produto: Optional[str] = None