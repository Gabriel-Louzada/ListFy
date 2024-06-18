from dataclasses import dataclass
from typing import Optional

@dataclass
class Itens_lista():
    id_produto: Optional[int] = None
    id_lista: Optional[int] = None
    quantidade: Optional[float] = None
    valor_produto: Optional[float] = None
    nome_produto: Optional[str] = None
