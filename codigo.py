# passo a passo do projeto
# passo 1:Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
 # installacoes utiliza o pip install

import pyautogui
import time

pyautogui.PAUSE = 0.5  #config de timer do processo
#pyautogui.click() clica em algum lugar da tela
#pyautogui.write() escreve um texto
#pyautogui.press() pressiona 1 tecla
#pyautogui.hotkey() combinacao de teclas

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
login = "Wesleyluan0511@gmail.com"
senha = "123"

pyautogui.press ("win")
pyautogui.write ("opera")
pyautogui.press ("enter")


pyautogui.write(link)
pyautogui.press ("enter")

time.sleep(3)

#login
pyautogui.click(x=1027, y=392)
pyautogui.write(login)
#senha
pyautogui.press("tab")
pyautogui.write(senha)
#buttom
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# Passo 3: Importar o csv de dados
import pandas   #pandas normalmente consegue ler as coisas de arquivos e para ler pdf utiliza o tabulas

tabelas = pandas.read_csv("./Aula 1/produtos.csv")
# passo 4: cadastrar 1 produto


#cadastrar o codigo do produto 
for linha in tabelas.index: #o for so funciona se o codigo estiver intendado com tab, se estiver fora do tab sai do loop
    
    pyautogui.click(x=1019, y=275)
    time.sleep(2) 
    #Codigo   
    pyautogui.write(tabelas.loc[linha, "codigo"])
    pyautogui.press("tab")

    #Marca
    pyautogui.write(tabelas.loc[linha, "marca"])
    pyautogui.press("tab")

    #Tipo
    pyautogui.write(tabelas.loc[linha, "tipo"])
    pyautogui.press("tab")

    #Categoria
    categoria = str(tabelas.loc[linha, "categoria"])  #conversao de int para str
    pyautogui.write(categoria)
    pyautogui.press("tab")

    #Preco
    pyautogui.write(str(tabelas.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    #Custo
    pyautogui.write(str(tabelas.loc[linha, "custo"]))
    pyautogui.press("tab")

    #Observacao
    obs = tabelas.loc[linha, "obs"]
    if not pandas.isna(obs):  #isna = é vazio 
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)  #scrolla para o topo da tela sendo + ou para baixo sendo -
time.sleep(2)



