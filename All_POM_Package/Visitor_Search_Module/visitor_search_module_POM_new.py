import os
import re
import sys
import time
from pathlib import Path

import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.file_detector import LocalFileDetector
from selenium.webdriver.support.select import Select
from All_Test_Cases_Package.conftest import Base_Class
from Config_Package.INI_Config_Files.Portal_Menu_Read_INI import Read_Portal_Menu_Components
from Config_Package.INI_Config_Files.Visitor_search_Read_INI import Read_Visitor_Search_Components


class Visitor_Search_Module_pom_new:

    def __init__(self):
        self.d = Base_Class.d

    def login_before(self):

        try:
            self.d.get(Read_Portal_Menu_Components().get_url())
            time.sleep(Base_Class.two_second)
            username = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_usernameField())
            counter = 0
            while not username.is_displayed():
                time.sleep(Base_Class.two_second)
                counter = counter + 1
                if counter > 3:
                    self.d.refresh()
                    time.sleep(Base_Class.two_second)
            time.sleep(Base_Class.two_second)
            username.send_keys(Read_Portal_Menu_Components().get_username())
            time.sleep(Base_Class.two_second)
            password = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_passwordField())
            password.send_keys(Read_Portal_Menu_Components().get_password())
            time.sleep(Base_Class.one_second)
            login_btn = self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton())
            self.d.execute_script("arguments[0].click();", login_btn)
            visitor_search_btn = self.d.find_element(By.XPATH,
                                                     Read_Portal_Menu_Components().
                                                     portal_menu_visitors_search_btn_by_xpath())
            time.sleep(3)
            self.d.execute_script("arguments[0].click();", visitor_search_btn)
            time.sleep(3)

        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\login_failed_for_portal_menu_pg_03.png")
                return False

    ############################ Visitor Search with image using NATS (Demographics Enabled) #######################

    def visitor_search_with_no_search_criteria(self):

        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.nats_checkbox()

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_Must_specify_start_and_end_date_for_meta_data_only_search()
            time.sleep(Base_Class.two_second)
            self.close_all_panel_one_by_one()
            time.sleep(Base_Class.two_second)
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_no_search_criteria_failed.png")
                return False

    def visitor_search_with_region_criteria_with_NATS(self):
        try:
            self.login_before()
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_Must_specify_start_and_end_date_for_meta_data_only_search()
            time.sleep(Base_Class.two_second)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\"
                    f"visitor_search_with_region_criteria_with_NATS_failed.png")
                return False

    def visitor_search_with_gender_criteria_with_NATS(self):
        try:
            self.login_before()
            time.sleep(2)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_Must_specify_start_and_end_date_for_meta_data_only_search()
            time.sleep(Base_Class.two_second)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\"
                    f"visitor_search_with_gender_criteria_with_NATS_failed.png")
                return False

    def visitor_search_with_region_and_gender_criteria_with_NATS(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            time.sleep(Base_Class.two_second)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_Must_specify_start_and_end_date_for_meta_data_only_search()
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
                    f"\\visitor_search_with_region_and_gender_criteria_with_NATS_failed.png")
                return False

    def visitor_search_with_age_criteria_with_NATS(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            time.sleep(Base_Class.two_second)
            self.select_start_age(start_age)
            time.sleep(Base_Class.two_second)
            self.select_end_age(end_age)
            time.sleep(Base_Class.two_second)
            self.nats_checkbox()

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_Must_specify_start_and_end_date_for_meta_data_only_search()
            time.sleep(Base_Class.two_second)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\"
                    f"visitor_search_with_age_criteria_with_NATS_failed.png")
                return False

    def visitor_search_with_region_and_age_criteria_with_NATS(self):
        try:
            self.login_before()

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            time.sleep(Base_Class.two_second)

            self.select_start_age(start_age)
            time.sleep(Base_Class.two_second)
            self.select_end_age(end_age)
            time.sleep(Base_Class.two_second)
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_Must_specify_start_and_end_date_for_meta_data_only_search()
            time.sleep(Base_Class.two_second)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\"
                    f"visitor_search_with_region_and_age_criteria_with_NATS_failed"
                    f".png")
                return False

    def visitor_search_with_age_and_gender_criteria_with_NATS(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            time.sleep(Base_Class.two_second)
            self.select_start_age(start_age)
            time.sleep(Base_Class.two_second)
            self.select_end_age(end_age)
            time.sleep(Base_Class.two_second)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_Must_specify_start_and_end_date_for_meta_data_only_search()
            time.sleep(Base_Class.two_second)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\"
                    f"visitor_search_with_age_and_gender_criteria_with_NATS_failed"
                    f".png")
                return False

    def visitor_search_with_region_age_and_gender_criteria_with_NATS(self):
        try:
            self.login_before()

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            time.sleep(Base_Class.two_second)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            time.sleep(Base_Class.two_second)
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_Must_specify_start_and_end_date_for_meta_data_only_search()
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
                    f"\\visitor_search_with_region_age_and_gender_criteria_with_NATS_failed.png")
                return False

    def visitor_search_with_only_date_criteria_with_NATS(self):
        try:
            self.login_before()
            date = int(Read_Visitor_Search_Components().meta_data_start_date())
            month = str(Read_Visitor_Search_Components().meta_data_start_month())
            year = int(Read_Visitor_Search_Components().meta_data_start_year())
            hour = str(Read_Visitor_Search_Components().meta_data_start_hour())
            minute = Read_Visitor_Search_Components().meta_data_start_minuet()
            period = str(Read_Visitor_Search_Components().meta_data_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().meta_data_end_month())
            e_date = int(Read_Visitor_Search_Components().meta_data_end_date())
            e_year = int(Read_Visitor_Search_Components().meta_data_end_year())
            e_hour = str(Read_Visitor_Search_Components().meta_data_end_hour())
            e_minute = Read_Visitor_Search_Components().meta_data_end_minuet()
            e_period = str(Read_Visitor_Search_Components().meta_data_end_am_pm_period())
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            self.nats_checkbox()
            time.sleep(Base_Class.two_second)
            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_only_date_criteria_with_NATS_failed.png")
                return False

    def visitor_search_with_date_and_region_criteria_with_NATS(self):
        try:
            self.login_before()
            date = int(Read_Visitor_Search_Components().meta_data_start_date())
            month = str(Read_Visitor_Search_Components().meta_data_start_month())
            year = int(Read_Visitor_Search_Components().meta_data_start_year())
            hour = str(Read_Visitor_Search_Components().meta_data_start_hour())
            minute = Read_Visitor_Search_Components().meta_data_start_minuet()
            period = str(Read_Visitor_Search_Components().meta_data_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().meta_data_end_month())
            e_date = int(Read_Visitor_Search_Components().meta_data_end_date())
            e_year = int(Read_Visitor_Search_Components().meta_data_end_year())
            e_hour = str(Read_Visitor_Search_Components().meta_data_end_hour())
            e_minute = Read_Visitor_Search_Components().meta_data_end_minuet()
            e_period = str(Read_Visitor_Search_Components().meta_data_end_am_pm_period())
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_Components().zone_data_input()
            time.sleep(Base_Class.two_second)
            self.select_zone(zone_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_region_from_match_list(zone_data)
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_date_and_region_criteria_with_NATS_failed.png")
                return False

    def visitor_search_with_only_date_and_gender_criteria_with_NATS(self):
        try:
            self.login_before()
            date = int(Read_Visitor_Search_Components().meta_data_start_date())
            month = str(Read_Visitor_Search_Components().meta_data_start_month())
            year = int(Read_Visitor_Search_Components().meta_data_start_year())
            hour = str(Read_Visitor_Search_Components().meta_data_start_hour())
            minute = Read_Visitor_Search_Components().meta_data_start_minuet()
            period = str(Read_Visitor_Search_Components().meta_data_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().meta_data_end_month())
            e_date = int(Read_Visitor_Search_Components().meta_data_end_date())
            e_year = int(Read_Visitor_Search_Components().meta_data_end_year())
            e_hour = str(Read_Visitor_Search_Components().meta_data_end_hour())
            e_minute = Read_Visitor_Search_Components().meta_data_end_minuet()
            e_period = str(Read_Visitor_Search_Components().meta_data_end_am_pm_period())
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_gender_match_list(gender_data)
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_only_date_and_gender_criteria_with_NATS_failed.png")
                return False

    def visitor_search_with_date_region_and_age_range_criteria(self):
        try:
            self.login_before()
            date = int(Read_Visitor_Search_Components().meta_data_start_date())
            month = str(Read_Visitor_Search_Components().meta_data_start_month())
            year = int(Read_Visitor_Search_Components().meta_data_start_year())
            hour = str(Read_Visitor_Search_Components().meta_data_start_hour())
            minute = str(Read_Visitor_Search_Components().meta_data_start_minuet())
            period = str(Read_Visitor_Search_Components().meta_data_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().meta_data_end_month())
            e_date = int(Read_Visitor_Search_Components().meta_data_end_date())
            e_year = int(Read_Visitor_Search_Components().meta_data_end_year())
            e_hour = str(Read_Visitor_Search_Components().meta_data_end_hour())
            e_minute = str(Read_Visitor_Search_Components().meta_data_end_minuet())
            e_period = str(Read_Visitor_Search_Components().meta_data_end_am_pm_period())
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            time.sleep(Base_Class.two_second)
            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            time.sleep(Base_Class.two_second)
            self.select_start_age(start_age)
            self.select_end_age(end_age)

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()

            self.verify_region_from_match_list(zone_data)
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.validate_age_matches_list(start_age, end_age)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_date_region_and_age_range_criteria_failed.png")
                return False

    def visitor_search_with_date_and_region_and_gender_criteria_with_NATS(self):
        try:
            self.login_before()
            date = int(Read_Visitor_Search_Components().meta_data_start_date())
            month = str(Read_Visitor_Search_Components().meta_data_start_month())
            year = int(Read_Visitor_Search_Components().meta_data_start_year())
            hour = str(Read_Visitor_Search_Components().meta_data_start_hour())
            minute = Read_Visitor_Search_Components().meta_data_start_minuet()
            period = str(Read_Visitor_Search_Components().meta_data_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().meta_data_end_month())
            e_date = int(Read_Visitor_Search_Components().meta_data_end_date())
            e_year = int(Read_Visitor_Search_Components().meta_data_end_year())
            e_hour = str(Read_Visitor_Search_Components().meta_data_end_hour())
            e_minute = Read_Visitor_Search_Components().meta_data_end_minuet()
            e_period = str(Read_Visitor_Search_Components().meta_data_end_am_pm_period())
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            time.sleep(Base_Class.two_second)
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_region_from_match_list(zone_data)
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_gender_match_list(gender_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_date_and_region_and_gender_criteria_with_NATS_failed.png")
                return False

    def visitor_search_with_date_and_age_criteria_with_NATS(self):
        try:
            self.login_before()
            date = int(Read_Visitor_Search_Components().meta_data_start_date())
            month = str(Read_Visitor_Search_Components().meta_data_start_month())
            year = int(Read_Visitor_Search_Components().meta_data_start_year())
            hour = str(Read_Visitor_Search_Components().meta_data_start_hour())
            minute = Read_Visitor_Search_Components().meta_data_start_minuet()
            period = str(Read_Visitor_Search_Components().meta_data_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().meta_data_end_month())
            e_date = int(Read_Visitor_Search_Components().meta_data_end_date())
            e_year = int(Read_Visitor_Search_Components().meta_data_end_year())
            e_hour = str(Read_Visitor_Search_Components().meta_data_end_hour())
            e_minute = Read_Visitor_Search_Components().meta_data_end_minuet()
            e_period = str(Read_Visitor_Search_Components().meta_data_end_am_pm_period())
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            time.sleep(Base_Class.two_second)
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            self.nats_checkbox()

            time.sleep(Base_Class.two_second)
            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.validate_age_matches_list(start_age, end_age)
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\"
                    f"visitor_search_with_date_and_age_criteria_with_NATS_failed.png")
                return False

    def visitor_search_with_date_region_and_age_range_criteria_with_NATS(self):
        try:
            self.login_before()
            date = int(Read_Visitor_Search_Components().meta_data_start_date())
            month = str(Read_Visitor_Search_Components().meta_data_start_month())
            year = int(Read_Visitor_Search_Components().meta_data_start_year())
            hour = str(Read_Visitor_Search_Components().meta_data_start_hour())
            minute = Read_Visitor_Search_Components().meta_data_start_minuet()
            period = str(Read_Visitor_Search_Components().meta_data_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().meta_data_end_month())
            e_date = int(Read_Visitor_Search_Components().meta_data_end_date())
            e_year = int(Read_Visitor_Search_Components().meta_data_end_year())
            e_hour = str(Read_Visitor_Search_Components().meta_data_end_hour())
            e_minute = Read_Visitor_Search_Components().meta_data_end_minuet()
            e_period = str(Read_Visitor_Search_Components().meta_data_end_am_pm_period())
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            time.sleep(Base_Class.two_second)
            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            time.sleep(Base_Class.two_second)
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_region_from_match_list(zone_data)
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.validate_age_matches_list(start_age, end_age)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_date_region_and_age_range_criteria_with_NATS_failed.png")
                return False

    def visitor_search_with_date_age_and_gender_criteria_with_NATS(self):
        try:
            self.login_before()
            date = int(Read_Visitor_Search_Components().meta_data_start_date())
            month = str(Read_Visitor_Search_Components().meta_data_start_month())
            year = int(Read_Visitor_Search_Components().meta_data_start_year())
            hour = str(Read_Visitor_Search_Components().meta_data_start_hour())
            minute = str(Read_Visitor_Search_Components().meta_data_start_minuet())
            period = str(Read_Visitor_Search_Components().meta_data_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().meta_data_end_month())
            e_date = int(Read_Visitor_Search_Components().meta_data_end_date())
            e_year = int(Read_Visitor_Search_Components().meta_data_end_year())
            e_hour = str(Read_Visitor_Search_Components().meta_data_end_hour())
            e_minute = str(Read_Visitor_Search_Components().meta_data_end_minuet())
            e_period = str(Read_Visitor_Search_Components().meta_data_end_am_pm_period())
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.validate_age_matches_list(start_age, end_age)
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_gender_match_list(gender_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_date_age_and_gender_criteria_with_NATS_failed.png")
                return False

    def visitor_search_with_date_region_age_range_and_gender_criteria_with_NATS(self):

        try:
            self.login_before()
            date = int(Read_Visitor_Search_Components().meta_data_start_date())
            month = str(Read_Visitor_Search_Components().meta_data_start_month())
            year = int(Read_Visitor_Search_Components().meta_data_start_year())
            hour = str(Read_Visitor_Search_Components().meta_data_start_hour())
            minute = Read_Visitor_Search_Components().meta_data_start_minuet()
            period = str(Read_Visitor_Search_Components().meta_data_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().meta_data_end_month())
            e_date = int(Read_Visitor_Search_Components().meta_data_end_date())
            e_year = int(Read_Visitor_Search_Components().meta_data_end_year())
            e_hour = str(Read_Visitor_Search_Components().meta_data_end_hour())
            e_minute = Read_Visitor_Search_Components().meta_data_end_minuet()
            e_period = str(Read_Visitor_Search_Components().meta_data_end_am_pm_period())
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            time.sleep(Base_Class.two_second)
            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            time.sleep(Base_Class.two_second)
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            time.sleep(Base_Class.two_second)
            self.select_gender(gender_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_region_from_match_list(zone_data)
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.validate_age_matches_list(start_age, end_age)
            self.verify_gender_match_list(gender_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_date_region_age_range_and_gender_criteria_with_NATS_failed.png")
                return False

    ################ Visitor Search with Image and Metadata with Nats (Demographics Enabled) #######################

    def visitor_search_with_image_and_NATS_criteria(self):
        try:

            self.add_image_search()
            self.nats_checkbox()

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()

            self.verify_image_from_match_list()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            self.d.delete_all_cookies()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\visitor_search_with_image_and_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_and_max_match_with_NATS_criteria(self):
        try:
            self.add_image_search()

            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()

            self.verify_image_from_match_list()
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            time.sleep(2)
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_and_max_match_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_and_thresh_hold_with_NATS_criteria(self):
        try:
            # self.d.execute_script("location.reload(true);")

            self.add_image_search()
            self.set_thresh_hold_slider()
            self.nats_checkbox()

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()

            self.verify_image_from_match_list()
            self.compare_thresh_hold_value_with_score()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_and_thresh_hold_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_thresh_hold_and_max_count_with_NATS_criteria(self):
        try:
            self.add_image_search()

            self.set_thresh_hold_slider()
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()

            self.verify_image_from_match_list()
            self.compare_thresh_hold_value_with_score()
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_thresh_hold_and_max_count_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_and_gender_with_NATS_criteria(self):
        try:
            self.add_image_search()

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.nats_checkbox()

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()

            self.verify_image_from_match_list()
            self.verify_gender_match_list(gender_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_and_gender_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_gender_and_max_count_with_NATS_criteria(self):
        try:
            self.add_image_search()

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)

            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()

            self.verify_image_from_match_list()
            self.verify_gender_match_list(gender_data)
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_gender_and_max_count_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_gender_and_thresh_hold_with_NATS_criteria(self):
        try:
            self.add_image_search()

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)

            self.set_thresh_hold_slider()
            self.nats_checkbox()

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()

            self.verify_image_from_match_list()
            self.verify_gender_match_list(gender_data)
            self.compare_thresh_hold_value_with_score()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_gender_and_thresh_hold_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_gender_thresh_hold_and_max_count_with_NATS_criteria(self):
        try:
            self.add_image_search()

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)

            self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)

            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()

            self.verify_image_from_match_list()
            self.verify_gender_match_list(gender_data)
            self.compare_thresh_hold_value_with_score()
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_gender_thresh_hold_and_max_count_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_and_age_range_with_NATS_criteria(self):
        try:
            self.add_image_search()

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            self.nats_checkbox()

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()

            time.sleep(Base_Class.two_second)
            self.verify_image_from_match_list()
            self.validate_age_matches_list(start_age, end_age)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_and_age_range_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_age_range_and_max_match_with_NATS_criteria(self):
        try:
            self.add_image_search()
            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.validate_age_matches_list(start_age, end_age)
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_age_range_and_max_match_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_age_range_and_thresh_hold_with_NATS_criteria(self):
        try:
            self.add_image_search()
            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)

            self.set_thresh_hold_slider()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            if self.check_if_match_is_found():
                self.verify_image_from_match_list()
                self.validate_age_matches_list(start_age, end_age)
                self.compare_thresh_hold_value_with_score()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_age_range_and_thresh_hold_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_age_range_and_max_matches_thresh_hold_with_NATS_criteria(self):
        try:
            self.add_image_search()
            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)

            self.set_thresh_hold_slider()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)
            time.sleep(Base_Class.two_second)
            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            if self.check_if_match_is_found():
                self.verify_image_from_match_list()
                self.validate_age_matches_list(start_age, end_age)
                self.compare_thresh_hold_value_with_score()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_age_range_and_max_matches_thresh_hold_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_age_range_and_gender_with_NATS_criteria(self):
        try:
            self.add_image_search()
            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.nats_checkbox()

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()

            self.compare_thresh_hold_value_with_score()
            self.verify_gender_match_list(gender_data)
            self.validate_age_matches_list(start_age, end_age)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_age_range_and_gender_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_age_range_gender_and_max_matches_with_NATS_criteria(self):
        try:
            self.add_image_search()
            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.validate_age_matches_list(start_age, end_age)
            self.compare_thresh_hold_value_with_score()
            self.verify_gender_match_list(gender_data)
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_age_range_gender_and_max_matches_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_age_range_gender_and_thresh_hold_with_NATS_criteria(self):
        try:
            self.add_image_search()
            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.set_thresh_hold_slider()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.validate_age_matches_list(start_age, end_age)
            self.verify_gender_match_list(gender_data)
            self.compare_thresh_hold_value_with_score()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_age_range_gender_and_thresh_hold_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_age_range_gender_thresh_hold_and_max_matches_with_NATS_criteria(self):
        try:
            self.add_image_search()
            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.set_thresh_hold_slider()
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.validate_age_matches_list(start_age, end_age)
            self.verify_gender_match_list(gender_data)
            self.compare_thresh_hold_value_with_score()
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_age_range_gender_thresh_hold_and_max_matches_"
                    f"with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_and_region_with_NATS_criteria(self):
        try:
            self.add_image_search()

            region_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(region_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.verify_region_from_match_list(region_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_and_region_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_region_and_max_match_with_NATS_criteria(self):
        try:
            self.add_image_search()

            region_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(region_data)

            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()

            self.verify_region_from_match_list(region_data)
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_region_and_max_match_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_region_and_thresh_hold_with_NATS_criteria(self):
        try:
            self.add_image_search()

            region_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(region_data)
            self.set_thresh_hold_slider()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.verify_region_from_match_list(region_data)
            self.compare_thresh_hold_value_with_score()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_region_and_thresh_hold_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_region_thresh_hold_and_max_count_with_NATS_criteria(self):
        try:
            self.add_image_search()

            region_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(region_data)

            self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.compare_count_match(count_data)
            self.verify_image_from_match_list()

            self.verify_region_from_match_list(region_data)
            self.compare_thresh_hold_value_with_score()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_region_thresh_hold_and_max_count_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_region_and_gender_with_NATS_criteria(self):
        try:
            self.add_image_search()

            region_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(region_data)

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_gender_match_list(gender_data)
            self.verify_image_from_match_list()

            self.verify_region_from_match_list(region_data)
            self.compare_thresh_hold_value_with_score()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_region_and_gender_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_region_gender_and_max_count_with_NATS_criteria(self):
        try:
            self.add_image_search()

            region_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(region_data)

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)

            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_gender_match_list(gender_data)
            self.verify_image_from_match_list()

            self.verify_region_from_match_list(region_data)
            self.compare_thresh_hold_value_with_score()
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_region_gender_and_max_count_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_region_gender_and_thresh_hold_with_NATS_criteria(self):
        try:
            self.add_image_search()

            region_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(region_data)

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)

            self.set_thresh_hold_slider()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_gender_match_list(gender_data)
            self.verify_image_from_match_list()

            self.verify_region_from_match_list(region_data)
            self.compare_thresh_hold_value_with_score()
            self.compare_thresh_hold_value_with_score()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_region_gender_and_thresh_hold_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_region_gender_thresh_hold_and_max_count_with_NATS_criteria(self):
        try:
            self.add_image_search()

            region_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(region_data)

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)

            self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_gender_match_list(gender_data)
            self.verify_image_from_match_list()

            self.verify_region_from_match_list(region_data)
            self.compare_thresh_hold_value_with_score()
            self.compare_thresh_hold_value_with_score()
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_region_gender_thresh_hold_and_max_count"
                    f"_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_region_and_age_with_NATS_criteria(self):
        try:
            self.add_image_search()
            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)

            region_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(region_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.validate_age_matches_list(start_age, end_age)
            self.verify_region_from_match_list(region_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_region_and_age_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_region_age_and_max_matches_with_NATS_criteria(self):
        try:
            self.add_image_search()
            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)

            region_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(region_data)

            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.validate_age_matches_list(start_age, end_age)
            self.verify_region_from_match_list(region_data)
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_region_age_and_max_matches_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_region_age_and_thresh_hold_with_NATS_criteria(self):
        try:
            self.add_image_search()
            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)

            region_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(region_data)

            self.set_thresh_hold_slider()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.validate_age_matches_list(start_age, end_age)
            self.verify_region_from_match_list(region_data)
            self.compare_thresh_hold_value_with_score()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_region_age_and_thresh_hold_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_region_age_thresh_hold_and_max_matches_with_NATS_criteria(self):
        try:
            self.add_image_search()
            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)

            region_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(region_data)

            self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.validate_age_matches_list(start_age, end_age)
            self.verify_region_from_match_list(region_data)
            self.compare_thresh_hold_value_with_score()
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_region_age_thresh_hold_and_max_matches_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_region_age_and_gender_with_NATS_criteria(self):
        try:
            self.add_image_search()
            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)

            region_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(region_data)

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.validate_age_matches_list(start_age, end_age)
            self.verify_region_from_match_list(region_data)
            self.verify_gender_match_list(gender_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_region_age_and_gender_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_region_age_gender_and_max_match_with_NATS_criteria(self):
        try:
            self.add_image_search()
            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)

            region_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(region_data)

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)

            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.validate_age_matches_list(start_age, end_age)
            self.verify_region_from_match_list(region_data)
            self.verify_gender_match_list(gender_data)
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_region_age_gender_and_max_match_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_region_age_gender_and_thresh_hold_with_NATS_criteria(self):
        try:
            self.add_image_search()
            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)

            region_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(region_data)

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)

            self.set_thresh_hold_slider()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.validate_age_matches_list(start_age, end_age)
            self.verify_region_from_match_list(region_data)
            self.verify_gender_match_list(gender_data)
            self.compare_thresh_hold_value_with_score()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_region_age_gender_and_thresh_hold_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_region_age_gender_thresh_hold_and_max_match_with_NATS_criteria(self):
        try:
            self.add_image_search()
            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)

            region_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(region_data)

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)

            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)

            self.set_thresh_hold_slider()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.validate_age_matches_list(start_age, end_age)
            self.verify_region_from_match_list(region_data)
            self.verify_gender_match_list(gender_data)
            self.compare_thresh_hold_value_with_score()
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_region_age_gender_thresh_hold_and"
                    f"_max_match_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_and_date_range_with_NATS_criteria(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            print("0")
            self.verify_image_from_match_list()
            print("1")
            self.verify_date(date, month, year, hour, minute, period)
            print("2")
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            print("3")
            self.verify_date_range(year, e_year)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_and_date_range_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_date_range_and_max_count_with_NATS_criteria(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_and_max_count_criteria_failed.png")
                return False

    def visitor_search_with_image_date_range_and_thresh_hold_with_NATS_criteria(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            self.set_thresh_hold_slider()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.compare_thresh_hold_value_with_score()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_and_thresh_hold_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_date_range_thresh_hold_and_max_matches_with_NATS_criteria(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            self.set_thresh_hold_slider()
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.compare_thresh_hold_value_with_score()
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_thresh_hold_and_max_matches_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_date_range_and_gender_with_NATS_criteria(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_gender_match_list(gender_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_and_gender_with_NATS_criteria_failed.png")
                return False

    def visitor_search_with_image_date_range_gender_criteria_and_max_matches_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_gender_match_list(gender_data)
            self.compare_count_match(count_data)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_gender_criteria_and_max_matches_with_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_gender_criteria_and_threshold_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.set_thresh_hold_slider()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_gender_match_list(gender_data)
            self.compare_thresh_hold_value_with_score()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_gender_criteria_and_threshold_with_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_gender_criteria_threshold_and_max_match_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.set_thresh_hold_slider()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_gender_match_list(gender_data)
            self.compare_thresh_hold_value_with_score()
            self.compare_count_match(count_data)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_gender_criteria_threshold_"
                    f"and_max_match_with_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_and_age_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.validate_age_matches_list(start_age, end_age)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_and_age_with_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_age_and_max_matches_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.validate_age_matches_list(start_age, end_age)
            self.verify_image_from_match_list()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.compare_count_match(count_data)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_age_and_max_matches_with_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_age_and_threshold_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            self.set_thresh_hold_slider()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.validate_age_matches_list(start_age, end_age)
            self.verify_image_from_match_list()
            self.compare_thresh_hold_value_with_score()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_age_and_threshold_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_age_threshold_and_max_matches_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            self.set_thresh_hold_slider()
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)
            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.validate_age_matches_list(start_age, end_age)
            self.verify_image_from_match_list()
            self.compare_thresh_hold_value_with_score()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.compare_count_match(count_data)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_age_threshold_and_max_matches_with_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_age_and_gender_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.validate_age_matches_list(start_age, end_age)
            self.verify_image_from_match_list()
            self.compare_thresh_hold_value_with_score()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_gender_match_list(gender_data)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_age_and_gender_with_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_age_gender_and_max_matches_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.validate_age_matches_list(start_age, end_age)
            self.verify_image_from_match_list()
            self.compare_thresh_hold_value_with_score()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_gender_match_list(gender_data)
            self.compare_count_match(count_data)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_age_gender_and_max_matches_with_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_age_gender_and_threshold_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.set_thresh_hold_slider()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.validate_age_matches_list(start_age, end_age)
            self.verify_image_from_match_list()
            self.compare_thresh_hold_value_with_score()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_gender_match_list(gender_data)
            self.compare_thresh_hold_value_with_score()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_age_gender_and_threshold_with_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_age_gender_threshold_and_max_matches_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.set_thresh_hold_slider()
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.validate_age_matches_list(start_age, end_age)
            self.verify_image_from_match_list()
            self.compare_thresh_hold_value_with_score()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_gender_match_list(gender_data)
            self.compare_thresh_hold_value_with_score()
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_age_gender_threshold_and_max_matches_with_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_and_region_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.compare_thresh_hold_value_with_score()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_region_from_match_list(zone_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_and_region_with_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_region_and_max_matches_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.compare_thresh_hold_value_with_score()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_region_from_match_list(zone_data)
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_region_and_max_matches_with_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_region_and_threshold_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.set_thresh_hold_slider()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.compare_thresh_hold_value_with_score()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_region_from_match_list(zone_data)
            self.compare_thresh_hold_value_with_score()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_region_and_threshold_with_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_region_threshold_and_max_matches_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.set_thresh_hold_slider()
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.compare_thresh_hold_value_with_score()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_region_from_match_list(zone_data)
            self.compare_thresh_hold_value_with_score()
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_region_threshold_and_max_matches_with_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_region_and_gender_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.compare_thresh_hold_value_with_score()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_region_from_match_list(zone_data)
            self.verify_gender_match_list(gender_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_region_and_gender_with_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_region_gender_and_max_matches_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.compare_thresh_hold_value_with_score()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_region_from_match_list(zone_data)
            self.verify_gender_match_list(gender_data)
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_region_gender_and_max_matches_with_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_region_gender_and_threshold_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.set_thresh_hold_slider()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.compare_thresh_hold_value_with_score()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_region_from_match_list(zone_data)
            self.verify_gender_match_list(gender_data)
            self.compare_thresh_hold_value_with_score()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_region_gender_and_threshold_with_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_region_gender_threshold_and_max_matches_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.set_thresh_hold_slider()
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.compare_thresh_hold_value_with_score()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_region_from_match_list(zone_data)
            self.verify_gender_match_list(gender_data)
            self.compare_thresh_hold_value_with_score()
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_region_gender"
                    f"_threshold_and_max_matches_with_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_region_and_age_criteria_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_region_from_match_list(zone_data)
            self.validate_age_matches_list(start_age, end_age)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_region_and_age_criteria_with_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_region_age_and_max_count_criteria_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_region_from_match_list(zone_data)
            self.validate_age_matches_list(start_age, end_age)
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_region_age_and_max_count_criteria_with_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_region_age_and_thresh_hold_criteria_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.set_thresh_hold_slider()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_region_from_match_list(zone_data)
            self.validate_age_matches_list(start_age, end_age)
            self.compare_thresh_hold_value_with_score()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_region_age_and_thresh_hold_criteria_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_region_age_thresh_hold_and_max_matches_criteria_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.set_thresh_hold_slider()
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_region_from_match_list(zone_data)
            self.validate_age_matches_list(start_age, end_age)
            self.compare_thresh_hold_value_with_score()
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_region_age_thresh_hold_"
                    f"and_max_matches_criteria_with_NATS_failed.png"
                )
                return False

    def visitor_search_with_image_date_range_region_age_and_gender_criteria_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_region_from_match_list(zone_data)
            self.validate_age_matches_list(start_age, end_age)
            self.verify_gender_match_list(gender_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_region_age_and_gender_criteria_with_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_region_age_gender_and_max_matches_criteria_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_region_from_match_list(zone_data)
            self.validate_age_matches_list(start_age, end_age)
            self.verify_gender_match_list(gender_data)
            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_region_age_gender_and"
                    f"_max_matches_criteria_with_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_region_age_gender_and_thresh_hold_criteria_with_NATS(self):
        try:
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.set_thresh_hold_slider()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)
            self.verify_region_from_match_list(zone_data)
            self.validate_age_matches_list(start_age, end_age)
            self.verify_gender_match_list(gender_data)
            self.compare_thresh_hold_value_with_score()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_region_age_gender_and_thresh"
                    f"_hold_criteria_with_NATS_failed.png")
                return False

    def visitor_search_with_image_date_range_region_age_gender_thresh_hold_and_max_matches_criteria_with_NATS(self):
        try:
            self.add_image_search()
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
            time.sleep(Base_Class.two_second)
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.set_thresh_hold_slider()
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()
            time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_image_from_match_list()
            print("1")
            self.verify_date(date, month, year, hour, minute, period)
            print("1")
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            print("2")
            self.verify_date_range(year, e_year)
            print("3")
            self.verify_region_from_match_list(zone_data)
            print("4")
            self.validate_age_matches_list(start_age, end_age)
            print("5")
            self.verify_gender_match_list(gender_data)
            print("6")
            self.compare_thresh_hold_value_with_score()
            print("7")
            self.compare_count_match(count_data)
            print("8")

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\visitor_search_with_image_date_range_region_age_gender_"
                    f"thresh_hold_and_max_matches_criteria_with_NATS_failed.png")
                return False

    def Visitor_search_with_no_image_and_should_not_display_Max_of_Matches_with_NATS(self):
        try:
            self.login_before()
            self.nats_checkbox()

            self.verify_max_matches_not_display()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\Visitor_search_with_no_image_and_should_not_display_Max_of_Matches_with_NATS_failed.png")
                return False

    def Visitor_search_with_no_image_and_should_not_display_Threshold_with_NATS(self):
        try:
            self.login_before()
            self.nats_checkbox()

            self.verify_threshold_not_display()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\Visitor_search_with_no_image_and_should_not_display_Threshold_with_NATS_failed.png")
                return False

    def Visitor_search_with_no_image_and_should_not_display_Threshold_max_matches_with_NATS(self):
        try:
            self.login_before()
            self.nats_checkbox()

            self.verify_max_matches_not_display()
            self.verify_threshold_not_display()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\Visitor_search_with_no_image_and_should_not_display_Threshold_max_matches_with_NATS_failed.png")
                return False

    def Visitor_search_with_no_image_and_Max_of_Matches_not_display_and_region_criteria_with_NATS(self):
        try:
            self.login_before()
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.verify_max_matches_not_display()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_Must_specify_start_and_end_date_for_meta_data_only_search()
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
                    f"\\Visitor_search_with_no_image_and_Max_of_Matches_not_display"
                    f"7_and_region_criteria_with_NATS_failed.png")
                return False

    def Visitor_search_with_no_image_and_threshold_not_display_and_region_criteria_with_NATS(self):
        try:
            self.login_before()
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.verify_threshold_not_display()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_Must_specify_start_and_end_date_for_meta_data_only_search()
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
                    f"\\Visitor_search_with_no_image_and_threshold_"
                    f"not_display_and_region_criteria_with_NATS_failed.png")
                return False

    def Visitor_search_with_no_image_and_threshold_max_matches_not_display_and_region_criteria_with_NATS(self):
        try:
            self.login_before()
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.verify_threshold_not_display()
            self.verify_max_matches_not_display()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_Must_specify_start_and_end_date_for_meta_data_only_search()
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
                    f"\\Visitor_search_with_no_image_and_threshold_max_matches_"
                    f"not_display_and_region_criteria_with_NATS_failed.png")
                return False

    def Visitor_search_with_no_image_and_Max_of_Matches_not_display_and_date_criteria_with_NATS(self):
        try:
            self.login_before()
            date = int(Read_Visitor_Search_Components().meta_data_start_date())
            month = str(Read_Visitor_Search_Components().meta_data_start_month())
            year = int(Read_Visitor_Search_Components().meta_data_start_year())
            hour = str(Read_Visitor_Search_Components().meta_data_start_hour())
            minute = Read_Visitor_Search_Components().meta_data_start_minuet()
            period = str(Read_Visitor_Search_Components().meta_data_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().meta_data_end_month())
            e_date = int(Read_Visitor_Search_Components().meta_data_end_date())
            e_year = int(Read_Visitor_Search_Components().meta_data_end_year())
            e_hour = str(Read_Visitor_Search_Components().meta_data_end_hour())
            e_minute = Read_Visitor_Search_Components().meta_data_end_minuet()
            e_period = str(Read_Visitor_Search_Components().meta_data_end_am_pm_period())
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)
            self.verify_max_matches_not_display()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)
            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\Visitor_search_with_no_image_and_Max_of_Matches_not"
                    f"_display_and_date_criteria_with_NATS_failed.png")
                return False

    def Visitor_search_with_no_image_and_threshold_not_display_and_date_criteria_with_NATS(self):
        try:
            self.login_before()
            date = int(Read_Visitor_Search_Components().meta_data_start_date())
            month = str(Read_Visitor_Search_Components().meta_data_start_month())
            year = int(Read_Visitor_Search_Components().meta_data_start_year())
            hour = str(Read_Visitor_Search_Components().meta_data_start_hour())
            minute = Read_Visitor_Search_Components().meta_data_start_minuet()
            period = str(Read_Visitor_Search_Components().meta_data_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().meta_data_end_month())
            e_date = int(Read_Visitor_Search_Components().meta_data_end_date())
            e_year = int(Read_Visitor_Search_Components().meta_data_end_year())
            e_hour = str(Read_Visitor_Search_Components().meta_data_end_hour())
            e_minute = Read_Visitor_Search_Components().meta_data_end_minuet()
            e_period = str(Read_Visitor_Search_Components().meta_data_end_am_pm_period())
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)
            self.verify_threshold_not_display()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)
            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\Visitor_search_with_no_image_and_threshold_not_display_and_date_criteria_with_NATS_failed.png")
                return False

    def Visitor_search_with_no_image_and_max_matches_threshold_not_display_and_date_criteria_with_NATS(self):
        try:
            self.login_before()
            date = int(Read_Visitor_Search_Components().meta_data_start_date())
            month = str(Read_Visitor_Search_Components().meta_data_start_month())
            year = int(Read_Visitor_Search_Components().meta_data_start_year())
            hour = str(Read_Visitor_Search_Components().meta_data_start_hour())
            minute = Read_Visitor_Search_Components().meta_data_start_minuet()
            period = str(Read_Visitor_Search_Components().meta_data_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().meta_data_end_month())
            e_date = int(Read_Visitor_Search_Components().meta_data_end_date())
            e_year = int(Read_Visitor_Search_Components().meta_data_end_year())
            e_hour = str(Read_Visitor_Search_Components().meta_data_end_hour())
            e_minute = Read_Visitor_Search_Components().meta_data_end_minuet()
            e_period = str(Read_Visitor_Search_Components().meta_data_end_am_pm_period())
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)
            self.verify_max_matches_not_display()
            self.verify_threshold_not_display()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)
            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\Visitor_search_with_no_image_and_max_matches_threshold_"
                    f"not_display_and_date_criteria_with_NATS_failed.png")
                return False

    def Visitor_search_with_no_image_and_max_matches_not_display_and_date_and_region_criteria_with_NATS(self):
        try:
            self.login_before()
            date = int(Read_Visitor_Search_Components().meta_data_start_date())
            month = str(Read_Visitor_Search_Components().meta_data_start_month())
            year = int(Read_Visitor_Search_Components().meta_data_start_year())
            hour = str(Read_Visitor_Search_Components().meta_data_start_hour())
            minute = Read_Visitor_Search_Components().meta_data_start_minuet()
            period = str(Read_Visitor_Search_Components().meta_data_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().meta_data_end_month())
            e_date = int(Read_Visitor_Search_Components().meta_data_end_date())
            e_year = int(Read_Visitor_Search_Components().meta_data_end_year())
            e_hour = str(Read_Visitor_Search_Components().meta_data_end_hour())
            e_minute = Read_Visitor_Search_Components().meta_data_end_minuet()
            e_period = str(Read_Visitor_Search_Components().meta_data_end_am_pm_period())
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_Components().zone_data_input()
            time.sleep(Base_Class.two_second)
            self.select_zone(zone_data)
            self.verify_max_matches_not_display()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_region_from_match_list(zone_data)
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\Visitor_search_with_no_image_and_max_matches_not_display_"
                    f"and_date_and_region_criteria_with_NATS_failed.png")
                return False

    def Visitor_search_with_no_image_and_threshold_not_display_and_date_and_region_criteria_with_NATS(self):
        try:
            self.login_before()
            date = int(Read_Visitor_Search_Components().meta_data_start_date())
            month = str(Read_Visitor_Search_Components().meta_data_start_month())
            year = int(Read_Visitor_Search_Components().meta_data_start_year())
            hour = str(Read_Visitor_Search_Components().meta_data_start_hour())
            minute = Read_Visitor_Search_Components().meta_data_start_minuet()
            period = str(Read_Visitor_Search_Components().meta_data_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().meta_data_end_month())
            e_date = int(Read_Visitor_Search_Components().meta_data_end_date())
            e_year = int(Read_Visitor_Search_Components().meta_data_end_year())
            e_hour = str(Read_Visitor_Search_Components().meta_data_end_hour())
            e_minute = Read_Visitor_Search_Components().meta_data_end_minuet()
            e_period = str(Read_Visitor_Search_Components().meta_data_end_am_pm_period())
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_Components().zone_data_input()
            time.sleep(Base_Class.two_second)
            self.select_zone(zone_data)
            self.verify_threshold_not_display()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_region_from_match_list(zone_data)
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\Visitor_search_with_no_image_and_threshold_not_display_and"
                    f"_date_and_region_criteria_with_NATS_failed.png")
                return False

    def Visitor_search_with_no_image_and_max_matches_threshold_not_display_and_date_and_region_criteria_with_NATS(self):
        try:
            self.login_before()
            date = int(Read_Visitor_Search_Components().meta_data_start_date())
            month = str(Read_Visitor_Search_Components().meta_data_start_month())
            year = int(Read_Visitor_Search_Components().meta_data_start_year())
            hour = str(Read_Visitor_Search_Components().meta_data_start_hour())
            minute = Read_Visitor_Search_Components().meta_data_start_minuet()
            period = str(Read_Visitor_Search_Components().meta_data_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().meta_data_end_month())
            e_date = int(Read_Visitor_Search_Components().meta_data_end_date())
            e_year = int(Read_Visitor_Search_Components().meta_data_end_year())
            e_hour = str(Read_Visitor_Search_Components().meta_data_end_hour())
            e_minute = Read_Visitor_Search_Components().meta_data_end_minuet()
            e_period = str(Read_Visitor_Search_Components().meta_data_end_am_pm_period())
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_Components().zone_data_input()
            time.sleep(Base_Class.two_second)
            self.select_zone(zone_data)
            self.verify_max_matches_not_display()
            self.verify_threshold_not_display()
            self.nats_checkbox()
            time.sleep(Base_Class.two_second)

            self.click_on_submit_search_button()

            time.sleep(Base_Class.two_second)
            self.submitting_icon_wait()
            time.sleep(Base_Class.two_second)
            self.refresh_icon_wait()
            time.sleep(Base_Class.two_second)

            self.verify_region_from_match_list(zone_data)
            self.verify_date(date, month, year, hour, minute, period)
            self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period)
            self.verify_date_range(year, e_year)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\Visitor_search_with_no_image_and_max_matches_threshold_not"
                    f"_display_and_date_and_region_criteria_with_NATS_failed.png")
                return False

    ################################## Resused methods  ########################################

    def verify_image_from_match_list(self):
        time.sleep(Base_Class.two_second)
        ele = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().image_match_list_by_xpath())
        for e in ele:
            if not e.is_displayed():
                assert False

    def verify_region_from_match_list(self, zone_data):
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().search_constraints_by_xpath())
        ac_zone_txt = ele.text
        result = True
        if zone_data.upper() not in ac_zone_txt:
            result = False

        # lower result zone text validation code
        # match_region = self.d.find_elements(By.XPATH,
        #                                     Read_Visitor_Search_Components().match_region_by_xpath())
        #
        # for x in match_region:
        #     if x.text != zone_data:
        #         result = False
        #         break

        if result:
            assert True
        else:
            assert False

    def verify_date(self, date, month, year, hour, minute, period):
        month_to_mm = {
            "January": "JAN",
            "February": "FEB",
            "March": "MAR",
            "April": "APR",
            "May": "MAY",
            "June": "JUN",
            "July": "JUL",
            "August": "AUG",
            "September": "SEP",
            "October": "OCT",
            "November": "NOV",
            "December": "DEC"
        }
        mon = month_to_mm.get(month)

        exp_asser = "{mon} {date}, {year} {hour}:{minu} {pe}"
        exp_asser = exp_asser.format(mon=mon, date=date, year=year, hour=int(hour), minu=minute, pe=period)

        time.sleep(3)

        ac_start_date = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().actual_start_date_by_xpath())
        print(ac_start_date.text)
        print(exp_asser)
        ac_ass_date = ac_start_date.text
        if exp_asser in ac_ass_date:
            assert True
        else:
            assert False

    def close_all_the_panels(self):
        """
        This function is used to close all the visitor search panels
        :return:
        """
        close_icon = self.d.find_elements(By.XPATH,
                                          Read_Visitor_Search_Components().close_all_visitor_search_panel_by_xpath())
        for x in close_icon:
            x.click()

    def select_zone(self, zone):
        """
        This function is used to handle the zone drop-down and select the required options
        :param zone_data:
        :return:
        """
        zone_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().zone_by_xpath())
        zone_ele.click()
        time.sleep(Base_Class.two_second)
        zone_text_list = self.d.find_elements(By.XPATH,
                                              Read_Visitor_Search_Components().zone_text_list_xpath())
        expected_zone_text = zone.upper()
        try:
            for i in range(len(zone_text_list) + 1):
                actual_zone_text = zone_text_list.__getitem__(i).text
                # expected_zone_text = Read_Visitor_Search_Components().get_zone().upper()
                print(actual_zone_text)
                print(expected_zone_text)
                if expected_zone_text.upper() in actual_zone_text.upper():
                    zone_text_list.__getitem__(i).click()
                    break
            save = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().zone_save_button_xpath())
            self.d.execute_script("arguments[0].click();", save)
        except Exception as ex:
            str(ex)
        # zone_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().zone_by_xpath())
        # zone_ele.click()
        # time.sleep(Base_Class.two_second)
        # root_selection = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().root_selection_xpath())
        # assert root_selection.is_displayed()
        # self.d.execute_script("arguments[0].click();", root_selection)
        # save = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().zone_save_button_xpath())
        # self.d.execute_script("arguments[0].click();", save)

    def select_start_age(self, start_age):
        """
        This function is used to select the start age
        :param start_age:
        :return:
        """
        start_age_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().start_age_by_xpath())
        s = Select(start_age_ele)
        s.select_by_visible_text(start_age)

    def select_end_age(self, end_age):
        """
        This function is used to select the end age
        :param end_age:
        :return:
        """
        end_age_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().end_age_by_xpath())
        s = Select(end_age_ele)
        s.select_by_visible_text(end_age)

    def validate_age_matches_list(self, start_age, end_age):
        """
        This function is used to validate the age from the matches list
        :param start_age:
        :param end_age:
        :return:
        """
        result = True
        matches_list = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().matches_gender_by_xpath())
        if len(matches_list) <= 0:
            assert False
        for ele in matches_list:
            age = int(ele.text.split(" ")[1])
            if not int(start_age) <= age <= int(end_age):
                result = False
                break
        if result:
            assert True
        else:
            assert False

    def compare_thresh_hold_value_with_score(self):
        """
        This function is used to compare the threshhold value with actual score
        :return:
        """
        slider = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().slider_icon_by_xpath())
        slider_value_str = str(slider.get_attribute("style"))
        slider_value_text = slider_value_str.split(" ")[1].strip()
        slider_value_text = re.sub("[% ;]", "", slider_value_text)

        match_list_score = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().score_by_xpath())
        for ele in match_list_score:
            score = ele.text
            score = int(score.split(".")[1][0:2])
            if not score >= int(slider_value_text):
                assert False

    def set_thresh_hold_slider(self):
        """
        This function is used to set the threshold value
        :return:
        """
        slider_pixel = Read_Visitor_Search_Components().slider_value_data_input()
        slider_pixel_value = int(slider_pixel)

        slider = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().slider_icon_by_xpath())
        action = ActionChains(self.d)
        action.drag_and_drop_by_offset(slider, -80, 0).perform()
        time.sleep(2)
        action.drag_and_drop_by_offset(slider, slider_pixel_value, 0).perform()
        time.sleep(2)

    def select_count(self, count_data):
        """
        This function is used to select the count from the count dropdown
        :param count_data:
        :return:
        """
        max_match = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().max_of_matches_by_xpath())
        select = Select(max_match)

        select.select_by_visible_text(count_data)

    def click_on_submit_search_button(self):
        """
        This function is used to click on the submit search button
        :return:
        """
        submit_btn = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().submit_search_button_by_xpath())
        submit_btn.click()

    def verify_gender_match_list(self, expected_gender):
        """
        This function is used to the verify te gender with the actual match list
        :param expected_gender:
        :return:
        """
        match_gender_list = self.d.find_elements(By.XPATH,
                                                 Read_Visitor_Search_Components().matches_gender_by_xpath())
        for ele in match_gender_list:
            gender = ele.text
            if expected_gender.upper() not in gender:
                assert False

    def select_gender(self, gender_data):
        """
        This function helps us to select the gender dropdown
        :return:
        """
        gender_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().select_gender_by_xpath())

        s = Select(gender_ele)
        s.select_by_value(gender_data)

    def refresh_icon_wait(self):
        """
        This function is used to wait for a particular period of time until the match has been found
        :return:
        """
        refresh_icon = self.d.find_element(By.XPATH,
                                           Read_Visitor_Search_Components().refresh_icon_by_xpath())
        while refresh_icon.is_displayed():
            time.sleep(Base_Class.two_second)

        time.sleep(Base_Class.three_second)

    def submitting_icon_wait(self):
        """
        This function is used to wait for a particular period of time until the submitting is not complete
        :return:
        """
        submit_icon = self.d.find_element(By.XPATH,
                                          Read_Visitor_Search_Components().submitting_archive_search_wait_icon())
        while submit_icon.is_displayed():
            time.sleep(Base_Class.two_second)

        time.sleep(Base_Class.three_second)

    def add_image_search(self):
        """
        This function is usd to upload the image and click on the search button
        :return:
        """
        self.login_before()
        upload_photo = self.d.find_element(By.XPATH,
                                           Read_Visitor_Search_Components().photo_upload_container_by_xpath())
        upload_photo.click()
        time.sleep(2)
        print("file path =====>>>> ")
        # file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\img1.png"
        # file_path = f"{os.environ['WORKSPACE']}/Test_Data/img/img1.png"
        #file_path = Path(__file__).parent / "img1.png"
        script_directory = Path(__file__).parent
        file_path = script_directory / ".." / ".." / "Test_Data" / "img" / "img1.png"
        print("file path =====>>>> ",file_path)
        # file_path = 'C:\\Users\\baps\\Pictures\\uim.png'
        # file_path = 'D:\Chrome_Download\img1.png'
        time.sleep(2)
        pyautogui.write(str(file_path))
        # pyautogui.write(file_path)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.press('enter')

        # configure_search = self.d.find_element(By.XPATH,
        #                                        Read_Visitor_Search_Components().configure_search_by_xpath())
        # configure_search.click()
        # configure_search.click()

    def compare_count_match(self, count_data):
        """
        This function is used to compare the count provided with the actual no. of match count
        :param count_data:
        :return:
        """
        # match_found = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().matches_found_by_xpath())
        # match_found_count = int(match_found.text)

        match_found_list = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().matches_list_by_xpath())
        match_found_list_count = len(match_found_list)
        match int(count_data):
            case 1:
                assert match_found_list_count == 1

            case 5:
                if not 0 < match_found_list_count <= 5:
                    assert False
            case 10:
                if not 0 < match_found_list_count <= 10:
                    assert False

            case 15:
                if not 0 < match_found_list_count <= 15:
                    assert False

            case 20:
                if not 0 < match_found_list_count <= 20:
                    assert False

            case 25:
                if not 0 < match_found_list_count <= 25:
                    assert False

            case 30:
                if not 0 < match_found_list_count <= 30:
                    assert False

            case 35:
                if not 0 < match_found_list_count <= 35:
                    assert False

            case 40:
                if not 0 < match_found_list_count <= 40:
                    assert False

            case 45:
                if not 0 < match_found_list_count <= 45:
                    assert False

            case 50:
                if not 0 < match_found_list_count <= 50:
                    assert False

            case _:
                assert False

    def handle_calender_pop_up(self, strategy, date, month, year, hour, minute, req_period):

        # click on the form calendar popup
        if strategy == "from":
            start_check_bx = self.d.find_element(By.XPATH,
                                                 Read_Visitor_Search_Components().start_date_checkbox_by_xpath())
            start_check_bx.click()
            start_date_txt_bx = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().start_date_by_xpath())
            self.d.execute_script("arguments[0].scrollIntoView();", start_date_txt_bx)
            start_date_txt_bx.click()
        else:
            # click on the to calender pop up
            end_check_bx = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().end_date_checkbox_by_xpath())
            end_check_bx.click()
            end_date_txt_bx = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().end_date_by_xpath())
            self.d.execute_script("arguments[0].scrollIntoView();", end_date_txt_bx)
            end_date_txt_bx.click()

        # click on the clock icon
        calender_clock = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().calender_timer_icon_by_xpath())
        calender_clock.click()

        time.sleep(3)

        # handle the hour and minute based on the strategy
        if strategy == "from":
            self.calender_handle_hour_minute_from(hour, minute)
        else:
            self.calender_handle_hour_minute_to(hour, minute)

        # select the period am or pm
        period = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().period_by_xpath())
        if period.text == req_period:
            print("")
        else:
            period.click()

        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().calender_tick_icon_by_xpath())
        tick_icon.click()

        if strategy == "from":
            start_date_txt_bx = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().start_date_by_xpath())
            start_date_txt_bx.click()
        else:
            # click on the to calender pop up
            start_date_txt_bx = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().end_date_by_xpath())
            start_date_txt_bx.click()

        req_month = month
        req_year = year
        month_to_num = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }
        month_year = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().calender_month_year_by_xpath())
        ac_month = month_year.text.split(" ")[0]
        ac_year = int(month_year.text.split(" ")[1])

        # click on the back button
        while month_to_num.get(req_month) < month_to_num.get(ac_month) or req_year < ac_year:
            cal_back_button = self.d.find_element(By.XPATH,
                                                  Read_Visitor_Search_Components().calender_back_button_by_xpath())
            if cal_back_button.is_enabled():
                cal_back_button.click()
            time.sleep(1)
            month_year = self.d.find_element(By.XPATH,
                                             Read_Visitor_Search_Components().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])

        # click on the forward button
        while month_to_num.get(req_month) > month_to_num.get(ac_month) or req_year > ac_year:
            cal_back_button = self.d.find_element(By.XPATH,
                                                  Read_Visitor_Search_Components().calender_forward_button_by_xpath())
            if cal_back_button.is_enabled():
                cal_back_button.click()
            time.sleep(1)
            month_year = self.d.find_element(By.XPATH,
                                             Read_Visitor_Search_Components().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])

        # click on the required date
        date = self.d.find_element(By.XPATH,
                                   "(//td[@class='day' or @class='day weekend' or @class='day active' "
                                   "or @class='day active today'])[" + str(date) + "]")
        date.click()

        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().calender_tick_icon_by_xpath())
        time.sleep(2)
        tick_icon.click()
        # tick_icon.click()

    def calender_handle_hour_minute_to(self, hour, minute):
        # set the hour
        current_hour_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().current_hour_ele_by_xpath())
        cur_hour = int(current_hour_ele.text)

        while int(cur_hour) != int(hour):
            hour_down = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().hour_down_by_xpath())
            time.sleep(2)
            self.d.execute_script("arguments[0].click();", hour_down)
            current_hour_ele = self.d.find_element(By.XPATH,
                                                   Read_Visitor_Search_Components().current_hour_ele_by_xpath())
            cur_hour = int(current_hour_ele.text)
        time.sleep(2)

        # set the minute
        current_min_ele = self.d.find_element(By.XPATH,
                                              Read_Visitor_Search_Components().current_minute_element_by_xpath())
        cur_min = int(current_min_ele.text)
        while int(cur_min) != int(minute):
            clock_down_button = self.d.find_element(By.XPATH, Read_Visitor_Search_Components()
                                                    .clock_min_down_button_by_xpath())
            self.d.execute_script("arguments[0].click();", clock_down_button)
            current_min_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components()
                                                  .current_minute_element_by_xpath())
            cur_min = int(current_min_ele.text)

    def calender_handle_hour_minute_from(self, hour, minute):
        # set the hour
        current_hour_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().current_hour_ele_by_xpath())
        cur_hour = int(current_hour_ele.text)

        # decrementHours
        while int(cur_hour) != int(hour):
            hour_down = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().hour_down_by_xpath())
            self.d.execute_script("arguments[0].click();", hour_down)
            current_hour_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components()
                                                   .current_hour_ele_by_xpath())
            cur_hour = int(current_hour_ele.text)

        time.sleep(2)

        # set the minute
        current_min_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components()
                                              .current_minute_element_by_xpath())
        cur_min = int(current_min_ele.text)
        while int(cur_min) != int(minute):
            clock_up_button = self.d.find_element(By.XPATH, Read_Visitor_Search_Components()
                                                  .clock_min_up_button_by_xpath())
            self.d.execute_script("arguments[0].click();", clock_up_button)
            current_min_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components()
                                                  .current_minute_element_by_xpath())
            cur_min = int(current_min_ele.text)

    def verify_date_range(self, start_year, end_year):
        month_to_num = {
            "JAN": 1,
            "FEB": 2,
            "MAR": 3,
            "APR": 4,
            "MAY": 5,
            "JUN": 6,
            "JUL": 7,
            "AUG": 8,
            "SEP": 9,
            "OCT": 10,
            "NOV": 11,
            "DEC": 12
        }
        date_list = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().match_date_list_by_xpath())
        ac_date = int()
        ac_month = int()
        ac_year = int()
        for x in date_list:
            dt = x.text
            b = dt.split(" ")
            ac_year = int(b[2])

        if start_year <= ac_year <= end_year:
            assert True
        else:
            assert False

    def close_all_panel_one_by_one(self):
        try:
            time.sleep(Base_Class.two_second)
            close_panel_list = self.d.find_elements(By.XPATH,
                                                    Read_Visitor_Search_Components().close_all_panel_one_by_one())
            for i in close_panel_list:
                time.sleep(Base_Class.two_second)
                i.click()
                time.sleep(Base_Class.two_second)
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
            time.sleep(Base_Class.two_second)
            logout_button = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().logout_btn_by_xpath())
            while not logout_button.is_displayed():
                time.sleep(Base_Class.two_second)
            time.sleep(Base_Class.two_second)
            try:
                self.d.execute_script("arguments[0].click();", logout_button)
            except Exception as ex:
                logout_button.click()
            time.sleep(Base_Class.one_second)
            self.d.delete_cookie()
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_logout_pg_03.png")
                return False

    def check_if_match_is_found(self):
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().no_match_found_by_xpath())
        if ele.is_displayed():
            return False
        else:
            return True

    def verify_Must_specify_start_and_end_date_for_meta_data_only_search(self):
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().
                                  start_end_date_validation_msg_verify_xpath())
        actutal_validation_text = ele.text.lower()
        expected_validation_text = Read_Visitor_Search_Components().meta_data_without_date_validation_msg().strip(). \
            lower()
        print(actutal_validation_text)
        print(expected_validation_text)
        if ele.is_displayed() and actutal_validation_text == expected_validation_text:
            return True
        else:
            return False

    def verify_limited_to_30_min_interval_validation(self):
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().
                                  limited_to_30_min_interval_validation())
        actutal_validation_text = ele.text.lower()
        expected_validation_text = Read_Visitor_Search_Components().limited_to_30_meta_data_search_validation().strip(). \
            lower()
        print(actutal_validation_text)
        print(expected_validation_text)
        if ele.is_displayed() and actutal_validation_text == expected_validation_text:
            return True
        else:
            return False

    def nats_checkbox(self):
        """
        This function is used to enable and disable NATS
        :param end_age:
        :return:
        """
        NATS_checkbox = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().nats_checkbox_xpath())
        NATS_checkbox.click()

    def verify_max_matches_not_display(self):
        """
        This function is used validate the max matches element
        :return:
        """
        max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().max_of_matches_by_xpath())
        assert not max_matches.is_displayed()

    def verify_threshold_not_display(self):
        """
        This function is used validate the threshold element
        :return:
        """
        threshold = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().threshold_slider_by_xpath())
        assert not threshold.is_displayed()
