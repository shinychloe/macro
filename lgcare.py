from retry import retry

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class Lgcare:
    def __init__(self, driver):
        self.url = "https://www.lgcareshop.co.kr:653/myshop/wishlist.jsp"
        self.userid = ""
        self.pw = ""
        self.delay = 5
        self.driver = driver
        self.driver.get(self.url)

    def login(self):
        try:
            # login
            id = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.NAME, 'userid')))
            id.send_keys(self.userid)

            input_passwd = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.NAME, 'passwd')))
            input_passwd.send_keys(self.pw, Keys.ENTER)


        except Exception:
            print("got exception(log_in)")


    def search_mask(self):
        try:
            element = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.NAME, "keyword")))
            element.send_keys("kf", Keys.ENTER)

            items = self.driver.findElements(By.xpath("//div[@id='prdListB overCont']/ul/li"));

        except:
            print("got exception(search_mask)")
            return False

    @retry(TimeoutError, tries=3)
    def buy_mask(self):
        try:
            buy = WebDriverWait(self.driver, self.delay).until(EC.element_to_be_clickable((By.LINK_TEXT, "마스크 구매하기")))
            buy.click()
            return True
        except:
            print("got exception(buy_mask)")
            return False

    def click_buy_mask(self):
        buy_btn = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, "//[contains(@onclick, 'CHG29638')]")))
        buy_btn.click()

    def handle_alert(self):
        alert = self.driver.switch_to_alert()
        alert.accept()
        print(alert.text)

    def run(self, bot):
        self.handle_alert()

        # login
        #print("login")
        #self.login()

        #buy
        #self.click_buy_mask()

