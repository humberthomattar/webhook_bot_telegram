import unittest
import webapp
from flask import url_for

class ControllerTestCase(unittest.TestCase):

    def setUp(self):
        webapp.app.config.from_object('webapp.config.DevelopmentConfig')
        webapp.app.testing = True
        self.app = webapp.app.test_client()
        return

    def tearDown(self):
        return

    def test_info_status_code(self):
        req = self.app.get('/info/')
        assert req.status_code == 200
        assert b"versao" in req.data

    def test_info_status_code_without_ends(self):
        req = self.app.get('/info')
        assert req.status_code == 301

    def test_info_status_code_with_params(self):
        req = self.app.get('/info/?teste=1')
        assert req.status_code == 200
        assert b"versao" in req.data


if __name__ == '__main__':
    unittest.main()