from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class Welkeeps:
    def __init__(self, driver):
        self.url = "https://www.welkeepsmall.com/shop/member.html?type=login"
        self.userid = ""
        self.pw = ""
        self.delay = 5

        self.driver = driver
        self.driver.get(self.url)

    def login_naver_with_execute_script(self):
        self.driver.execute_script("sns_login_log('naver')")

        script = "                                      \
        (function execute(){                            \
            document.querySelector('#id').value = '" + self.userid + "'; \
            document.querySelector('#pw').value = '" + self.pw + "'; \
        })();"
        self.driver.execute_script(script)
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.btn_global")))
        element.click()
        return False

    def click_mask(self):
        maskbtn = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.LINK_TEXT, '미세먼지마스크')))
        maskbtn.click()

    def check_stock(self):
        #allElements = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, "//div[@class='tb-center']")))
        allElements = WebDriverWait(self.driver, self.delay).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='tb-center']")))
        result_list = []

        for elem in allElements:
            if "SOLD OUT" not in elem.text:
                result_list.append(elem)
        return result_list

    def login(self):
        self.driver.execute_script("sns_login_log('naver')")
        id = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.NAME, 'id')))
        id.send_keys(self.userid)

        input_passwd = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.NAME, 'pw')))
        input_passwd.send_keys(self.pw, Keys.ENTER)

    def run(self, bot, threshold=100):
        # login
        print("login")
        self.login_naver_with_execute_script()

        # click mask
        print("click mask")
        self.click_mask()

        # check_stock
        print("check stock start")
        count = 1
        while True:
            try:
                available = self.check_stock()
                chat_id = bot.getUpdates()[-1].message.chat.id

                if len(available) > 0:
                    bot.send_message(chat_id, text="웰킵스 재고 있음\n" + self.driver.current_url + "\n" + available[0].text)
                    available[0].click()
                    break
                else:
                    print("refresh ", count)
                    if count % threshold == 0:
                        print("=========================")
                        bot.send_message(chat_id, text="웰킵스 재고 없음ㅠㅠ")
                    self.driver.refresh()

            except Exception as e:
                print("unkown error")
                print(e)

            count = count + 1
            time.sleep(5)