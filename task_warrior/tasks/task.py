from ..helper import Helper

class Task:
    id = None
    uuid = None
    description = None
    due = None
    entry = None
    modified = None
    project = None
    start = None
    status = None
    urgency = None

    def hydrate(self, task):
        """
        sets Task property values
        Args:
            task (dictionary): contains task details
        """
        helper = Helper()

        for key, value in task.items():
            if key == 'due' or key == 'entry' or key == 'modified':
                setattr(self, key, helper.convert_date_to_datetime(value))
            else:
                setattr(self, key, value)

        return self