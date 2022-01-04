import time
def dels_Page(driver):
    driver.find_element_by_xpath('//*[@id="2113"]/td[3]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[2]/div[1]/button[3]').click()
    time.sleep(1)
    driver.find_element_by_class_name("swal-button.swal-button--confirm.swal-button--danger").click()
    time.sleep(1)
    driver.find_element_by_class_name("swal-button.swal-button--confirm").click()



#做了修改操作