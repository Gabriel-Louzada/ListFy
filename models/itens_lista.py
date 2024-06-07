from dataclasses import dataclass
from typing import Optional


@dataclass
class Itens_lista():
    id_produto: Optional[int] = None
    quantidade: Optional[int] = None
    id_lista: Optional[int] = None
