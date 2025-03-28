import pytest
from data.data_provider import DataProvider
from pages.login import Login
from pages.products import Products
from dotenv import load_dotenv
import os
import allure

login_data = DataProvider.login_data
load_dotenv()

saucedemo_url = os.getenv('SAUCE_DEMO_URL')
saucedemo_products_url = os.getenv('SAUCE_DEMO_PRODUCTS_URL')
valid_username = os.getenv('VALID_USERNAME')
valid_password = os.getenv('VALID_PASSWORD')

@pytest.mark.positiveTc
@pytest.mark.loginCase
@allure.title("Test login feature")
@allure.description("This test is for covering login feature | positive case")
@allure.testcase("testrail-12345")
def test_login_web(setup):
  login_page = Login(setup)
  product_page = Products(setup)
  
  with allure.step("Input username"):
    login_page.fill_username(valid_username)
  
  with allure.step("Input password"):
    login_page.fill_pasword(valid_password)
  
  with allure.step("Click login button"):
    login_page.click_login_button()

  with allure.step("Validate assertions"):
    current_url = setup.current_url
    product_page.check_current_tag_line()
    product_page.check_cart_icon()
    len_products = product_page.get_count_product()

    assert current_url == saucedemo_products_url
    assert len_products > 0
    setup.save_screenshot('success_login_screenshot.png')
    allure.attach.file("success_login_screenshot.png", name="Screenshot Login", attachment_type=allure.attachment_type.PNG)

@pytest.mark.negativeTc
@pytest.mark.loginCase
@pytest.mark.parametrize('username, password, error_message', login_data)
@allure.title("Test login feature - negative test case")
@allure.description("This test is for covering login feature | negative case")
@allure.testcase("testrail-12346")
def test_negative_case_login_web(username, password, error_message, setup):
  login_page = Login(setup)

  # login web-app
  with allure.step("Input username"):
    login_page.fill_username(username)
  
  with allure.step("Input password"):
    login_page.fill_pasword(password)
  
  with allure.step("Click login button"):
    login_page.click_login_button()
  
  with allure.step("Validate assertions"):
    login_page.validate_error_message(error_message)
    assert setup.current_url == saucedemo_url
