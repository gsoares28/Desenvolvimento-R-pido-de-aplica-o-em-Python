from datetime import date
from Pessoa import	Pessoa
from Main import Main
from Marca import Marca
from Veiculo import Veiculo
from banco import banco

pessoa1 = Pessoa(cpf=123456789000, nome="Raphael", nascimento=date(1984, 7, 26), oculos=True)

marca1 = Marca(id=1, nome = "Fiat", sigla ="FIA")

veiculo1 = Veiculo(placa="LRW1I27", cor="Cinza", proprietario=pessoa1, Marca=marca1)


print("\nMarcas:")
for marca in banco.buscar_todas_marcas():
    print(marca)    
print("\nVeículo:")
for veiculo in banco.buscar_todos_veiculos():
    print(veiculo)
    
banco.fechar_conexao()

