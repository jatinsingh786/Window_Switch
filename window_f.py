import unittest
from selenium import webdriver

path = '/home/jatin/Downloads/chromedriver'


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(path)
        self.driver.maximize_window()

    def test_window(self):
        driver = self.driver
        driver.get('https://www.naukri.com/')
        win1 = driver.title
        print(win1)

        window_after = driver.window_handles[1]

        driver.switch_to.window(window_after)
        win2 = driver.title
        print(win2)

        window_after1 = driver.window_handles[2]

        driver.switch_to.window(window_after1)
        win3 = driver.title
        print(win3)

        window_after2 = driver.window_handles[3]

        driver.switch_to.window(window_after2)
        win4 = driver.title
        print(win4)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
