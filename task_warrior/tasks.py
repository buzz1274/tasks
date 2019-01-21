from .task_warrior import TaskWarrior
from .projects import Projects


class Tasks(TaskWarrior):
    projects = False
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
        if 'project' not in task:
            self.tasks_with_no_project += 1
        elif task['project'] == 'inbox':
            self.tasks_in_inbox += 1
        else:
            self.projects.hydrate(task['project'].split('.'))

    """
    doc block goes in here
    """
    def hydrate_tags(self, task):
        pass


