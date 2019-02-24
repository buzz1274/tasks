import subprocess
import json
from task_warrior.projects.projects import Projects
from task_warrior.tasks.tasks import Tasks


class TaskWarrior:
    projects = {}
    tags = {}
    tasks = {}
    all_raw_tasks = False
    filtered_raw_tasks = False
    tasks_in_inbox = 0

    def __init__(self, query=None):
        if query is not None:
            self.all_raw_tasks = self.search()
            self.filtered_raw_tasks = self.search(query)

            self.import_task_data()

    def import_task_data(self):
        """
        doc block goes in here
        """
        self.projects = Projects()
        self.tasks = Tasks()

        for task in self.all_raw_tasks:
            self.hydrate_projects(task)
            self.hydrate_tags(task)

        for task in self.filtered_raw_tasks:
            self.hydrate_tasks(task)

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

    def hydrate_tasks(self, task):
        """
        doc block goes in here
        """
        pass

    def hydrate_projects(self, task):
        """
        doc block goes in here
        """
        if 'project' not in task or task['project'] == 'inbox':
            self.tasks_in_inbox += 1
        else:
            self.projects.hydrate(task['project'].split('.'))

    def hydrate_tags(self, task):
        """
        doc block goes in here
        """
        pass

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

        return json.loads(output)

