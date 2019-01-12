from flask import Flask, render_template
from task_warrior.task_warrior import TaskWarrior

app = Flask(__name__)
tw = TaskWarrior()


@app.route('/')
def index():
    return render_template('tasks.html',
                           tasks=tw.query('+OVERDUE or due.before:31days +PENDING'))

