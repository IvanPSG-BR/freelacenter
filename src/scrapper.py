# IMPORTAÇÕES
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


class Scrapper:
    def __init__(self, browser: WebDriver) -> None:
        """
        Construtor do WebScrapper
        
        @param: (browser: WebDriver)
        @return: None
        """
        load_dotenv()  # pyright: ignore[reportUnusedCallResult]
        
        self.browser: WebDriver = browser
    
    def login(self, freela_website: str) -> None:
        """
        Método responsável pelo login na plataforma freelancer
        
        @param: (freela_website: str)
        - "WORKANA"
        - "99FREELA"
        @return: None
        """
        url = ""
        email: str | None = os.getenv("WORKANA_EMAIL")
        password: str | None = os.getenv("WORKANA_PASS")
        
        match freela_website:
            case "WORKANA":
                url = "https://www.workana.com/pt/login"
                self.browser.get(url)
                
                email_field: WebElement = self.browser.find_element(By.ID, "email-input")
                password_field: WebElement = self.browser.find_element(By.ID, "password-input")
                submit_btn = self.browser.find_element(By.NAME, "submit")
                
                if self.browser.current_url == "https://www.workana.com/dashboard":
                    raise Exception(f"Já está logado no website {freela_website}")
                
                sleep(15)
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

firefox_options: Options = Options()
firefox_options.add_argument("--window-size:512,512")

scrp: Scrapper = Scrapper(webdriver.Firefox(firefox_options))

scrp.login("WORKANA")
