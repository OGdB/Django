import src.AccountManager as AccountManager
from unittest import TestCase

class Tester(TestCase):
    def setUp(self):
        AccountManager.clear()
        AccountManager.addAccount("alice@xample.org", "qwerty")

    def test_verifyUser(self):
        self.assertFalse( AccountManager.verifyUser( "bob", "s3cr3t"),
            "should return false if user doesn't exist")

    def test_verifyUser2(self):
        self.assertTrue( AccountManager.verifyUser( "alice@xample.org", "qwerty"),
            "should return true if user does exist and password matches")

    def test_verifyUser3(self):
        self.assertFalse( AccountManager.verifyUser( "alice", "s3cr3t"),
            "should return false if password doesn't match")

    def test_verifyUser4(self):
        self.assertFalse( AccountManager.verifyUser( "bob", "qwerty"),
            "should return false if user doesn't exist and password does match")

    def test_verifyUser5(self):
        #test for missing parameters
        self.assertRaises( Exception, AccountManager.verifyUser )