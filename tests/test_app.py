import logging

from chalice.test import Client
from app import app


def test_index():
    with Client(app) as client:
        response = client.lambda_.invoke('get_folder_size', {
            'bucket': 'l',
            'path': "591c3d2e-fe0a-4f12-8967-52103b74f9be/"
        })
        logging.debug("Size {}".format(response.payload))
        assert response.payload is not None
