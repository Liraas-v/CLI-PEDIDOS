from dataclasses import dataclass
from typing import Optional


@dataclass
class Pedido:
    cliente: str
    servico: str
    valor: float
    status: str = "Em andamento"
    criado_em: Optional[str] = None
    id: Optional[int] = None
