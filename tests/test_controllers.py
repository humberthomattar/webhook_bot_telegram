import unittest
import webapp


class ControllerTestCase(unittest.TestCase):

    def setUp(self):
        webapp.app.config.from_object('webapp.config.DevelopmentConfig')
        webapp.app.testing = True
        self.app = webapp.app.test_client()
        return

#    def tearDown(self):
#        return

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


if __name__ == '__main__':
    unittest.main()
