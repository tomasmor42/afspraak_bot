from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

IND_LIST = ['IND Amsterdam', 'IND Den Haag', 'IND Zwolle', 'IND Den Bosch']
URL = "https://oap.ind.nl/oap/nl/#/BIO"

def find_spot(driver):
    try:
        driver.find_element(By.CSS_SELECTOR, "button.btn.btn-sm.available.btn-default")
        return True
    except NoSuchElementException:
        arrow = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-default.btn-secondary.btn-sm.pull-right')
        arrow.click()
        return False


def iterate_through_cities(driver):
    for city in IND_LIST:
        select = Select(driver.find_element('name', 'desk'))
        select.select_by_visible_text(city)
        for _ in range(2):
            res = find_spot(driver)
            if res:
                print(f"There is a spot in in {city} ")
                return city
        driver.refresh()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.NAME, "desk")))

def get_data():
    driver = webdriver.Chrome()
    driver.get(URL)
    res = iterate_through_cities(driver)
    driver.quit()

