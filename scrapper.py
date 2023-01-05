import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Scrapper:
    def __init__(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)

        pokemon_url = 'https://redeem.tcg.pokemon.com/en-us/'
        self.driver.get(pokemon_url)
        WebDriverWait(self.driver, 3600).until(expected_conditions.presence_of_element_located((By.ID, "code")))

        time.sleep(5)
        self.code_box       = self.driver.find_element(By.ID, "code")  
        self.send_code_box  = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Soumettre le code')]")
        self.validate_codes_box  = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Obtenir')]")
        print(self.send_code_box)
        self.current_codes  = 0

    def add_item(self, code):
        self.code_box.send_keys(code)
        time.sleep(0.2)
        self.validate_code()

    def validate_code(self):
        try:
            self.send_code_box.click()
        except Exception as e:
            self.send_code_box  = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Soumettre le code')]")
            self.send_code_box.click()
        time.sleep(1)
        self.current_codes += 1
        if self.current_codes > 9:
            self.validate_form()
            self.current_codes = 0

    def validate_form(self):
        try:
            self.validate_codes_box  = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Obtenir')]")
            self.validate_codes_box.click()
        except Exception as e:
            self.validate_codes_box  = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Obtenir')]")
            self.validate_codes_box.click()
        time.sleep(5)