import src.AccountManager as AccountManager
from unittest import TestCase

class Tester(TestCase):
    def setUp(self):
        AccountManager.clear()
        AccountManager.addAccount("alice@xample.org", "qwerty")

    def test_invalidVerifyUser(self):
        self.assertFalse( AccountManager.verifyUser( "bob@validemail.org", "s3cr3t"),
            "should return false if user doesn't exist")

    def test_validVerifyUser(self):
        self.assertTrue( AccountManager.verifyUser( "alice@xample.org", "qwerty"),
            "should return true if user does exist and password matches")

    def test_noMatchingPassword(self):
        self.assertFalse( AccountManager.verifyUser( "alice@validemail.org", "s3cr3t"),
            "should return false if password doesn't match")

    def test_noMatchingCredentials(self):
        self.assertFalse( AccountManager.verifyUser( "bob@validemail.org", "qwerty"),
            "should return false if user doesn't exist and password does match")

    def test_noVerifyParameters(self):
        #test for missing parameters
        self.assertRaises( Exception, AccountManager.verifyUser )
        