# _*_coding:utf-8_*_  
from selenium import webdriver
import datetime  
import time
from selenium.webdriver.chrome.options import Options

shoes_name = 'kyrie-5-nike-day/'
#Chrome浏览器。
driver = webdriver.Chrome(executable_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.fullscreen_window()
#无头
#chrome_options = Options()
#chrome_options.add_argument('--headless')
#driver = webdriver.Chrome(chrome_options=chrome_options)

def login(username, password):
   driver.get("https://www.nike.com/cn/launch/")

   #点击登录链接
   driver.find_element_by_css_selector('#root > div > div > div.main-layout > div > header > div.d-sm-h.d-lg-b > section > ul > li.member-nav-item.d-sm-ib.va-sm-m > button').click()
   #通过二次定位找到用户名输入框
   div=driver.find_element_by_class_name("mobileNumber-div").find_element_by_name("verifyMobileNumber")
   div.send_keys(username)
   driver.find_element_by_name("password").send_keys(password)  
   driver.find_element_by_xpath("//div[contains(@class, 'submit')]").click()
   time.sleep(3)
   driver.get("https://www.nike.com/cn/launch/t/" + shoes_name)
   time.sleep(5)
   driver.find_element_by_xpath("//li[5]/button").click()
   driver.find_element_by_xpath("//div[2]/div/button").click()
   driver.find_element_by_xpath("//div[1]/section/ul/li[3]/a").click()
   try:
       element = WebDriverWait(driver, 10).until(
           EC.presence_of_element_located((By.xpath, "//div[2]/div[2]/aside/div[6]/div/button"))
       )
   finally:
       driver.quit()
   driver.find_element_by_xpath("//div[2]/div[2]/aside/div[6]/div/button").click()
   driver.find_element_by_xpath("//div[contains(@class, 'ncss-btn-accent')]").click()


# buytime = '2019-01-01 10:00:00   #以下是定时操作
def buy_on_time(buytime):
    while True:
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
            driver.find_element_by_link_text("立即购买").click()


# entrance
#login('账号', '密码')
login('18810286625', 'Esteem940625')
#buy_on_time('2019-01-01 10:00:00')    #抢购时间
  
