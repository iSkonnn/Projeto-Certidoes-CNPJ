import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import tkinter as tk

win = tk.Tk()
y = 0

win.geometry("600x600")
win.resizable(False, False);
win.title("Consulta CNPJ")


credits = tk.Label(
    win,
    text = "Desenvolvido com ❤ por Luis Humberto & Rafael Dantas",
    font=("Segoe UI", 11, "bold"),
    fg="#333333",
    bg=win["bg"]
)

credits.pack(side = "bottom")

label = tk.Label(
    win,
    text = "Digite os CNPJs (um por linha):",
    font=("Segoe UI", 11, "bold"),
    fg="#333333",
    bg=win["bg"]
)

label.pack()

entrada = tk.Text(
    win,
    font = ("Segoe UI", 12),
    wrap = "word",
    width = 33,
    height = 18
)

entrada.pack(pady = 15)

## PARTE DA UI ##
def enviar():
    conteudo = entrada.get("1.0", "end-1c")
    linhas = conteudo.splitlines()
    linhas = [l for l in linhas if l.strip()]

    ## TIRANDO AS PONTUAÇÕES DO CNPJ
    linhas = [
        l.replace(".", "").replace("/", "").replace("-", "")
        for l in linhas
    ]
    print(linhas)

b = tk.Button(
    win,
    text='Enviar',
    font=("Arial", 12, "bold"),
    width = 10,
    height = 2,
    background = "#2d89ef",
    foreground = "white",
    activebackground="#1e5fbf",
    activeforeground="white",
    command = enviar
)

b.pack(side="bottom", pady=40)


win.mainloop()


## RESTO DO BOT ##

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
