from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from exts import db
from models import UserModel, CurrentModel, TargetModel
from blueprints.forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash


bp = Blueprint("auth", __name__, url_prefix="/")

@bp.route('/login', methods=['GET','POST'])
def login ():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = db.session.execute(db.select(UserModel).filter_by(email=email)).scalar()
            if not user:
                return render_template("notregistered.html")
            if check_password_hash(user.password, password):
                session['user_id']=user.id
                target = db.session.execute(db.select(TargetModel).filter_by(author_id=user.id)).scalar()
                if target.firsttime:
                    target.firsttime = 0
                    db.session.commit()
                    return redirect(url_for("progress.settarget"))
                else:
                    return redirect('/')
            else:
                return render_template("wronginfo.html")
        else:
            return render_template("wronginfo.html")




@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            firstname = form.firstname.data
            lastname = form.lastname.data
            email = form.email.data
            password = form.password.data
            username = firstname[0].upper() + lastname[0].upper()
            user = UserModel(username=username, firstname=firstname, lastname=lastname, email=email, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            user_id = user.id
            current = CurrentModel(author_id=user_id)
            target = TargetModel(author_id=user_id)
            db.session.add(target)
            db.session.add(current)
            db.session.commit()
            return render_template("registerok.html")
        else:
            if form.email.errors:
                return render_template("alreadyregistered.html")
            else:
                return redirect(url_for("auth.register"))

@bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')