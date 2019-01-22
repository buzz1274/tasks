import collections
from .task_warrior import TaskWarrior
from .project import Project


class Projects(TaskWarrior):
    projects = None
    parent = ''

    """
    doc block goes in here
    """
    def __init__(self, parent=''):
        self.projects = {}
        self.parent = parent

    """
    doc block goes in here
    """
    def hydrate(self, project_hierarchy):
        project_id = self.get_project_id(project_hierarchy[0])

        if project_id not in self.projects:
            self.projects[project_id] = Project(
                project_name=project_hierarchy[0],
                projects=Projects(parent=project_id))

        if len(project_hierarchy[1:]) >= 1:
            self.projects[project_id].projects.\
                hydrate(project_hierarchy[1:])

        self.projects[project_id].increment_task_count()

    def get_project_id(self, project):
        if not self.parent:
            return project

        return '{}.{}'.format(self.parent, project)

    """
    doc block goes in here
    """
    def sort(self):
        for key, project in self.projects.items():
            project.projects.sort()

        self.projects = collections.OrderedDict(sorted(self.projects.items()))







