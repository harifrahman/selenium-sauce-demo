import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from dotenv import load_dotenv
import os
import allure

load_dotenv()
saucedemo_url = os.getenv('SAUCE_DEMO_URL')

@pytest.fixture
def setup():
  with allure.step('init & setup option chrome driver'):
    chrome_option = ChromeOptions()
    chrome_option.add_experimental_option('detach', True)
    chrome_option.add_argument("--headless=new")
    driver = webdriver.Chrome(options= chrome_option)
    driver.implicitly_wait(5) # can be general stuff for waiting time boundaries
    driver.maximize_window()

  with allure.step('go to url'):
    driver.get(saucedemo_url)

  yield driver

  with allure.step('tear down'):
    driver.quit()
