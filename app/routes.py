from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Tasks


main = Blueprint('main', __name__)

@main.route('/')
def index():
    tasks = Tasks.query.all()
    return render_template("index.html",tasks=tasks)

@main.route('/append',methods=["POST"])
def append():
    task = request.form["task"]

    new_task = Tasks(task=task)

    db.session.add(new_task)
    db.session.commit()

    return redirect(url_for('main.index'))

@main.route("/status",methods=["POST"])
def status():
    task_id = request.form["id"]
    task = Tasks.query.filter_by(id=task_id).first()
    if task.status:
        task.status = False
    else:
        task.status = True
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route("/delete")
def delete():
    task_id = request.args.get('id')
    task = Tasks.query.filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.index'))