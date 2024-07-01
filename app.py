from conf import *
from model import *

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/listar_livros")
def listar_livros():
    with db_session:
    
        livros = Livros.select() 
        return render_template("listar_livros.html", livros=livros)

@app.route("/form_adicionar_livros")
def form_adicionar_livros():
    return render_template("form_adicionar_livros.html")

@app.route("/adicionar_livro")
def adicionar_livro():

    nome = request.args.get("nome")
    autor = request.args.get("autor")
    ano = request.args.get("ano")
    genero = request.args.get("genero")
    classificacao = request.args.get("classificacao")
    avaliacao = request.args.get("avaliacao")

    # salvar
    with db_session:
        p = Livros(**request.args)
        # salvar
        commit()
        # encaminhar de volta para a listagem
        return redirect("listar_livros") 

'''
run:
$ flask run
'''
