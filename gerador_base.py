from application.model.dao.periodo_dao import PeriodoDAO
from application.model.entity.disciplina import Disciplina
from application.model.entity.periodo import Periodo

periodo_dao = PeriodoDAO()

primeiro_periodo = Periodo()
primeiro_periodo.set_nome("Primeiro Periodo")
primeiro_periodo.set_disciplina([])

periodo_dao.inserir(primeiro_periodo)

eng_req = Disciplina()
eng_req.set_nome("Engenharia de Requisitos e Analise de Sistemas")
eng_req.set_presencial(True)
eng_req.set_carga_horaria(60)

segundo_periodo = Periodo()
segundo_periodo.set_nome("Segundo Periodo")
segundo_periodo.set_disciplina([eng_req])

periodo_dao.inserir(segundo_periodo)

lab_prog = Disciplina()
lab_prog.set_nome("Laboratório de Programação Hipermídia")
lab_prog.set_presencial(True)
lab_prog.set_carga_horaria(60)
iot = Disciplina()
iot.set_nome("Internet das Coisas")
iot.set_presencial(True)
iot.set_carga_horaria(60)

terceiro_periodo = Periodo()
terceiro_periodo.set_nome("Terceiro Periodo")
terceiro_periodo.set_disciplina([lab_prog, iot])

periodo_dao.inserir(terceiro_periodo)

lab_prog_inter = Disciplina()
lab_prog_inter.set_nome("Laboratório de Programação de Interfaces com o Usuário")
lab_prog_inter.set_presencial(True)
lab_prog_inter.set_carga_horaria(60)

quarto_periodo = Periodo()
quarto_periodo.set_nome("Quarto Periodo")
quarto_periodo.set_disciplina([lab_prog_inter])

periodo_dao.inserir(quarto_periodo)