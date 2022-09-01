# Импорт необходимых библиотек
import time
import datetime
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Подготовка переменных
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
base_url = "https://select2.org/selections"

# Вход на сайт
driver.get(base_url)
driver.maximize_window()

# Проверка наличия слов 'Built-in escaping'.
# Способ №1. Проверка по всей странице.
assert 'Built-in escaping' in driver.page_source

# Способ №2. Проверка конкретного элемента.
assert 'Built-in escaping' == driver.find_element(By.ID, 'built-in-escaping').text

# Открыть первый выпадающий список и выбрать 3-ий пункт
driver.find_element(By.XPATH, '//span[@class="select2-selection select2-selection--single"]').send_keys(Keys.RETURN + Keys.DOWN*2 + Keys.RETURN)

# Сделать скриншот выбора и сохранить в папке screen
time.sleep(1)
driver.save_screenshot('./screen/' + 'screenshot_' + datetime.datetime.utcnow().strftime('%Y.%m.%d_%H:%M:%S') + '.png')

# Открыть второй выпадающий список и выбрать 2-ий пункт
driver.find_element(By.XPATH, '//span[@class="select2-selection select2-selection--multiple"]').send_keys(Keys.RETURN + Keys.DOWN + Keys.RETURN)

# Сделать скриншот выбора и сохранить в папке screen
time.sleep(1)
driver.save_screenshot('./screen/' + 'screenshot_' + datetime.datetime.utcnow().strftime('%Y.%m.%d_%H:%M:%S') + '.png')

# Переход по ссылке в тексте
driver.get(driver.find_element(By.LINK_TEXT, 'internal representation of the selected option').get_attribute('href'))
assert driver.current_url == 'https://select2.org/options'

# Закрытие веб-драйвер
time.sleep(2)
driver.close()
