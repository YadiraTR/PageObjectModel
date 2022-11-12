from datetime import time
from threading import Thread

from page_object.home_page import HomePage
from page_object import home_page
from selenium_wrapper.base import Base


class TestLogin(Base):

    def test_1_view_page(self):
        driver = self.driver
        driver.get(home_page.base_url)
        element = HomePage(driver).view_page()
        self.assertTrue(element, "not image")

    def test_2_login(self):
        driver = self.driver
        HomePage(driver).send_text_user("standard_user")

        #time.sleep(5)
        HomePage(driver).send_password("secret_sauce")
        #time.sleep(5)
        HomePage(driver).home_page()
        #time.sleep(5)
        HomePage(driver).home_inventory()
        #time.sleep(5)

        #HomePage(driver).view_page("login-button")
