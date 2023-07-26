# Passo a passo:
# 1 entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time
import pandas as pd

# pyautogui.write
# pyautogui.press
# pyautogui.click
# pyautogui.hotkey
# pyautogui.PAUSE

pyautogui.PAUSE = 0.6

# abrir o navegador:
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "l")

# entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

# 2 fazer login
# selecionar o campo de email
pyautogui.click(x=316, y=463)

# escrever o seu email / adicionar um email de acesso
pyautogui.write("#")
# adicionar um email de acesso
pyautogui.press("tab")
# adicionar uma senha de acesso
pyautogui.write("#")
pyautogui.hotkey("tab", "enter")
time.sleep(2)

# 3 importar a base de produtos pra cadastrar
tabela = pd.read_csv("produtos.csv")

# 4 cadastrar um produto
# # +
# 5 repetir o processo de cadastro até o fim
for linha in tabela.index:
    print(linha)
    # clicar no campo de código
    pyautogui.click(x=290, y=313)
    # pegar da tabela o valor do campo que quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # próximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    # dar scroll pra cima
    pyautogui.scroll(5000)
    