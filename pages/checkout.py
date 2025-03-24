from selenium.webdriver.common.by import By
from locators.checkout import Locater

class Checkout:

  def __init__(self, driver):
    self.driver = driver
  
  def check_current_tag_line(self):
    checkout_tagline = self.driver.find_element(By.XPATH, Locater.xpath_checkout_tagline).text
    assert checkout_tagline == "Checkout: Your Information"

  def fill_first_name(self, first_name):
    self.driver.find_element(By.ID, Locater.input_first_name).send_keys(first_name)

  def fill_last_name(self, last_name):
    self.driver.find_element(By.ID, Locater.input_last_name).send_keys(last_name)
  
  def fill_zip_code(self, zip_code):
    self.driver.find_element(By.ID, Locater.input_zip_code).send_keys(zip_code)

  def get_continue_btn(self):
    return self.driver.find_element(By.XPATH, Locater.xpath_continue_btn)

  def click_continue_btn(self):
    self.get_continue_btn().click()
