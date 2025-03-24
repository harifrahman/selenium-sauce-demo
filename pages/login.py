from selenium.webdriver.common.by import By
from locators.login import Locater

class Login:
  def __init__(self, driver):
    self.driver = driver
  
  def fill_username(self, username):
    self.driver.find_element(By.ID, Locater.input_username).send_keys(username)

  def fill_pasword(self, password):
    self.driver.find_element(By.ID, Locater.input_password).send_keys(password)
  
  def click_login_button(self):
    self.driver.find_element(By.XPATH, Locater.xpath_login_button).click()

  def validate_error_message(self, expected_err_msg):
    assert self.get_error_message().text == expected_err_msg

  def get_error_message(self):
    error_text = self.driver.find_element(By.XPATH, Locater.xpath_login_err_msg)
    assert error_text.is_displayed()
    return error_text
