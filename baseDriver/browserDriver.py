import os.path
import time


from selenium import webdriver


basePath=os.path.dirname(os.path.abspath(__file__))
driverPath=os.path.join(basePath,'chromedriver.exe')


class BDriver:

    driver=None

    def __init__(self,driverpath):

        if  hasattr(BDriver,'driver') :
            # s=Service(driverPath)
            self.driver=webdriver.Chrome(executable_path=driverpath)
            self.driver.maximize_window()



if __name__ == '__main__':
    b_driver = BDriver(driverPath)
    # url="https://www.baidu.com"
    print(b_driver.driver)
