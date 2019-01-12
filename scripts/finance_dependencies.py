#!/usr/bin/python
import subprocess
import json

process = subprocess.Popen(['task', 'project:finances', '+PENDING',
                            'due.before:eom', 'export'], stdout=subprocess.PIPE)

output, error = process.communicate()

tasks = json.loads(output)

for task in tasks:
    if task['description'] == 'Month end accounts':
        month_end_accounts_id = task['id']
        break


for task in tasks:
    if task['id'] and task['id'] != month_end_accounts_id:
        subprocess.Popen(['task', str(month_end_accounts_id), 'modify',
                          'depends:' + str(task['id'])],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)