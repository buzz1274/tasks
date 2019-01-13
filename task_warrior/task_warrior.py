import subprocess
import collections
import json


class TaskWarrior:
    def __init__(self):
        pass

    def projects(self):
        tasks = self.search()
        projects = {}

        for task in tasks:
            if 'project' in task:
                if task['project'] not in projects:
                    projects[task['project']] = 1
                else:
                    projects[task['project']] += 1

        return collections.OrderedDict(sorted(projects.items()))

    def search(self, query=''):
        result = self.execute(("task %s +PENDING export" % (query, )).split())

        result.sort(key=lambda x: x['urgency'], reverse=True)

        return result

    def execute(self, query):
        process = subprocess.Popen(query, stdout=subprocess.PIPE)

        output, error = process.communicate()

        return json.loads(output)

