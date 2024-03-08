import pyautogui as py
import pandas as pd
import time

py.PAUSE = 0.9 # Espera para poder dar tempo de carregar o navegador, para poder escrever o link

# Abrindo o navegador
py.press("win")  
py.write("chrome")
py.press("enter")
py.click(x=273, y=635)

# Fazer login no sistema
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
py.write(link)
py.press("enter")

time.sleep(3)
py.click(x=424, y=374) # Clicar campo de email
py.write("ana@hotmail.com")
py.press("tab")
py.write("123456789")
py.press("enter")
time.sleep(3)

# Importar a base de dados produtos.csv
produtos = pd.read_csv("C:\Curso_Python\Automoção de tarefa\produtos.csv") #caminho do arquivo

# Cadastrando os produto 
for linha in produtos.index:

    py.click(x=440, y=262) # Clicar campo de codigo do produto

    codigo = produtos.loc[linha, "codigo"]
    py.write(str(codigo))
    py.press("tab")

    py.write(str(produtos.loc[linha, "marca"]))
    py.press("tab")
    
    py.write(str(produtos.loc[linha, "tipo"]))
    py.press("tab")
    
    py.write(str(produtos.loc[linha, "categoria"]))
    py.press("tab")
    
    py.write(str(produtos.loc[linha, "preco_unitario"]))
    py.press("tab")
    
    py.write(str(produtos.loc[linha, "custo"]))
    py.press("tab")
    
    obs = produtos.loc[linha, "obs"]
    if not pd.isna(obs):
        py.write(str(produtos.loc[linha, "obs"]))
    py.press("tab")
    py.press("enter") 
   
    # dar scroll de tudo pra cima
    py.scroll(5000)


