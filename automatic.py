from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep


servico = Service(ChromeDriverManager().install())

listNames = ['alisson','alexandre','roberto']
lissEmails = ['alisson@gmail.com','alexandre@gmail.com','carvalho@gmail.com']
listNumbers = [85875737,87287383,95749473]
count = 0



while True:
    if count >= len(listaNomes):
        exit()
    navegador = webdriver.Chrome(service=servico)

    navegador.get("https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_videoselenium")

    navegador.find_element('xpath', 
                       '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys((listaNomes[count]))
    navegador.find_element('xpath', 
                       '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys((listaEmail[count]))
    navegador.find_element('xpath',
                           '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[3]/div/input').send_keys((listaNumeros[count]))
    navegador.find_element('xpath', 
                           '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/button').click()
    sleep(3)    
    navegador.close()
    count += 1
        
