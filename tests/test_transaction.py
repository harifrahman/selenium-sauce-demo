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
  
  # Login to the web app
  login_page.fill_username(valid_username)
  login_page.fill_pasword(valid_password)
  login_page.click_login_button()

  # Verify navigation to products page
  assert setup.current_url == saucedemo_products_url
  product_page.check_current_tag_line()
  product_page.check_cart_icon()
  assert product_page.get_count_product() > 0

  # Add first product to cart
  first_product = product_page.get_products()[0]
  product_page.get_add_to_cart_btn(first_product).click()
  product_page.click_cart_icon()

  # Verify navigation to cart page
  assert setup.current_url == saucedemo_cart_url
  cart_page.check_current_tag_line()
  cart_page.click_cart_icon()

  # Verify navigation to checkout page
  assert setup.current_url == saucedemo_checkout_url
  checkout_page.check_current_tag_line()
  checkout_page.fill_first_name("John")
  checkout_page.fill_last_name("Foe")
  checkout_page.fill_zip_code("123456")
  sleep(3)
  checkout_page.click_continue_btn()

  # Verify navigation to checkout overview page
  assert setup.current_url == saucedemo_checkout_overview_url
  checkout_overview_page.check_current_tag_line()
  checkout_overview_page.is_total_amount_calculation_correct()
  sleep(3)
  checkout_overview_page.click_finish_btn()

  # Verify navigation to checkout complete page
  assert setup.current_url == saucedemo_checkout_complete_url
  checkout_complete_page.verify_success_message()
