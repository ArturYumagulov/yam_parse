from selenium import webdriver
import time


class Parse:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)

    def connect(self, url, product_name):
        self.browser.get(url)
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_id("header-search").send_keys(product_name)
        search = self.browser.find_element_by_class_name("_1XiEJDPVpk")
        search.click()
        self.browser.implicitly_wait(10)

    def find_element(self):
        self.browser.find_element_by_class_name("_3gaRuC1vxz").click()
        self.browser.implicitly_wait(10)

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

    def close(self):
        self.browser.close()


if __name__ == '__main__':
    run = Parse()
    run.connect("https://market.yandex.ru/", "mobil")
    run.find_element()
    res = []
    result = []
    result_1 = []
    product_list = run.find_products_name()
    price_list = run.find_products_price()
    for i in product_list:
        result.append(i.text)

    for j in price_list:
        result_1.append(j.text)

    for item in range(len(result)):
        try:
            # print([result[item], result_1[item]])
            res.append([result[item], result_1[item]])
        except IndexError:
            break
    print(res)
    run.close()