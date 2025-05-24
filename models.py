from exts import db
from datetime import datetime
from sqlalchemy import CheckConstraint


class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable = False, unique = True)
    reg_time = db.Column(db.DateTime, default=datetime.now)


class TargetModel(db.Model):
    __tablename__ = "target"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    targetleetcode = db.Column(db.Integer, CheckConstraint('targetleetcode >=1 AND targetleetcode <=9999'), nullable=True)
    targetproject = db.Column(db.Integer, CheckConstraint('targetleetcode >=1 AND targetleetcode <=10'), nullable=True)
    targetdate = db.Column(db.Date, nullable=True)
    startdate = db.Column(db.Date, nullable=True)
    firsttime = db.Column(db.Boolean, default=True, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    author = db.relationship(UserModel, backref="targets")


class CurrentModel(db.Model):
    __tablename__ = "current"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    currentleetcode = db.Column(db.Integer, CheckConstraint('currentleetcode >=0 AND currentleetcode <=9999'), default=0, nullable=True)
    currentproject = db.Column(db.Integer, CheckConstraint('currentproject >=1 AND currentproject <=10'), default=0, nullable=True)
    currentinterview = db.Column(db.Integer, CheckConstraint('currentinterview >=1 AND currentinterview <=10'), default=0, nullable=True)
    resume = db.Column(db.Boolean, default=False, nullable=True)
    bq = db.Column(db.Boolean, default=False, nullable=True)
    tq = db.Column(db.Boolean, default=False, nullable=True)
    mock = db.Column(db.Boolean, default=False, nullable=True)

    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    author = db.relationship(UserModel, backref="currents")



