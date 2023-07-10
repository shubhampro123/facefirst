import time
from pathlib import Path

import pyautogui
from selenium.webdriver.common.by import By

from All_POM_Package.Visitor_Search_Module.Visitor_Search_Module_POM import Visitor_Search_Module_pom
from All_Test_Cases_Package.conftest import Base_Class
from Config_Package.INI_Config_Files.Portal_Menu_Read_INI import Read_Portal_Menu_Components
from Config_Package.INI_Config_Files.VisitorSearchJob_Filter_combination_INI import \
    Read_Visitor_Search_jobs_filter_Components
from Config_Package.INI_Config_Files.Visitor_search_Read_INI import Read_Visitor_Search_Components


class VisitorSearchJob_Filter_combination_pom:

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

            time.sleep(Base_Class.two_second)
            self.click_on_visitor_search_jobs_link()
            time.sleep(Base_Class.two_second)

        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\login_failed_for_portal_menu_pg_03.png")
                return False

    def visitor_search_jobs_with_no_filter_criteria(self):

        try:
            self.login_before()
            self.click_on_search_dropdown()
            self.click_on_search_dropdown_search_btn()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_jobs_with_no_filter_criteria_failed.png")
                return False

    def visitor_search_jobs_with_include_jobs_for_all_user_filter_criteria(self):

        try:
            self.login_before()
            self.click_on_search_dropdown()
            self.click_on_include_jobs_all_users_yes_radio_btn()
            self.click_on_search_dropdown_search_btn()

            self.validate_include_jobs_for_all_users_criteria()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_jobs_with_include_jobs_for_all_user_filter_criteria_failed.png")
                return False

    def visitor_search_jobs_with_include_jobs_with_deleted_results_filter_criteria(self):

        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()
            time.sleep(Base_Class.two_second)
            self.click_on_include_jobs_deleted_results_yes_radio_btn()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown_search_btn()
            time.sleep(Base_Class.two_second)

            self.validate_jobs_deleted_user()
            time.sleep(Base_Class.two_second)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_jobs_with_include_jobs_with_deleted_results_filter_criteria_failed.png")
                return False

    def visitor_search_jobs_with_include_jobs_with_deleted_results_and_for_all_users_filter_criteria(self):

        try:
            self.login_before()

            self.click_on_search_dropdown()
            self.click_on_include_jobs_deleted_results_yes_radio_btn()
            self.click_on_include_jobs_all_users_yes_radio_btn()
            self.click_on_search_dropdown_search_btn()

            self.validate_include_jobs_for_all_users_criteria()
            self.validate_jobs_deleted_user()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_jobs_with_include_jobs_with_deleted_"
                    f"results_and_for_all_users_filter_criteria_failed.png")
                return False

    def visitor_search_jobs_with_only_incomplete_jobs_filter_criteria(self):

        try:
            self.login_before()

            self.click_on_search_dropdown()

            self.click_on_only_incomplete_jobs_yes_radio_btn()

            self.click_on_search_dropdown_search_btn()
            self.validate_incomplete_filter_criteria()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_jobs_with_only_complete_jobs_filter_criteria")
                return False

    def visitor_search_jobs_with_only_incomplete_jobs_and_jobs_for_all_users_filter_criteria(self):

        try:
            self.login_before()

            self.click_on_search_dropdown()
            self.click_on_only_incomplete_jobs_yes_radio_btn()
            self.click_on_include_jobs_all_users_yes_radio_btn()

            self.click_on_search_dropdown_search_btn()
            self.validate_incomplete_filter_criteria()
            self.validate_include_jobs_for_all_users_criteria()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_jobs_with_only_complete_jobs_and_jobs_for_all_users_filter_criteria_failed")
                return False

    def visitor_search_jobs_with_only_incomplete_jobs_and_jobs_with_deleted_users_filter_criteria(self):

        try:
            self.login_before()
            self.click_on_search_dropdown()
            self.click_on_only_incomplete_jobs_yes_radio_btn()
            self.click_on_include_jobs_deleted_results_yes_radio_btn()
            self.click_on_search_dropdown_search_btn()

            self.validate_incomplete_filter_criteria()
            self.validate_jobs_deleted_user()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_jobs_with_only_incomplete_jobs_and_jobs_with"
                    f"_deleted_users_filter_criteria_failed")
                return False

    def visitor_search_jobs_with_incomplete_jobs_deleted_users_jobs_for_all_users_filter_criteria(self):

        try:
            self.login_before()
            self.click_on_search_dropdown()
            self.click_on_only_incomplete_jobs_yes_radio_btn()
            self.click_on_include_jobs_deleted_results_yes_radio_btn()
            self.click_on_search_dropdown_search_btn()

            self.validate_incomplete_filter_criteria()
            self.validate_jobs_deleted_user()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_jobs_with_incomplete_jobs_deleted_users_jobs_for_all_users_filter_criteria")
                return False

    def visitor_search_jobs_with_date_range_filter_criteria(self):

        try:
            self.login_before()
            self.click_on_search_dropdown()
            time.sleep(Base_Class.three_second)
            self.set_date_in_search_filter()
            time.sleep(Base_Class.three_second)
            self.click_on_search_dropdown_search_btn()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_jobs_with_date_range_filter_criteria_failed")
                return False

    def visitor_search_jobs_with_date_range_and_include_jobs_all_users_filter_criteria(self):
        try:
            self.login_before()
            self.click_on_search_dropdown()
            time.sleep(Base_Class.two_second)
            self.set_date_in_search_filter()
            time.sleep(Base_Class.two_second)
            self.click_on_include_jobs_all_users_yes_radio_btn()
            self.click_on_search_dropdown_search_btn()

            self.validate_include_jobs_for_all_users_criteria()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_jobs_with_date_range_and_include_jobs_all_users_filter_criteria_failed")
                return False

    def visitor_search_jobs_with_date_range_and_include_jobs_deleted_users_filter_criteria(self):
        try:
            self.login_before()
            self.click_on_search_dropdown()
            time.sleep(Base_Class.two_second)
            self.set_date_in_search_filter()
            time.sleep(Base_Class.two_second)
            self.click_on_include_jobs_deleted_results_yes_radio_btn()
            self.click_on_search_dropdown_search_btn()

            self.validate_jobs_deleted_user()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_jobs_with_date_range_and_include_jobs_deleted_users_filter_criteria_failed")
                return False

    def visitor_search_jobs_with_date_range_include_jobs_deleted_and_all_users_filter_criteria(self):
        try:
            self.login_before()
            self.click_on_search_dropdown()
            time.sleep(Base_Class.two_second)
            self.set_date_in_search_filter()
            time.sleep(Base_Class.two_second)
            self.click_on_include_jobs_deleted_results_yes_radio_btn()
            self.click_on_include_jobs_all_users_yes_radio_btn()
            self.click_on_search_dropdown_search_btn()

            self.validate_jobs_deleted_user()
            self.validate_include_jobs_for_all_users_criteria()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_jobs_with_date_range_include_jobs_deleted_and_all_users_filter_criteria_failed")
                return False

    def visitor_search_jobs_with_date_range_and_only_incomplete_jobs_criteria(self):
        try:
            self.login_before()
            self.click_on_search_dropdown()
            time.sleep(Base_Class.two_second)
            self.set_date_in_search_filter()
            time.sleep(Base_Class.two_second)
            self.click_on_only_incomplete_jobs_yes_radio_btn()
            self.click_on_search_dropdown_search_btn()

            self.validate_incomplete_filter_criteria()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_jobs_with_date_range_and_only_complete_jobs_criteria_failed")
                return False

    def visitor_search_jobs_with_date_range_incomplete_jobs_and_jobs_all_users_criteria(self):
        try:
            self.login_before()
            self.click_on_search_dropdown()
            time.sleep(Base_Class.two_second)
            self.set_date_in_search_filter()
            time.sleep(Base_Class.two_second)
            self.click_on_only_incomplete_jobs_yes_radio_btn()
            self.click_on_include_jobs_all_users_yes_radio_btn()
            self.click_on_search_dropdown_search_btn()

            self.validate_incomplete_filter_criteria()
            self.validate_include_jobs_for_all_users_criteria()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_jobs_with_date_range_incomplete_jobs_and_jobs_all_users_criteria_failed")
                return False

    def visitor_search_jobs_with_date_range_incomplete_jobs_and_jobs_deleted_users_criteria(self):
        try:
            self.login_before()
            self.click_on_search_dropdown()
            time.sleep(Base_Class.two_second)
            self.set_date_in_search_filter()
            time.sleep(Base_Class.two_second)
            self.click_on_only_incomplete_jobs_yes_radio_btn()
            self.click_on_include_jobs_deleted_results_yes_radio_btn()
            self.click_on_search_dropdown_search_btn()

            self.validate_incomplete_filter_criteria()
            self.validate_jobs_deleted_user()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_jobs_with_date_range_incomplete_jobs_and_jobs_deleted_users_criteria_failed")
                return False

    ############################################# RESUABLE METHODS ###################################################

    def validate_include_jobs_for_all_users_criteria(self):
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_filter_Components()
                                  .all_users_job_by_xpath())
        assert ele.is_displayed()

    def validate_incomplete_filter_criteria(self):
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_filter_Components()
                                  .only_incomplete_jobs_by_xpath())
        assert ele.is_displayed()

    def set_date_in_search_filter(self):
        try:
            start_date = Read_Visitor_Search_jobs_filter_Components().start_date_data()
            end_date = Read_Visitor_Search_jobs_filter_Components().end_date_data()
            start_date_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_filter_Components()
                                                 .start_date_input_tbx_by_xpath())

            start_date_ele.send_keys(start_date)
            to_ele = self.d.find_element(By.XPATH, "//p[text()='to']")
            to_ele.click()
            time.sleep(Base_Class.one_second)
            end_date_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_filter_Components()
                                               .end_date_input_tbx_by_xpath())

            end_date_ele.send_keys(end_date)
            time.sleep(Base_Class.one_second)
            to_ele.click()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_only_match_count_criteria_failed.png")
                return False

    def click_on_search_dropdown(self):
        search_dropdown = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_filter_Components()
                                              .search_by_xpath())
        search_dropdown.click()

    def click_on_only_incomplete_jobs_yes_radio_btn(self):
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_filter_Components()
                                  .only_incomplete_jobs_yes_radio_btn_by_xpath())
        ele.click()

    def click_on_only_incomplete_jobs_no_radio_btn(self):
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_filter_Components()
                                  .only_incomplete_jobs_no_radio_btn_by_xpath())
        ele.click()

    def click_on_include_jobs_deleted_results_yes_radio_btn(self):
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_filter_Components()
                                  .include_jobs_deleted_results_jobs_yes_radio_btn_by_xpath())
        ele.click()

    def click_on_include_jobs_deleted_results_no_radio_btn(self):
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_filter_Components()
                                  .include_jobs_deleted_results_jobs_no_radio_btn_by_xpath())
        ele.click()

    def click_on_include_jobs_all_users_yes_radio_btn(self):
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_filter_Components()
                                  .include_jobs_all_users_yes_radio_btn_by_xpath())
        ele.click()

    def click_on_include_jobs_all_users_no_radio_btn(self):
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_filter_Components()
                                  .include_jobs_all_users_no_radio_btn_by_xpath())
        ele.click()

    def click_on_search_dropdown_search_btn(self):
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_filter_Components()
                                  .search_dropdown_search_btn_by_xpath())
        ele.click()

    def click_on_search_dropdown_clear_btn(self):
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_filter_Components()
                                  .search_dropdown_clear_btn_by_xpath())
        ele.click()

    def click_on_visitor_search_jobs_link(self):
        ele = visitor_search_job_btn = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_filter_Components()
                                                           .visitor_search_job_btn_by_xpath())

        self.d.execute_script("arguments[0].click();", visitor_search_job_btn)

    def validate_jobs_deleted_user(self):
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_filter_Components()
                                  .including_deleted_criteria_by_xpath())
        assert ele.is_displayed()

    def close_all_panel_one_by_one(self):
        try:
            close_panel_list = self.d.find_elements(By.XPATH,
                                                    Read_Visitor_Search_Components().close_all_panel_one_by_one())
            for i in close_panel_list:
                i.click()
                time.sleep(Base_Class.one_second)
            return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\close_all_panel_failed_pg_03.png")
                return False

    def click_on_logout_button(self):
        try:
            time.sleep(Base_Class.one_second)
            logout_button = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().logout_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            logout_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_logout_pg_03.png")
                return False
