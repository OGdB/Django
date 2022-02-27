from unittest import TestCase
import src.foo as foo
class T2(TestCase):
    def test_2(self):
        self.assertEqual( 0.5, foo.reciprocal(2) )
    def test_0(self):
        self.assertRaises( ZeroDivisionError, foo.reciprocal, 0 )
    # tests if there is an exception. If there is an exception, no error is reported.
    # (it SHOULD give an exception)
    def test_exception(self):
        self.assertRaises(Exception, foo.isPositive, "foo")