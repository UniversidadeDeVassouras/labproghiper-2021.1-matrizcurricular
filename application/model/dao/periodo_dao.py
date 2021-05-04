from application.model.entity.periodo import Periodo
from application.model.entity.disciplina import Disciplina
import json
from typing import List


class PeriodoDAO():

    def inserir(self, periodo: Periodo) -> None:
        periodo_list = self.listar_todos()
        periodo.set_id(len(periodo_list) + 1)
        periodo_list.append(periodo)
        dict_list = self.__converter_periodolist_dictlist(periodo_list)
        with open('periodo.json', 'w') as file:
            json.dump(dict_list, file)

    def busca_por_id(self, periodo_id: int) -> Periodo:
        with open('periodo.json', 'r') as file:
            periodo_list = json.load(file)
            for periodo in self.__converter_dictlist_periodolist(periodo_list):
                if periodo.get_id() == periodo_id:
                    return periodo
        return None

    def listar_todos(self) -> List[Periodo]:
        result = []
        with open('periodo.json', 'r') as file:
            periodo_list = json.load(file)
            result = self.__converter_dictlist_periodolist(periodo_list)
        return result

    def __converter_periodolist_dictlist(self, periodo_list: List[Periodo]) -> List:
        result = []
        for periodo in periodo_list:
            result.append(periodo.toDict())
        return result

    def __converter_dictlist_periodolist(self, periodo_list: List) -> List[Periodo]:
        result = []
        for periodo_dict in periodo_list:
            periodo = Periodo()
            periodo.set_id(periodo_dict['id'])
            periodo.set_nome(periodo_dict['nome'])
            disciplina_list = []
            for disciplina_dict in periodo_dict['disciplinas']:
                disciplina = Disciplina()
                disciplina.set_id(disciplina_dict['id'])
                disciplina.set_nome(disciplina_dict['nome'])
                disciplina.set_presencial(disciplina_dict['presencial'])
                disciplina.set_carga_horaria(disciplina_dict['carga_horaria'])
                disciplina_list.append(disciplina)
            periodo.set_disciplina(disciplina_list)
            result.append(periodo)
        return result
