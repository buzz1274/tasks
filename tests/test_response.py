import pytest
from unittest.mock import patch
from task_warrior.tasks import Tasks

import tasks


class TestTasks(object):

    @pytest.fixture
    def client(self):
        client = tasks.app.test_client()

        yield(client)

    def test_index_returns_a_200_status_code(self, client):
        with patch.object(Tasks, 'search', return_value='') as mocked_search:
            response = client.get('/')

            mocked_search.assert_called_once()

            assert response.status_code == 200
            assert b'<title>tasks.zz50.co.uk</title>' in response.data
