from selenium.webdriver.common.by import By
from locators.products import Locater

class Products:

  def __init__(self, driver):
    self.driver = driver
  
  def check_current_tag_line(self):
    product_tagline = self.driver.find_element(By.XPATH, Locater.xpath_product_tagline).text
    assert product_tagline == "Products"

  def get_products(self):
    return self.driver.find_elements(By.CLASS_NAME, Locater.class_btn_list_of_add_to_cart_item)
  
  def get_add_to_cart_btn(self, product):
    return product.find_element(By.CSS_SELECTOR, Locater.xpath_first_btn_add_to_cart)
  
  def get_add_to_cart_for_specific_product_id(self, id):
    return self.driver.find_element(By.ID, id)
  
  def get_count_product(self):
    return len(self.get_products())
  
  def get_cart_icon(self):
    return self.driver.find_element(By.XPATH, Locater.xpath_cart_icon)

  def check_cart_icon(self):
    assert self.get_cart_icon().is_displayed()

  def click_cart_icon(self):
    self.get_cart_icon().click()
