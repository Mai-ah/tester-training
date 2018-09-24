import unittest


class TestUnittestAssertions(unittest.TestCase):

    def setUp(self):
        self.element = 0
        self.collection = [1, 2, 3]

    def test_assert_equal(self):
        self.assertEqual(self.element, 0)

    def test_assert_in_fail(self):
        self.assertIn(self.element, self.collection)  # prints detailed error message

    def test_asser_fail(self):
        assert self.element in self.collection  # prints only AssertionError stack trace


if __name__ == "__main__":
    unittest.main()
