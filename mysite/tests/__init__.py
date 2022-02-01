# Activate myenv
# powershell -noexit -executionPolicy bypass .\myenv\scripts\activate

# Activate site (do within mysite folder)
# python manage.py runserver

# UNIT TESTS
# Test case: Tests one part of functionality of one function

# Test suite: Collection of test cases
# Also known as test harness

# Test fixture: Setup & cleanup required for a particular test

# Stub: Replacement for some other component of the system; returns a canned response

# unittest considers only files beginning with “test”

# Method names need to follow some patterns
# setUp: Called before any tests in that class execute

# Test functions must start with “test”

# tearDown: Called after all tests in that class execute

# Class must be subclass of unittest.TestCase

# These are the checks we have (all are called as self.method())
# assertEqual(x,y)
# assertNotEqual(x,y)
# assertTrue(x)
# assertFalse(x)
# assertRaises(exception, func, args )