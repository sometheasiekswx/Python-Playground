import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PythonOrgSearch (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')

    def test_search_wikipedia(self):
        driver = self.driver
        driver.get("https://www.wikipedia.org/")
        print(driver.title)
        # self.assertIn("Wikipedia", driver.title)
        self.assertIn("Wikipedia", driver.title)
        input_bar = driver.find_element(By.ID, "searchInput")
        title = "Coronavirus"
        input_bar.send_keys(title)
        input_bar.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.title_contains(title))
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (
                    By.XPATH,
                    "//html/body/div[3]/div[3]/div[4]/div/table[1]/tbody/tr[12]/td[2]/b/i"
                ),
                "Orthocoronavirinae"
            )
        )

        self.assertIn("Coronavirus", driver.title)
        assert "No results found" not in driver.page_source

        print()

    def test_english_main_page_wikipedia(self):
        driver = self.driver
        driver.get("https://www.wikipedia.org/")
        link = driver.find_element(By.ID, "js-link-box-en")
        link.click()
        WebDriverWait(driver, 5).until(
            EC.title_is("Wikipedia, the free encyclopedia"))
        in_the_news = driver.find_element(By.ID, "In_the_news")
        print(in_the_news.text)

        from_todays_featured_article = driver.find_element(
            By.ID, "From_today's_featured_article")
        print(from_todays_featured_article.text)

        assert "Welcome" in driver.page_source

        print()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
