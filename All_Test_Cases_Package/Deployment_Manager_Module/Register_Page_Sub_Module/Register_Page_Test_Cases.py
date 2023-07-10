import time
import pytest
from pathlib import Path

from All_POM_Package.Deployment_Manager_Module.Register_Page_Sub_Module.Register_Page_POM import Deployment_manager_pom
from All_Test_Cases_Package.conftest import Base_Class


class Test_Deployment_Manager_Test_Cases(Base_Class):
    user_list = None
    results = list()

    def setup_method(self):
        try:
            print("\n setup start")
            self.d = Base_Class.d
            self.d.maximize_window()
            self.d.set_page_load_timeout(50)
            self.d.set_script_timeout(30)
            self.d.implicitly_wait(30)
            self.logger = Base_Class.logger_object()
            self.screenshots_path = f"{Path(__file__).parent.parent.parent}\\Reports\\Screenshots"
            print("\nsetup end")

        except Exception as ex:
            print("\nException in Test_Deployment_Manager_Test_Cases/setup_method: ", ex)

    def test_verify_link(self):
        print("Test Case ff_01 execution started..")
        self.logger.info("testing test")
        if Deployment_manager_pom().compare_actual_dm_url():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_link.png")
            assert False

    def test_verify_page_heading(self):
        print("verifying page heading..")
        print(Deployment_manager_pom().verify_registration_page_heading())
        if Deployment_manager_pom().verify_registration_page_heading():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_page_heading.png")
            assert False

    def test_verify_registration_page_menu_button_visible(self):
        print("test_verify_registration_page_menu_button_visible Test")
        if Deployment_manager_pom().registration_page_menu_btn_visible():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_registration_page_menu_button_visible.png")
            assert False

    def test_verify_registration_page_menu_button_enabled(self):
        print("verify_registration_page_menu_button_visible Test")
        if Deployment_manager_pom().registration_page_menu_btn_enabled():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_registration_page_menu_button_enabled.png")
            assert False

    def test_verify_login_link_visible(self):
        print("verify login link is visible test")
        if Deployment_manager_pom().login_link_is_visible():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_login_link_visible.png")
            assert False

    def test_verify_login_link_clickable(self):
        print("verify login link is clickable test")
        if Deployment_manager_pom().login_link_is_enabled():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_login_link_clickable.png")
            assert False

    def test_verify_login_link_in_title_bar_working_properly(self):
        print("verify login link in title bar working properly")
        if Deployment_manager_pom().verify_login_url():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_login_link_in_title_bar_working_properly.png")
            assert False
        self.d.back()
        time.sleep(2)

    def test_verify_fill_out_from_text_displayed_in_registration_form_panel_heading(self):
        print("verifying fill out form text displayed")
        if Deployment_manager_pom().fill_out_form_text_by_xpath():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_fill_out_from_text_displayed_in_registration_form_panel_heading.png")
            assert False

    def test_verify_name_text_displayed_inside_name_text_box(self):
        print("verifying name text displayed in name text box")
        if Deployment_manager_pom().verify_name_text_displayed():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_name_text_displayed_inside_name_text_box.png")
            assert False

    def test_verify_star_displayed_after_name_in_name_text_box(self):
        print("verifying star displayed after name in text box")
        if Deployment_manager_pom().verify_star_after_name_text_displayed():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_star_displayed_after_name_in_name_text_box.png")
            assert False

    def test_verify_email_label_displayed_in_email_text_box(self):
        print("verifying email label displayed in email text box")
        if Deployment_manager_pom().verify_email_label_displayed_in_email_text_box():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_email_label_displayed_in_email_text_box.png")
            assert False

    def test_verify_star_displayed_after_email_label(self):
        print("verifying star displayed after email label")
        if Deployment_manager_pom().verify_email_label_displayed_in_email_text_box():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_star_displayed_after_email_label.png")
            assert False

    def test_verify_invalid_email_msg_displayed(self):
        print("verifying invalid email text displayed")
        if Deployment_manager_pom().verify_invalid_email_msg_displayed():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_invalid_email_msg_displayed.png")
            assert False

    def test_verify_password_label_displayed_in_password_text_box(self):
        print("verifying password text displayed in password text box")
        if Deployment_manager_pom().verify_password_label_by_xpath():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_password_label_displayed_in_password_text_box.png")
            assert False

    def test_verify_star_displayed_in_new_password_text_box(self):
        print("verifying star displayed in new password text box")
        if Deployment_manager_pom().verify_star_displayed_in_new_password_text_box():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_star_displayed_in_new_password_text_box.png")
            assert False

    def test_verify_new_password_helper_text_displayed(self):
        print("verifying new password helper text is displayed ")
        if Deployment_manager_pom().verify_new_password_helper_text_displayed():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_new_password_helper_text_displayed.png")
            assert False

    def test_verify_new_password_text_displayed_as_expected(self):
        print("verify_new_password_text_displayed_as_expected ")
        if Deployment_manager_pom().verify_new_password_text_displayed_as_expected():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_new_password_text_displayed_as_expected.png")
            assert False

    def test_verify_password_confirm_text_inside_confirm_password_text_box(self):
        print("verifying confirm password displayed")
        if Deployment_manager_pom().verify_password_confirm_text_inside_confirm_password_text_box():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_password_confirm_text_inside_confirm_password_text_box.png")
            assert False

    def test_verify_star_after_confirm_password_text_in_confirm_password_text_box(self):
        print("verifying star after confirm password text")
        if Deployment_manager_pom().verify_star_after_confirm_password_text_in_confirm_password_text_box():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_star_after_confirm_password_text_in_confirm_password_text_box.png")
            assert False

    def test_verify_password_complexity_text_is_displayed(self):
        print("verify password complexity text is displayed")
        if Deployment_manager_pom().verify_password_complexity_text_is_displayed():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_password_complexity_text_is_displayed.png")
            assert False

    def test_verify_password_confirmation_text_is_displayed_as_expected(self):
        print("verify password complexity text is displayed as expected ")
        if Deployment_manager_pom().verify_password_confirmation_text_is_displayed_as_expected():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_password_confirmation_text_is_displayed_as_expected.png")
            assert False

    def test_verify_already_registered_text_is_displayed(self):
        print("verify_already_registered_text_is_displayed")
        if Deployment_manager_pom().verify_already_registered_text_is_displayed():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_already_registered_text_is_displayed.png")
            assert False

    def test_verify_already_registered_text_is_displayed_as_expected(self):
        print("verify_already_registered_text_is_displayed_as_expected")
        if Deployment_manager_pom().verify_already_registered_text_is_displayed_as_expected():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_already_registered_text_is_displayed_as_expected.png")
            assert False

    def test_verify_login_link_after_already_registered_by_xpath_is_displayed(self):
        print("verify_login_link_after_already_registered_by_xpath_is_displayed")
        if Deployment_manager_pom().verify_login_link_after_already_registered_by_xpath_is_displayed():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_login_link_after_already_registered_by_xpath_is_displayed.png")
            assert False

    def test_verify_login_link_after_already_registered_by_xpath_is_enabled(self):
        print("test_verify_login_link_after_already_registered_by_xpath_is_enabled")
        if Deployment_manager_pom().verify_login_link_after_already_registered_by_xpath_is_enabled():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_login_link_after_already_registered_by_xpath_is_enabled.png")
            assert False

    def test_verify_login_link_after_already_registered__text_by_xpath_is_working_as_expected(self):
        print("verify_login_link_after_already_registered__text_by_xpath_is_working_as_expected")
        if Deployment_manager_pom().verify_login_link_after_already_registered__text_by_xpath_is_working_as_expected():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_login_link_after_already_registered__text_by_xpath_is_working_as_expected.png")
            assert False

    # @pytest.mark.skip
    def test_verify_password_visibility_btn_by_xpath_is_visible(self):
        print("verify_password_visibility_btn_by_xpath_is_visible")
        if Deployment_manager_pom().verify_password_visibility_btn_by_xpath_is_visible():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_login_link_after_already_registered__text_by_xpath_is_working_as_expected.png")
            assert False

    # @pytest.mark.skip
    def test_verify_password_visibility_btn_by_xpath_is_clickable(self):
        print("verify_password_visibility_btn_by_xpath_is_clickable")
        if Deployment_manager_pom().verify_password_visibility_btn_by_xpath_is_clickable():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_password_visibility_btn_by_xpath_is_clickable.png")
            assert False

    # @pytest.mark.skip
    def test_verify_password_visibility_btn_by_xpath_is_working_as_expected(self):
        print("verify_password_visibility_btn_by_xpath_is_working_as_expected")
        if Deployment_manager_pom().verify_password_visibility_btn_by_xpath_is_working_as_expected():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_password_visibility_btn_by_xpath_is_working_as_expected.png")
            assert False

    # @pytest.mark.skip
    def test_verify_all_elements_are_visible(self):
        print("verify_all_elements_are_visible")

        if Deployment_manager_pom().verify_elements_visible():
            assert True
        else:
            self.d.save_screenshot(
                f"{Path(__file__).parent.parent}\\Screenshots\\test_verify_all_elements_are_visible.png")
            assert False

    # @pytest.mark.skip
    def test_verify_all_elements_are_clickable(self):
        print("verify_all_elements_are_clickable")
        if Deployment_manager_pom().verify_elements_clickable():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_verify_all_elements_are_clickable.png")
            assert False

    # @pytest.mark.skip
    def test_register_new_user(self):
        print("test_register_new_user")
        if Deployment_manager_pom().register_new_user():
            assert True
        else:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_register_new_user.png")
            assert False

    # @pytest.mark.skip
    @pytest.mark.parametrize('name, email, password', Base_Class.user_list)
    def test_registration_new_user_data_driven(self, name, email, password):
        print("new user registration using data driven from excel")
        count = 0
        if Deployment_manager_pom().new_user_registration_data_driven(name, email, password):
            assert True

        else:
            count = count+1
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_registration_new_user_data_driven_{count}.png")
            assert False

        # Base_Class.df.to_csv(f"{Path(__file__).parent.parent}\\Results_Folder\\test.csv")
        # Base_Class.df.to_excel(f"{Path(__file__).parent.parent}\\Results_Folder\\test1.xlsx")

    # @pytest.mark.skip
    def test_open_login_page_ff_04(self):
        print("login page is opening..")
        Deployment_manager_pom().open_login_page()

    # @pytest.mark.skip
    def test_check_login_page_title_ff_05(self):
        print("checking login page title")
        Deployment_manager_pom().check_login_page_title()

    # @pytest.mark.skip
    def test_login_to_portal_ff_06(self):
        print("checking login credentials.. ")
        Deployment_manager_pom().login_to_portal()

    # @pytest.mark.skip
    def test_check_deployment_manager_home_page_title_ff_07(self):
        print("checking deployment manager home page title")
        Deployment_manager_pom().check_deployment_manager_home_page_title()

    # @pytest.mark.skip
    def test_check_license_status_edit_btn_clickable_ff_08(self):
        print("checking edit btn clickable ")
        Deployment_manager_pom().check_license_status_edit_btn_clickable()

    # @pytest.mark.skip
    def test_enter_customer_id_and_save_ff_09(self):
        print("entering customer ID")
        Deployment_manager_pom().check_customer_id_by_xpath_clickable()

    # @pytest.mark.skip
    def test_check_license_updated_successfully_ff_10(self):
        print("check update successfully running")
        Deployment_manager_pom().check_licence_update_successfully()

    # @pytest.mark.skip
    def test_check_domain_status_editable_ff_11(self):
        print("checking domain status editable..")
        Deployment_manager_pom().check_domain_Status_editable()

    # @pytest.mark.skip
    def test_menu_option_listed_in_edit_btn_ff_12(self):
        print("checking options listed in domain status popup")
        Deployment_manager_pom().check_menu_options_listed()

    # @pytest.mark.skip
    def test_dns_dialog_box_opened_ff_13(self):
        print("checking dns dialog box is opened")
        Deployment_manager_pom().check_dns_dialog_box_opened()

    def teardown(self):
        print("\nTeardown start")

        print("\nTeardown end")
