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
        self.projects = collections.OrderedDict()
        self.parent = parent

    """
    doc block goes in here
    """
    def hydrate(self, project_hierarchy):
        project_id = self.get_project_id(project_hierarchy[0])

        self.add(project_id=project_id,
                 project_name=project_hierarchy[0])

        if len(project_hierarchy[1:]) >= 1:
            self.projects[project_id].projects.\
                hydrate(project_hierarchy[1:])

        self.projects[project_id].increment_task_count()

    """
    doc block goes in here
    """
    def add(self, project_id, project_name, task_count=0, last=True):
        if project_id not in self.projects:
            project = {project_id: Project(
                    project_name=project_name,
                    task_count=task_count,
                    projects=Projects(parent=project_id))}

            self.projects.update(project)

            if not last:
                self.projects.move_to_end(project_id, last=last)

    """
    doc block goes in here
    """
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







