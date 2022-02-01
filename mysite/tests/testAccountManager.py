import src.AccountManager as AccountManager
from unittest import TestCase

class Tester(TestCase):
    def setUp(self):
        Tester.A = AccountManager.AccountManager()
        Tester.A.addUser( "alice", "qwerty" )

    def test_verifyUser(self):
        A = Tester.A
        self.assertFalse( A.verifyUser( "bob", "s3cr3t"),
            "should return false if user doesn't exist")

    def test_verifyUser2(self):
        A = Tester.A
        self.assertTrue( A.verifyUser( "alice", "qwerty"),
            "should return true if user does exist and password matches")

    def test_verifyUser3(self):
        A = Tester.A
        self.assertFalse( A.verifyUser( "alice", "s3cr3t"),
            "should return false if password doesn't match")

    def test_verifyUser4(self):
        A = Tester.A
        self.assertFalse( A.verifyUser( "bob", "qwerty"),
            "should return false if user doesn't exist and password does match")

    def test_verifyUser5(self):
        A = Tester.A
        #test for missing parameters
        self.assertRaises( Exception, A.verifyUser )