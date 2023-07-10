import configparser
from pathlib import Path


class Read_Login_Page_INI:
    def __init__(self):
        self.config = configparser.RawConfigParser()

        try:
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\Data_From_INI\\Login_Page_INI.ini"

            print("config_file path: ", file_path)
            self.config.read(file_path)
            # print(config.get("LOGIN_PAGE_AFTER_REGISTRATION", "url"))
        except Exception as ex:
            print(ex)

    def get_login_url(self):
        login_url = self.config.get("LOGIN_PAGE_AFTER_REGISTRATION", "url")
        print("login page url: ", login_url)
        return login_url

    def get_login_page_heading_by_xpath(self):
        login_page_heading_xpath = self.config.get("LOGIN_PAGE_AFTER_REGISTRATION", "login_page_heading_by_xpath")
        print("Login page heading: ", login_page_heading_xpath)
        return login_page_heading_xpath

    def get_menu_btn_by_xpath(self):
        menu_btn_xpath = self.config.get("LOGIN_PAGE_AFTER_REGISTRATION", "menu_btn_by_xpath")
        print("menu button xpath: ", menu_btn_xpath)
        return menu_btn_xpath

    def get_login_or_email_link_by_xpath(self):
        login_or_email_link_by_xpath = self.config.get("LOGIN_PAGE_AFTER_REGISTRATION", "login_or_email_link_by_xpath")
        print("Login or email link xpath: ", login_or_email_link_by_xpath)
        return login_or_email_link_by_xpath

    def get_profile_menu_by_xpath(self):
        profile_menu_by_xpath = self.config.get("LOGIN_PAGE_AFTER_REGISTRATION", "profile_menu_by_xpath")
        print("Profile Menu by xpath: ", profile_menu_by_xpath)
        return profile_menu_by_xpath

    def get_logout_menu_by_xpath(self):
        logout_menu_by_xpath = self.config.get("LOGIN_PAGE_AFTER_REGISTRATION", "logout_menu_by_xpath")
        print("logout menu xpath: ", logout_menu_by_xpath)
        return logout_menu_by_xpath

    def get_successfully_registered_msg_by_xpath(self):
        successfully_registered_msg_by_xpath = self.config.get("LOGIN_PAGE_AFTER_REGISTRATION", "successfully_registered_msg_by_xpath")
        print("successfully registered message xapth: ", successfully_registered_msg_by_xpath)
        return successfully_registered_msg_by_xpath

    def get_username_password_panel_heading_by_xpath(self):
        username_password_panel_heading_by_xpath = self.config.get("LOGIN_PAGE_AFTER_REGISTRATION", "username_password_panel_heading_by_xpath")
        print("username password panel heading xpath: ", username_password_panel_heading_by_xpath)
        return username_password_panel_heading_by_xpath

    def get_email_username_label_by_xpath(self):
        email_username_label_by_xpath = self.config.get("LOGIN_PAGE_AFTER_REGISTRATION", "email_username_label_by_xpath")
        print("email username label by xpath: ", email_username_label_by_xpath)
        return email_username_label_by_xpath

    def get_email_username_label_star_by_xpath(self):
        email_username_label_star_by_xpath = self.config.get("LOGIN_PAGE_AFTER_REGISTRATION", "email_username_label_star_by_xpath")
        print("email username label xpath: ", email_username_label_star_by_xpath)
        return email_username_label_star_by_xpath




