import unittest
import webapp

class ControllerTestCase(unittest.TestCase):

    def setUp(self):
        webapp.app.config.from_object('webapp.config.DevelopmentConfig')
        webapp.app.testing = True
        self.app = webapp.app.test_client()
        return

    def tearDown(self):
        return

    def test_return_default_info(self):
        text = '{"versao": "%s", "nome da aplicacao": "%s"}' % (webapp.app.config['APP_NAME'], webapp.app.config['VERSION'])
        req = self.app.get('/')
        assert b'{"versao": "%s", "nome da aplicacao": "%s"}' % (webapp.app.config['APP_NAME'], webapp.app.config['VERSION']) in req.data


if __name__ == '__main__':
    unittest.main()
