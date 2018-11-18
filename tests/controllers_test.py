from flask_testing import TestCase
import unittest
import os
import sys

top_dir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(top_dir)

# noinspection PyPep8
from webapp import app


class ControllersTest(TestCase):
    def create_app(self):
        self.app = app.test_client()
        return app

    def test_index(self):
        req = self.client.get('/')
        assert req.status_code == 404
        assert b"not found" in req.data

    def test_index_with_params(self):
        req = self.client.get('/?teste=1')
        assert req.status_code == 404
        assert b"not found" in req.data

    def test_not_found(self):
        req = self.client.get('/index.html')
        assert req.status_code == 404
        assert b"not found" in req.data

    def test_info_status_code(self):
        req = self.client.get('/info/')
        assert req.status_code == 200
        assert b"versao" in req.data

    def test_info_redirect(self):
        req = self.client.get('/info')
        assert req.status_code == 301

    def test_info_status_code_with_params(self):
        req = self.client.get('/info/?teste=1')
        assert req.status_code == 200
        assert b"versao" in req.data

    def test_uptimeRobotAlerts_without_params(self):
        req = self.client.get('/uptimeRobotAlerts/')
        assert req.status_code == 400
        assert b"bad request" in req.data

    def test_uptimeRobotAlerts_redirect(self):
        req = self.client.get('/uptimeRobotAlerts')
        assert req.status_code == 301

if __name__ == '__main__':
    unittest.main(verbosity=2)
