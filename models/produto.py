from dataclasses import dataclass
from typing import Optional


@dataclass
class Produto():
    id_produto: Optional[int] = None
    nome_produto: Optional[str] = None
    id_categoria: Optional[int] = None
    valor_produto: Optional[float] = None
