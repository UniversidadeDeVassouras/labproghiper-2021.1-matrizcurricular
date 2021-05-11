import json
from typing import List

from application.model.entity.preinscricao import PreInscricao


class PreInscricaoDao:

    def inserir(self, pre_inscricao: PreInscricao):
        pre_inscricao_list = self.listar_todos()
        pre_inscricao.id = len(pre_inscricao_list) + 1
        pre_inscricao_list.append(pre_inscricao)
        pre_inscricao_dict_list = []
        for pre_inscricao in pre_inscricao_list:
            pre_inscricao_dict_list.append(pre_inscricao.toDict())
        with open('preinscricao.json', 'w') as file:
            json.dump(pre_inscricao_dict_list, file)

    def listar_todos(self) -> List[PreInscricao]:
        result = []
        with open("preinscricao.json", 'r') as file:
            preinscrica_dict_list = json.load(file)
            for preinscricao_dict in preinscrica_dict_list:
                pre_inscricao = PreInscricao()
                pre_inscricao.id = preinscricao_dict.get('id', None)
                pre_inscricao.nome = preinscricao_dict.get('nome', None)
                pre_inscricao.idade = preinscricao_dict.get('idade', None)
                pre_inscricao.documento = preinscricao_dict.get('documento', None)
                pre_inscricao.observacoes = preinscricao_dict.get('observacoes', None)
                result.append(pre_inscricao)
        return result
