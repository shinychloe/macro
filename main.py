from lgcare import Lgcare
from welkeeps import Welkeeps
from selenium import webdriver
import telegram
import time

factory = 0
#0: lg 1: welkeeps
if __name__ == '__main__':
    telgram_token = '1082143969:AAHKI7hbuXeNh6uQRBnE2L9lezxYwdWgaOs'
    bot = telegram.Bot(token=telgram_token)

    # chrome web driver
    driver = webdriver.Chrome("chromedriver.exe")
    driver.maximize_window()

    if factory == 0:
        lgcare = Lgcare(driver)
        lgcare.run(bot)

    elif factory == 1:
        welkeeps = Welkeeps(driver)
        welkeeps.run(bot, threshold=10)




    # WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//div[@class='prdListB overCont']/ul/li"))))
    # allElements = driver.find_elements_by_xpath("//div[@class='prdListB overCont']/ul/li")
    #
    # for elem in allElements:
    #     if all(word in elem.text for word in check_text) and "품절" not in elem.text:
    #         paybtn = elem.find_element_by_class_name("goPay")
    #         driver.execute_script("$(argument[0]).click();", paybtn)