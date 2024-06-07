from dataclasses import dataclass
from typing import Optional



@dataclass
class Usuario():
    id_usuario: Optional[int] = None
    nome: Optional[str] = None
    email: Optional[str] = None
    senha: Optional[str] = None