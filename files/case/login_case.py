from unittest import TestCase
from  selenium import  webdriver
import  unittest

from files.page import login_page


class LoginCase(TestCase):
    driver = None
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
    def test_o1(self):
        self.driver.maximize_window()
        self.driver.get("http://xiaonengedu.com:9001/admin/login")
        login_page.test_Login(self.driver)


if __name__ =="__name__":
    unittest.main()