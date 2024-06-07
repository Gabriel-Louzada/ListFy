from dataclasses import dataclass
from typing import Optional



@dataclass
class Lista():
    id_lista: Optional[int] = None
    estabelecimento: Optional[str] = None
    id_user: Optional[int] = None
    status_lista: Optional[int] = None