# import pyautogui
import requests
import bs4
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
# Importa el módulo de acciones encadenadas
from selenium.webdriver import ActionChains

# Crea un objeto Service con la ruta del chromedriver
service = Service(
    executable_path="C:\\chromedriver\\chromedriver-win32\\chromedriver.exe")

# Crea una instancia del objeto WebDriver para Google Chrome
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

# Abre la página web de bowman
driver.get("https://bowman.game-files.crazygames.com/ruffle/bowman.html?v=1.271")

input("Abriendo navegador, cuando esté listo presione 'Enter'")

# ENCUENTRA EL ELEMENTO HTML QUE REPRESENTA EL FONDO DEL JEUGO
id_archer = driver.find_element(By.XPATH, '//*[@id="game"]/div[1]')

# Crea un objeto de acciones encadenadas
actions = ActionChains(driver)

# Mueve el mouse a una posición relativa al fondo del juego
# El primer argumento es el elemento de referencia
# El segundo argumento es el desplazamiento horizontal en píxeles
# El tercer argumento es el desplazamiento vertical en píxeles
actions.move_to_element_with_offset(id_archer, 100, 100)

# Hace clic con el botón izquierdo del mouse
actions.click()

# Ejecuta la cadena de acciones
actions.perform()
print(id_archer)


# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--ignore-ssl-errors')
# options.add_argument('--ssl-protocol=any')

# import requests
# from bs4 import BeautifulSoup

# # Hace una petición HTTP a la página web de bowman
# response = requests.get("https://www.1001juegos.com/juego/bowman")

# # Crea una instancia del objeto BeautifulSoup con el contenido HTML de la respuesta
# soup = BeautifulSoup(response.content, "html.parser")

# # Obtiene el título de la página web
# title = soup.title.string

# Imprime el título de la página web
# print(title)


# import pyautogui

# # Mueve el cursor a la posición (100, 200)
# pyautogui.moveTo(666, 333)

# # Hace clic con el botón izquierdo del mouse
# pyautogui.rightClick()
