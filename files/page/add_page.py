import  time

from selenium.webdriver import ActionChains

def AddPage(driver):
    time.sleep(2)
    driver.find_element_by_class_name("fa.fa-list-alt.nav-icon").click()
    time.sleep(2)
    driver.find_element_by_class_name("btn.btn-success").click()
    driver.find_element_by_id("blogName").send_keys("test111")
    driver.find_element_by_id("blogSubUrl").send_keys("test路径")
    driver.find_element_by_id("blogTags_tag").send_keys("test标签")
    time.sleep(4)
    #先点击下富文本
    driver.find_element_by_class_name("CodeMirror-scroll").click()
    time.sleep(2)
    #操作键盘
    ActionChains(driver).send_keys("啦啦啦").perform()

    driver.find_element_by_id("confirmButton").click()
    driver.find_element_by_id("randomCoverImage").click()
    time.sleep(1)
    driver.find_element_by_id("saveButton").click()
    driver.find_element_by_class_name("swal-button.swal-button--confirm").click()

