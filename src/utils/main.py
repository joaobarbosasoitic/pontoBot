from app import ChromeAuto
from time import sleep 

if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://www.ahgora.com.br/novabatidaonline/?defaultDevice=a265669')
    sleep(1)
    #passar como parametro sua matricula e senha. EX: 'teste', "123456"
    chrome.registra_ponto()
    