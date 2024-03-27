from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains 
import pytest

class Test_Login:
    
    def setup_method(self):
        self.driver= webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
    
    def teardown_method(self):
        self.driver.quit()
    
    def getData():
        return [("deneme","1"),("abc","1"),("123","secret_sauce")]
    
    @pytest.mark.parametrize("username,password", getData())
    def test_invalid_login(self,username,password):
        username = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name"))) #usernameInput
        password = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))  #passwordInput
        username.send_keys(username)
        password.send_keys(password)
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        errorMessage =WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"


    def test_empty_field(self):
        userName= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        password= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        actions= ActionChains(self.driver)
        actions.send_keys_to_element(userName, "")
        actions.send_keys_to_element(password, "")
        actions.perform()
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "login-button")))
        loginButton.click()
        errorMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//div[@id='login_button_container']//form//h3")))
        assert errorMessage.text == "Epic sadface: Username is required"

    def test_empty_password(self):
        userName= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        password= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        actions= ActionChains(self.driver)
        actions.send_keys_to_element(userName, "standard_user")
        actions.send_keys_to_element(password, "")
        actions.perform()
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "login-button")))
        loginButton.click()
        errorMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//div[@id='login_button_container']//form//h3")))
        assert errorMessage.text == "Epic sadface: Password is required"

    def test_locked_out(self):
        userName= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        password= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        actions= ActionChains(self.driver)
        actions.send_keys_to_element(userName, "locked_out_user")
        actions.send_keys_to_element(password, "secret_sauce")
        actions.perform()
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "login-button")))
        loginButton.click()
        errorMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//div[@id='login_button_container']//form//h3")))
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

    def test_valid_login(self):
        userName= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        password= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        actions= ActionChains(self.driver)
        actions.send_keys_to_element(userName, "standard_user")
        actions.send_keys_to_element(password, "secret_sauce")
        actions.perform()
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "login-button")))
        loginButton.click()
        assert "https://www.saucedemo.com/inventory.html" in self.driver.current_url

        itemList= self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        assert len(itemList)==6

    def test_add_to_cart(self): #sepete ürün ekleme
        userName= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        password= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        actions= ActionChains(self.driver)
        actions.send_keys_to_element(userName, "standard_user")
        actions.send_keys_to_element(password, "secret_sauce")
        actions.perform()
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "login-button")))
        loginButton.click()
        addToCart= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")))
        addToCart.click()
        remove= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='remove-sauce-labs-backpack']")))
        assert remove.is_displayed()
    
    def test_low_to_high(self): #fiyatları düşükten yükseğe sıralama
        userName= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        password= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        actions= ActionChains(self.driver)
        actions.send_keys_to_element(userName, "standard_user")
        actions.send_keys_to_element(password, "secret_sauce")
        actions.perform()
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "login-button")))
        loginButton.click()
        productSort= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/div/span/select")))
        productSort.click()
        sleep(2)
        lowToHigh= self.driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/div/span/select/option[3]")
        lowToHigh.click()
        sleep(2)
        priceList= self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        prices = [float(price.text.strip('$')) for price in priceList]
        sortedPrice= sorted(prices)
        assert sortedPrice == prices
        print(sortedPrice)
        print(prices)
