import time
from pathlib import Path

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from All_Test_Cases_Package.conftest import Base_Class
from Config_Package.INI_Config_Files.Notes_Search_Filter_Combination_Read_INI import \
    Read_notes_search_filter_combination
from Config_Package.INI_Config_Files.Portal_Menu_Read_INI import Read_Portal_Menu_Components
from Config_Package.INI_Config_Files.Visitor_search_Read_INI import Read_Visitor_Search_Components


class Notes_search_filter_combination_pom:

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
            notes = self.d.find_element(By.XPATH, Read_notes_search_filter_combination().notes_menu_button_by_xpath())
            notes.click()
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\login_failed_for_Notes_search_filter_combination_pom.png")
                return False

    def click_on_notes_search_button(self):
        time.sleep(Base_Class.one_second)
        search_button = self.d.find_element(By.XPATH,
                                            Read_notes_search_filter_combination().notes_search_button_by_xpath())
        time.sleep(Base_Class.one_second)
        search_button.click()
        time.sleep(Base_Class.one_second)

    def click_on_description_dropdown_option(self):
        description_option = self.d.find_element(By.XPATH,
                                                 Read_notes_search_filter_combination().
                                                 search_dropdown_description_option_by_xpath())
        time.sleep(Base_Class.one_second)
        description_option.click()
        time.sleep(Base_Class.one_second)

    def enter_location_or_store(self):
        location_or_store = self.d.find_element(By.XPATH,
                                                Read_notes_search_filter_combination().
                                                location_or_store_input_field_by_xpath())
        time.sleep(Base_Class.one_second)
        location_or_store.send_keys(Read_notes_search_filter_combination().get_location_or_store())
        time.sleep(Base_Class.one_second)

    def enter_case_or_subject(self):
        case_or_subject = self.d.find_element(By.XPATH,
                                              Read_notes_search_filter_combination().
                                              case_or_subject_input_field_by_xpath())
        time.sleep(Base_Class.one_second)
        case_or_subject.send_keys(Read_notes_search_filter_combination().get_case_or_subject())
        time.sleep(Base_Class.one_second)

    def click_on_filter_search_button(self):
        filter_search_button = self.d.find_element(By.XPATH,
                                                   Read_notes_search_filter_combination().
                                                   notes_filter_search_button_by_xpath())
        time.sleep(Base_Class.one_second)
        filter_search_button.click()
        time.sleep(Base_Class.one_second)

    def sort_by_case_or_subject(self):
        ele = self.d.find_element(By.XPATH, Read_notes_search_filter_combination().sort_by_dropdown_by_xpath())
        select = Select(ele)
        time.sleep(Base_Class.one_second)
        sort_by = Read_notes_search_filter_combination().get_sort_by_case_or_subject()
        time.sleep(Base_Class.one_second)
        select.select_by_visible_text(sort_by)
        time.sleep(Base_Class.one_second)

    def sort_by_location_or_store(self):
        time.sleep(Base_Class.one_second)
        ele = self.d.find_element(By.XPATH, Read_notes_search_filter_combination().sort_by_dropdown_by_xpath())
        time.sleep(Base_Class.one_second)
        select = Select(ele)
        time.sleep(Base_Class.one_second)
        sort_by = Read_notes_search_filter_combination().get_sort_by_location_or_store()
        time.sleep(Base_Class.one_second)
        select.select_by_visible_text(sort_by)
        time.sleep(Base_Class.one_second)

    def location_or_store_search_result_validation(self):
        result_validation = self.d.find_element(By.XPATH, Read_notes_search_filter_combination().
                                                location_or_store_search_result_validation_by_xpath())
        time.sleep(Base_Class.one_second)
        actual_text = result_validation.text.lower()
        time.sleep(Base_Class.one_second)
        expected_text = Read_notes_search_filter_combination().get_location_or_store().lower()
        time.sleep(Base_Class.one_second)
        assert expected_text in actual_text
        time.sleep(Base_Class.one_second)

    def case_or_subject_search_result_validation(self):
        result_validation = self.d.find_element(By.XPATH, Read_notes_search_filter_combination().
                                                case_or_subject_search_result_validation_by_xpath())
        time.sleep(Base_Class.one_second)
        actual_text = result_validation.text.lower()
        time.sleep(Base_Class.one_second)
        expected_text = Read_notes_search_filter_combination().get_case_or_subject().lower()
        time.sleep(Base_Class.one_second)
        assert expected_text in actual_text
        time.sleep(Base_Class.one_second)

    def sort_by_location_or_store_validation(self):
        result_validation = self.d.find_element(By.XPATH, Read_notes_search_filter_combination().
                                                sort_by_result_validation_by_xpath())
        time.sleep(Base_Class.one_second)
        actual_text = result_validation.text.lower()
        time.sleep(Base_Class.one_second)
        expected_text = Read_notes_search_filter_combination().get_sort_by_location_or_store().lower()
        time.sleep(Base_Class.one_second)
        assert expected_text in actual_text
        time.sleep(Base_Class.one_second)

    def sort_by_case_or_subject_validation(self):
        result_validation = self.d.find_element(By.XPATH, Read_notes_search_filter_combination().
                                                sort_by_result_validation_by_xpath())
        time.sleep(Base_Class.one_second)
        actual_text = result_validation.text.lower()
        time.sleep(Base_Class.one_second)
        expected_text = Read_notes_search_filter_combination().get_sort_by_case_or_subject().lower()
        time.sleep(Base_Class.one_second)
        assert expected_text in actual_text
        time.sleep(Base_Class.one_second)

        # close tab and logout method

    def close_all_panel_one_by_one(self):
        try:
            close_panel_list = self.d.find_elements(By.XPATH,
                                                    Read_Visitor_Search_Components().close_all_panel_one_by_one())
            time.sleep(Base_Class.one_second)
            for i in close_panel_list:
                i.click()
                time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\close_panel_failed_event_search_filter_combination.png")
                return False

    def click_on_logout_button(self):
        try:
            time.sleep(Base_Class.one_second)
            logout_button = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().logout_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            logout_button.click()
            self.d.refresh()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_logout_pg_03.png")
                return False

    ######################################### Business Methods #################################################

    def notes_with_no_filter_combination(self):
        try:
            self.login_before()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()
            time.sleep(Base_Class.one_second)

            self.click_on_filter_search_button()
            time.sleep(Base_Class.one_second)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            time.sleep(Base_Class.one_second)
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\notes_with_no_filter_combination_failed.png")
                return False

    def notes_with_sort_by_Case_Subject_filter_combination(self):
        try:
            self.login_before()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()
            time.sleep(Base_Class.one_second)

            self.sort_by_case_or_subject()
            time.sleep(Base_Class.one_second)

            self.click_on_filter_search_button()
            time.sleep(Base_Class.one_second)

            self.sort_by_case_or_subject_validation()
            time.sleep(Base_Class.one_second)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            time.sleep(Base_Class.one_second)
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\notes_with_sort_by_case_Subject_filter_combination_failed.png")
                return False

    def notes_with_sort_by_location_store_filter_combination(self):
        try:
            self.login_before()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()
            time.sleep(Base_Class.one_second)

            self.sort_by_location_or_store()
            time.sleep(Base_Class.one_second)

            self.click_on_filter_search_button()
            time.sleep(Base_Class.one_second)

            self.sort_by_location_or_store_validation()
            time.sleep(Base_Class.one_second)

            time.sleep(2)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            time.sleep(Base_Class.one_second)
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\notes_with_sort_by_location_store_filter_combination_failed.png")
                return False

    def notes_with_Sort_by_Location_Store_and_Sort_by_Case_Subject_filter_combination(self):
        try:
            self.notes_with_sort_by_Case_Subject_filter_combination()
            time.sleep(2)
            self.notes_with_sort_by_location_store_filter_combination()
            time.sleep(Base_Class.one_second)
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\notes_with_Sort_by_Location_Store_and_Sort_by_Case_Subject_filter_combination_failed.png")
                return False

    def notes_with_Case_Subject_filter_combination(self):
        try:
            time.sleep(Base_Class.one_second)
            self.login_before()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()
            time.sleep(Base_Class.one_second)

            self.enter_case_or_subject()
            time.sleep(Base_Class.one_second)

            self.click_on_filter_search_button()
            time.sleep(Base_Class.one_second)

            self.case_or_subject_search_result_validation()
            time.sleep(Base_Class.one_second)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            time.sleep(Base_Class.one_second)
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\notes_with_Case_Subject_filter_combination_failed.png")
                return False

    def notes_with_Case_Subject_and_Sort_by_Case_Subject_filter_combination(self):
        try:
            self.login_before()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()
            time.sleep(Base_Class.one_second)

            self.enter_case_or_subject()
            self.sort_by_case_or_subject()
            time.sleep(Base_Class.one_second)

            self.click_on_filter_search_button()
            time.sleep(Base_Class.one_second)

            self.case_or_subject_search_result_validation()
            self.sort_by_case_or_subject_validation()
            time.sleep(Base_Class.one_second)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            time.sleep(Base_Class.one_second)
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\notes_with_Case_Subject_and_Sort_by_Case_Subject_filter_combination_failed.png")
                return False

    def notes_with_filter_Case_Subject_and_Sort_by_Location_Store_combination(self):
        try:
            self.login_before()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()
            time.sleep(Base_Class.one_second)

            self.enter_case_or_subject()
            self.sort_by_location_or_store()
            time.sleep(Base_Class.one_second)

            self.click_on_filter_search_button()
            time.sleep(Base_Class.one_second)

            self.case_or_subject_search_result_validation()
            self.sort_by_location_or_store_validation()
            time.sleep(Base_Class.one_second)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            time.sleep(Base_Class.one_second)
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\notes_with_filter_Case_Subject_and_Sort_by_Location_Store_combination_failed.png")
                return False

    def notes_with_Case_Subject_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination(self):
        try:
            self.notes_with_Case_Subject_filter_combination()
            time.sleep(2)
            self.notes_with_sort_by_Case_Subject_filter_combination()
            time.sleep(2)
            self.notes_with_sort_by_location_store_filter_combination()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\notes_with_Case_Subject_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination_failed.png")
                return False

    def notes_with_Location_Store_filter_combination(self):
        try:
            self.login_before()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()
            time.sleep(Base_Class.one_second)

            self.enter_location_or_store()
            time.sleep(Base_Class.one_second)

            self.click_on_filter_search_button()
            time.sleep(Base_Class.one_second)

            self.location_or_store_search_result_validation()
            time.sleep(Base_Class.one_second)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            time.sleep(Base_Class.one_second)
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\notes_with_Location_Store_filter_combination_failed.png")
                return False

    def notes_with_Location_Store_and_Sort_by_Case_Subject_filter_combination(self):
        try:
            self.login_before()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()
            time.sleep(Base_Class.one_second)

            self.enter_location_or_store()
            self.sort_by_case_or_subject()
            time.sleep(Base_Class.one_second)

            self.click_on_filter_search_button()
            time.sleep(Base_Class.one_second)

            self.location_or_store_search_result_validation()
            self.sort_by_case_or_subject_validation()
            time.sleep(Base_Class.one_second)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            time.sleep(Base_Class.one_second)

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\notes_with_Location_Store_and_Sort_by_Case_Subject_filter_combination_failed.png")
                return False

    def notes_with_Location_Store_and_Sort_by_Location_Store_filter_combination(self):
        try:
            self.login_before()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()
            time.sleep(Base_Class.one_second)

            self.enter_location_or_store()
            self.sort_by_location_or_store()
            time.sleep(Base_Class.one_second)

            self.click_on_filter_search_button()
            time.sleep(Base_Class.one_second)

            self.location_or_store_search_result_validation()
            self.sort_by_location_or_store_validation()
            time.sleep(Base_Class.one_second)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            time.sleep(Base_Class.one_second)

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\notes_with_Location_Store_and_Sort_by_Location_Store_filter_combination_failed.png")
                return False

    def notes_with_Location_Store_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination(self):
        try:
            self.notes_with_Location_Store_filter_combination()
            time.sleep(2)
            self.notes_with_sort_by_location_store_filter_combination()
            time.sleep(2)
            self.notes_with_sort_by_Case_Subject_filter_combination()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\notes_with_Location_Store_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination_failed.png")
                return False

    def notes_with_Location_Store_and_Case_Subject_filter_combination(self):
        try:
            self.login_before()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()
            time.sleep(Base_Class.one_second)

            self.enter_location_or_store()
            self.enter_case_or_subject()
            time.sleep(Base_Class.one_second)

            self.click_on_filter_search_button()
            time.sleep(Base_Class.one_second)

            self.location_or_store_search_result_validation()
            self.case_or_subject_search_result_validation()
            time.sleep(Base_Class.one_second)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            time.sleep(Base_Class.one_second)

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\notes_with_Location_Store_and_Case_Subject_filter_combination_failed.png")
                return False

    def notes_with_Location_Store_Case_Subject_and_Sort_by_Case_Subject_filter_combination(self):
        try:
            self.login_before()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()
            time.sleep(Base_Class.one_second)

            self.enter_location_or_store()
            self.enter_case_or_subject()
            self.sort_by_case_or_subject()
            time.sleep(Base_Class.one_second)

            self.click_on_filter_search_button()
            time.sleep(Base_Class.one_second)

            self.location_or_store_search_result_validation()
            self.case_or_subject_search_result_validation()
            self.sort_by_case_or_subject_validation()
            time.sleep(Base_Class.one_second)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            time.sleep(Base_Class.one_second)

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\notes_with_Location_Store_Case_Subject_and_Sort_by_Case_Subject_filter_combination_failed.png")
                return False

    def notes_with_Location_Store_Case_Subject_and_Sort_by_Location_Store_filter_combination(self):
        try:
            self.login_before()
            self.click_on_notes_search_button()
            self.click_on_description_dropdown_option()
            time.sleep(Base_Class.one_second)

            self.enter_location_or_store()
            self.enter_case_or_subject()
            self.sort_by_location_or_store()
            time.sleep(Base_Class.one_second)

            self.click_on_filter_search_button()
            time.sleep(Base_Class.one_second)

            self.location_or_store_search_result_validation()
            self.case_or_subject_search_result_validation()
            self.sort_by_location_or_store_validation()
            time.sleep(Base_Class.one_second)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            time.sleep(Base_Class.one_second)

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\notes_with_Location_Store_Case_Subject_and_Sort_by_Location_Store_filter_combination_failed.png")
                return False

    def notes_with_Location_Store_Case_Subject_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination(self):
        try:
            self.notes_with_sort_by_Case_Subject_filter_combination()
            time.sleep(2)
            self.notes_with_sort_by_location_store_filter_combination()
            time.sleep(2)
            self.notes_with_sort_by_Case_Subject_filter_combination()
            time.sleep(2)
            self.notes_with_sort_by_location_store_filter_combination()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\notes_with_Location_Store_Case_Subject_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination_failed.png")
                return False