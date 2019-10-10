import unittest
from selenium import webdriver
import time
import HtmlTestRunner
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from POM.page.registration.registration1 import RegistrationPage
from POM.page.cart.Addtocart import AddCart
from POM.page.loginpage import Loginpage
from POM.screenshot import screen
from POM import report

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/akkar/PycharmProjects/sobiasif/POM/Driver/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        print("Test Start")

    def test1_sign_up1(self):
        driver = self.driver
        driver.get("http://demo.automationtesting.in/")
        driver.implicitly_wait(5)
        login = Loginpage(driver)
        login.click_sign_up()
        driver.implicitly_wait(5)
        reg = RegistrationPage(driver)
        reg.enter_firstname("sk")
        reg.enter_lastname("Ali")
        #reg.address("123 ABC")
        reg.enter_email_address("Cacctesting@gmail.com")
        reg.enter_phone("6473344677")
        reg.click_male()
        reg.click_cricket()
        #reg.select_language()
        reg.select_skills()
        reg.select_country()
        reg.select_countries()
        reg.select_year()
        reg.select_month()
        reg.select_day()
        reg.enter_password("Skali2019")
        reg.enter_confirmed_password("Skali2019")
        reg.click_submit()
        driver.implicitly_wait(20)

    def test2_Addcart2(self):
        driver = self.driver
        driver.implicitly_wait(20)
        driver.maximize_window()
        driver.get("http://practice.automationtesting.in/")
        driver.implicitly_wait(20)
        cart = AddCart(driver)
        cart.click_practice_page()
        screen.screenshot(self)
        driver.implicitly_wait(5)
        cart.click_add_cart()
        cart.view_cart()
        cart.click_proceed_to_checkout()
        cart.enter_firstname("Sk")
        cart.enter_lastname("Ali")
        cart.enter_companyname("CACC")
        cart.enter_email("Cacctesting@gmail.com")
        cart.enter_phone("6473344677")
        cart.select_country()
        cart.enter_address("123 ABC")
        cart.enter_city()
        cart.select_province()
        cart.enter_postalcode("a2s2t2")
        cart.select_payment()
        cart.place_order()
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=(HtmlTestRunner.HTMLTestRunner(output="/Users/akkar/PycharmProjects/sobiasif/POM/report/report1")))
