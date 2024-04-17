from dataclasses import dataclass
from Pessoa import Pessoa
from Marca import Marca

@dataclass
class Veiculo:
    placa: str
    cor: str
    proprietario: Pessoa
    Marca: Marca