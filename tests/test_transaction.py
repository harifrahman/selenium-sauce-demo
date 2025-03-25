from data.data_provider import DataProvider
from pages.login import Login
from pages.products import Products
from pages.cart import Cart
from pages.checkout import Checkout
from pages.checkout_overview import CheckoutOverview
from pages.checkout_complete import CheckoutComplete
from dotenv import load_dotenv
import os
from time import sleep

login_data = DataProvider.login_data
load_dotenv()

saucedemo_url = os.getenv('SAUCE_DEMO_URL')
saucedemo_products_url = os.getenv('SAUCE_DEMO_PRODUCTS_URL')
saucedemo_cart_url = os.getenv('SAUCE_DEMO_CART_URL')
saucedemo_checkout_url = os.getenv('SAUCE_DEMO_CHECKOUT_URL')
saucedemo_checkout_overview_url = os.getenv('SAUCE_DEMO_CHECKOUT_OVERVIEW_URL')
saucedemo_checkout_complete_url = os.getenv('SAUCE_DEMO_CHECKOUT_COMPLETE_URL')
valid_username = os.getenv('VALID_USERNAME')
valid_password = os.getenv('VALID_PASSWORD')

def test_complete_payment_with_one_item(setup):
  login_page = Login(setup)
  product_page = Products(setup)
  cart_page = Cart(setup)
  checkout_page = Checkout(setup)
  checkout_overview_page = CheckoutOverview(setup)
  checkout_complete_page = CheckoutComplete(setup)
  
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

  # assert success navigate to checkout page
  current_url = setup.current_url
  assert current_url == saucedemo_checkout_url
  checkout_page.check_current_tag_line()

  checkout_page.fill_first_name("John")
  checkout_page.fill_last_name("Foe")
  checkout_page.fill_zip_code("123456")
  sleep(3)
  checkout_page.click_continue_btn()

  # assert success navigate to checkout-overview page
  current_url = setup.current_url
  assert current_url == saucedemo_checkout_overview_url
  checkout_overview_page.check_current_tag_line()
  checkout_overview_page.is_total_amount_calculation_correct()
  sleep(3)
  checkout_overview_page.click_finish_btn()

  # assert success navigate to checkout-complete page
  current_url = setup.current_url
  assert current_url == saucedemo_checkout_complete_url
  checkout_complete_page.verify_success_message()


  
  