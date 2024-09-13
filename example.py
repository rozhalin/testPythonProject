from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Указываем путь к Yandex Browser
yandex_browser_path = "C:\\Users\\rozro\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe"
# Замените на ваш путь

# Указываем путь к ChromeDriver
chrome_driver_path = "WebDriver/chromedriver.exe"  # Замените на путь к ChromeDriver

# Настройки для WebDriver
options = Options()
options.binary_location = yandex_browser_path  # Устанавливаем путь к Yandex Browser

# Создаем объект WebDriver
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Открываем веб-страницу
driver.get("https://yandex.ru")

# Пример взаимодействия с браузером
print(driver.title)


# Закрываем браузер
driver.quit()