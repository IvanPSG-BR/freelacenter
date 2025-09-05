# ========== IMPORTAÇÕES ========== #
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver
from requests.models import Response

import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
# ========== IMPORTAÇÕES ========== #

class Scrapper:
    def __init__(self, browser: WebDriver) -> None:
        """
        Construtor do WebScrapper
        
        ## Parameters
        browser: WebDriver
        - Navegador utilizado
        
        ## Return
        - None
        """
        load_dotenv()  # pyright: ignore[reportUnusedCallResult]
        
        self.browser: WebDriver = browser
    
    def login(self, freela_website: str) -> None:
        """
        Executa login na plataforma freelancer
        
        ## Parameters
        freela_website: str
        - Plataforma freelancer a se fazer o scrapping
            1. "WORKANA"
            2. "99FREELA"
        
        ## Return
        - None
        """
        email: str | None = os.getenv("WORKANA_EMAIL")
        password: str | None = os.getenv("WORKANA_PASS")
        
        match freela_website:
            case "WORKANA":
                url = "https://www.workana.com/pt/login"
                self.browser.get(url)
                
                email_field: WebElement = self.browser.find_element(By.ID, "email-input")
                password_field: WebElement = self.browser.find_element(By.ID, "password-input")
                submit_btn: WebElement = self.browser.find_element(By.NAME, "submit")
                
                if self.browser.current_url == "https://www.workana.com/dashboard":
                    raise Exception(f"Já está logado no website {freela_website}")
                sleep(10)
                
                # Rejeitar cookies
                self.browser.find_element(By.ID, "onetrust-pc-btn-handler").click()
                sleep(2.5)
                self.browser.find_element(By.CLASS_NAME, "ot-pc-refuse-all-handler").click()
                sleep(2.5)
                
                # Preencher os campos e enviar
                email_field.send_keys(email)  # pyright: ignore[reportArgumentType]
                sleep(5)
                password_field.send_keys(password)  # pyright: ignore[reportArgumentType]
                sleep(5)
                submit_btn.click()
                sleep(5)
                
            case "99FREELA":
                url = "" # TODO: ADICIONAR URL DO 99FREELA
                
            case _:
                raise ValueError(f"Website {freela_website} não suportado")

    def goto_works(self, category_name: str) -> None:
        """
        Acessa a página dos trabalhos
        
        ## Parameters
        category_name: str
        - Categoria específica de trabalho
            1. TI
            2. DESIGN
            3. ...
        
        ## Return
        - None
        """
        self.browser.find_element(By.CLASS_NAME, "btn-find").click()
        sleep(5)
        categories: list[WebElement] = self.browser.find_elements(By.CSS_SELECTOR, "li.checkbox")
        category: WebElement
        
        match category_name:
            case "TI":
                category = categories[1]
            case "DESIGN":
                category = categories[2]
            case _:
                raise ValueError(f"Categoria {category_name} inválida")
        
        category.click()
        sleep(5)

firefox_options: Options = Options()
firefox_options.add_argument("window-size=512,512")

scrp: Scrapper = Scrapper(webdriver.Firefox(firefox_options))

try:
    scrp.login("WORKANA")
except Exception as e:
    print(f"Atenção: {e}")
    pass

scrp.goto_works("TI")
