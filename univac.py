import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import  Keys

driver: WebDriver = webdriver.Chrome(executable_path="C:\selenium browser drivers\chromedriver.exe")

driver.maximize_window()

driver.get("https://univac.pntdns.com/")

driver.find_element_by_xpath("/html/body/header/div/nav/div/div/ul/li[6]/a").click()

time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/form/div[1]/div/input").send_keys("sabit")

time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/form/div[2]/div/input").send_keys("sab99@gmail.com")

time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/form/div[3]/div/input").send_keys("123456@Ss")

time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/form/div[4]/div/input").send_keys("123456@Ss")


time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/form/div[5]/div/button").send_keys(Keys.ENTER)


#part 2


time.sleep(1)
registration = driver.find_element_by_xpath("/html/body/header/div/nav/div/div/ul/li[1]/a")

birth = driver.find_element_by_xpath("/html/body/header/div/nav/div/div/ul/li[1]/div/a[3]")

actions = ActionChains(driver)

actions.move_to_element(registration).move_to_element(birth). click().perform()


#part 3
time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[1]/div/span/span[1]/span/span[1]").click()



time.sleep(1)
driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys("University of Dhaka")
act = ActionChains(driver)
act.send_keys(Keys.ENTER).perform()




time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[1]/div/span/span[1]/span/span[1]").click()

time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[2]/div[1]/div/input").send_keys("boys ")



time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[5]/div[1]/div/input").send_keys("5566778")

time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[6]/div[1]/div/input").send_keys("01716302462")

time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[2]/div[2]/div/input").send_keys("CSE")


time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[5]/div[2]/div/input").send_keys("22212312312398765")


time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/form/div[7]/div[2]/div/div/input").send_keys("2000-01-01")


time.sleep(3)
driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[8]/button").send_keys(Keys.ENTER)















