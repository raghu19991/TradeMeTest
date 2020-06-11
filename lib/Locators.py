from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    MOTORS_Tab = (By.ID, 'SearchTabs1_MotorsLink')

class MotorsPageLocators(object):
    USED_CARS_Link = (By.XPATH, "//h2/a[text()='Used cars']")

class UsedCarsPageLocators(object):
    USED_CARS_heading = (By.XPATH,"//h1[text()='Used Cars']")
    MORE_MAKES_heading = (By.XPATH,"//h1[text()='More makes']")
    MAKES_ul= "//table[@id='makes']"
    MOREMAKES_ul="//table[@id='makeTable']"
    brands_locator = "//td/a"
    count_locator = "//td//span[@class='count']"
    more_link="//strong[text()='more...']"
