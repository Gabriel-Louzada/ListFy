from dataclasses import dataclass
from typing import Optional



@dataclass
class Usuario():
    id_usuario: Optional[int] = None
    email: Optional[str] = None
    nome: Optional[str] = None
    senha: Optional[str] = None
    token: Optional[str] = None