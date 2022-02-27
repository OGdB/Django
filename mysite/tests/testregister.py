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

    def testInvalidRegistrationInput(self):
        c = django.test.Client()
        resp = c.post("/register")
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST,
        "Should return bad request as there was no input")

    def testValidRegistration(self):
        resp = register("bob@xample.org","asecret")
        self.assertEqual(resp.status_code, http.HTTPStatus.OK,
        "Should return OK as email is valid and user does not exist")
    
    def testNoRegisterDupe(self):
        resp = register("sue@xample.org","asecret")
        self.assertEqual(resp.status_code, http.HTTPStatus.OK,
        "Should return OK as e-mail is not yet registered")

        resp = register("sue@xample.org","fpp")
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST,
        "Should return bad request as e-mail is already registered")

    def testNoInput(self):
        resp = register("", "foo")
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST,
            "Should return bad request as no e-mail was entered")
            
    def testNoUsername(self):
        resp = register("@xample.org", "foo")
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST,
        "should return bad request as there are no characters before the @")
    
    def testNoDomain(self):
        resp = register("sue@.org", "foo")
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST,
        "should return bad request as there are no characters before the dot.")

    def testNoDomainType(self):
        resp = register("sue@invalidemail.", "foo")
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST,
        "should return bad request as there is no domain type after dot.")
