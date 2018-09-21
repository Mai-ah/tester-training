import datetime
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Create webdriver."""
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # comment this line to see browser window
        cls.driver = webdriver.Chrome(chrome_options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        """Close webdriver."""
        cls.driver.quit()

    def setUp(self):
        """Open login page."""
        self.driver.get("http://localhost:7272")

    def tearDown(self):
        """Take screenshot."""
        self.driver.get_screenshot_as_file(
            "{dir}/{method_name}_{creation_time}.png".format(
                dir="reports",
                method_name=self._testMethodName,
                creation_time=datetime.datetime.now().strftime(
                    "%Y-%m-%d_%H-%M-%S"
                ),
            )
        )
        print("Screenshoot Captured for test:{}".format(self._testMethodName))

    def test_valid_login(self):
        """TODO: valid login scenario"""
        pass

    def test_invalid_login(self):
        """TODO: invalid login scenario"""
        pass


if __name__ == "__main__":
    unittest.main()
