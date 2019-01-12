import subprocess
import json


class TaskWarrior:
    def __init__(self):
        pass

    def query(self, query):
        query = ("%s %s %s" % ('task', query, 'export')).split()
        process = subprocess.Popen(query, stdout=subprocess.PIPE)

        output, error = process.communicate()
        result = json.loads(output)

        result.sort(key=lambda x: x['urgency'], reverse=True)

        return result
