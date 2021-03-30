from application.model.entity.disciplina import Disciplina
import json
import os
from typing import List

class DisciplinaDAO():

    def __init__(self):
        disciplina = Disciplina()
        disciplina.set_id(1)
        disciplina.set_nome('Laboratório de Programação Hipermídia')
        disciplina.set_carga_horaria(60)
        disciplina.set_presencial(True)
        with open('data.json', 'w') as outfile:
            json.dump(disciplina.toDict(), outfile)


    def busca_por_periodo(self, periodo: int) -> List[Disciplina]:
        with open('data.json', 'w') as outfile:
            json.load(outfile)
        