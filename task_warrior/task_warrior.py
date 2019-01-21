from datetime import datetime
import subprocess
import collections
import json


class TaskWarrior:
    tasks = {}
    projects = {}
    task_in_inbox = 0

    def __init__(self):
        pass

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

