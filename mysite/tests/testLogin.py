import django.test
import http
from unittest import TestCase
import tests.utils as utils

class Tester(TestCase):
    def testNotLoggedIn(self):
        c = django.test.Client()
        resp = c.get("/who")
        self.assertEqual("", resp.content.decode())

    def test_RegisterAndLogin(self):
        resp = utils.addAccount("bob@example.com", "pssw")
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)

        uname = resp.client.get("/who").content.decode()
        self.assertEqual(uname, "bob@example.com")
