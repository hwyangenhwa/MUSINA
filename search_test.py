import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ViewProductDetails(unittest.TestCase):
    # declare variable to store the URL to be visited
    base_url = "https://www.musinsa.com/"

    # declare variable to store search term
    search_term = "스니커즈"

    # declare variable to store search term
    title_term = "무신사"

    # --- Pre - Condition ---
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/jun.k/driver/chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # 10 is in seconds

    # --- Steps for MUSINSA_Search_TC_001 ---
    def test_load_home_page(self):

        driver = self.driver
        driver.get(self.base_url)
        self.assertIn("무신사 - 스트릿패션, 패션잡지, 멀티샵, 중고장터", driver.title)

    # --- Steps for MUSINSA_Search_TC_002 ---
    def test_search_for_a_term(self):
        self.driver.get(self.base_url)
        searchTextBox = self.driver.find_element_by_xpath("//*[@id='wrapper']/div[1]/div/div[1]/div[1]/div[1]/input")
        searchTextBox.send_keys(self.search_term)
        searchTextBox.send_keys(Keys.RETURN)

        self.driver.implicitly_wait(10)

        self.assertIn(self.title_term, self.driver.title)
        self.assertNotIn("검색된 목록이 없습니다.", self.driver.page_source)

    # --- post - condition ---
    def tearDown(self):
        # to close the browser
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/jun.k/driver'))
