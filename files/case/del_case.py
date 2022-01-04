from unittest import TestCase
import unittest

from files.page import del_page


class delCase(TestCase):
    driver = None
    @classmethod
    def setUpClass(cls) -> None:
        print("-------------")

    def test_del(self):
        del_page.dels_Page(self.driver)


if __name__ == "__name__":
    unittest.main()