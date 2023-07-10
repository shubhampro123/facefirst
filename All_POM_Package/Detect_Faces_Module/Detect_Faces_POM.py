import time
from pathlib import Path

import pyautogui
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

from All_Test_Cases_Package.conftest import Base_Class
from Config_Package.INI_Config_Files.Detect_Faces_Read_INI import Read_Detect_Faces_Components
from Config_Package.INI_Config_Files.Portal_Menu_Read_INI import Read_Portal_Menu_Components
from Config_Package.INI_Config_Files.Register_Page_Read_INI import Read_Deployment_Manager_Components


class Detect_Faces_pom:

    def __init__(self):
        self.d = Base_Class.d

    def login_before(self):

        try:
            self.d.get(Read_Portal_Menu_Components().get_url())
            time.sleep(Base_Class.one_second)
            username = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_usernameField())
            username.send_keys(Read_Portal_Menu_Components().get_username())
            password = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_passwordField())
            password.send_keys(Read_Portal_Menu_Components().get_password())
            time.sleep(Base_Class.one_second)
            login_btn = self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton())
            self.d.execute_script("arguments[0].click();", login_btn)


        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\login_faild_for_portal_menu_pg_03.png")
                return False

    def click_on_detect_faces_button(self):
        try:
            time.sleep(Base_Class.one_second)
            detect_faces_button = self.d.find_element(By.XPATH,
                                                      Read_Portal_Menu_Components().portal_menu_detect_faces_btn_by_xpath())
            detect_faces_button.click()
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_portal_menu_detect_faces_pg_03.png")
                return False

    def click_on_upload_photo(self):
        try:
            time.sleep(Base_Class.one_second)
            click_on_upload_photo = self.d.find_element(By.XPATH, Read_Detect_Faces_Components().detect_faces_upload_photo_by_xpath())
            click_on_upload_photo.click()
            time.sleep(2)
            file_path = 'C:\\Users\\shree\\OneDrive - DnT Infotech LLP\\Desktop\\upload_photo.jpg'
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('enter')
            detected_faces_validation = self.d.find_element(By.XPATH,
                                                      "(//div[@class='select-areas-background-area'])[0]")
            if detected_faces_validation.is_displayed() :
                detected_faces = self.d.find_element(By.XPATH, )

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\click_on_upload_photo_failed_pg_03.png")
                return False