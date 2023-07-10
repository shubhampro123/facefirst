import logging
import os
import time

from datetime import date
from datetime import datetime

import numpy as np
import pytest as pytest
# from _pytest.mark import param
from selenium import webdriver

# from All_POM_Package.LoginPage import Login
# from utilities import XLUtils
from pathlib import Path

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Other_Utilities.Read_Excel import Read_excel

resultPath = f"{Path(__file__).parent.parent}\\Test_Data\\Data_From_Excel\\Test_Cases.xlsx"


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )




driver = None


@pytest.fixture(scope="class")
def setup1(request):
    try:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        d = webdriver.Chrome(options=chrome_options)
        df = Read_excel.get_registration_form_data_df()
        df = df.replace(np.nan, '', regex=True)
        name = [i for i in df['Name']]
        email = [i for i in df['Email']]
        password = [i for i in df['new_password']]
        zip_list = zip(name, email, password)
        user_list = list(zip_list)
        one_second = 1
        two_second = 2
        three_second = 3
    except Exception as ex:
        print("init constructor in base class has an err: ", ex)

    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = d
        # driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
        # driver = driver

    elif browser_name == "firefox":
        # driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
        driver = d

    elif browser_name == "edge":
        # driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
        driver = d

    '''
        driver.get("https://localhost/")
        # https: // rahulshettyacademy.com / angularpractice /
        driver.maximize_window()
        request.cls.driver = driver
    '''
    yield
    #driver.close()


@pytest.fixture(scope="class")
def setup(request):

    try:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        d = webdriver.Chrome(options=chrome_options)
        df = Read_excel.get_registration_form_data_df()
        df = df.replace(np.nan, '', regex=True)
        name = [i for i in df['Name']]
        email = [i for i in df['Email']]
        password = [i for i in df['new_password']]
        zip_list = zip(name, email, password)
        user_list = list(zip_list)
        one_second = 1
        two_second = 2
        three_second = 3
    except Exception as ex:
        print("init constructor in base class has an err: ", ex)



    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        # driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
        driver = d

    elif browser_name == "firefox":
        # driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
        driver = d

    elif browser_name == "edge":
        # driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
        driver = d

    '''
    driver.get("https://localhost/")
    driver.maximize_window()
    login = Login(driver)
    login.setUser().clear()
    login.setUser().send_keys("shubham")
    login.setPass().send_keys("Shubham@123")
    time.sleep(2)
    login.driver.execute_script("arguments[0].click();", login.loginbtn())
    request.cls.driver = driver'''
    yield





def Implicit_wait(seconds):
    driver.implicitly_wait(seconds)


"""set Explicit wait function to be used by all the web elements where ever it is needed"""


def Explicit_wait(seconds, element):
    wait = WebDriverWait(driver, seconds)
    ele = wait.until(expected_conditions.element_to_be_clickable(element))



class Base_Class:

    try:


        # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
        #              "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        # options = webdriver.ChromeOptions()
        # options.headless = True
        # options.add_argument(f'user-agent={user_agent}')
        # options.add_argument("--window-size=1920,1080")
        # options.add_argument('--ignore-certificate-errors')
        # options.add_argument('--allow-running-insecure-content')
        # options.add_argument("--disable-extensions")
        # options.add_argument("--proxy-server='direct://'")
        # options.add_argument("--proxy-bypass-list=*")
        # options.add_argument("--start-maximized")
        # options.add_argument('--disable-gpu')
        # options.add_argument('--disable-dev-shm-usage')
        # options.add_argument('--no-sandbox')

        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        d = webdriver.Chrome(options=chrome_options)
        df = Read_excel.get_registration_form_data_df()
        df = df.replace(np.nan, '', regex=True)
        name = [i for i in df['Name']]
        email = [i for i in df['Email']]
        password = [i for i in df['new_password']]
        zip_list = zip(name, email, password)
        user_list = list(zip_list)
        one_second = 1
        two_second = 2
        three_second = 3
    except Exception as ex:
        print("init constructor in base class has an err: ", ex)

    @staticmethod
    def logger_object():
        try:
            print("pass")
            log_folder = f"{Path(__file__).parent.parent}\\Application_Logs"
            files_list = os.listdir(log_folder)
            list_size = len(files_list)
            print("file List : ", files_list, " file count: ", list_size)
            i = 0
            base_path = Path(log_folder)
            files_in_base_path = base_path.iterdir()
            print(type(files_in_base_path))
            print(files_in_base_path)
            for file in files_list[:-3]:
                for file_name in files_in_base_path:
                    if file_name.name == file:
                        os.remove(file_name)

            now = datetime.now()
            print("now =", now)
            dt = now.strftime("%d_%m_%Y_%H_%M_%S")
            file_name = f"{Path(__file__).parent.parent}\\Application_Logs\\Application_logs_{dt}.log"
            print("Log_file_name: ", file_name)
            formatter = logging.Formatter("%(asctime)s : %(name)-12s : %(levelname)-8s : %(message)s",
                                          datefmt='%d/%m/%Y %r')
            handler = logging.FileHandler(filename=file_name)
            handler.setFormatter(formatter)
            logger = logging.getLogger()
            logger.setLevel(logging.INFO)
            logger.addHandler(handler)
            return logger
        except Exception as ex:
            print(ex)
