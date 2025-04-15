
from flask  import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
#permissão: pip install flask-sqlalchemy


# a linha abaixo inicia a variavel de aplicação
#Se não colocar URI não tem como conectar o banco em pg html
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']  = \
    'mysql+pymysql://root:we123@localhost:3306/projeto_semestral'

#a linha abaixo instancia o banco de dados
db = SQLAlchemy(app)



class Cadastro_paciente(db.Model):
    nome = db.Column(db.String(200), nullable = False)
    cpf = db.Column(db.String(200), primary_key =True)
    email = db.Column(db.String(200),  nullable=False)
    senha = db.Column(db.String(200), nullable=False)

@app.route("/login")
def logar():
    return render_template("./login.html")


@app.route("/cadastrar")
def cadastrar_usuario():
    return render_template("./cadastrar.html")

@app.route("/resetar")
def resetar_senha():
    return  render_template("./resetarsenha.html")

@app.route("/add", methods = ['POST'])
def add_banco():
    nome_input = request.form['nome']
    cpf_input = request.form['cpf']
    email_input = request.form['email']
    senha_input = request.form['senha']
    
    novo_usuario = Cadastro_paciente(nome = nome_input, cpf = cpf_input, email = email_input, senha = senha_input)

        #a linha abaixo adiciona os dados para verificação da entrada de dados
    db.session.add(novo_usuario)


    #a linha abaixo grava as alterações no banco de dados
    db.session.commit()

    return render_template("./cadastrar.html")

app.run(debug=True)