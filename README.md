# Selenium Sauce Demo

Arif learn selenium with Page Object Model approach.

This repository contains automated tests for the Sauce Demo web application using Selenium and Python. The tests are organized using the pytest framework.

## Project Structure

```
data/       -> contains data provider that will consume for parameterize tests
locators/   -> contains list of locator stuff (like id or xpath for each page components)
pages/      -> contains each action for specific pages (filling field, find elements, click-able action, etc)
reports/    -> folder to store dynmic reports when tests run
tests/      -> contains tests scenario
.env        -> list of config-environments
pytest.ini  -> configuration file for the pytest framework
conftest.py -> fixture (preparation and teardown method)
requirements.txt
.gitignore
LICENSE
```

## Setup

1. **Clone the repository:**
    ```sh
    git clone git@github.com:harifrahman/selenium-sauce-demo.git
    cd selenium-sauce-demo
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv-selenium
    source venv-selenium/bin/activate  # On Windows use `venv-selenium\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    Create a file `.env` file in the root directory and add the following variables:
    ```
    SAUCE_DEMO_URL=<sauce_demo_url>
    SAUCE_DEMO_PRODUCTS_URL=<sauce_demo_products_url>
    VALID_USERNAME=<valid_username>
    VALID_PASSWORD=<valid_password>

    ...
    etc
    ```

## Running Tests

To run the tests, use the following command:
```sh
pytest
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to contribute to this project by creating pull requests or reporting issues.