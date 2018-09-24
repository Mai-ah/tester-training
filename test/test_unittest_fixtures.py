import unittest

from sut import multiply


class TestUnittestFixtures(unittest.TestCase):

    def setUp(self):
        print("setup              %s" % self.id())

    def tearDown(self):
        print("teardown           %s" % self.id())

    @classmethod
    def setUpClass(cls):
        print("setup_class        %s" % cls.__name__)

    @classmethod
    def tearDownClass(cls):
        print("teardown_class     %s" % cls.__name__)

    def test_numbers_5_6(self):
        print("test_case          %s" % self.id())
        self.assertEqual(multiply(5, 6), 30)

    def test_strings_b_2(self):
        print("test_case          %s" % self.id())
        self.assertEqual(multiply("b", 2), "bb")


if __name__ == "__main__":
    unittest.main()
