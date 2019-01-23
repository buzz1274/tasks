from task_warrior.tasks import Tasks, Projects


class TestTasks(object):
    def test_projects_are_hydrated_into_a_projects_object(self):
        tasks = Tasks()
        assert isinstance(tasks.projects, Projects)