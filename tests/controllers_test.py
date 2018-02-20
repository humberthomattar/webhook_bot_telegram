import unittest
from flask_testing import TestCase
import os
import sys

topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)

class ControllersTest(TestCase):

    def create_app(self):
        from webapp import app
        app.config.testing = True
        self.app = app.test_client()
        return app

    def test_asset_info(self):
        response = self.client.get('/info/')
        assert b'versao' in response.data
        self.assert200(response)

"""
    def test_index(self):
        req = self.app.get('/')
        assert req.status_code == 404
        assert b"not found" in req.data

    def test_not_found(self):
        req = self.app.get('/index.html')
        assert req.status_code == 404
        assert b"not found" in req.data

    def test_info_status_code(self):
        req = self.app.get('/info/')
        assert req.status_code == 200
        assert b"versao" in req.data

    def test_info_status_code_without_params(self):
        req = self.app.get('/info')
        assert req.status_code == 301

    def test_info_status_code_with_params(self):
        req = self.app.get('/info/?teste=1')
        assert req.status_code == 200
        assert b"versao" in req.data

    def test_uptimeRobotAlerts_status_code_without_params(self):
        req = self.app.get('/uptimeRobotAlerts/')
        assert req.status_code == 400
        assert b"bad request" in req.data

"""
if __name__ == '__main__':
    unittest.main()