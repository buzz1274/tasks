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

    def test_inbox_project_is_created(self):
        with patch.object(Tasks, 'search',
                          return_value=Helper.load_fixture('projects')):

            tasks = Tasks()

            assert 'inbox' in tasks.projects.projects
            assert tasks.projects.projects['inbox'].task_count == 1

    def test_sub_projects_are_created(self):
        with patch.object(Tasks, 'search',
                          return_value=Helper.load_fixture('projects')):

            tasks = Tasks()

            assert 'project_1.sub_project_1' in \
                   tasks.projects.projects['project_1'].projects.projects


