import unittest
from fixtures import page
from selenium import webdriver

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
       cls.driver = webdriver.Firefox()
       cls.driver.get("https://www.tmsandbox.co.nz/")
       cls.get_All_UsedCar_Brands(cls)

    def get_All_UsedCar_Brands(self):
        page.MainPage(self.driver).go_to_motors()
        page.MotorsPage(self.driver).go_to_UsedCars()
        used_cars=page.UsedCarsPage(self.driver)
        all_UsedCars=used_cars.get_displayed_car_brands()
        #available_cars=used_cars.available_cars()
        #print('Used brands of Cars available in the marketplace are:', *available_cars, sep=' , ')

    def test_Available_UsedCarBrands(self):
        list1=page.UsedCarsPage.available_cars(self)
        length=len(list1)
        print(self._testMethodName+" --> pass")
        print('    There are "{}" brand of used cars available currently'.format(length))
        print('    They are:-', *list1, sep=' ')
        print()

    def test_kia_exists(self):
        list1=page.UsedCarsPage.available_cars(self)
        self.assertTrue('Kia' in list1)
        print(self._testMethodName+" --> pass\n")

    def test_HispanoSuiza_doesnt_exist(self):
        list1=page.UsedCarsPage.available_cars(self)
        self.assertTrue("Hispano Suiza" not in list1)
        print(self._testMethodName+" --> pass\n")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
