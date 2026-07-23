from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from models import db, Task
from forms import TaskForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    tasks = Task.query.order_by(Task.completed, Task.due_date).all()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["GET","POST"])
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            priority=form.priority.data,
            category=form.category.data,
            due_date=form.due_date.data,
        )
        db.session.add(task)
        db.session.commit()
        flash("Task added successfully.","success")
        return redirect(url_for("home"))
    return render_template("add_task.html", form=form)

@app.route("/edit/<int:task_id>", methods=["GET","POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        form.populate_obj(task)
        db.session.commit()
        flash("Task updated.","success")
        return redirect(url_for("home"))
    return render_template("edit_task.html", form=form)

@app.route("/toggle/<int:task_id>")
def toggle(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete/<int:task_id>")
def delete(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted.","danger")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
