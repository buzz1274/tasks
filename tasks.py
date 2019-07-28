from urllib import parse
from flask import Flask, render_template, request, redirect
from task_warrior.task_warrior import TaskWarrior
from task_warrior.helper import Helper

app = Flask(__name__)

@app.template_filter()
def to_date(date):
    date = Helper().convert_date_to_datetime(date)

    if not date or date.year == 2038:
        return '-'

    return date.strftime('%d %b, %Y')

@app.template_filter()
def format_project(project):
    if not project:
        return '-'

    return project.replace('_', ' ').replace('.', '&nbsp;&raquo;&nbsp;')


@app.template_filter()
def row_colour(date):
    date = Helper().convert_date_to_datetime(date)

    if not date or not date.date() or date.date() > date.now().date():
        return '#0000FF'
    elif date.date() == date.now().date():
        return '#00802B'

    return '#FF0000'


@app.route('/')
def index():
    project = request.args.get('project')
    complete = request.args.get('complete')

    if project:
        query = 'project:"%s" +PENDING' % (project, )
    else:
        query = '+OVERDUE or due.before:31days'

    task_warrior = TaskWarrior(query)


    return render_template('tasks.html',
                           projects=task_warrior.projects.projects,
                           tasks=task_warrior.filtered_raw_tasks,
                           complete=complete)

@app.route('/filter/')
def task_filter():
    priority = request.args.get('priority')
    due = request.args.get('due')
    query = ''

    if priority:
        query = 'priority:%s' % (priority,)

    if due:
        if query:
            query = '%s and ' % (query,)

        query = '%s due.before:%s' % (query, due,)

    task_warrior = TaskWarrior(query)

    return render_template('tasks.html',
                           projects=task_warrior.projects.projects,
                           tasks=task_warrior.filtered_raw_tasks,
                           complete=complete)

@app.route('/task/<string:task_uuid>/complete')
def complete(task_uuid):
    task_warrior = TaskWarrior()

    try:
        task_warrior.complete(task_uuid)

        complete = "success"
    except IndexError:
        complete = "failure"
    except Exception:
        complete = "failure"

    qs = parse.urlparse(request.referrer)

    return redirect("{}&complete={}".format(request.referrer, complete))