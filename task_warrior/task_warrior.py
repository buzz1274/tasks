import subprocess
import json
from .projects.projects import Projects
from .tasks.tasks import Tasks
from .tasks.task import Task


class TaskWarrior:
    projects = {}
    tags = {}
    tasks = {}
    all_raw_tasks = False
    filtered_raw_tasks = False
    tasks_in_inbox = 0

    def __init__(self, query=None):
        self.all_raw_tasks = self.search()

        if query is not None:
            self.filtered_raw_tasks = self.search(query)
        else:
            self.filtered_raw_tasks = self.all_raw_tasks

        self.hydrate()

    def hydrate(self):
        """
        doc block goes in here
        """
        self.projects = Projects()
        #self.tasks = Tasks()

        for task in self.all_raw_tasks:
            self.hydrate_projects(task)
            self.hydrate_tags(task)

        for task in self.filtered_raw_tasks:
            self.tasks[task['uuid']] = Task().hydrate(task)

        self.house_keep_task_data()

    def hydrate_projects(self, task):
        """
        add project to projects object
        Args:
            task (dictionary): contains task details
        """
        if 'project' not in task or task['project'] == 'inbox':
            self.tasks_in_inbox += 1
        else:
            self.projects.hydrate(task['project'].split('.'))

    def house_keep_task_data(self):
        """
        Performs final housekeeping on projects, tasks and tags
        """
        self.projects.sort()
        self.projects.add('inbox', 'Inbox', self.tasks_in_inbox, False)

    def hydrate_tags(self, task):
        """
        doc block goes in here
        """
        pass

    def complete(self, task_uuid):
        """
        doc block goes in here
        """
        if task_uuid not in self.tasks:
            raise IndexError

        self.execute(("task id:%d done" %
                      (self.tasks[task_uuid].id, )).split())

    def delete(self, task_uuid):
        """
        doc block goes in here
        """
        if task_uuid not in self.tasks:
            raise IndexError

        self.execute(("task id:%d delete" %
                      (self.tasks[task_uuid].id, )).split())

    def search(self, query=''):
        """
        doc block goes in here
        """
        result = self.execute(("task %s +PENDING export" % (query, )).split())

        result.sort(key=lambda x: x['urgency'], reverse=True)

        return result

    def execute(self, query):
        """
        doc block goes in here
        """
        process = subprocess.Popen(query, stdout=subprocess.PIPE)

        output, error = process.communicate()

        if 'export' in query:
            return json.loads(output)
        else:
            return output

