import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.3

cnpj = input("CNPJ: ");

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://consulta-crf.caixa.gov.br/consultacrf/pages/consultaEmpregador.jsf")

# espera o site carregar totalmente
time.sleep(9)

# ===== LOCALIZA O CAMPO DE CNPJ =====
location = None
for i in range(5):
    location = pyautogui.locateCenterOnScreen(
        "textBox.png",
        confidence=0.9
    )
    if location:
        break
    time.sleep(1)

if not location:
    print("Campo de CNPJ NÃO encontrado")
    exit()

pyautogui.click(location)
time.sleep(0.5)
pyautogui.write(cnpj, interval=0.05)
print("CNPJ digitado")

# ===== ESPERA UM POUCO ANTES DO BOTÃO =====
time.sleep(1.5)

# ===== LOCALIZA O BOTÃO CONSULTAR =====
botao = None
for i in range(5):
    botao = pyautogui.locateCenterOnScreen(
        "botaoConsultar.png",
        confidence=0.9
    )
    if botao:
        break
    time.sleep(1)

if not botao:
    print("Botão CONSULTAR NÃO encontrado")
    exit()

pyautogui.click(botao)
print("Botão CONSULTAR clicado")

input("Pressione ENTER para fechar o navegador...")
