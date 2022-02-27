from unittest import TestCase
#import urllib
import http
import django.test
import src.AccountManager as AccountManager

def register(uname, pwd):
    c = django.test.Client()
    resp = c.post("/register",
    {
        "username": uname,
        "password":pwd
    }
    )
    return resp

class T(TestCase):
    
    def setUp(self):
        AccountManager.clear() # Clear registered users every test

    def test_register1(self):
        c = django.test.Client()
        resp = c.post("/register")
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST,
        "Should return bad request as there was no input")

    def test_register2(self):
        resp = register("bob@xample.org","asecret")
        self.assertEqual(resp.status_code, http.HTTPStatus.OK,
        "Should return OK as email is valid and user does not exist")
    
    def test_registerNoDupe(self):
        resp = register("sue@xample.org","asecret")
        self.assertEqual(resp.status_code, http.HTTPStatus.OK,
        "Should return OK as e-mail is not yet registered")

        resp = register("sue@xample.org","fpp")
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST,
        "Should return bad request as e-mail is already registered")

    def test_noinput(self):
        resp = register("", "foo")
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST,
            "Should return bad request as no e-mail was entered")
            
    def test_no_username(self):
        resp = register("@xample.org", "foo")
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST,
        "should return bad request as there is no characters before the @")
