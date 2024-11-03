from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Caminho para o ChromeDriver
caminho_driver = 

# Inicializa o navegador
navegador = webdriver.Chrome(executable_path=caminho_driver)

# Abre o Google
navegador.get("https://www.google.com")

# Aguarda o carregamento da página
time.sleep(2)

# Localiza a barra de pesquisa do Google
barra_pesquisa = navegador.find_element("name", "q")

# Digita o termo de pesquisa
termo_pesquisa = "Python RPA"
barra_pesquisa.send_keys(termo_pesquisa)

# Pressiona Enter para realizar a busca
barra_pesquisa.send_keys(Keys.RETURN)

# Aguarda alguns segundos para ver os resultados
time.sleep(5)

# Fecha o navegador
navegador.quit()
