from unittest.mock import patch
from task_warrior.task_warrior import TaskWarrior, Projects
from .helper import Helper


class TestTasks(object):

    def test_task_is_hydrated_into_a_task_object(self):
        task_properties = [
            "id", "uuid", "project","description","due", "entry", "modified",
            "project", "start", "status","urgency"]

        with patch.object(TaskWarrior, 'search',
                          return_value=Helper.load_fixture('tasks')) as \
                mocked_search:

            tasks = TaskWarrior('')

            mocked_search.assert_called()

            print(tasks.tasks)
            print("HERP")
            print(tasks.tasks['a1a'])
            print("DONE")

            assert hasattr(tasks.tasks['a1a'], 'id')

            for task_property in task_properties:
                assert getattr(tasks.tasks['a1a'], task_property) is not None

