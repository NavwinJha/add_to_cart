import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.regression
def test_setup():
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)


@pytest.mark.regression
def test_shopping():
    driver.get("https://www.flipkart.com/")
    homePages = driver.current_window_handle
    driver.maximize_window()
    driver.implicitly_wait(5)
    close_button = driver.find_element(By.XPATH, "//*[text()= '✕']")
    close_button.click()
    order1 = driver.find_element(By.NAME, 'q')
    order1.send_keys("Toy gun")
    order1.submit()
    min_dropdown = Select(driver.find_element(By.CLASS_NAME, "_2YxCDZ"))
    min_dropdown.select_by_value("250")
    driver.find_element(By.CLASS_NAME, "s1Q9rs").click()
    orderPage = driver.window_handles[1]
    driver.switch_to.window(orderPage)
    driver.find_element(By.ID, "pincodeInputId").send_keys("110086")
    driver.find_element(By.XPATH, "//*[text()= 'Check']").click()
    driver.find_element(By.XPATH, "//*[text()= 'Buy Now']").click()

# myShopping = FlipkartShopping()
# print(myShopping)
