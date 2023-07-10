import configparser
from pathlib import Path


class Read_Detect_Faces_Components:
    def __init__(self):

        self.config = configparser.RawConfigParser()

        try:
            portal_menu_ini_file_path = f'{Path(__file__).parent.parent.parent}\\Test_Data\\Data_From_INI\\Detect_Faces.ini'
            print("dm url path: ", portal_menu_ini_file_path)
            print("File location: ", portal_menu_ini_file_path)
            # Base_Class.logger.info("File location: ", deployment_manager_ini_file_path)
            self.config.read(portal_menu_ini_file_path)
        except Exception as ex:
            print("config file got an exception", ex)

    def detect_faces_upload_photo_by_xpath(self):
        try:
            detect_faces_upload_photo_by_xpath = self.config.get("LOCATORS", "upload_photo_by_xpath")
            print("detect faces upload photo by xpath: ", detect_faces_upload_photo_by_xpath)
            return detect_faces_upload_photo_by_xpath
        except Exception as ex:
            print("detect_faces_upload_photo_by_xpath : ", ex)


