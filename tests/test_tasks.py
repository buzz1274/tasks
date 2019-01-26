from unittest.mock import patch
from task_warrior.tasks import Tasks, Projects
from .helper import Helper


class TestTasks(object):

    def test_projects_are_hydrated_into_a_projects_object(self):
        with patch.object(Tasks, 'search',
                          return_value=Helper.load_fixture('projects')) as \
                mocked_search:

            tasks = Tasks()

            mocked_search.assert_called_once()

            assert isinstance(tasks.projects, Projects)
            assert len(tasks.projects.projects) == 5
