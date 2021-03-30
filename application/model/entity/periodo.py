from typing import List
from application.model.entity.disciplina import *

class Periodo:
    __id:int
    __nome:str
    __disciplinas: List[Disciplina] = []

    def get_id(self) -> int:
        return self.__id
        
    def set_id(self, id:int) -> None:
        self.__id = id
    
    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome:str) -> None:
        self.__nome = nome
        
    def get_disciplina(self) -> List[Disciplina]:
        return self.__disciplinas

    def set_disciplina(self, disciplinas:List[Disciplina]) -> None:
        self.__disciplinas = disciplinas

    def add_disciplina(self, disciplina: Disciplina) -> None:
        self.__disciplinas.append(disciplina)