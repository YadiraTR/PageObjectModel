from selenium.webdriver.common.by import By

base_url = "https://www.saucedemo.com/"


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.xpath_image_login = '//*[@id="root"]/div/div[2]/div[1]/div[2]'
        self.input_user = 'user-name'
        self.input_password = 'password'
        self.button = 'login-button'
        self.xpath_page_init = '//*[@id="header_container"]/div[2]/span'
        self.xpath_button_page = '//*[@id="login-button"]'
        self.xpath_image_page = '//*[@id="item_4_img_link"]/img'

    def get_page_login(self):
        return self.driver.find_element(By.XPATH, self.xpath_image_login)

    def get_home_page(self):
        return self.driver.find_element(By.XPATH, self.xpath_button_page)

    def get_home_inventory(self):
        return self.driver.find_element(By.XPATH, self.xpath_image_page)

    def get_input_user(self):
        return self.driver.find_element(By.ID, self.input_user)

    def get_input_password(self):
        return self.driver.find_element(By.ID, self.input_password)

    #def get_click_button(self):
    #    return self.driver.find_element(By.ID, self.button)

    #def button(self):
     #   self.get_click_button().click()

    def send_text_user(self, user):
        self.get_input_user().send_keys(user)

    def send_password(self, password):
        self.get_input_password().send_keys(password)

    def view_page(self):
        return self.get_page_login().is_displayed()

    def home_page(self):
        return self.get_home_page().click()

    def home_inventory(self):
        return self.get_home_inventory().click()

