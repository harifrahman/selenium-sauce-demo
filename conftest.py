import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions

@pytest.fixture
def setup():
  # init setup part
  chrome_option = ChromeOptions()
  chrome_option.add_experimental_option('detach', True)
  # chrome_option.add_argument("--headless=new")

  # init chrome driver
  driver = webdriver.Chrome(options= chrome_option)
  driver.implicitly_wait(5) # can be general stuff for waiting time boundaries
  driver.maximize_window()

  # go to url
  driver.get("https://www.saucedemo.com/")

  # yield driver
  yield driver

  # tear down
  driver.quit()
