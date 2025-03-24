import pytest
from data.data_provider import DataProvider
from pages.login import Login
from pages.products import Products
from pages.cart import Cart
from dotenv import load_dotenv
import os

login_data = DataProvider.login_data
load_dotenv()

saucedemo_url = os.getenv('SAUCE_DEMO_URL')
saucedemo_products_url = os.getenv('SAUCE_DEMO_PRODUCTS_URL')
saucedemo_cart_url = os.getenv('SAUCE_DEMO_CART_URL')
valid_username = os.getenv('VALID_USERNAME')
valid_password = os.getenv('VALID_PASSWORD')

def test_complete_payment_with_one_item(setup):
  login_page = Login(setup)
  product_page = Products(setup)
  cart_page = Cart(setup)
  
  # login web-app
  login_page.fill_username(valid_username)
  login_page.fill_pasword(valid_password)
  login_page.click_login_button()

  current_url = setup.current_url
  product_page.check_current_tag_line()
  product_page.check_cart_icon()
  len_products = product_page.get_count_product()
  
  # assert success navigate to products page
  assert current_url == saucedemo_products_url
  assert len_products > 0

  products_list = product_page.get_products()
  first_product = products_list[0]
  add_to_cart_button = product_page.get_add_to_cart_btn(first_product)
  add_to_cart_button.click()

  product_page.click_cart_icon()

  # assert success navigate to cart page
  current_url = setup.current_url
  assert current_url == saucedemo_cart_url
  cart_page.check_current_tag_line()

  cart_page.click_cart_icon()
