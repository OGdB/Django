from unittest import TestCase
#import urllib
import http
import django.test
import src.AccountManager as AccountManager
import tests.utils as utils
import src.user as user

class T(TestCase):
    
    def setUp(self):
        AccountManager.clear() # Clear registered users every test

    def testInvalidRegistrationInput(self):
        c = django.test.Client()
        resp = c.post("/register")
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST,
        "Should return bad request as there was no input")

    def testValidRegistration(self):
        resp = utils.addAccount("bob@xample.org","asecret")
        self.assertEqual(resp.status_code, http.HTTPStatus.OK,
        "Should return OK as email is valid and user does not exist")
    
    def testNoRegisterDupe(self):
        resp = utils.addAccount("sue@xample.org","asecret")
        self.assertEqual(resp.status_code, http.HTTPStatus.OK,
        "Should return OK as e-mail is not yet registered")

        resp = utils.addAccount("sue@xample.org","fpp")
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST,
        "Should return bad request as e-mail is already registered")

    def testNoInput(self):
        resp = utils.addAccount("", "foo")
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST,
            "Should return bad request as no e-mail was entered")
            
    def testNoUsername(self):
        resp = utils.addAccount("@xample.org", "foo")
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST,
        "should return bad request as there are no characters before the @")
    
    def testNoDomain(self):
        resp = utils.addAccount("sue@.org", "foo")
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST,
        "should return bad request as there are no characters before the dot.")

    def testNoDomainType(self):
        resp = utils.addAccount("sue@invalidemail.", "foo")
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST,
        "should return bad request as there is no domain type after dot.")

    def testDuplicateRegistrationLogin(self):
        resp = utils.addAccount("bob@duplicatemail.org","asecret")
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)
        resp2 = utils.addAccount("bob@duplicatemail.org","asecret2")
        self.assertEqual(resp2.status_code, http.HTTPStatus.BAD_REQUEST,
        "should return bad request; username already registered")