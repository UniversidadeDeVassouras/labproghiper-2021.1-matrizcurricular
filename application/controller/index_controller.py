from application.model.dao.periodo_dao import PeriodoDAO
from flask import render_template, request
from application import app
from application.model.entity.preinscricao import PreInscricao
from application.model.dao.preinscricao_dao import PreInscricaoDao


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


@app.route("/pre-inscricao", methods=['GET', 'POST'])
def preinscricao():
    if request.method == 'POST':
        pre_inscricao = PreInscricao()
        pre_inscricao.nome = request.form.get('nome', None)
        pre_inscricao.idade = request.form.get('idade', None)
        pre_inscricao.observacoes = request.form.get('observacoes', None)
        PreInscricaoDao().inserir(pre_inscricao)
    return render_template("preinscricao.html")
