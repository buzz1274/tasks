from flask import Flask, render_template, request
from task_warrior.task_warrior import TaskWarrior

app = Flask(__name__)
tw = TaskWarrior()


@app.route('/')
def index():
    project = request.args.get('project')

    if project:
        query = 'project:%s +PENDING' % (project, )
    else:
        query = '+OVERDUE or due.before:31days'

    return render_template('tasks.html',
                           projects=tw.projects(),
                           tasks=tw.search(query))

