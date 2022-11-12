import unittest

from selenium import webdriver

from selenium.webdriver.chrome.webdriver import WebDriver

from main import print_hi


class Base(unittest.TestCase):
    driver = webdriver.Chrome(executable_path="chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        driver = cls.driver
        #driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)

        # @classmethod
        # def tearDownClass(cls):
        # cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

