from datetime import datetime
import subprocess
import collections
import json


class TaskWarrior:
    tasks = {}
    projects = {}
    task_in_inbox = 0

    def __init__(self):
        self.get_projects()

        print(self.projects)

    def get_projects(self):
        tasks = self.search()

        for task in tasks:
            if 'project' in task:
                if task['project'] == 'inbox':
                    self.task_in_inbox += 1
                else:
                    if task['project'] not in self.projects:
                        project = task['project'].split('.')
                        depth = len(project) - 1
                        parent_project = '.'.join(project[:-1])

                        self.projects[task['project']] = \
                            {'task_count': 1,
                             'project_display_name': project[-1],
                             'depth': depth,
                             'parent_project': parent_project}
                    else:
                        self.projects[task['project']]['task_count'] += 1

                    self.increment_task_count_parent_project(
                        self.projects[task['project']]['parent_project'])

        self.projects = collections.OrderedDict(sorted(self.projects.items()))

    def increment_task_count_parent_project(self, project):
        if project:
            if project not in self.projects:
                project = project.split('.')
                parent_project = '.'.join(project[:-1])
                project_display_name = project[-1]
                depth = len(project) - 1
                project = '.'.join(project)

                self.projects[project] = \
                    {'task_count': 1,
                     'project_display_name': project_display_name,
                     'depth': depth,
                     'parent_project': parent_project}
            else:
                self.projects[project]['task_count'] += 1

            self.increment_task_count_parent_project(
                self.projects[project]['parent_project'])

    def convert_date_to_datetime(self, date):
        if not date:
            return None

        return datetime.strptime(date, '%Y%m%dT%H%M%SZ')

    def search(self, query=''):
        result = self.execute(("task %s +PENDING export" % (query, )).split())

        result.sort(key=lambda x: x['urgency'], reverse=True)

        return result

    def execute(self, query):
        process = subprocess.Popen(query, stdout=subprocess.PIPE)

        output, error = process.communicate()

        return json.loads(output)

