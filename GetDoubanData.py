import time

from selenium import webdriver


CHROME_PATH = "/Users/xh/Downloads/ks/publicOpinionSystem/chromedriver_91_0_4472"  # your chromedriver_91_0_4472's path
chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument('--no-sandbox')
chrome_opt.add_argument("--disable-dev-shm-usage")
# chrome_opt.add_argument("proxy-server=http://127.0.0.1:1087")  # 加载代理IP

driver = webdriver.Chrome(executable_path=CHROME_PATH, desired_capabilities=chrome_opt.to_capabilities())
driver.get("http://www.douban.com")
driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])#切换iframe子框架，因为豆瓣的网页中的登录那部分是一个ifrme，必须切换才能寻找到对应元素
time.sleep(6)
driver.find_element_by_class_name('account-tab-account').click()
# driver.find_element_by_class_name("account-tab-account").click()
driver.find_element_by_id("username").click()
driver.find_element_by_id("username").send_keys("13651286925")
driver.find_element_by_id("password").click()
driver.find_element_by_id("password").send_keys("13651286925")
time.sleep(2)
driver.find_element_by_class_name("account-form-field-submit ").click()
time.sleep(2)
#识别滑块进行登录