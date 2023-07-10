import configparser
from pathlib import Path
from All_Test_Cases_Package.conftest import Base_Class


class Read_Deployment_Manager_Components:
    def __init__(self):

        self.config = configparser.RawConfigParser()

        try:
            deployment_manager_ini_file_path = f'{Path(__file__).parent.parent.parent}\\Test_Data\\Data_From_INI\\Register_Page.ini'
            print("dm url path: ", deployment_manager_ini_file_path)
            print("File location: ", deployment_manager_ini_file_path)
            # Base_Class.logger.info("File location: ", deployment_manager_ini_file_path)
            self.config.read(deployment_manager_ini_file_path)
        except Exception as ex:
            print("config file got an exception", ex)

    def get_url(self):
        try:
            url = self.config.get('URL', 'deployment_manager_url')
            # Base_Class.logger.info("URL read successfully : ", url)
            print("URL read successfully : ", url)
            return url
        except Exception as ex:
            print(ex)

    def get_expected_page_heading(self):
        try:
            expected_heading = self.config.get("REGISTRATION_PAGE_LOCATORS", "expected_page_heading")
            print("expected page heading: ", expected_heading)
            return expected_heading
        except Exception as ex:
            print(ex)

    def registration_page_menu_btn_by_xpath(self):
        try:
            menu_btn_by_xpath = self.config.get("REGISTRATION_PAGE_LOCATORS", "registration_page_menu_btn_by_xpath")
            print("menu btn xpath: ", menu_btn_by_xpath)
            return menu_btn_by_xpath
        except Exception as ex:
            print("registration_page_menu_btn_by_xpath: ", ex)

    def registration_heading_by_id(self):
        try:
            heading = self.config.get("REGISTRATION_PAGE_LOCATORS", "registration_heading_by_id")
            print("registration page heading by id: ", heading)
            return heading
        except Exception as ex:
            print(ex)

    def login_link_by_xpath(self):
        try:
            login_link = self.config.get("REGISTRATION_PAGE_LOCATORS", "login_link_by_xpath")
            print("login_link_by_xpath: ", login_link)
            return login_link
        except Exception as ex:
            print(ex)

    def read_login_url(self):
        try:
            login_url = self.config.get("REGISTRATION_PAGE_LOCATORS", "login_url")
            print("login page url: ", login_url)
            return login_url
        except Exception as ex:
            print(ex)

    def fill_out_form_text_by_xpath(self):
        try:
            text = self.config.get("REGISTRATION_PAGE_LOCATORS", "fill_out_form_text_by_xpath")
            print("fill out form text by xpath: ", text)
            return text
        except Exception as ex:
            print(ex)

    def fill_out_form_text(self):
        try:
            text = self.config.get("REGISTRATION_PAGE_LOCATORS", "fill_out_form_text")
            print("fill out form heading text: ", text)
            return text
        except Exception as ex:
            print(ex)

    def name_label_by_xpath(self):
        try:
            name_text = self.config.get("REGISTRATION_PAGE_LOCATORS", "name_label_by_xpath")
            print("name text xpath: ", name_text)
            return name_text
        except Exception as ex:
            print(ex)

    def name_text(self):
        try:
            name_text = self.config.get("REGISTRATION_PAGE_LOCATORS", "name_text")
            print("name text expected: ", name_text)
            return name_text
        except Exception as ex:
            print(ex)

    def star_after_name_by_xpath(self):
        try:
            star_by_xpath = self.config.get("REGISTRATION_PAGE_LOCATORS", "star_after_name_by_xpath")
            print("star by xpath: ", star_by_xpath)
            return star_by_xpath
        except Exception as ex:
            print(ex)

    def star(self):
        try:
            star = self.config.get("REGISTRATION_PAGE_LOCATORS", "star_text")
            print("star displayed in: ", star)
            return star
        except Exception as ex:
            print(ex)

    def email_label_by_xpath(self):
        try:
            email_label = self.config.get("REGISTRATION_PAGE_LOCATORS", "email_label_by_xpath")
            print("email label xpath: ", email_label)
            return email_label
        except Exception as ex:
            print(ex)

    def email_label_expected(self):
        try:
            email_expected = self.config.get("REGISTRATION_PAGE_LOCATORS", "email_label_expected")
            print("email label expected: ", email_expected)
            return email_expected
        except Exception as ex:
            print(ex)

    def invalid_email_msg_by_xpath(self):
        try:
            invalid_email_text = self.config.get("REGISTRATION_PAGE_LOCATORS", "invalid_email_msg_by_xpath")
            print("invalid email text xpath: ", invalid_email_text)
            return invalid_email_text
        except Exception as ex:
            print(ex)

    def password_label_by_xpath(self):
        try:
            password_text = self.config.get("REGISTRATION_PAGE_LOCATORS", "password_label_by_xpath")
            print("password text xpath: ", password_text)
            return password_text
        except Exception as ex:
            print(ex)

    def password_label_expected(self):
        try:
            password_expected = self.config.get("REGISTRATION_PAGE_LOCATORS", "password_text")
            print("password label expected: ", password_expected)
            return password_expected
        except Exception as ex:
            print(ex)

    def new_password_helper_text_by_xpath(self):
        try:
            new_pass_helper = self.config.get("REGISTRATION_PAGE_LOCATORS", "new_password_helper_text_by_xpath")
            print("New password helper text xpath: ", new_pass_helper)
            return new_pass_helper
        except Exception as ex:
            print(ex)

    def new_password_helper_text(self):
        try:
            new_password_helper_text = self.config.get("REGISTRATION_PAGE_LOCATORS", "new_password_helper_text")
            print("new password helper text: ", new_password_helper_text)
            return new_password_helper_text
        except Exception as ex:
            print(ex)

    def password_confirmation_label_by_xpath(self):
        try:
            password_confirm = self.config.get("REGISTRATION_PAGE_LOCATORS", "password_confirmation_label_by_xpath")
            print("password confirmation text: ", password_confirm)
            return password_confirm
        except Exception as ex:
            print(ex)

    def password_confirmation_text(self):
        try:
            password = self.config.get("REGISTRATION_PAGE_LOCATORS", "password_confirmation_text")
            print("pass confirm text: ", password)
            return password
        except Exception as ex:
            print(ex)

    def password_complexity_text_by_xpath(self):
        try:
            password_complexity_text_xpath = self.config.get("REGISTRATION_PAGE_LOCATORS",
                                                             "password_complexity_text_by_xpath")
            print("Password complexity text xpath: ", password_complexity_text_xpath)
            return password_complexity_text_xpath
        except Exception as ex:
            print(ex)

    def password_complexity_text(self):
        try:
            password_complexity_text = self.config.get("REGISTRATION_PAGE_LOCATORS", "password_complexity_text")
            print("password complexity text: ", password_complexity_text)
            return password_complexity_text
        except Exception as ex:
            print(ex)

    def star_after_password_confirmation_by_xpath(self):
        try:
            star_by_xpath = self.config.get("REGISTRATION_PAGE_LOCATORS", "star_after_password_confirmation_by_xpath")
            return star_by_xpath
        except Exception as ex:
            print(ex)

    def already_registered_text_by_xpath(self):
        try:
            login_link_xpath = self.config.get("REGISTRATION_PAGE_LOCATORS", "already_registered_text_by_xpath")
            print("login link xpath: ", login_link_xpath)
            return login_link_xpath
        except Exception as ex:
            print(ex)

    def already_registered_text(self):
        try:
            already_registered_text = self.config.get("REGISTRATION_PAGE_LOCATORS", "already_registered_text")
            print("already registered text expected: ", already_registered_text)
            return already_registered_text
        except Exception as ex:
            print(ex)

    def login_link_after_already_registered_by_xpath(self):
        try:
            login_link_by_xpath = self.config.get("REGISTRATION_PAGE_LOCATORS",
                                                  "login_link_after_already_registered_by_xpath")
            print("login link after already_registered xpath: ", login_link_by_xpath)
            return login_link_by_xpath
        except Exception as ex:
            print(ex)

    def login_text(self):
        try:
            login_text = self.config.get("REGISTRATION_PAGE_LOCATORS", "login_link_text")
            print("login text: ", login_text)
            return login_text
        except Exception as ex:
            print(ex)

    def name_text_box_by_id(self):
        try:
            text_box = self.config.get("LOCATORS", "name_by_id")
            # Base_Class.logger.info("Locator Read Successfully: ", text_box)
            print("Locator Read Successfully: ", text_box)
            return text_box
        except Exception as ex:
            print(ex)

    def email_text_box_by_id(self):
        try:
            email = self.config.get("LOCATORS", "email_by_id")
            # Base_Class.logger.info("email locator read successfully: ", email)
            print("email locator read successfully: ", email)
            return email
        except Exception as ex:
            print(ex)

    def new_password_text_box_by_id(self):
        try:
            password = self.config.get("LOCATORS", "new_password_by_id")
            # Base_Class.logger.info("new password locator read successfully: ", password)
            print("new password locator read successfully: ", password)
            return password
        except Exception as ex:
            print(ex)

    def confirm_password_text_box_by_id(self):
        try:
            confirm_pass = self.config.get("LOCATORS", "confirm_password_by_id")
            # Base_Class.logger.info("confirm password text box locator read successfully: ", confirm_pass)
            print("confirm password text box locator read successfully: ", confirm_pass)
            return confirm_pass
        except Exception as ex:
            print(ex)

    def password_visibility_btn_by_xpath(self):
        try:
            password_visibility_btn_by_xpath = self.config.get("REGISTRATION_PAGE_LOCATORS", "password_visibility_btn_by_xpath")
            print("password visibility btn xpath: ", password_visibility_btn_by_xpath)
            return password_visibility_btn_by_xpath
        except Exception as ex:
            print(ex)

    def register_btn_text_box_by_xpath(self):
        try:
            register_btn = self.config.get("LOCATORS", "register_btn_by_xpath")
            # Base_Class.logger.info("register btn locator read successfully: ", register_btn)
            print("register btn locator read successfully: ", register_btn)
            return register_btn
        except Exception as ex:
            print(ex)

    def message_after_registration_by_xpath(self):
        try:
            register_msg_xpath = self.config.get("LOCATORS", "message_after_registration_by_xpath")
            print("register msg xpath: ", register_msg_xpath)
            return register_msg_xpath
        except Exception as ex:
            print(ex)

    def registration_page_title(self):
        try:
            title = self.config.get("ASSERTIONS", "registration_page_title")
            print("Expected title: ", title)
            return title
        except Exception as ex:
            print(ex)

    def user_name(self):
        try:
            name = self.config.get("USER_DATA", "name")
            print("user name: ", name)
            return name
        except Exception as ex:
            print(ex)

    def user_email(self):
        try:
            email = self.config.get("USER_DATA", "email")
            print("user email: ", email)
            return email
        except Exception as ex:
            print(ex)

    def user_pass(self):
        try:
            password = self.config.get("USER_DATA", "pass")
            print("user password: ", password)
            return password
        except Exception as ex:
            print(ex)

    def login_link_by_xpath(self):
        try:
            link_xpath = self.config.get("LOCATORS", "login_link_by_xpath")
            print("login link xpath: ", link_xpath)
            return link_xpath
        except Exception as ex:
            print(ex)

    def login_page_title(self):
        try:
            title = self.config.get("ASSERTIONS", "login_page_title")
            print("login page title: ", title)
            return title
        except Exception as ex:
            print(ex)

    def login_username_txt_box_by_id(self):
        try:
            user_name = self.config.get("LOCATORS", "login_page_email_txt_box_by_id")
            print("username by id: ", user_name)
            return user_name
        except Exception as ex:
            print(ex)

    def login_password_txt_box_by_id(self):
        try:
            password = self.config.get("LOCATORS", "login_page_password_txt_box_by_id")
            print("password by id: ", password)
            return password
        except Exception as ex:
            print(ex)

    def login_btn_by_xpath(self):
        try:
            login_btn = self.config.get("LOCATORS", "login_btn_by_xpath")
            print("login btn by xpath: ", login_btn)
            return login_btn
        except Exception as ex:
            print(ex)

    def deployment_manager_body_tag(self):
        try:
            body_tag = self.config.get("LOCATORS", "tag_name_body")
            print("Deployment Manager Tag Name: ", body_tag)
            return body_tag
        except Exception as ex:
            print(ex)

    def deployment_manager_home_page_title(self):
        try:
            title = self.config.get("ASSERTIONS", "deployment_manager_home_page_title")
            print("Deployment Manager Home Page Title: ", title)
            return title
        except Exception as ex:
            print(ex)

    def license_status_edit_btn_by_xpath(self):
        try:
            edit_btn = self.config.get("LOCATORS", "license_status_edit_btn_by_xpath")
            print("license status edit button by xpath: ", edit_btn)
            return edit_btn
        except Exception as ex:
            print(ex)

    def customer_id_text_box_by_xpath(self):
        try:
            customer_id = self.config.get("LOCATORS", "customer_id_text_box_by_xpath")
            print("customer id by xpath: ", customer_id)
            return customer_id
        except Exception as ex:
            print(ex)

    def customer_id(self):
        try:
            customer_id = self.config.get("USER_DATA", "customer_id")
            print("customer id : ", customer_id)
            return customer_id
        except Exception as ex:
            print(ex)

    def customer_id_save_btn_by_xpath(self):
        try:
            save_btn = self.config.get("LOCATORS", "customer_id_save_btn_by_xpath")
            print("customer_id save button xpath: ", save_btn)
            return save_btn
        except Exception as ex:
            print(ex)

    def p_tag_content_check_by_xpath(self):
        try:
            p_tag_content = self.config.get("LOCATORS", "P_tag_content_check_by_xpath")
            print("p_tag content check by xpath: ", p_tag_content)
            return p_tag_content
        except Exception as ex:
            print(ex)

    def domain_status_3_dots_by_xpath(self):
        try:
            domain_status_3_dots = self.config.get("LOCATORS", "domain_status_3_dots_by_xpath")
            print("domain_Status_3_dots xpath: ", domain_status_3_dots)
            return domain_status_3_dots
        except Exception as ex:
            print(ex)

    def domain_status_edit_btn_by_xpath(self):
        try:
            domain_status_edit_btn_xpath = self.config.get("LOCATORS", "domain_status_edit_btn_by_xpath")
            print("domain status edit option xpath: ", domain_status_edit_btn_xpath)
            return domain_status_edit_btn_xpath
        except Exception as ex:
            print(ex)

    def ip_address_option_by_xpath(self):
        try:
            ip_address_option_by_xpath = self.config.get("LOCATORS", "IP_Address_option_by_xpath")
            print("ip address option xpath: ", ip_address_option_by_xpath)
            return ip_address_option_by_xpath
        except Exception as ex:
            print(ex)

    def domain_name_option_by_xpath(self):
        try:
            domain_name_option_xpath = self.config.get("LOCATORS", "Domain_name_option_by_xpath")
            print("domain name option xpath: ", domain_name_option_xpath)
            return domain_name_option_xpath
        except Exception as ex:
            print(ex)

    def select_ip_address_dropdown_by_xpath(self):
        try:
            select_ip_address_by_xpath = self.config.get("LOCATORS", "select_ip_address_by_xpath")
            print("select ip address dropdown xpath", select_ip_address_by_xpath)
            return select_ip_address_by_xpath
        except Exception as ex:
            print(ex)

    def local_host_option_by_xpath(self):
        try:
            local_host_option_by_xpath = self.config.get("LOCATORS", "local_host_option_by_xpath")
            print("local host xpath: ", local_host_option_by_xpath)
            return local_host_option_by_xpath
        except Exception as ex:
            print(ex)

    def ip_address_save_btn_by_xpath(self):
        try:
            ip_address_save_btn_by_xpath = self.config.get("LOCATORS", "IP_Address_save_btn_by_xpath")
            print("ip address save btn xpath: ", ip_address_save_btn_by_xpath)
            return ip_address_save_btn_by_xpath
        except Exception as ex:
            print(ex)

    def login_url_after_successful_new_register(self):
        try:
            login_url = Read_Deployment_Manager_Components().read_login_url()
            return login_url
        except Exception as ex:
            print(ex)

    def successfully_registered_msg_by_xpath(self):
        try:
            successful_registered = Read_Deployment_Manager_Components().successfully_registered_msg_by_xpath()
            return successful_registered
        except Exception as ex:
            print(ex)
'''
Read_Deployment_Manager_Components().get_url()
Read_Deployment_Manager_Components().name_text_box_by_id()
Read_Deployment_Manager_Components().email_text_box_by_id()
Read_Deployment_Manager_Components().new_password_text_box_by_id()
Read_Deployment_Manager_Components().confirm_password_text_box_by_id()
Read_Deployment_Manager_Components().register_btn_text_box_by_xpath()
'''
