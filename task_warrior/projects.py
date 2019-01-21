from .task_warrior import TaskWarrior
from .project import Project


class Projects(TaskWarrior):
    projects = None

    """
    doc block goes in here
    """
    def __init__(self):
        self.projects = {}

    """
    doc block goes in here
    """
    def hydrate(self, project_hierarchy):
        if not project_hierarchy[0] in self.projects:
            self.projects[project_hierarchy[0]] = Project(
                project_name=project_hierarchy[0],
                projects=Projects())

        if len(project_hierarchy[1:]) >= 1:
            self.projects[project_hierarchy[0]].projects.\
                hydrate(project_hierarchy[1:])

        self.projects[project_hierarchy[0]].increment_task_count()




