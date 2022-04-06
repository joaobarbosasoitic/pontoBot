from pathlib import Path
from tkinter import BROWSE
from webbrowser import Chrome
from selenium import webdriver
from time import sleep 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions


ROOT_FOLDER = Path(__file__).parent.parent.parent       
CHROME_DRIVER_PATH = ROOT_FOLDER / 'bin'/ 'chromedriver.exe'

class ChromeAuto:


    def __init__(self):
        self.driver_path = CHROME_DRIVER_PATH
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--profile-directory=1')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options = self.options
        )
    
    def acessa(self, site):
        self.chrome.get(site)


    def exit(self):
        sleep(5)
        self.chrome.quit()

    def registra_ponto(self, matricula, senha):
        try:
            self.chrome.find_element(By.CSS_SELECTOR, ".MuiButton-text").click()
            self.chrome.find_element(By.ID, "outlined-basic-account").send_keys(matricula)
            self.chrome.find_element(By.ID, "outlined-basic-password").send_keys(senha)
            sleep(2)
            self.chrome.find_element(By.CSS_SELECTOR, ".jss105").click()
            self.chrome.find_element(By.CSS_SELECTOR, ".jss105").click()
            sleep(2)
            self.chrome.find_element(By.CSS_SELECTOR, ".jss91").click()
            
        except Exception as e:
            print('Erro ao bater o ponto', e)


if __name__ == '__main__':
    matricula = input("Digite sua matricula: ")
    senha = input('Digite sua senha: ')
    chrome = ChromeAuto()
    chrome.acessa('https://www.ahgora.com.br/novabatidaonline/?defaultDevice=a265669')
    sleep(1)
    chrome.registra_ponto(matricula, senha)
    chrome.exit()

    
