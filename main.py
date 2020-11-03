from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, InvalidSessionIdException
import time


class Parse:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)

    def close(self):
        self.browser.close()

    def connect(self, url, product_name):
        self.browser.get(url)
        self.browser.implicitly_wait(10)
        alert = self.browser.find_element_by_css_selector("body > div._111XIPXNiH.main > div:nth-child(6) > div > "
                                                          "div:nth-child(6) > div > div > div > div:nth-child(2) > "
                                                          "div > div > div > div:nth-child(2) > button")
        alert.click()

        self.browser.find_element_by_id("header-search").send_keys(product_name)
        self.browser.implicitly_wait(3)
        search = self.browser.find_element_by_class_name("_1XiEJDPVpk")
        search.click()

    def find_element(self):
        self.browser.find_element_by_class_name("_3gaRuC1vxz").click()

    def find_products_name(self):
        product_names = self.browser.find_elements_by_css_selector("body > div._111XIPXNiH.main > div:nth-child(4) > "
                                                                   "div.tamefSzMtq > div:nth-child(5) > div > "
                                                                   "div:nth-child(1) > div > div > div > article > "
                                                                   "div._1OAvzJPfIW > div._1B9w_GzQuM > h3 > a > span")
        self.browser.implicitly_wait(10)

        return product_names

    def find_products_price(self):
        product_prices = self.browser.find_elements_by_css_selector("body > div._111XIPXNiH.main > div:nth-child(4) > "
                                                                    "div.tamefSzMtq > div:nth-child(5) > div > "
                                                                    "div:nth-child(1) > div > div > div > article > "
                                                                    "div._2NT_3f9Yo2 > div._tQj_HEc1V > "
                                                                    "div._3d77BH2-30._31Wu8VzvWW > div > "
                                                                    "span > span:nth-child(1)")
        self.browser.implicitly_wait(10)
        return product_prices

    def get_name_price(self):
        res = []

        def write():
            result_1 = []
            result_2 = []
            product_list = self.find_products_name()
            price_list = self.find_products_price()

            for i in product_list:
                result_1.append(i.text)

            for j in price_list:
                result_2.append(j.text)

            for item in range(len(result_1)):
                try:
                    res.append([result_1[item], result_2[item]])
                except IndexError:
                    break

        while True:
            more = self.browser.find_element_by_css_selector("body > div._111XIPXNiH.main > div:nth-child(4) > "
                                                             "div.tamefSzMtq > div:nth-child(5) > div > "
                                                             "div:nth-child(2) > div > button")
            more.location_once_scrolled_into_view
            pages = self.browser.find_element_by_link_text("2").click()
            time.sleep(20)

            break
            # print(more)
            # if more is not None:
            #     write()
            #     more.click()
            # elif more is None:
            #     self.close()
            #     break
        return res


if __name__ == '__main__':
    run = Parse()
    run.connect("https://market.yandex.ru/", "motul")
    run.find_element()
    print(run.get_name_price())
    # run.next_page()
    run.close()
