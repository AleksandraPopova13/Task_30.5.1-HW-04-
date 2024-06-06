import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import  Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(autouse=True)
def driver():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')

    yield driver

    driver.quit()

# Явное ожидание
def test_all_my_pets(driver):
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'email')))
    driver.find_element(By.ID, 'email').send_keys('qwertyuio@gmail.com')
    driver.find_element(By.ID, 'pass').send_keys('123456789')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    driver.find_element(By.XPATH, '//a[text()="Мои питомцы"]').click()



# Неявное ожидание


def test_show_my_pets(driver):
    driver.find_element(By.ID, 'email').send_keys('Ваша почта')
    driver.find_element(By.ID, 'pass').send_keys('ваш пароль')
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'PetFriends'