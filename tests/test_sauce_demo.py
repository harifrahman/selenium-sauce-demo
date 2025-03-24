import pytest
from data.data_provider import DataProvider
from pages.login import Login
from pages.products import Products
from dotenv import load_dotenv
import os

login_data = DataProvider.login_data
load_dotenv()

saucedemo_url = os.getenv('SAUCE_DEMO_URL')
saucedemo_products_url = os.getenv('SAUCE_DEMO_PRODUCTS_URL')
valid_username = os.getenv('VALID_USERNAME')
valid_password = os.getenv('VALID_PASSWORD')

@pytest.mark.positiveTc
@pytest.mark.loginCase
def test_login_web(setup):
  login_page = Login(setup)
  product_page = Products(setup)
  
  # login web-app
  login_page.fill_username(valid_username)
  login_page.fill_pasword(valid_password)
  login_page.click_login_button()

  current_url = setup.current_url
  product_page.check_current_tag_line()
  product_page.check_cart_icon()
  len_products = product_page.get_count_product()
  
  assert current_url == saucedemo_products_url
  assert len_products > 0

@pytest.mark.negativeTc
@pytest.mark.loginCase
@pytest.mark.parametrize('username, password, error_message', login_data)
def test_negative_case_login_web(username, password, error_message, setup):
  login_page = Login(setup)

  # login web-app
  login_page.fill_username(username)
  login_page.fill_pasword(password)
  login_page.click_login_button()
  
  # assert err message
  login_page.validate_error_message(error_message)
  
  assert setup.current_url == saucedemo_url
