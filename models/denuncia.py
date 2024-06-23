from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Denuncia():
    id_denuncia: Optional[int] = None
    id_usuario: Optional[int] = None
    assunto: Optional[str] = None
    descricao: Optional[str] = None
    data: Optional[date] = None
