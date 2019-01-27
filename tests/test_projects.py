from unittest.mock import patch
from task_warrior.tasks import Tasks, Projects
from .helper import Helper


class TestProjects(object):

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

    def test_inbox_project_is_first(self):
        with patch.object(Tasks, 'search',
                          return_value=Helper.load_fixture('projects')):

            tasks = Tasks()
            projects = list(tasks.projects.projects)

            assert projects[0] == 'inbox'

    def test_sub_projects_are_created(self):
        with patch.object(Tasks, 'search',
                          return_value=Helper.load_fixture('projects')):

            tasks = Tasks()

            assert 'project_1.sub_project_1' in \
                   tasks.projects.projects['project_1'].projects.projects

    def test_projects_are_sorted_alphabetically(self):
        with patch.object(Tasks, 'search',
                          return_value=Helper.load_fixture('projects')):

            tasks = Tasks()
            projects = list(tasks.projects.projects)

            assert (projects[0] == 'inbox' and projects[1] == 'project_1' and
                    projects[2] == 'project_2' and projects[3] == 'project_3' and
                    projects[4] == 'project_4')

    def test_calling_increment_task_count_increases_tasks_count_by_one(self):
        with patch.object(Tasks, 'search',
                          return_value=Helper.load_fixture('projects')):

            tasks = Tasks()

            assert tasks.projects.projects['inbox'].task_count == 1

            tasks.projects.projects['inbox'].increment_task_count()

            assert tasks.projects.projects['inbox'].task_count == 2

    def test_calling_increment_task_count_with_value_increases_tasks_count_by_value(self):
        with patch.object(Tasks, 'search',
                          return_value=Helper.load_fixture('projects')):

            tasks = Tasks()

            assert tasks.projects.projects['inbox'].task_count == 1

            tasks.projects.projects['inbox'].increment_task_count(5)

            assert tasks.projects.projects['inbox'].task_count == 6







