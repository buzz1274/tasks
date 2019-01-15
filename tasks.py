from flask import Flask, render_template, request
from task_warrior.task_warrior import TaskWarrior
from datetime import datetime

app = Flask(__name__)
tw = TaskWarrior()


@app.template_filter()
def to_date(date):
    if not date:
        return '-'

    date = datetime.strptime(date, '%Y%m%dT%H%M%SZ')

    if not date or date.year == 2038:
        return '-'

    return date.strftime('%d %b, %Y')


@app.template_filter()
def format_project(project):
    if not project:
        return '-'

    return project.replace('_', ' ').replace('.', '&nbsp;&raquo;&nbsp;')


@app.route('/')
def index():
    project = request.args.get('project')

    if project:
        query = 'project:"%s" +PENDING' % (project, )
    else:
        query = '+OVERDUE or due.before:31days'

    return render_template('tasks.html',
                           projects=tw.projects(),
                           tasks=tw.search(query))

