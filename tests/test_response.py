import pytest

import tasks


class TestTasks(object):

    @pytest.fixture
    def client(self):
        client = tasks.app.test_client()

        yield(client)

    def test_index_returns_a_200_status_code(self, client):
        response = client.get('/')

        assert response.status_code == 200
        assert b'<title>tasks.zz50.co.uk</title>' in response.data
