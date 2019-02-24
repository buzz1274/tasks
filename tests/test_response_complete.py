import pytest
from unittest.mock import patch
from task_warrior.task_warrior import TaskWarrior
import tasks


class TestTasks(object):

    @pytest.fixture
    def client(self):
        client = tasks.app.test_client()

        yield(client)

    def test_complete_returns_200_status_code(self, client):
        with patch.object(TaskWarrior, 'search', return_value='') as mocked_search:
            response = client.get('/task/1/complete')

            assert response.status_code == 200
