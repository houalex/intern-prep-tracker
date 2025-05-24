from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify,g

from decorators import loginrequired
from exts import db
from models import TargetModel, UserModel, CurrentModel
from blueprints.forms import TargetForm, CurrentForm
from datetime import datetime


bp = Blueprint("progress", __name__, url_prefix="/")


@bp.route('/')
def index():
    if g.user:
        user_id = session['user_id']
        target = db.session.execute(db.select(TargetModel).filter_by(author_id=user_id)).scalar()
        current = db.session.execute(db.select(CurrentModel).filter_by(author_id=user_id)).scalar()

        currentdate = datetime.today().date()
        targetdate = target.targetdate
        startdate = target.startdate
        if targetdate is None or startdate is None or startdate>currentdate or currentdate>targetdate:
            progresstodate = 0
        else:
            dayspassed = (currentdate - startdate).days
            totaldays = (targetdate - startdate).days
            if totaldays>0:
                progresstodate = round((dayspassed/totaldays)*100)
            else:
                progresstodate = 0

        targetleetcode = target.targetleetcode
        currentleetcode = current.currentleetcode
        if targetleetcode is None or currentleetcode is None:
            leetcodeprogress = 0
        else:
            if currentleetcode>=targetleetcode:
                leetcodeprogress = 100
            else:
                leetcodeprogress = round((currentleetcode/targetleetcode)*100)

        targetproject = target.targetproject
        currentproject = current.currentproject
        if targetproject is None or currentproject is None:
            projectprogress = 0
        else:
            if currentproject>=targetproject:
                projectprogress = 100
            else:
                projectprogress = round((currentproject/targetproject)*100)

        resume = 1 if current.resume is True else 0
        bq = 1 if current.bq is True else 0
        tq = 1 if current.tq is True else 0
        mock = 1 if current.mock is True else 0
        interviewprogress = round((resume+bq+tq+mock)/4*100)

        currentprogress = round(leetcodeprogress*0.4+projectprogress*0.4+interviewprogress*0.2)

        if currentprogress >= progresstodate:
            barcolor = "#87ceeb"
        else:
            barcolor = "#8b0000"
    else:
        leetcodeprogress = 0
        projectprogress = 0
        interviewprogress = 0
        currentprogress = 0
        progresstodate = 0
        barcolor = "#4caf50"
    return render_template("index.html",
                           leetcodeprogress=leetcodeprogress,
                           projectprogress=projectprogress,
                           interviewprogress=interviewprogress,
                           currentprogress=currentprogress,
                           progresstodate=progresstodate,
                           barcolor=barcolor)


@bp.route('/leetcode', methods=['GET', 'POST'])
@loginrequired
def leetcode():
    user_id = session['user_id']
    current = db.session.execute(db.select(CurrentModel).filter_by(author_id=user_id)).scalar()
    target = db.session.execute(db.select(TargetModel).filter_by(author_id=user_id)).scalar()

    if request.method == "GET":
        currentdate = datetime.today().date()
        targetdate = target.targetdate
        startdate = target.startdate
        if targetdate is None or startdate is None or startdate > currentdate or currentdate > targetdate:
            progresstodate = 0
        else:
            dayspassed = (currentdate - startdate).days
            totaldays = (targetdate - startdate).days
            if totaldays > 0:
                progresstodate = round((dayspassed / totaldays) * 100)
            else:
                progresstodate = 0

        targetleetcode = target.targetleetcode
        currentleetcode = current.currentleetcode
        if targetleetcode is None or currentleetcode is None:
            leetcodeprogress = 0
        else:
            if currentleetcode >= targetleetcode:
                leetcodeprogress = 100
            else:
                leetcodeprogress = round((currentleetcode / targetleetcode) * 100)

        return render_template("leetcode.html",
                               currentleetcode=currentleetcode,
                               leetcodeprogress=leetcodeprogress,
                               progresstodate= progresstodate)
    else:
        form = CurrentForm(request.form)
        if form.validate():
            current.currentleetcode = form.currentleetcode.data
            db.session.commit()
        else:
            redirect(url_for("progress.leetcode"))
    return redirect(url_for("progress.leetcode"))



@bp.route('/project', methods=['GET', 'POST'])
@loginrequired
def project():
    user_id = session['user_id']
    current = db.session.execute(db.select(CurrentModel).filter_by(author_id=user_id)).scalar()
    target = db.session.execute(db.select(TargetModel).filter_by(author_id=user_id)).scalar()

    if request.method == "GET":
        currentdate = datetime.today().date()
        targetdate = target.targetdate
        startdate = target.startdate
        if targetdate is None or startdate is None or startdate > currentdate or currentdate > targetdate:
            progresstodate = 0
        else:
            dayspassed = (currentdate - startdate).days
            totaldays = (targetdate - startdate).days
            if totaldays > 0:
                progresstodate = round((dayspassed / totaldays) * 100)
            else:
                progresstodate = 0

        targetproject = target.targetproject
        currentproject = current.currentproject
        if targetproject is None or currentproject is None:
            projectprogress = 0
        else:
            if currentproject >= targetproject:
                projectprogress = 100
            else:
                projectprogress = round((currentproject / targetproject) * 100)

        return render_template("project.html",
                               currentproject=currentproject,
                              projectprogress=projectprogress,
                               progresstodate= progresstodate)
    else:
        form = CurrentForm(request.form)
        if form.validate():
            current.currentproject = form.currentproject.data
            db.session.commit()
        else:
            redirect(url_for("progress.project"))
    return redirect(url_for("progress.project"))


@bp.route('/interview', methods=['GET', 'POST'])
@loginrequired
def interview():
    user_id = session['user_id']
    current = db.session.execute(db.select(CurrentModel).filter_by(author_id=user_id)).scalar()
    target = db.session.execute(db.select(TargetModel).filter_by(author_id=user_id)).scalar()

    resume = 1 if current.resume is True else 0
    bq = 1 if current.bq is True else 0
    tq = 1 if current.tq is True else 0
    mock = 1 if current.mock is True else 0


    if request.method == "GET":
        currentdate = datetime.today().date()
        targetdate = target.targetdate
        startdate = target.startdate
        if targetdate is None or startdate is None or startdate > currentdate or currentdate > targetdate:
            progresstodate = 0
        else:
            dayspassed = (currentdate - startdate).days
            totaldays = (targetdate - startdate).days
            if totaldays > 0:
                progresstodate = round((dayspassed / totaldays) * 100)
            else:
                progresstodate = 0

        currentinterview = resume + bq + tq + mock
        interviewprogress = round(currentinterview/4*100)

        return render_template("interview.html",
                              interviewprogress=interviewprogress,
                               progresstodate= progresstodate,
                               resume = resume,
                               bq = bq,
                               tq = tq,
                               mock = mock)
    else:
        form = CurrentForm(request.form)
        if form.validate():
            current.resume = form.resume.data
            current.bq = form.bq.data
            current.tq = form.tq.data
            current.mock = form.mock.data
            db.session.commit()
        else:
            redirect(url_for("progress.interview"))
    return redirect(url_for("progress.interview"))


@bp.route('/settartget', methods=['GET', 'POST'])
@loginrequired
def settarget():
    user_id = session["user_id"]
    if request.method == 'GET':
        today = datetime.today().date()
        target = db.session.execute(db.select(TargetModel).filter_by(author_id=user_id).order_by(TargetModel.id.desc())).scalar()
        return render_template("settarget.html",target=target, today=today)
    else:
        form = TargetForm(request.form)
        if form.validate():
            targetleetcode = form.targetleetcode.data
            targetproject = form.targetproject.data
            targetdate = form.targetdate.data
            if form.startdate.data is None:
                startdate = datetime.today().date()
            else:
                startdate = form.startdate.data
            target = db.session.execute(db.select(TargetModel).filter_by(author_id=user_id)).scalar()
            if target is None:
                target = TargetModel(targetleetcode=targetleetcode, targetproject=targetproject,
                                     targetdate=targetdate, startdate=startdate, author=g.user)
                db.session.add(target)
            else:
                if targetleetcode:
                    target.targetleetcode = targetleetcode
                if targetproject:
                    target.targetproject = targetproject
                if targetdate:
                    target.targetdate = targetdate
                if startdate:
                    target.startdate = startdate
            db.session.commit()
            return redirect('/')
        else:
            return redirect(url_for("progress.settarget"))