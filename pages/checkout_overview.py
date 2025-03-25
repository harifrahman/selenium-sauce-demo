from selenium.webdriver.common.by import By
from locators.checkout_overview import Locater
import re

class CheckoutOverview:

  def __init__(self, driver):
    self.driver = driver
  
  def check_current_tag_line(self):
    checkout_tagline = self.driver.find_element(By.XPATH, Locater.xpath_checkout_tagline).text
    assert checkout_tagline == "Checkout: Overview"

  def get_finish_btn(self):
    return self.driver.find_element(By.XPATH, Locater.xpath_finish_btn)

  def click_finish_btn(self):
    self.get_finish_btn().click()
  
  def get_item_price(self):
    return self.driver.find_element(By.XPATH, Locater.xpath_inventory_item_price).text
  
  def get_item_qty(self):
    return self.driver.find_element(By.XPATH, Locater.xpath_item_quantity).text
  
  def get_subtotal(self):
    return self.driver.find_element(By.XPATH, Locater.xpath_subtotal).text
  
  def get_tax_label(self):
    return self.driver.find_element(By.XPATH, Locater.xpath_tax_label).text
  
  def get_total(self):
    return self.driver.find_element(By.XPATH, Locater.xpath_total).text
  
  def extract_float(self, value_str):
    return float(re.findall(r"[-+]?\d*\.\d+|\d+", value_str)[0])

  def is_subtotal_correct(self):
    item_price = self.extract_float(self.get_item_price())
    item_qty = float(self.get_item_qty())
    subtotal = self.extract_float(self.get_subtotal())

    expected_subtotal = item_price * item_qty

    # Assertion
    assert expected_subtotal == subtotal, f"Expected subtotal {expected_subtotal}, but got {subtotal}"

  def is_total_correct(self):
    subtotal = self.extract_float(self.get_subtotal())
    tax = self.extract_float(self.get_tax_label())
    total = self.extract_float(self.get_total())

    expected_total = subtotal + tax

    # Assertion for total
    assert expected_total == total, f"Expected total {expected_total}, but got {total}"

  def is_total_amount_calculation_correct(self):
    self.is_subtotal_correct()
    self.is_total_correct()
  