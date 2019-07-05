import collections
from ..task_warrior import TaskWarrior

class CleanDuplicateTasks:
    tw = None
    tasks = {}

    def __init__(self):
        """
        doc block goes here
        """
        self.tw = TaskWarrior()

        self.delete_duplicate_tasks()

    def delete_duplicate_tasks(self):
        """
        doc block goes here
        """
        for raw_task in self.tw.all_raw_tasks:
            for raw_task_duplicate in self.tw.all_raw_tasks:
                if self.is_duplicate(raw_task, raw_task_duplicate):
                    raw_task['duplicate'] = True

        for raw_task in self.tw.all_raw_tasks:
            if 'duplicate' in raw_task and raw_task['duplicate'] == True:
                self.tw.delete(raw_task['uuid'])

    @staticmethod
    def is_duplicate(task_a, task_b):
        if ('due' in task_a and 'due' in task_b and
            task_a['id'] != task_b['id'] and
            task_a['description'] == task_b['description'] and
            task_a['project'] == task_b['project'] and
            task_a['due'] <= task_b['due'] and
            ('duplicate' not in task_b or task_b['duplicate'] == False)):
            return True

        return False


if __name__ == "__main__":
    CleanDuplicateTasks()

