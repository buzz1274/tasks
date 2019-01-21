

class Project:
    project_name = ''
    task_warrior_name = ''
    sub_projects = False
    task_count = 0

    """
    doc block goes in here
    """
    def __init__(self, project_name, projects):
        self.project_name = project_name
        self.projects = projects

    """
    doc block goes in here
    """
    def increment_task_count(self):
        self.task_count += 1
