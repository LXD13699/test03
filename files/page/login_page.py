import  time
from selenium import  webdriver
def test_Login(driver):
  # driver = webdriver.Chrome()
  driver.find_element_by_id("userName").send_keys("admin")
  driver.find_element_by_id("password").send_keys("xn123456")
  time.sleep(3)
  driver.find_element_by_class_name("pointer").click()
  time.sleep(1)
  driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/form/div[3]/div[1]/input').send_keys("5cwwg")
  driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/form/div[5]/div[2]/button').click()