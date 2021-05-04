from application.model.entity.periodo import Periodo
from application.model.dao.periodo_dao import PeriodoDAO
from flask import render_template, request
from application import app


@app.route('/')
def home():
    periodo_lista = PeriodoDAO().listar_todos()
    return render_template("index.html", periodo_list=periodo_lista)


@app.route('/<int:id>')
def periodo(id: int):
    periodo_lista = PeriodoDAO().listar_todos()
    if id:
        periodo = PeriodoDAO().busca_por_id(id)
        return render_template("index.html", periodo_list=periodo_lista, periodo_selecionado=periodo)
    return render_template("index.html", periodo_list=periodo_lista)
