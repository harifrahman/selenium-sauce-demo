from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.checkout import Locater

class Checkout:

  def __init__(self, driver):
    self.driver = driver
  
  def check_current_tag_line(self):
    checkout_tagline = self.driver.find_element(By.XPATH, Locater.xpath_checkout_tagline).text
    assert checkout_tagline == "Checkout: Your Information"

  def fill_first_name(self, first_name):
      first_name_field = WebDriverWait(self.driver, 10).until(
          EC.element_to_be_clickable((By.ID, Locater.input_first_name))
      )
      first_name_field.clear()
      first_name_field.send_keys(first_name)

  def fill_last_name(self, last_name):
      last_name_field = WebDriverWait(self.driver, 10).until(
          EC.element_to_be_clickable((By.ID, Locater.input_last_name))
      )
      last_name_field.send_keys(last_name)

  def fill_zip_code(self, zip_code):
      zip_code_field = WebDriverWait(self.driver, 10).until(
          EC.element_to_be_clickable((By.ID, Locater.input_zip_code))
      )
      zip_code_field.send_keys(zip_code)
      
  def get_continue_btn(self):
    return self.driver.find_element(By.XPATH, Locater.xpath_continue_btn)

  def click_continue_btn(self):
    self.get_continue_btn().click()
