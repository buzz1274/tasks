from flask import Flask, render_template, request
from task_warrior.task_warrior import TaskWarrior
from task_warrior.projects import Projects
from task_warrior.tasks import Tasks

app = Flask(__name__)
tw = TaskWarrior()


@app.template_filter()
def to_date(date):
    date = tw.convert_date_to_datetime(date)

    if not date or date.year == 2038:
        return '-'

    return date.strftime('%d %b, %Y')


@app.template_filter()
def nest_project(depth):
    if depth:
        return 'padding-left:{pixels}px'.format(pixels=depth * 20)

    return ''

@app.template_filter()
def format_project(project):
    if not project:
        return '-'

    return project.replace('_', ' ').replace('.', '&nbsp;&raquo;&nbsp;')


@app.template_filter()
def row_colour(date):
    date = tw.convert_date_to_datetime(date)

    if not date or not date.date() or date.date() > date.now().date():
        return '#0000FF'
    elif date.date() == date.now().date():
        return '#00802B'

    return '#FF0000'


@app.route('/')
def index():
    project = request.args.get('project')

    if project:
        query = 'project:"%s" +PENDING' % (project, )
    else:
        query = '+OVERDUE or due.before:31days'

    tasks = Tasks()

    return render_template('tasks.html',
                           projects=tasks.projects.projects,
                           tasks=tw.search(query),
                           task_in_inbox=tw.task_in_inbox)

