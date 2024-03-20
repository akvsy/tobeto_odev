from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Login:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def site(self):
        self.driver.get("https://www.saucedemo.com/")
        return self.driver
    
    def empty_field(self):
        driver = self.site()
        userName= self.driver.find_element(By.ID, "user-name")
        password= self.driver.find_element(By.ID, "password")
        sleep(2)
        userName.send_keys("")
        password.send_keys("")
        loginButton = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginButton.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH, "//div[@id='login_button_container']//form//h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı gösterilmesi sonucu= {testResult}")

    def empty_password(self):
        driver = self.site()
        userName = driver.find_element(By.ID, "user-name")
        userName.send_keys("standard_user")
        sleep(2)
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH, "//div[@id='login_button_container']//form//h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Şifre alanı boş geçildiğinde uyarı mesajı gösterilmesi sonucu= {testResult}")

    def locked_out(self):
        self.driver.get("https://www.saucedemo.com/")
        userName= self.driver.find_element(By.ID, "user-name")
        password= self.driver.find_element(By.ID, "password")
        sleep(2)
        userName.send_keys("locked_out_user")
        password.send_keys("secret_sauce")
        sleep(2)
        loginButton= self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(2)
        errorMessage= self.driver.find_element(By.XPATH, "//div[@id='login_button_container']//form//h3")
        testResult= errorMessage.text== "Epic sadface: Sorry, this user has been locked out."
        print(f"Locked out uyarı mesajı gösterilmesi sonucu= {testResult}")

    def valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        userName= self.driver.find_element(By.ID, "user-name")
        password= self.driver.find_element(By.ID, "password")
        sleep(2)
        userName.send_keys("standard_user")
        password.send_keys("secret_sauce")
        sleep(2)
        loginButton= self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        assert "https://www.saucedemo.com/inventory.html" in self.driver.current_url, "Giriş Başarısız"
        print("Giriş Başarılı")
        sleep(2)

        itemList= self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        testResult= len(itemList)==6
        print(f"Ekranda 6 öğe gösterilmesi durumu: {testResult}")

testClass = Login()
testClass.empty_field()
testClass.empty_password()
testClass.locked_out()
testClass.valid_login()



# Locators

# Selenium Locators, web sayfasındaki web ögelerini tanımlamak için kullanılır. ID, NAME, XPATH, LINK_TEXT, PARTIAL_LINK_TEXT, TAG_NAME, CLASS_NAME, CSS_SELECTOR olmak üzere 8 adettir.

# ```
# ID = "id"
# NAME = "name"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"
# ```

# Bir elementi bulmak için find_element() methodu

# Birden fazla elementi bulmak için find_elements() methodu kullanılır.

# “By” classı sayfadaki elementi hangi özellik ile bulacağımızı belirtir.

# ```
# find_element(By.ID, "id")
# find_element(By.NAME, "name")
# find_element(By.XPATH, "xpath")
# find_element(By.LINK_TEXT, "link text")
# find_element(By.PARTIAL_LINK_TEXT, "partial link text")
# find_element(By.TAG_NAME, "tag name")
# find_element(By.CLASS_NAME, "class name")
# find_element(By.CSS_SELECTOR, "css selector")
# ```

# ID:

# Elementin id’sini biliniyorsa locator olarak id kullanılabilir. Girilen id ye sahip ilk element döner.

# Eğer hiçbir element eşleşmiyorsa NoSuchElementException hatası ortaya çıkar.

# örnek:

# ```
# web sayfasını incelediğimizde: 
# <html>
#  <body>
#   <form id="loginForm">
#  ise locatoru:
#   login_form = driver.find_element(By.ID, 'loginForm')
#  olur.
# ```

# NAME:

# Elementin name’i biliniyorsa locator olarak name kullanılabilir. Girilen name’e sahip ilk element döner.

# Eğer hiçbir element eşleşmiyorsa NoSuchElementException hatası ortaya çıkar.

# örnek:

# ```
# Page Source:
# <html>
#  <body>
#   <form id="loginForm">
#    <input name="continue" type="submit" value="Login" />
#    <input name="continue" type="button" value="Clear" />
   
# Locator: Login butonu şu şekilde locate edilir:
# continue = driver.find_element(By.NAME, 'continue')

# *Clear butonundan önce olduğu için Login butonunu verir. 
# ```

# XPATH:

# XML ifadelerini kullanarak elementleri bulur.

# Selenium'da "copy XPath" özelliğinin çıktısı genellikle parent-child ilişkilerini dikkate alır.

# Kullanımının ana sebeplerinden biri bulmak istediğimiz element için uygun bir kimlik veya ad bulamadığımız durumlardır.

# İstediğimiz element in konumu, sırası değişirse xpath genelde değişir.

# örnek:

# ```
# <html>
#  <body>
#   <form id="loginForm">
#    <input name="username" type="text" />
#    <input name="password" type="password" />
#    <input name="continue" type="submit" value="Login" />
#   </form>
# </body>
# </html>

# Locator: text, password ve continue şu şekilde locate edilir:
# login_form = driver.find_element(By.XPATH, "/html/body/form[1]")
# login_form = driver.find_element(By.XPATH, "//form[1]")
# login_form = driver.find_element(By.XPATH, "//form[@id='loginForm']")
# ```

# LINK TEXT ve PARTIAL LINK TEXT:

# Web sayfalarındaki bağlantıları bulmak ve sonrasında işlem yaptırmak içindir.

# Bağlantı metnini kullanarak bağlantı linkini bulur. Bağlantı linkini bulduktan sonra üzerine tıklama gibi işlemler yaptırabiliriz.

# Bağlantı metninin tam eşleşmesi gerekir.

# Partial Link Text: Bağlantı metninin belirli bir kısmının belirtilerek bağlantının bulunmasını sağlar.

# Bağlantı metni tam olarak bilinmiyorsa kullanışlı olur.

# Ortak kısmi bir metne sahip bir sayfada birden çok bağlantıyı bulmak için de faydalıdır.

# örnek:

# ```
# <html>
#  <body>
#   <p>Are you sure you want to do this?</p>
#   <a href="continue.html">Continue</a>
#   <a href="cancel.html">Cancel</a>
# </body>
# </html>

# Locator: continue.html link şu şekilde locate edilir:
# continue_link = driver.find_element(By.LINK_TEXT, 'Continue')
# continue_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Conti')
# ```

# TAG NAME:

# Belirli bir etiket türüne sahip tüm ögeleri bulmak içindir.

# HTML tag name lerini kullanarak elementleri buluruz.

# Belirli bir öge türünün tüm ögelerini bulmak için faydalı olabilir.

# Geniş kapsamlı alanlarda fayda sağlayabilir.

# Örneğin sayfadaki tüm input alanlarını bulabilir, içeriğini temizleyebilir veya değiştirebiliriz.

# örnek:

# ```
# <html>
#  <body>
#   <h1>Welcome</h1>
#   <p>Site content goes here.</p>
# </body>
# </html>

# Locator: h1 şu şekilde locate edilir:
# heading1 = driver.find_element(By.TAG_NAME, 'h1')
# ```

# *bu bir element olduğunda, geniş kapsamlı bir aramada:

# tag name’i input olan elementler için locate:

# inputs = driver.find_elements_by_tag_name("input")

# for input_element in inputs:
# print(input_element.get_attribute("name"))

# şeklinde olabilir.

# CLASS NAME: Elementi class name i kullanarak bulmak istediğimizde kullanırız. Girilen class name’e sahip ilk element döner.

# Eğer hiçbir element eşleşmiyorsa NoSuchElementException hatası ortaya çıkar.

# örnek: class name’i content olan bir p elementi

# ```
# <html>
#  <body>
#   <p class="content">Site content goes here.</p>
# </body>
# </html>
# Locator:
# content = driver.find_element(By.CLASS_NAME, 'content')
# ```

# CSS SELECTORS: Elementi Css selector sintaxı kullanarak bulmak istediğimizde kullanırız. Girilen css selectore sahip ilk element döner. Eğer hiçbir element eşleşmiyorsa NoSuchElementException hatası ortaya çıkar.

# örnek:

# ```
# <html>
#  <body>
#   <p class="content">Site content goes here.</p>
# </body>
# </html>
# Locator: 
# content = driver.find_element(By.CSS_SELECTOR, 'p.content')
# ```

# **NOT: Bir elementin konumu değişse bile ID ve Name özellikleri genelde değişmez. ID ve Name elementleri tanımlamak için en yaygın kullanılan ve genellikle değişmeyen özniteliklerdir.

# Konumu değişirse ve name ve id ile çalışamıyorsak, yeni konumundaki xpath veya css selectors ile bulmak çözüm olabilir.