from unittest import TestCase
import urllib
import http
import django.test

class T(TestCase):
    def test_register1(self):
        c = django.test.Client()
        resp = c.post("/register")
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)
        # Open register page (start up server first)
        # with urllib.request.urlopen("http://localhost:8000/register") as u:
        #     self.assertEqual(u.getcode(), http.OK)