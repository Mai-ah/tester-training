import unittest

from sut import multiply


class TestUM(unittest.TestCase):

    def setUp(self):
        print("setup             class:TestStuff")

    def tearDown(self):
        print("teardown          class:TestStuff")

    @classmethod
    def setUpClass(cls):
        print("setup_class       class:%s" % cls.__name__)

    @classmethod
    def tearDownClass(cls):
        print("teardown_class    class:%s" % cls.__name__)

    def test_numbers_5_6(self):
        print 'test_numbers_5_6  <============================ actual test code'
        self.assertEqual(multiply(5, 6), 30)

    def test_strings_b_2(self):
        print 'test_strings_b_2  <============================ actual test code'
        self.assertEqual(multiply('b', 2), 'bb')


if __name__ == "__main__":
    unittest.main()
