import os
import pathlib
import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver


def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()


driver = webdriver.Chrome()


class WebpageTests(unittest.TestCase):

    def test_title(self):
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title, "Counter with Sound")  # or change your HTML title

    def test_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element(By.ID, "increase")
        increase.click()
        heading = driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(heading, "1")

    def test_decrease(self):
        driver.get(file_uri("counter.html"))
        # Set value to 1 first so decrease shows 0
        increase = driver.find_element(By.ID, "increase")
        increase.click()

        decrease = driver.find_element(By.ID, "decrease")
        decrease.click()
        heading = driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(heading, "0")

    def test_multiple_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element(By.ID, "increase")
        for _ in range(4):
            increase.click()
        heading = driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(heading, "4")


if __name__ == "__main__":
    unittest.main()