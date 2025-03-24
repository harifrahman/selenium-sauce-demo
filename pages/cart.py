from selenium.webdriver.common.by import By
from locators.cart import Locater

class Cart:

  def __init__(self, driver):
    self.driver = driver
  
  def check_current_tag_line(self):
    cart_tagline = self.driver.find_element(By.XPATH, Locater.xpath_cart_tagline).text
    assert cart_tagline == "Your Cart"

  def get_checkout_btn(self):
    return self.driver.find_element(By.XPATH, Locater.xpath_checkout_btn)

  def click_cart_icon(self):
    self.get_checkout_btn().click()
