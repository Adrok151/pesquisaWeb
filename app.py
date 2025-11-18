from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, Cargos


app = Flask(__name__)
app.config["SECRET_KEY"] = "chave_muito_secreta_aqui"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///meubanco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

with app.app_context():
    db.create_all()

    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin')
        admin.set_password('123')
        db.session.add(admin)

    if Cargos.query.count() == 0:
        dadosIniciais = [
            {'nome': 'Arquiteto de Soluções SR', 'salario': '30000', 'area': 'Técnico e Desenvolvimento'},
            {'nome': 'Arquiteto de Soluções SR', 'salario': '20000', 'area': 'Técnico e Desenvolvimento'},
            {'nome': 'Arquiteto de Soluções JR', 'salario': '10000', 'area': 'Técnico e Desenvolvimento'},
            {'nome': 'Arquiteto de Soluções JR', 'salario': '7000', 'area': 'Técnico e Desenvolvimento'},
            {'nome': 'Diretor de TI', 'salario': '71821', 'area': 'Liderança e Gestão'},
            {'nome': 'Diretor de TI', 'salario': '22049', 'area': 'Liderança e Gestão'},
            {'nome': 'Diretor de Tecnologia', 'salario': '51000', 'area': 'Liderança e Gestão'},
            {'nome': 'Diretor de Tecnologia', 'salario': '12000', 'area': 'Liderança e Gestão'},
            {'nome': 'Desenvolvedor de Software JR', 'salario': '4500', 'area': 'Técnico e Desenvolvimento'},
            {'nome': 'Desenvolvedor de Software JR', 'salario': '2000', 'area': 'Técnico e Desenvolvimento'},
            {'nome': 'Desenvolvedor de Software PL', 'salario': '8000', 'area': 'Técnico e Desenvolvimento'},
            {'nome': 'Desenvolvedor de Software PL', 'salario': '5000', 'area': 'Técnico e Desenvolvimento'},
            {'nome': 'Desenvolvedor de Software SR', 'salario': '12000', 'area': 'Técnico e Desenvolvimento'},
            {'nome': 'Desenvolvedor de Software SR', 'salario': '8000', 'area': 'Técnico e Desenvolvimento'},
            ]
        for itemData in dadosIniciais:
            novoItem = Cargos(
                nome=itemData['nome'],
                salario=itemData['salario'],
                area=itemData['area']
            )
            db.session.add(novoItem)
    db.session.commit()

def cargoParaDic(cargo):
    return {
        'id': cargo.id,
        'nome': cargo.nome,
        'salario': cargo.salario,
        'area': cargo.area
    }


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
            return redirect(url_for("pesquisa"))
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            flash("Login realizado com sucesso!", "success")
            return redirect(url_for("pesquisa"))
        else:
            flash("Usuário ou senha incorretos!", "danger")
            return render_template("login.html", error="Credenciais inválidas.")
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logout realizado.", "info")
    return redirect(url_for("login"))

@app.route("/pesquisa")
@login_required
def pesquisa():
    return render_template("pesquisa.html", user=current_user.username, usuarios = Cargos.query.all())

@app.route("/mostragem")
@login_required
def mostragem():
    busca = request.args.get("busca", "").lower()
    if busca:
        filtrados = Cargos.query.filter(
            (Cargos.nome.ilike(f"%{busca}%")) |
            (Cargos.area.ilike(f"%{busca}%"))
        ).all()
        if filtrados:
            filtradosDic = [cargoParaDic(cargo) for cargo in filtrados]
            return render_template("mostragem.html", usuarios = filtradosDic)
    return render_template("pesquisa.html", user=current_user.username, usuarios = Cargos.query.all(), error="Nenhum resultado encontrado")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)