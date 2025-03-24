from selenium.webdriver.common.by import By
from locators.products import Locater

class Products:

  def __init__(self, driver):
    self.driver = driver
  
  def check_current_tag_line(self):
    product_tagline = self.driver.find_element(By.XPATH, Locater.xpath_product_tagline).text
    assert product_tagline == "Products"

  def get_products(self):
    return self.driver.find_elements(By.XPATH, Locater.xpath_product_list)
  
  def get_count_product(self):
    return len(self.get_products())
  
  def check_cart_icon(self):
    cart_icon = self.driver.find_element(By.XPATH, Locater.xpath_cart_icon)
    assert cart_icon.is_displayed()
