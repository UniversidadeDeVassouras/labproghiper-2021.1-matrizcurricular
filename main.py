from flask import Flask
import os
from application.model.dao.disciplina_dao import DisciplinaDAO

DisciplinaDAO()

app = Flask(__name__, template_folder=os.path.abspath('application/view/templates'), static_folder=os.path.abspath("application/view/static"))
