from selenium.webdriver.common.by import By
from locators.checkout_complete import Locater

class CheckoutComplete:

  def __init__(self, driver):
    self.driver = driver
  
  def check_current_tag_line(self):
    checkout_tagline = self.driver.find_element(By.XPATH, Locater.xpath_checkout_tagline).text
    assert checkout_tagline == "Checkout: Complete!"

  def verify_success_message(self):
    success_message =  self.driver.find_element(By.XPATH, Locater.xpath_complete_message)
    assert success_message.is_displayed()
    assert success_message.text == "Thank you for your order!"

