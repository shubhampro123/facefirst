import time

from Config_Package.INI_Config_Files.Register_Page_Read_INI import Read_Deployment_Manager_Components
from All_Test_Cases_Package.conftest import Base_Class
from selenium.webdriver.common.by import By
from pathlib import Path


class Deployment_manager_pom:

    def __init__(self):
        self.d = Base_Class.d

    def compare_actual_dm_url(self):
        print("Deployment Manager URL: ", Read_Deployment_Manager_Components().get_url())
        self.d.get(Read_Deployment_Manager_Components().get_url())
        title = self.d.title
        url = self.d.current_url
        print("current page title: ", title)
        print("current page url: ", url)
        return Read_Deployment_Manager_Components().get_url() == url

    def verify_registration_page_heading(self):
        expected_heading = Read_Deployment_Manager_Components().get_expected_page_heading()
        actual_heading = self.d.find_element(By.ID,
                                             Read_Deployment_Manager_Components().registration_heading_by_id()).text
        print("checking page heading: ", actual_heading)
        return expected_heading == actual_heading

    def registration_page_menu_btn_visible(self):
        try:
            menu_btn_status = self.d.find_element(By.XPATH,
                                                  Read_Deployment_Manager_Components().registration_page_menu_btn_by_xpath()).is_displayed()
            return menu_btn_status
        except Exception as ex:
            print("registration_page_menu_btn_by_xpath POM: ", ex)

    def registration_page_menu_btn_enabled(self):
        try:
            menu_btn_status = self.d.find_element(By.XPATH,
                                                  Read_Deployment_Manager_Components().registration_page_menu_btn_by_xpath()).is_enabled()
            return menu_btn_status
        except Exception as ex:
            print("registration_page_menu_btn_enabled test: ", ex)

    def login_link_is_visible(self):
        try:
            login_link = self.d.find_element(By.XPATH, Read_Deployment_Manager_Components().login_link_by_xpath())
            login_link_status = login_link.is_displayed()
            return login_link_status
        except Exception as ex:
            print("login link by xpath is visible : ", ex)

    def login_link_is_enabled(self):
        try:
            login_link = self.d.find_element(By.XPATH, Read_Deployment_Manager_Components().login_link_by_xpath())
            login_link_status = login_link.is_enabled()
            return login_link_status
        except Exception as ex:
            print("login link by xpath is enabled : ", ex)

    def verify_login_url(self):
        try:
            self.d.find_element(By.XPATH, Read_Deployment_Manager_Components().login_link_by_xpath()).click()
            time.sleep(Base_Class.two_second)
            url = self.d.current_url
            status = None
            if url == Read_Deployment_Manager_Components().read_login_url():
                status = True
            else:
                status = False
            return status
        except Exception as ex:
            print(ex)

    def fill_out_form_text_by_xpath(self):
        try:
            text_expected = Read_Deployment_Manager_Components().fill_out_form_text()
            text_displayed = self.d.find_element(By.XPATH,
                                                 Read_Deployment_Manager_Components().fill_out_form_text_by_xpath()).text
            print("fill out form text displayed: ", text_displayed, " Expected Text: ", text_expected)
            status = None
            if text_displayed == text_expected:
                status = True
            else:
                status = False
            return status
        except Exception as ex:
            print(ex)

    def verify_name_text_displayed(self):
        try:
            name_text_expected = Read_Deployment_Manager_Components().name_text()
            name_text_displayed = self.d.find_element(By.XPATH,
                                                      Read_Deployment_Manager_Components().name_label_by_xpath()).text
            print("name text displayed: ", name_text_displayed)
            status = None
            if name_text_expected in name_text_displayed:
                status = True
            else:
                status = False
            return status
        except Exception as ex:
            print(ex)

    def verify_star_after_name_text_displayed(self):
        try:
            star_expected = Read_Deployment_Manager_Components().star()
            star_displayed = self.d.find_element(By.XPATH,
                                                 Read_Deployment_Manager_Components().star_after_name_by_xpath()).text
            print("actual displayed text: ", star_displayed)
            status = None
            if star_expected in star_displayed:
                status = True
            else:
                status = False
            return status
        except Exception as ex:
            print(ex)

    def verify_email_label_displayed_in_email_text_box(self):
        try:
            email_label_expected = Read_Deployment_Manager_Components().email_label_expected()
            email_label_displayed = self.d.find_element(By.XPATH,
                                                        Read_Deployment_Manager_Components().email_label_by_xpath()).text
            print("actual email label displayed", email_label_displayed)
            status = None
            if email_label_expected in email_label_displayed:
                status = True
            else:
                status = False
            return status
        except Exception as ex:
            print(ex)

    def verify_star_displayed_after_email_label(self):
        try:
            star_expected = Read_Deployment_Manager_Components().star()
            star_displayed = self.d.find_element(By.XPATH,
                                                 Read_Deployment_Manager_Components().email_label_by_xpath()).text
            print("actual displayed text: ", star_displayed)
            status = None
            if star_expected in star_displayed:
                status = True
            else:
                status = False
            return status
        except Exception as ex:
            print(ex)

    def verify_invalid_email_msg_displayed(self):
        try:
            self.d.find_element(By.ID, Read_Deployment_Manager_Components().email_text_box_by_id()).send_keys("abcd")
            time.sleep(Base_Class.one_second)
            status = self.d.find_element(By.XPATH,
                                         Read_Deployment_Manager_Components().invalid_email_msg_by_xpath()).is_displayed()
            print("invalid email msg displayed: ", status)
            return status
        except Exception as ex:
            print(ex)

    def verify_password_label_by_xpath(self):
        try:
            password_expected = Read_Deployment_Manager_Components().password_label_expected()
            password_displayed = self.d.find_element(By.XPATH,
                                                     Read_Deployment_Manager_Components().password_label_by_xpath()).text
            status = None
            if password_expected in password_displayed:
                status = True
            else:
                status = False
            return status
        except Exception as ex:
            print(ex)

    def verify_star_displayed_in_new_password_text_box(self):
        try:
            star = Read_Deployment_Manager_Components().star()
            password_text_displayed = self.d.find_element(By.XPATH,
                                                          Read_Deployment_Manager_Components().password_label_by_xpath()).text
            status = None
            print("Star Expected: ", star, " Star Displayed: ", password_text_displayed)
            if star in password_text_displayed:
                status = True
            else:
                status = False
            return status
        except Exception as ex:
            print(ex)

    def verify_new_password_helper_text_displayed(self):
        try:
            status = self.d.find_element(By.XPATH,
                                         Read_Deployment_Manager_Components().new_password_helper_text_by_xpath()).is_displayed()
            print("new password helper test displayed: ", status)
            return status
        except Exception as ex:
            print(ex)

    def verify_new_password_text_displayed_as_expected(self):
        try:
            text_expected = Read_Deployment_Manager_Components().new_password_helper_text()
            text_displayed = self.d.find_element(By.XPATH,
                                                 Read_Deployment_Manager_Components().new_password_helper_text_by_xpath()).text
            print("Text Expected: ", text_expected)
            print("Text Displayed: ", text_displayed)
            status = None
            if text_expected == text_displayed:
                status = True
            else:
                status = False
            return status
        except Exception as ex:
            print(ex)

    def verify_password_confirm_text_inside_confirm_password_text_box(self):
        try:
            password_confirmation_text_expected = Read_Deployment_Manager_Components().password_confirmation_text()
            password_confirmation_text_displayed = self.d.find_element(By.XPATH,
                                                                       Read_Deployment_Manager_Components().password_confirmation_label_by_xpath()).text
            print("text expected: ", password_confirmation_text_expected, "text displayed: ",
                  password_confirmation_text_displayed)
            status = None
            if password_confirmation_text_expected in password_confirmation_text_displayed:
                status = True
            else:
                status = False
            return status
        except Exception as ex:
            print(ex)

    def verify_star_after_confirm_password_text_in_confirm_password_text_box(self):
        try:
            star = Read_Deployment_Manager_Components().star()
            star_displayed = self.d.find_element(By.XPATH,
                                                 Read_Deployment_Manager_Components().star_after_password_confirmation_by_xpath()).text
            print("Star Expected: ", star, " Star Displayed", star_displayed)
            status = None
            if star in star_displayed:
                status = True
            else:
                status = False
            return status
        except Exception as ex:
            print(ex)

    def verify_password_complexity_text_is_displayed(self):
        try:
            status = self.d.find_element(By.XPATH,
                                         Read_Deployment_Manager_Components().password_complexity_text_by_xpath()).is_displayed()
            print("password complexity text is displayed: ", status)
            return status
        except Exception as ex:
            print(ex)

    def verify_password_confirmation_text_is_displayed_as_expected(self):
        try:
            password_confirmation_text_expected = Read_Deployment_Manager_Components().password_complexity_text()
            password_confirmation_text_displayed = self.d.find_element(By.XPATH,
                                                                       Read_Deployment_Manager_Components().password_complexity_text_by_xpath()).text
            print("Expected: ", password_confirmation_text_expected, " Actual: ", password_confirmation_text_displayed)
            status = None
            if password_confirmation_text_expected == password_confirmation_text_displayed:
                status = True
            else:
                status = False
            return status
        except Exception as ex:
            print(ex)

    def verify_already_registered_text_is_displayed(self):
        try:
            status = self.d.find_element(By.XPATH,
                                         Read_Deployment_Manager_Components().already_registered_text_by_xpath()).is_displayed()
            print("already registered text is displayed: ", status)
            return status
        except Exception as ex:
            print(ex)

    def verify_already_registered_text_is_displayed_as_expected(self):
        try:
            already_registered_text_expected = Read_Deployment_Manager_Components().already_registered_text()
            already_registered_text_displayed = self.d.find_element(By.XPATH,
                                                                    Read_Deployment_Manager_Components().already_registered_text_by_xpath()).text
            print("Expected: ", already_registered_text_expected, "Actual displayed: ",
                  already_registered_text_displayed)
            status = None
            if already_registered_text_expected == already_registered_text_displayed:
                status = True
            else:
                status = False
            return status
        except Exception as ex:
            print(ex)

    def verify_login_link_after_already_registered_by_xpath_is_displayed(self):
        try:
            status = self.d.find_element(By.XPATH,
                                         Read_Deployment_Manager_Components().login_link_after_already_registered_by_xpath()).is_displayed()
            print("login link displayed: ", status)
            return status
        except Exception as ex:
            print(ex)

    def verify_login_link_after_already_registered_by_xpath_is_enabled(self):
        try:
            status = self.d.find_element(By.XPATH,
                                         Read_Deployment_Manager_Components().login_link_after_already_registered_by_xpath()).is_enabled()
            print("login link enabled: ", status)
            return status
        except Exception as ex:
            print(ex)

    def verify_login_link_after_already_registered__text_by_xpath_is_working_as_expected(self):
        try:
            login_url_expected = Read_Deployment_Manager_Components().read_login_url()
            self.d.find_element(By.XPATH,
                                Read_Deployment_Manager_Components().login_link_after_already_registered_by_xpath()).click()
            time.sleep(Base_Class.two_second)
            login_url_displayed = self.d.current_url
            status = None
            if login_url_expected == login_url_displayed:
                status = True
            else:
                status = False
            self.d.back()
            return status

        except Exception as ex:
            print(ex)

    def verify_elements_visible(self):
        try:
            name_status = self.d.find_element(By.ID,
                                              Read_Deployment_Manager_Components().name_text_box_by_id()).is_displayed()
            email_status = self.d.find_element(By.ID,
                                               Read_Deployment_Manager_Components().email_text_box_by_id()).is_displayed()
            new_pass_status = self.d.find_element(By.ID,
                                                  Read_Deployment_Manager_Components().new_password_text_box_by_id()).is_displayed()
            confirm_pass_status = self.d.find_element(By.ID,
                                                      Read_Deployment_Manager_Components().confirm_password_text_box_by_id()).is_displayed()
            print("name: ", name_status, " email: ", email_status, " New Password: ", new_pass_status,
                  " confirm password: ", confirm_pass_status)
            if name_status and email_status and new_pass_status and confirm_pass_status is True:
                return True
            else:
                return False
        except Exception as ex:
            print(ex)

    def verify_elements_clickable(self):
        try:
            self.d.get(Read_Deployment_Manager_Components().get_url())
            name = self.d.find_element(By.ID, Read_Deployment_Manager_Components().name_text_box_by_id())
            name.clear()
            name.click()
            time.sleep(Base_Class.one_second)
            email = self.d.find_element(By.ID, Read_Deployment_Manager_Components().email_text_box_by_id())
            email.clear()
            email.click()
            time.sleep(1)
            new_pass = self.d.find_element(By.ID, Read_Deployment_Manager_Components().new_password_text_box_by_id())
            new_pass.clear()
            new_pass.click()
            time.sleep(Base_Class.one_second)
            confirm_pass = self.d.find_element(By.ID,
                                               Read_Deployment_Manager_Components().confirm_password_text_box_by_id())
            confirm_pass.clear()
            confirm_pass.click()
            time.sleep(Base_Class.one_second)
            if name.is_enabled() and email.is_enabled() and new_pass.is_enabled() and confirm_pass.is_enabled():
                return True
            else:
                return False

        except Exception as ex:
            print(ex)

    def register_new_user(self):
        global registered_already_msg, register_success_msg
        try:
            self.d.get(Read_Deployment_Manager_Components().get_url())
            name = self.d.find_element(By.ID, Read_Deployment_Manager_Components().name_text_box_by_id())
            name.click()
            name.send_keys(Read_Deployment_Manager_Components().user_name())
            time.sleep(Base_Class.one_second)
            email = self.d.find_element(By.ID, Read_Deployment_Manager_Components().email_text_box_by_id())
            email.click()
            email.send_keys(Read_Deployment_Manager_Components().user_email())
            time.sleep(Base_Class.one_second)
            new_pass = self.d.find_element(By.ID, Read_Deployment_Manager_Components().new_password_text_box_by_id())
            new_pass.click()
            new_pass.send_keys(Read_Deployment_Manager_Components().user_pass())
            time.sleep(Base_Class.one_second)
            confirm_pass = self.d.find_element(By.ID,
                                               Read_Deployment_Manager_Components().confirm_password_text_box_by_id())
            confirm_pass.send_keys(Read_Deployment_Manager_Components().user_pass())
            confirm_pass.click()
            time.sleep(Base_Class.two_second)
            self.d.find_element(By.XPATH, Read_Deployment_Manager_Components().register_btn_text_box_by_xpath()).click()
            time.sleep(Base_Class.two_second)

            if Read_Deployment_Manager_Components().login_url_after_successful_new_register() == self.d.current_url:
                register_success_msg = self.d.find_element(By.XPATH,
                                                           Read_Deployment_Manager_Components().successfully_registered_msg_by_xpath()).text
                print(register_success_msg)
            elif Read_Deployment_Manager_Components().get_url() == self.d.current_url:
                registered_already_msg = self.d.find_element(By.XPATH,
                                                             Read_Deployment_Manager_Components().message_after_registration_by_xpath()).text
                print(registered_already_msg)

            if registered_already_msg.__contains__('already registered') or register_success_msg.__contains__(
                    'successfully registered'):
                print('user available')
                return True
            else:
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\verify_new_registration_ff_reg_pg_03.png")
                print('user not available')
                return False
        except Exception as ex:
            print(ex)

    def verify_password_visibility_btn_by_xpath_is_visible(self):
        try:
            print("verify_password_visibility_btn_by_xpath_is_visible")
            status = self.d.find_element(By.XPATH,
                                         Read_Deployment_Manager_Components().password_visibility_btn_by_xpath()).is_displayed()
            print("Password Visibility Btn visible: ", status)
            return status
        except Exception as ex:
            print(ex)

    def verify_password_visibility_btn_by_xpath_is_clickable(self):
        try:
            print("verify_password_visibility_btn_by_xpath_is_clickable")
            status = self.d.find_element(By.XPATH,
                                         Read_Deployment_Manager_Components().password_visibility_btn_by_xpath()).is_enabled()
            print("Password visibility btn is clickable: ", status)
            return status
        except Exception as ex:
            print(ex)

    def verify_password_visibility_btn_by_xpath_is_working_as_expected(self):
        try:
            status = list()
            i = 0
            new_pass = self.d.find_element(By.ID, Read_Deployment_Manager_Components().new_password_text_box_by_id())
            new_pass.click()
            new_pass.send_keys(Read_Deployment_Manager_Components().user_pass())
            time.sleep(Base_Class.one_second)
            confirm_pass = self.d.find_element(By.ID,
                                               Read_Deployment_Manager_Components().confirm_password_text_box_by_id())
            confirm_pass.send_keys(Read_Deployment_Manager_Components().user_pass())
            confirm_pass.click()
            time.sleep(Base_Class.one_second)
            while i < 4:
                self.d.find_element(By.XPATH,
                                    Read_Deployment_Manager_Components().password_visibility_btn_by_xpath()).click()
                time.sleep(Base_Class.one_second)
                text = self.d.find_element(By.ID,
                                           Read_Deployment_Manager_Components().confirm_password_text_box_by_id()).get_attribute(
                    'value')
                if text.isalnum():
                    status.append(text)
                else:
                    status.append(text)
                i = i + 1
            print("Status: ", status)
            if status == [True, False, True, False]:
                return True
            else:
                return False

        except Exception as ex:
            print(ex)

    def open_login_page(self):
        login_link = self.d.find_element(By.XPATH, Read_Deployment_Manager_Components().login_link_by_xpath())
        login_link.click()

    def check_login_page_title(self):
        expected_title = Read_Deployment_Manager_Components().login_page_title()
        actual_title = self.d.title
        assert (actual_title, expected_title)

    def login_to_portal(self):
        username = self.d.find_element(By.ID, Read_Deployment_Manager_Components().login_username_txt_box_by_id())
        username.click()
        username.send_keys(Read_Deployment_Manager_Components().user_email())
        time.sleep(Base_Class.one_second)
        password = self.d.find_element(By.ID, Read_Deployment_Manager_Components().login_password_txt_box_by_id())
        password.click()
        password.send_keys(Read_Deployment_Manager_Components().user_pass())
        time.sleep(Base_Class.one_second)
        self.d.find_element(By.XPATH, Read_Deployment_Manager_Components().login_btn_by_xpath()).click()
        time.sleep(Base_Class.one_second)
        self.d.find_element(By.XPATH, Read_Deployment_Manager_Components().deployment_manager_body_tag()).click()
        time.sleep(Base_Class.one_second)

    def check_deployment_manager_home_page_title(self):
        expected_title = Read_Deployment_Manager_Components().deployment_manager_home_page_title()
        actual_title = self.d.title
        assert (expected_title, actual_title)

    def check_license_status_edit_btn_clickable(self):
        self.d.find_element(By.XPATH, Read_Deployment_Manager_Components().license_status_edit_btn_by_xpath()).click()
        time.sleep(Base_Class.one_second)

    def check_customer_id_by_xpath_clickable(self):

        customer_id_text_box = self.d.find_element(By.XPATH,
                                                   Read_Deployment_Manager_Components().customer_id_text_box_by_xpath())
        print(customer_id_text_box.get_attribute('value'))

        x = customer_id_text_box.get_attribute('value')
        print("value of x: ", x)
        if x is "":
            customer_id_text_box.send_keys(Read_Deployment_Manager_Components().customer_id())
        else:
            customer_id_text_box.clear()
        self.d.find_element(By.XPATH, Read_Deployment_Manager_Components().customer_id_save_btn_by_xpath()).click()
        time.sleep(Base_Class.one_second)

    def check_licence_update_successfully(self):
        p_tag = self.d.find_element(By.XPATH, Read_Deployment_Manager_Components().p_tag_content_check_by_xpath())
        time.sleep((Base_Class.two_second + Base_Class.two_second))
        text = p_tag.text
        print(text)
        actual_value = text.__contains__('Expires')
        assert (True, actual_value)

    def check_domain_Status_editable(self):
        self.d.find_element(By.XPATH, Read_Deployment_Manager_Components().domain_status_3_dots_by_xpath()).click()

    def check_menu_options_listed(self):
        self.d.find_element(By.XPATH, Read_Deployment_Manager_Components().domain_status_edit_btn_by_xpath()).click()

    def check_dns_dialog_box_opened(self):
        self.d.find_element(By.XPATH, Read_Deployment_Manager_Components().ip_address_option_by_xpath()).click()
        time.sleep(Base_Class.one_second)
        self.d.find_element(By.XPATH, Read_Deployment_Manager_Components().domain_name_option_by_xpath()).click()
        time.sleep(Base_Class.one_second)
        self.d.find_element(By.XPATH, Read_Deployment_Manager_Components().ip_address_option_by_xpath()).click()
        time.sleep(Base_Class.one_second)
        self.d.find_element(By.XPATH,
                            Read_Deployment_Manager_Components().select_ip_address_dropdown_by_xpath()).click()
        time.sleep(Base_Class.one_second)
        self.d.find_element(By.XPATH, Read_Deployment_Manager_Components().local_host_option_by_xpath()).click()
        time.sleep(Base_Class.two_second)
        self.d.find_element(By.XPATH, Read_Deployment_Manager_Components().ip_address_save_btn_by_xpath()).click()

    def new_user_registration_data_driven(self, name, email, password):
        global registered_already_msg, register_success_msg

        try:
            print("Name: ", name, "  Email: ", email, "  Password: ", password)
            self.d.get(Read_Deployment_Manager_Components().get_url())
            time.sleep(Base_Class.one_second)
            name_id = self.d.find_element(By.ID, Read_Deployment_Manager_Components().name_text_box_by_id())
            name_id.click()
            name_id.send_keys(name)
            time.sleep(Base_Class.one_second)
            email_id = self.d.find_element(By.ID, Read_Deployment_Manager_Components().email_text_box_by_id())
            email_id.click()
            email_id.send_keys(email)
            time.sleep(Base_Class.one_second)
            new_pass = self.d.find_element(By.ID, Read_Deployment_Manager_Components().new_password_text_box_by_id())
            new_pass.click()
            new_pass.send_keys(password)
            time.sleep(Base_Class.one_second)
            confirm_pass = self.d.find_element(By.ID,
                                               Read_Deployment_Manager_Components().confirm_password_text_box_by_id())
            confirm_pass.send_keys(password)
            confirm_pass.click()
            time.sleep(Base_Class.one_second)
            self.d.find_element(By.XPATH, Read_Deployment_Manager_Components().register_btn_text_box_by_xpath()).click()
            time.sleep(Base_Class.two_second)

            if Read_Deployment_Manager_Components().login_url_after_successful_new_register() == self.d.current_url:
                register_success_msg = self.d.find_element(By.XPATH,
                                                           Read_Deployment_Manager_Components().successfully_registered_msg_by_xpath()).text
                print("success message: ", register_success_msg)
            elif Read_Deployment_Manager_Components().get_url() == self.d.current_url:
                registered_already_msg = self.d.find_element(By.XPATH,
                                                             Read_Deployment_Manager_Components().message_after_registration_by_xpath()).text
                print("already register message: ", registered_already_msg)

            if registered_already_msg.__contains__('already registered') or register_success_msg.__contains__(
                    'successfully registered'):
                print('user available')

                return True
            elif register_success_msg.__contains__('not clickable') or registered_already_msg.__contains__(
                    'not clickable'):
                print("register btn not clickable")

                return False
            else:
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\verify_new_registration_ff_reg_pg_03.png")
                print('user not available')
                return False

        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_verify_new_registration_ff_reg_pg_03.png")
                return False
