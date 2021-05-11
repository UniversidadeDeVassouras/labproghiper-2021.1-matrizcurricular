class PreInscricao:

    def __init__(self):
        self.__id: int
        self.__nome: str
        self.__idade: int
        self.__documento: str
        self.__observacoes: str

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, value):
        self.__idade = value

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, value):
        self.__documento = value

    @property
    def observacoes(self):
        return self.__observacoes

    @observacoes.setter
    def observacoes(self, value):
        self.__observacoes = value

    def toDict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'observacoes': self.observacoes
        }
