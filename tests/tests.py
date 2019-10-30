import unittest
import time


from oslo_config import cfg as CONF
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# CONF = config

class LogInActions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_log_in(self):
        driver = self.driver
        driver.get(CONF.horizon.url)
        time.sleep(3)
        user_name = driver.find_element_by_id('id_username').send_keys(CONF.horizon.admin_username)
        passw = driver.find_element_by_id('id_password').send_keys(CONF.horizon.admin_password)
        driver.find_element_by_id('loginBtn').click()

    def test_log_in_negative(self):
        driver = self.driver
        driver.get(CONF.horizon.url)
        time.sleep(3)
        user_name = driver.find_element_by_id('id_username').send_keys('admin1')
        passw = driver.find_element_by_id('id_password').send_keys('secret1')
        driver.find_element_by_id('loginBtn').click()
        alert = driver.switch_to_alert()
        alert.text('Invalid credentials.')


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

