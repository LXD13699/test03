import  unittest
from unittest import TestCase
from  selenium import  webdriver

from files.page import login_page, add_page, del_page


class AddCase(TestCase):
    driver = None
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()

    def test_01login(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://xiaonengedu.com:9001/admin/login")
        login_page.test_Login(self.driver)

    def test_02Add(self):
        add_page.AddPage(self.driver)

    def test_03del(self):
        del_page.dels_Page(self.driver)



if __name__ == "__name__":
    unittest.main()