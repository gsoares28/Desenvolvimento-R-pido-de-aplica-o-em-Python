import os
import sqlite3
from Pessoa import  Pessoa  
from Marca import Marca
from Veiculo import Veiculo

class BancoDeDados:
    def __init__(self, nome_banco="banco.sqlite"):
        self.nome_banco = os.path.join(os.path.dirname(__file__), nome_banco)
        self.conn = None
    def conectar(self):
        try:
            self.conn = sqlite3.connect(self.nome_banco)
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
    def criar_tabela_pessoa(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                         """CREATE TABLE IF NOT EXISTS Pessoa(
                                cpf INTEGER PRIMARY Key,
                                nome TEXT NOT FULL,
                                nascimento DATE,
                                oculos BOOLEAN
                                )"""   
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao criar tabela Pessoa: {e}")
    def criar_tabela_marca(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                         """CREATE TABLE IF NOT EXISTS Marca(
                                id INTEGER PRIMARY KEY,
                                nome TEXT NOT FULL,
                                sigla TEXT NOT NULL,
                                )"""   
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao criar tabela marca: {e}")
    def criar_tabela_veiculo(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                         """CREATE TABLE IF NOT EXISTS Veiculo(
                                placa TEXT PRIMARY KEY,
                                cor TEXT NOT FULL,
                                cpf_proprietario INTEGER,
                                id_marca INTEGER,
                                FOREGEIN KEY(cpf_proprietario) REFERENCES Pessoa(cpf), FOREGEIN KEY(id_marca) REFERENCES Marca(id)
                                )"""   
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao criar tabela Veiculo: {e}")
    def inserir_pessoa(self, pessoa: Pessoa):
        if self.comn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO Pessoas VALUES(?,?,?,?)",(pessoa.cpf, pessoa.nome, pessoa.nascimento, pessoa.oculos),)
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"Erro ao inserir pessoa:{e}")
    
                
    def inserir_veiculo(self, veiculo:Veiculo):
         if self.comn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO Veiculo VALUES(?,?,?,?),"
                (
                    veiculo.placa,
                    veiculo.cor, 
                    veiculo.proprietario.cpf,
                    veiculo.marca,id
                ),
                )
   
                self.conn.commit()
            except sqlite3.Error as e:
                    print(f"Erro ao inserir Veiculo:{e}")
                
            """def atualizar_pessoa(self, pessoa):
                if self.conn:
                    try:
                        cursor = self.conn.cursor()
                        cursor.execute("UPDATE Pessoa SET nome =?, nascimento=?, oculos=? WHERE cpf=?",
                        (pessoa.nome pessoa.nascimento,pessoa.oculos, pessoa.cpf))
                
                        self.conn.commit()
                    except sqlite3.Error as e:
                        print(f"Erro ao atualizar Pessoa:{e}")"""
                        
    def atualizar_pessoa(self, pessoa):
     if self.conn:
        try:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE Pessoa SET nome=?, nascimento=?, oculos=? WHERE cpf=?",
                           (pessoa.nome, pessoa.nascimento, pessoa.oculos, pessoa.cpf))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao atualizar Pessoa: {e}")

            
            
            def apagar_veiculo(self, veiculo):
                if self.conn:
                    try:
                        cursor = self.conn.cursor()
                        cursor.execute("DELETE FROM Veiculo WHERE placa =?",(veiculo.placa))
                        self.conn.commit()
                    except sqlite3.Error as e:
                        print(f"Erro ao apagar Veiculo:{e}")        
            
    def criar_tabelas(self):
        self.criar_tabelas()
        self.criar_tabelas_marcas()
        self.criar_tabelas_veiculo()
        
def buscar_todas_pessoas(self):
    pessoas = []
    if self.conn:
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM pessoa")
            for row in cursor.fetchall():
                cpf, nome, nascimento, oculos = row 
                pessoas.append(Pessoa(cpf, nome, nascimento, oculos))
        except sqlite3.Error as e:
            print(f"Erro ao buscar pessoas: {e}")
    return pessoas


def buscar_todos_veiculos(self):
    veiculos = []
    if self.conn:
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Veiculo")
            for row in cursor.fetchall():
                placa, cor, cpf_proprietario, id_marca = row
                proprietario = self.buscar_pessoa_por_cpf(cpf_proprietario)
                marca = self.buscar_marca_por_id(id_marca)
                veiculos.append(Veiculo(placa,cor,proprietario,marca))
        except sqlite3.Error as e:
            print(f"Erro ao buscar veículo: {e}")
    return veiculos    
                
def buscar_pessoa_por_cpf(self, cpf: int):
    if self.conn:
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Pessoa WHERE cpf=?" , (cpf,))
            row = cursor.fetchone()
            if row:
                cpf, nome, nascimento, oculos = row
                return Pessoa(cpf, nome, nascimento, oculos)
        except sqlite3.Error as e:
            print(f"Erro ao buscar pessoa por CPF: {e}")
    return None

def buscar_marca_por_id(self, id: int):
    if self.conn:
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Marca WHERE id=?" , (id,))
            row = cursor.fetchone()
            if row:
                id, nome, sigla = row
                return Marca(id, nome, sigla)
        except sqlite3.Error as e:
            print(f"Erro ao buscar marca por ID: {e}")
    return None

def fechar_conexao(self):
    if self.conn:
        self.conn.close()
        self.conn = None