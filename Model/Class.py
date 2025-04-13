from typing import List
from Specialization import Specialization


class Class:
    def __init__(self, class_id: int, nome: str):
        self.class_id = class_id  
        self.nome = nome  
        self.especializacoes: List['Specialization'] = []  

    def criar_classe(self, class_id: int, nome: str) -> 'Class':
        return Class(class_id, nome)

    def editar_classe(self, novo_nome: str) -> bool:
        self.nome = novo_nome
        return True

    def remover_classe(self) -> bool:
        return True 

    def adicionar_especializacao(self, especializacao: 'Specialization') -> bool:
        self.especializacoes.append(especializacao)
        return True

    def visualizar_lista_classes(self) -> List['Class']:
        return [self] 