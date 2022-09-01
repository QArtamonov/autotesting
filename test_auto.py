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

# Проверка наличия слов 'Built-in escaping'
# Способ №1. Проверка по всей странице
assert 'Built-in escaping' in driver.page_source

# Способ №2. Проверка в конкретном элементе
assert 'Built-in escaping' == driver.find_element(By.ID, 'built-in-escaping').text

# Открытие первого выпадающего списока и выбор 3-го пункта
driver.find_element(By.XPATH, '//span[@class="select2-selection select2-selection--single"]').send_keys(Keys.RETURN + Keys.DOWN*2 + Keys.RETURN)

# Сохранение сделанного скриншота в папку screen
time.sleep(1)
driver.save_screenshot('./screen/' + 'screenshot_' + datetime.datetime.utcnow().strftime('%Y.%m.%d_%H:%M:%S') + '.png')

# Открытие второго выпадающего списока и выбор 2-го пункта
driver.find_element(By.XPATH, '//span[@class="select2-selection select2-selection--multiple"]').send_keys(Keys.RETURN + Keys.DOWN + Keys.RETURN)

# Сохранение сделанного скриншота в папку screen
time.sleep(1)
driver.save_screenshot('./screen/' + 'screenshot_' + datetime.datetime.utcnow().strftime('%Y.%m.%d_%H:%M:%S') + '.png')

# Переход по ссылке в тексте
driver.get(driver.find_element(By.LINK_TEXT, 'internal representation of the selected option').get_attribute('href'))
assert driver.current_url == 'https://select2.org/options'

# Закрытие веб-драйвера
time.sleep(2)
driver.close()
