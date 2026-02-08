import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.3

cnpj = input("CNPJ: ")
cnpj = cnpj.replace(".", "").replace("/", "").replace("-", "")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://consulta-crf.caixa.gov.br/consultacrf/pages/consultaEmpregador.jsf")

# espera o site carregar totalmente
sleep(5)

# ===== LOCALIZA O CAMPO DE CNPJ =====
location = None
for i in range(5):
    location = pyautogui.locateCenterOnScreen(
        "textBox.png",
        confidence=0.9
    )
    if location:
        break
    sleep(1)

if not location:
    print("Campo de CNPJ NÃO encontrado")
    exit()

pyautogui.click(location)
sleep(0.2)
pyautogui.write(cnpj, interval=0.05)
print("CNPJ digitado")

# ===== ESPERA UM POUCO ANTES DO BOTÃO =====
sleep(0.7)

# ===== LOCALIZA O BOTÃO CONSULTAR =====
botao = None
for i in range(5):
    botao = pyautogui.locateCenterOnScreen(
        "botaoConsultar.png",
        confidence=0.9
    )
    if botao:
        break
    sleep(0.7)

if not botao:
    print("Botão CONSULTAR NÃO encontrado")
    exit()

pyautogui.click(botao)
print("Botão CONSULTAR clicado")

input("Pressione ENTER para fechar o navegador...")
