from selenium.common.exceptions import NoSuchElementException
from lib.Locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    def go_to_motors(self):
        MotorTab = self.driver.find_element(*MainPageLocators.MOTORS_Tab)
        MotorTab.click()


class MotorsPage(BasePage):
    def go_to_UsedCars(self):
        UsedCars_link=WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MotorsPageLocators.USED_CARS_Link)))
        UsedCars_link.click()


class UsedCarsPage(BasePage):
    BasePage.used_brands = {}

    def get_displayed_car_brands(self):
        driver=self.driver
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((UsedCarsPageLocators.USED_CARS_heading)))
        assert "Used Cars" in driver.page_source
        brands=UsedCarsPageLocators.MAKES_ul + UsedCarsPageLocators.brands_locator
        count=UsedCarsPageLocators.MAKES_ul+UsedCarsPageLocators.count_locator
        more_brands=UsedCarsPageLocators.MOREMAKES_ul+ UsedCarsPageLocators.brands_locator
        more_count=UsedCarsPageLocators.MOREMAKES_ul+UsedCarsPageLocators.count_locator
        more_link=UsedCarsPageLocators.MAKES_ul+UsedCarsPageLocators.more_link
        try:
            # page1_brands
            for i,j in zip(driver.find_elements_by_xpath(brands),driver.find_elements_by_xpath(count)):
                if i.text != 'more...':
                    self.used_brands.update({i.text: j.text})
            # page2_brands if more... exists
            if driver.find_elements_by_xpath(more_link):
                driver.find_element_by_xpath(more_link).click()
                WebDriverWait(driver, 10).until(ec.presence_of_element_located(UsedCarsPageLocators.MORE_MAKES_heading))
                for x,y in zip(driver.find_elements_by_xpath(more_brands),driver.find_elements_by_xpath(more_count)):
                    if x.text != 'more...':
                        self.used_brands.update({x.text: y.text})
            all_brands=self.used_brands.keys()
            #print("All the brands shown are :", *all_brands,sep=',')
            return all_brands
        except NoSuchElementException as e:
            print(e)

    def available_cars(self):
        used_brands=UsedCarsPage.used_brands
        available=[i for i in used_brands.keys() if used_brands[i]!='(0)']
        return available



