class Disciplina():
    __id:int = -1
    __nome:str
    __carga_horaria:int
    __presencial:bool

    def get_id(self) -> int:
        return self.__id

    def set_id(self, id) -> None:
        self.__id = id

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str) -> None:
        self.__nome = nome

    def get_carga_horaria(self) -> int:
        return self.__carga_horaria

    def set_carga_horaria(self, carga_horaria: int) -> None:
        self.__carga_horaria = carga_horaria

    def get_presencial(self) -> bool:
        return self.__presencial

    def set_presencial(self, presencial: bool) -> None:
         self.__presencial = presencial
    
    def toDict(self):
        return {
            'id': self.get_id(),
            'nome': self.get_nome(),
            'carga_horaria': self.get_carga_horaria(),
            'presencial': self.get_presencial()
        }

    