from .task_warrior import TaskWarrior
from .projects import Projects


class Tasks(TaskWarrior):
    projects = False
    tags = False
    tasks = {}
    tasks_with_no_project = 0
    tasks_in_inbox = 0

    """
    doc block goes in here
    """
    def __init__(self):
        self.projects = Projects()
        self.tasks = self.search()

        self.hydrate()
        self.projects.sort()
        self.projects.add('inbox', 'Inbox', self.tasks_in_inbox, False)

    """
    doc block goes in here
    """
    def hydrate(self):
        for task in self.tasks:
            self.hydrate_tasks(task)
            self.hydrate_projects(task)
            self.hydrate_tags(task)

    """
    doc block goes in here
    """
    def hydrate_tasks(self, task):
        pass

    """
    doc block goes in here
    """
    def hydrate_projects(self, task):
        if 'project' not in task or task['project'] == 'inbox':
            self.tasks_in_inbox += 1
        else:
            self.projects.hydrate(task['project'].split('.'))

    """
    doc block goes in here
    """
    def hydrate_tags(self, task):
        pass


