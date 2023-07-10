import time
from pathlib import Path

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from All_Test_Cases_Package.conftest import Base_Class
from Config_Package.INI_Config_Files.Enrollments_Read_INI import Read_Enrollments_Components
from Config_Package.INI_Config_Files.Portal_Menu_Read_INI import Read_Portal_Menu_Components


class Enrollments_Filter_combination_pom:
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
            self.click_on_enrollments_link()
            time.sleep(Base_Class.two_second)

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\login_failed_for_portal_menu_pg_03.png")
                return False

    def enrollments_search_with_no_filter_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            time.sleep(3)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
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

    def enrollments_search_with_sort_by_case_subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.verify_sort_key_case_subject()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollments_search_with_sort_by_case_subject_criteria_failed.png")
                return False

    def enrollments_search_with_sort_by_location_store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.verify_sort_key_location_store()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollments_search_with_sort_by_location_store_filter_combination_failed.png")
                return False

    def enrollments_search_with_Sort_by_Enrolled_On_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollments_search_with_Sort_by_Enrolled_On_filter_combination_failed.png")
                return False

    def enrollments_search_with_expiration_Date_Range_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_expiration_start_or_end_date_search_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollments_search_with_expiration_Date_Range_criteria_failed.png")
                return False

    def enrollments_search_with_expiration_Date_Range_and_sort_by_case_subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_expiration_start_or_end_date_search_result()
            self.verify_sort_key_case_subject()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollments_search_with_expiration_Date_Range_and_sort_by_case_subject_criteria_failed.png")
                return False

    def enrollments_search_with_expiration_date_range_and_sort_by_Location_store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_expiration_start_or_end_date_search_result()
            self.verify_sort_key_location_store()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollments_search_with_expiration_date_range_and_sort_by_Location_store_criteria_failed.png")
                return False

    def enrollments_search_with_expiration_date_range_and_sort_by_enrolled_On_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_expiration_start_or_end_date_search_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollments_search_with_expiration_date_range_and_sort_by_enrolled_On_criteria_failed.png")
                return False

    def enrollments_search_with_enrollment_Date_Range_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_enrolled_start_or_end_date_search_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollments_search_with_enrollment_Date_Range_criteria_failed.png")
                return False

    def enrollments_search_with_enrollment_Date_Range_and_Sort_by_Case_Subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_enrolled_start_or_end_date_search_result()
            self.verify_sort_key_case_subject()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollments_search_with_enrollment_Date_Range_and_Sort_by_Case_Subject_criteria_failed.png")
                return False

    def enrollments_search_with_enrollment_Date_Range_and_Sort_by_Location_Store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_enrolled_start_or_end_date_search_result()
            self.verify_sort_key_location_store()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollments_search_with_enrollment_Date_Range_and_Sort_by_Location_Store_criteria_failed.png")
                return False

    def enrollments_search_with_Enrollment_Date_Range_and_Sort_by_enrolledOn_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_enrolled_start_or_end_date_search_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollments_search_with_Enrollment_Date_Range_and_Sort_by_enrolledOn_criteria_failed.png")
                return False

    def enrollments_search_with_Enrollment_Date_Range_and_Expiration_Date_Range_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollments_search_with_Enrollment_Date_Range_and_Expiration_Date_Range_criteria_failed.png")
                return False

    def enrollments_search_with_Enrollment_Date_Range_Expiration_Date_Range_and_Sort_by_Case_Subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.verify_sort_key_case_subject()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollments_search_with_Enrollment_Date_Range_Expiration_Date_Range_and_Sort_by_Case_Subject_criteria_failed.png")
                return False

    def enrollments_search_with_Enrollment_Date_Range_Expiration_Date_Range_and_Sort_by_Location_Store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.verify_sort_key_location_store()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollments_search_with_Enrollment_Date_Range_Expiration_"
                    f"Date_Range_and_Sort_by_Location_Store_criteria_failed.png")
                return False

    def enrollments_search_with_Enrollment_Date_Range_Expiration_Date_Range_and_Sort_by_EnrolledOn_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollments_search_with_Enrollment_Date_Range_Expiration"
                    f"_Date_Range_and_Sort_by_EnrolledOn_criteria_failed.png")
                return False

    def enrollments_search_with_Exact_Text_Search_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.click_on_exact_text_search_checkBox()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_Exact_Text_Search_criteria_failed.png")
                return False

    def enrollments_search_with_Exact_Text_Search_and_sort_by_case_subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.click_on_exact_text_search_checkBox()
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.verify_sort_key_case_subject()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_Exact_Text_Search_and_sort_by_case_subject_criteria_failed.png")
                return False

    def enrollments_search_with_Exact_Text_Search_and_Sort_by_Location_Store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.click_on_exact_text_search_checkBox()
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.verify_sort_key_location_store()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_Exact_Text_Search_and_Sort_by_Location_Store_criteria_failed.png")
                return False

    def enrollments_search_with_exact_text_search_and_sort_by_enrolledOn_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.click_on_exact_text_search_checkBox()
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_exact_text_search_and_sort_by_enrolledOn_criteria_failed.png")
                return False

    def enrollments_search_with_exact_text_search_and_expiration_date_range_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_expiration_start_or_end_date_search_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_exact_text_search_and_expiration_date_range_criteria_failed.png")
                return False

    def enrollments_search_with_exact_text_search_expiration_date_range_and_sort_by_case_subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_expiration_start_or_end_date_search_result()
            self.verify_sort_key_case_subject()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_exact_text_search_and_expiration_date_range_criteria_failed.png")
                return False

    def enrollments_search_with_exact_text_search_expiration_date_range_and_sort_by_location_store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_expiration_start_or_end_date_search_result()
            self.verify_sort_key_location_store()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_exact_text_search_expiration_"
                    f"date_range_and_sort_by_location_store_criteria_failed.png")
                return False

    def enrollments_search_with_exact_text_search_expiration_date_range_and_Sort_by_EnrolledOn_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_expiration_start_or_end_date_search_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_exact_text_search_expiration_date_range_"
                    f"and_Sort_by_EnrolledOn_criteria_failed.png")
                return False

    def enrollments_search_with_exact_text_search_and_enrollment_date_range_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_enrolled_start_or_end_date_search_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_exact_text_search_and_enrollment_date_range_criteria_failed.png")
                return False

    def enrollments_search_with_exact_text_search_enrollment_date_range_and_sort_by_case_subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_enrolled_start_or_end_date_search_result()
            self.verify_sort_key_case_subject()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_exact_text_search_enrollment_date_range_and_"
                    f"sort_by_case_subject_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_enrollment_date_range_and_expiration_date_range_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.validate_location_store_search_criteria_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_enrollment_date_range_and_"
                    f"expiration_date_range_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_enrollment_date_range_and_expiration_date_range_and_sort_by_case_subject_criteria(
            self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.validate_location_store_search_criteria_result()
            self.verify_sort_key_case_subject()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_enrollment_date_range_and_expiration_date_"
                    f"range_and_sort_by_case_subject_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_enrollment_date_range_and_expiration_date_range_and_sort_by_location_store_criteria(
            self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.validate_location_store_search_criteria_result()
            self.verify_sort_key_location_store()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_enrollment_date_range_and_expiration_date_range_"
                    f"and_sort_by_location_store_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_enrollment_date_range_and_expiration_date_range_and_sort_by_enrolledOn_criteria(
            self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.validate_location_store_search_criteria_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_enrollment_date_range_and_"
                    f"expiration_date_range_and_sort_by_enrolledOn_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_and_exact_text_search_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_and_exact_text_search_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_and_exact_text_search_and_sort_by_case_subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.verify_sort_key_case_subject()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_and_exact_text_search_and_"
                    f"sort_by_case_subject_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_and_exact_text_search_and_sort_by_location_store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.verify_sort_key_location_store()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_and_exact_text_search_and_"
                    f"sort_by_location_store_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_and_exact_text_search_and_sort_by_enrolledOn_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_and_exact_text_search_and_sort_by_"
                    f"enrolledOn_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_exact_text_search_and_expiration_date_range_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_exact_text_search_and_expiration_"
                    f"date_range_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_exact_text_search_expiration_date_range_and_sort_by_case_subject_criteria(
            self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.verify_sort_key_case_subject()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_exact_text_search_expiration_date_range_and_"
                    f"sort_by_case_subject_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_exact_text_search_expiration_date_range_and_sort_by_location_store_criteria(
            self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.verify_sort_key_location_store()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_exact_text_search_expiration_date_range_"
                    f"and_sort_by_location_store_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_exact_text_search_expiration_date_range_and_sort_by_enrolledOn_criteria(
            self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_exact_text_search_expiration_date_range_and_"
                    f"sort_by_enrolledOn_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_exact_text_search_and_enrollment_date_range_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_exact_text_search_and_"
                    f"enrollment_date_range_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_exact_text_search_enrollment_date_range_and_sort_by_case_subject_criteria(
            self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.verify_sort_key_case_subject()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_exact_text_search_enrollment_date_"
                    f"range_and_sort_by_case_subject_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_exact_text_search_enrollment_date_range_and_sort_by_location_store_criteria(
            self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.verify_sort_key_location_store()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_exact_text_search_enrollment_date_"
                    f"range_and_sort_by_location_store_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_exact_text_search_enrollment_date_range_and_sort_by_enrolledOn_criteria(
            self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_exact_text_search_enrollment_date_range_and_"
                    f"sort_by_enrolledOn_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_exact_text_search_enrollment_date_range_and_expiration_date_range_criteria(
            self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_exact_text_search_enrollment_date_range_and_"
                    f"expiration_date_range_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_exact_text_search_enrollment_date_range_expiration_date_range_and_sort_by_case_subject_criteria(
            self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.verify_sort_key_case_subject()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_exact_text_search_enrollment_date_range_"
                    f"expiration_date_range_and_sort_by_case_subject_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_exact_text_search_enrollment_date_range_expiration_date_range_and_sort_by_location_store_criteria(
            self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.verify_sort_key_location_store()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_exact_text_search_enrollment_date_range_"
                    f"expiration_date_range_and_sort_by_location_store_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_exact_text_search_enrollment_date_range_expiration_date_range_and_sort_by_enrolledOn_criteria(
            self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_exact_text_search_enrollment_date_range_"
                    f"expiration_date_range_and_sort_by_enrolledOn_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_and_case_subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_and_case_subject_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_case_subject_and_sort_by_case_subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.verify_sort_key_case_subject()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_case_subject_and_sort_by_case_subject_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_case_subject_and_sort_by_location_store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.verify_sort_key_location_store()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_case_subject_and_sort_by_location_store_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_case_subject_and_sort_by_enrolledOn_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_case_subject_and_sort_by_enrolledOn_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_case_subject_and_expiration_date_range_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_case_subject_and_expiration_"
                    f"date_range_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_case_subject_expiration_date_range_sort_by_case_subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.verify_sort_key_case_subject()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_case_subject_expiration_date_range_sort_"
                    f"by_case_subject_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_case_subject_expiration_date_range_sort_by_location_store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.verify_sort_key_location_store()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_case_subject_expiration_date_range_sort_"
                    f"by_location_store_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_case_subject_expiration_date_range_sort_by_enrolledOn_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_case_subject_expiration_date_range_"
                    f"sort_by_enrolledOn_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_case_subject_Enrollment_date_range_criteria_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_case_subject_Enrollment_date_range_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_case_subject_Enrollment_date_range_sort_by_case_subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.verify_sort_key_case_subject()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_case_subject_Enrollment_date_range_"
                    f"sort_by_case_subject_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_case_subject_Enrollment_date_range_sort_by_location_store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.verify_sort_key_location_store()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_case_subject_Enrollment_date_range_"
                    f"sort_by_location_store_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_case_subject_Enrollment_date_range_sort_by_enrolledOn_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_case_subject_Enrollment_date_range_"
                    f"sort_by_enrolledOn_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_case_subject_EnrollmentDateRange_expiration_date_range_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_case_subject_EnrollmentDateRange_"
                    f"expiration_date_range_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_case_subject_EnrollmentDateRange_expiration_date_range_sort_by_case_subject_criteria(
            self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.verify_sort_key_case_subject()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_case_subject_EnrollmentDateRange_expiration_"
                    f"date_range_sort_by_case_subject_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_case_subject_EnrollmentDateRange_expiration_date_range_sort_by_location_store_criteria(
            self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.verify_sort_key_location_store()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_case_subject_EnrollmentDateRange_expiration_date_range_"
                    f"sort_by_location_store_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_case_subject_EnrollmentDateRange_expiration_date_range_sort_by_enrolledOn_criteria(
            self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_case_subject_EnrollmentDateRange_expiration_date_range_"
                    f"sort_by_enrolledOn_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_case_subject_exact_text_search_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_case_subject_exact_text_search_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_case_subject_exact_text_search_sort_by_case_subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.verify_sort_key_case_subject()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_case_subject_exact_text_search_sort_by_"
                    f"case_subject_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_case_subject_exact_text_search_sort_by_location_store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.verify_sort_key_location_store()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_case_subject_exact_text_search_sort_by_location"
                    f"_store_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_case_subject_exact_text_search_sort_by_enrolledOn_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_case_subject_exact_text_search_sort"
                    f"_by_enrolledOn_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_case_subject_exact_text_search_expiration_date_range_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_case_subject_exact_text_search_expiration_"
                    f"date_range_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_case_subject_exact_text_search_expiration_date_range_sort_by_case_subject_criteria(
            self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.verify_sort_key_case_subject()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_case_subject_exact_text_search_expiration_date_range_"
                    f"sort_by_case_subject_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_case_subject_exact_text_search_expiration_date_range_sort_by_location_store_criteria(
            self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.verify_sort_key_location_store()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_case_subject_exact_text_search_expiration_date_range_"
                    f"sort_by_location_store_criteria_failed.png")
                return False

    def enrollments_search_with_location_store_case_subject_exact_text_search_expiration_date_range_sort_by_enrolledOn_criteria(
            self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)

            if self.verify_if_match_found():
                self.validate_match_list_output(4)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"enrollments_search_with_location_store_case_subject_exact_text_search_expiration_date_"
                    f"range_sort_by_enrolledOn_criteria_failed.png")
                return False

    def enrollment_search_with_exact_text_enrollment_date_range_and_sort_by_location_store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")

            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)
            self.validate_enrolled_start_or_end_date_search_result()
            self.verify_sort_key_location_store()
            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_exact_text_enrollment_date_range_"
                    f"and_sort_by_location_store_criteria_failed.png")
                return False

    def enrollment_search_with_exact_text_enrollment_date_range_and_sort_by_enrolled_on_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")

            self.select_sort_by_enrolled_on()
            self.click_on_search_button()
            time.sleep(Base_Class.three_second)
            self.validate_enrolled_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_exact_text_enrollment_date_range_and"
                    f"_sort_by_enrolled_on_criteria_failed.png")
                return False

    def enrollment_search_with_exact_text_enrollment_date_and_expiration_date_range_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_exact_text_enrollment_date_and"
                    f"_expiration_date_range_criteria_failed.png")
                return False

    def enrollment_search_with_exact_text_enrollment_expiration_date_range_and_sort_by_case_subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(Base_Class.three_second)
            self.verify_sort_key_case_subject()
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_exact_text_enrollment_expiration_date_range_"
                    f"and_sort_by_case_subject_criteria_failed.png")
                return False

    def enrollment_search_with_exact_text_enrollment_expiration_date_range_and_sort_by_location_store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)
            self.verify_sort_key_location_store()
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_exact_text_enrollment_expiration_date_range_"
                    f"and_sort_by_location_store_criteria_failed.png")
                return False

    def enrollment_search_with_exact_text_enrollment_expiration_date_range_and_sort_by_enrolled_on_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_exact_text_enrollment_expiration_date_range_"
                    f"and_sort_by_enrolled_on_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_case_subject_search_criteria_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_and_sort_by_case_subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.select_sort_by_case_or_subject()
            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_case_subject_search_criteria_result()
            self.verify_sort_key_case_subject()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_and_sort_by_case_subject_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_and_sort_by_location_store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.select_sort_by_location_or_store()
            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_case_subject_search_criteria_result()
            self.verify_sort_key_location_store()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_and_sort_by_location_store_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_and_sort_by_enrolled_on_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.select_sort_by_enrolled_on()
            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_case_subject_search_criteria_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_and_sort_by_enrolled_on_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_and_expiration_date_range_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_case_subject_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_and_expiration_date_range_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_expiration_date_range_and_sort_by_case_subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()
            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.verify_sort_key_case_subject()
            self.validate_case_subject_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_expiration_date_range_"
                    f"and_sort_by_case_subject_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_expiration_date_range_and_sort_by_location_store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()
            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.verify_sort_key_location_store()
            self.validate_case_subject_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_expiration_date_range_"
                    f"and_sort_by_location_store_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_expiration_date_range_and_sort_by_enrolled_on_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()
            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_case_subject_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_expiration_date_range_"
                    f"and_sort_by_enrolled_on_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_and_enrollment_date_range_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_and_enrollment_date_range_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_enrollment_date_range_and_sort_by_case_subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.verify_sort_key_case_subject()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_enrollment_date_range_"
                    f"and_sort_by_case_subject_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_enrollment_date_range_and_sort_by_location_store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.verify_sort_key_location_store()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_enrollment_date_range_"
                    f"and_sort_by_location_store_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_enrollment_date_range_and_sort_by_enrolled_on_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_enrollment_date_range_"
                    f"and_sort_by_enrolled_on_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_enrollment_date_and_expiration_date_range_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_enrollment_date_"
                    f"and_expiration_date_range_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_enrollment_expiration_date_range_sort_by_case_subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.verify_sort_key_case_subject()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_enrollment_expiration_"
                    f"date_range_sort_by_case_subject_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_enrollment_expiration_date_range_sort_by_location_store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.verify_sort_key_location_store()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_enrollment_expiration_"
                    f"date_range_sort_by_location_store_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_enrollment_expiration_date_range_sort_by_enrolled_on_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_enrollment_expiration_date_"
                    f"range_sort_by_enrolled_on_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_and_exact_text_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_case_subject_search_criteria_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_and_exact_text_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_exact_text_and_sort_by_case_subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.verify_sort_key_case_subject()
            self.validate_case_subject_search_criteria_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_exact_text_and_sort_by_case_subject_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_exact_text_and_sort_by_location_store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.verify_sort_key_location_store()
            self.validate_case_subject_search_criteria_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_exact_text_and_sort_by_location_store_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_exact_text_and_sort_by_enrolled_on_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_case_subject_search_criteria_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_exact_text_and_sort_by_enrolled_on_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_exact_text_and_expiration_date_range_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_case_subject_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_exact_text_and_expiration_date_range_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_exact_text_expiration_date_range_sort_by_case_subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.verify_sort_key_case_subject()
            self.validate_case_subject_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_exact_text_expiration_date_range_sort_by_case_"
                    f"subject_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_exact_text_expiration_date_range_sort_by_location_store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.verify_sort_key_location_store()
            self.validate_case_subject_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_exact_text_expiration_date_range_"
                    f"sort_by_location_store_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_exact_text_expiration_date_range_sort_by_enrolled_on_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_case_subject_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_exact_text_expiration_date_"
                    f"range_sort_by_enrolled_on_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_exact_text_and_enrollment_date_range_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_exact_text_and_enrollment_date_range_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_exact_text_enrollment_date_range_sort_by_case_subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.verify_sort_key_case_subject()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_exact_text_enrollment_date_range_sort_by_"
                    f"case_subject_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_exact_text_enrollment_date_range_sort_by_location_store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.verify_sort_key_location_store()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_exact_text_enrollment_date_range_"
                    f"sort_by_location_store_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_exact_text_enrollment_date_range_sort_by_enrolled_on_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_exact_text_enrollment_date_range_sort_by_"
                    f"enrolled_on_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_exact_text_enrollment_expiration_date_range_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_exact_text_enrollment_expiration_"
                    f"date_range_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_exact_text_enrollment_expiration_date_range_sort_case_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.verify_sort_key_case_subject()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_exact_text_enrollment_"
                    f"expiration_date_range_sort_case_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_exact_text_enrollment_expiration_date_range_sort_store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.verify_sort_key_location_store()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_exact_text_enrollment_"
                    f"expiration_date_range_sort_store_criteria_failed.png")
                return False

    def enrollment_search_with_case_subject_exact_text_enrollment_expiration_date_range_sort_enrolled_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_case_subject_exact_text_enrollment_expiration"
                    f"_date_range_sort_enrolled_criteria_failed.png")
                return False

    def enrollment_search_with_location_store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_location_store_search_criteria_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_location_store_criteria_failed.png")
                return False

    def enrollment_search_with_location_store_and_sort_by_case_subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_location_store_search_criteria_result()
            self.verify_sort_key_case_subject()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_location_store_and_sort_by_case_subject_criteria_failed.png")
                return False

    def enrollment_search_with_location_store_and_sort_by_location_store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_location_store_search_criteria_result()
            self.verify_sort_key_location_store()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_location_store_and_sort_by_location_store_criteria_failed.png")
                return False

    def enrollment_search_with_location_store_and_sort_by_enrolled_on_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_location_store_search_criteria_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_location_store_and_sort_by_enrolled_on_criteria_failed.png")
                return False

    def enrollment_search_with_location_store_and_expiration_date_range_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_location_store_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_location_store_and_expiration_date_range_criteria_failed.png")
                return False

    def enrollment_search_with_location_store_expiration_date_range_and_sort_by_case_subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_location_store_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.verify_sort_key_case_subject()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_location_store_expiration_date_range_and_"
                    f"sort_by_case_subject_criteria_failed.png")
                return False

    def enrollment_search_with_location_store_expiration_date_range_and_sort_by_location_store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_location_store_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.verify_sort_key_location_store()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_location_store_expiration_date_range_"
                    f"and_sort_by_location_store_criteria_failed.png")
                return False

    def enrollment_search_with_location_store_expiration_date_range_and_sort_by_enrolled_on_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_location_store_search_criteria_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_location_store_expiration_date_range_"
                    f"and_sort_by_enrolled_on_criteria_failed.png")
                return False

    def enrollment_search_with_location_store_and_enrollment_date_range_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_location_store_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_location_store_and_enrollment_date_range_criteria_failed.png")
                return False

    def enrollment_search_with_location_store_enrollment_date_range_and_sort_by_case_subject_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_location_store_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.verify_sort_key_case_subject()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_location_store_enrollment_date_range_and"
                    f"_sort_by_case_subject_criteria_failed.png")
                return False

    def enrollment_search_with_location_store_enrollment_date_range_and_sort_by_location_store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_location_store_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.verify_sort_key_location_store()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_location_store_enrollment_date_range_"
                    f"and_sort_by_location_store_criteria_failed.png")
                return False

    def enrollment_search_with_location_store_enrollment_date_range_and_sort_by_enrolled_on_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_location_store_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_location_store_enrollment_date_range_"
                    f"and_sort_by_enrolled_on_criteria_failed.png")
                return False

    def enrollment_search_with_location_store_case_subject_exact_text_enrollment_date_range_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_location_store_case_subject_exact_text_enrollment"
                    f"_date_range_criteria_failed.png")
                return False

    def enrollment_search_with_location_store_case_subject_exact_text_enrollment_date_range_sort_case_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.verify_sort_key_case_subject()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_location_store_case_subject_exact_"
                    f"text_enrollment_date_range_sort_case_criteria_failed.png")
                return False

    def enrollment_search_with_location_store_case_subject_exact_text_enrollment_date_sort_by_store_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.verify_sort_key_location_store()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_location_store_case_subject_exact_text_enrollment_"
                    f"date_sort_by_store_criteria_failed.png")
                return False

    def enrollment_search_with_location_store_case_subject_exact_text_enrollment_date_sort_enrolled_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_location_store_case_subject_exact_text_enrollment"
                    f"_date_sort_enrolled_criteria_failed.png")
                return False

    def enrollment_search_with_location_store_case_subject_exact_text_enrollment_expiration_date_criteria(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_location_store_case_subject_exact_text_"
                    f"enrollment_expiration_date_criteria_failed.png")
                return False

    def enrollment_search_with_location_store_case_subject_exact_text_enrollment_expiration_date_sort_by_case_criteria(
            self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.verify_sort_key_case_subject()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_location_store_case_subject_exact_text_enrollment"
                    f"_expiration_date_sort_by_case_criteria_failed.png")
                return False

    def enrollment_search_with_location_store_case_subject_exact_text_enrollment_expiration_date_sort_by_store_criteria(
            self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()
            self.verify_sort_key_location_store()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_location_store_case_subject_exact_text_enrollment_"
                    f"expiration_date_sort_by_store_criteria_failed.png")
                return False

    def enrollment_search_with_location_store_case_subject_exact_text_enrollment_expiration_date_sort_by_enrolled_on_criteria(
            self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(Base_Class.three_second)

            self.validate_location_store_search_criteria_result()
            self.validate_case_subject_search_criteria_result()
            self.validate_enrolled_start_or_end_date_search_result()
            self.validate_expiration_start_or_end_date_search_result()

            time.sleep(Base_Class.three_second)
            if self.verify_if_match_found():
                self.validate_match_list_output(4)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\enrollment_search_with_location_store_case_subject_exact_text_enrollment_"
                    f"expiration_date_sort_by_enrolled_on_criteria_failed.png")
                return False

    ####################################### REUSABLE METHODS ###############################################

    def click_on_enrollments_link(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().enrollments_link_by_xpath())
        ele.click()

    def click_on_search_dropdown(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().search_drop_down_by_xpath())
        ele.click()

    def enter_location_or_store(self):
        location_store_data = Read_Enrollments_Components().location_store_data_input()
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().location_store_txt_bx_by_xpath())
        ele.send_keys(location_store_data)

    def enter_case_subject(self):
        case_subject_data = Read_Enrollments_Components().case_subject_data_input()
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().case_subject_txt_bx_by_xpath())
        ele.send_keys(case_subject_data)

    def click_on_exact_text_search_checkBox(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().exact_text_search_check_bx_by_xpath())
        ele.click()

    def click_on_enrollment_start_date_checkBox(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().enrollment_start_date_check_bx_by_xpath())
        ele.click()

    def click_on_enrollment_end_date_checkBox(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().enrollment_end_date_check_bx_by_xpath())
        ele.click()

    def click_on_expiration_start_date_checkBox(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().expiration_start_date_check_bx_by_xpath())
        ele.click()

    def click_on_expiration_end_date_checkBox(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().expiration_end_date_check_bx_by_xpath())
        ele.click()

    def click_on_enrollment_start_date_inputBox(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().enrollment_start_date_input_bx_by_xpath())
        ele.click()

    def click_on_enrollment_end_date_inputBox(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().enrollment_end_date_input_bx_by_xpath())
        ele.click()

    def click_on_expiration_start_date_inputBox(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().expiration_start_date_input_bx_by_xpath())
        ele.click()

    def click_on_expiration_end_date_inputBox(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().expiration_end_date_input_bx_by_xpath())
        ele.click()

    def select_sort_by_enrolled_on(self):
        visible_text_data = Read_Enrollments_Components().sort_by_data_input_Enrolled_On()
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().sort_by_by_xpath())
        s = Select(ele)
        s.select_by_visible_text(visible_text_data)

    def select_sort_by_case_or_subject(self):
        visible_text_data = Read_Enrollments_Components().sort_by_data_input_CASE_SUBJECT()
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().sort_by_by_xpath())
        s = Select(ele)
        s.select_by_visible_text(visible_text_data)

    def select_sort_by_location_or_store(self):
        visible_text_data = Read_Enrollments_Components().sort_by_data_input_LOCATION_STORE()
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().sort_by_by_xpath())
        s = Select(ele)
        s.select_by_visible_text(visible_text_data)

    def click_on_clear_btn(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().clear_btn_by_xpath())
        ele.click()

    def click_on_search_button(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().search_btn_by_xpath())
        ele.click()

    def validate_location_store_search_criteria_result(self):
        location_store_data = Read_Enrollments_Components().location_store_data_input()
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().location_store_filter_result_by_xpath())
        print("Expected data = " + location_store_data)
        print("Actual data = " + ele.text)
        assert location_store_data.lower() in ele.text.lower()

    def validate_case_subject_search_criteria_result(self):
        case_subject_data = Read_Enrollments_Components().case_subject_data_input()
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().case_subject_filter_result_by_xpath())
        print("Expected data = " + case_subject_data)
        print("Actual data = " + ele.text)
        assert case_subject_data.lower() in ele.text.lower()

    def validate_enrolled_start_or_end_date_search_result(self):
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

        date = int(Read_Enrollments_Components().enroll_get_start_date())
        month = str(Read_Enrollments_Components().enroll_get_start_month())
        year = int(Read_Enrollments_Components().enroll_get_start_year())
        hour = str(Read_Enrollments_Components().enroll_get_start_hour())
        minute = int(Read_Enrollments_Components().enroll_get_start_minuet())
        req_period = str(Read_Enrollments_Components().enroll_get_start_am_pm_period())
        mon = month_to_num.get(month)

        if 1 <= date <= 9:
            date = "0" + str(date)

        exp_asser1 = "{mon}/{date}/{year} {hour}:{min} {pe}"
        exp_asser1 = exp_asser1.format(mon=mon, date=date, year=year, hour=int(hour), min=minute, pe=req_period)
        print(exp_asser1)

        date = int(Read_Enrollments_Components().enroll_get_end_date())
        month = str(Read_Enrollments_Components().enroll_get_end_month())
        year = int(Read_Enrollments_Components().enroll_get_end_year())
        hour = str(Read_Enrollments_Components().enroll_get_end_hour())
        minute = int(Read_Enrollments_Components().enroll_get_end_minuet())
        req_period = str(Read_Enrollments_Components().enroll_get_end_am_pm_period())
        mon = month_to_num.get(month)

        if 1 <= date <= 9:
            date = "0" + str(date)
        exp_asser2 = "{mon}/{date}/{year} {hour}:{min} {pe}"
        exp_asser2 = exp_asser2.format(mon=mon, date=date, year=year, hour=int(hour), min=minute, pe=req_period)
        print("date format: ", exp_asser2)

        time.sleep(3)
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().enrolled_filter_result_by_xpath())
        assert exp_asser1 in ele.text
        assert exp_asser2 in ele.text

    def validate_expiration_start_or_end_date_search_result(self):
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

        date = int(Read_Enrollments_Components().expiration_get_start_date())
        month = str(Read_Enrollments_Components().expiration_get_start_month())
        year = int(Read_Enrollments_Components().expiration_get_start_year())
        hour = str(Read_Enrollments_Components().expiration_get_start_hour())
        minute = int(Read_Enrollments_Components().expiration_get_start_minuet())
        req_period = str(Read_Enrollments_Components().expiration_get_start_am_pm_period())
        mon = month_to_num.get(month)

        if 1 <= date <= 9:
            date = "0" + str(date)

        exp_asser1 = "{mon}/{date}/{year} {hour}:{minu} {pe}"
        exp_asser1 = exp_asser1.format(mon=mon, date=date, year=year, hour=int(hour), minu=minute, pe=req_period)
        print("date format: ", exp_asser1)

        date = int(Read_Enrollments_Components().expiration_get_end_date())
        month = str(Read_Enrollments_Components().expiration_get_end_month())
        year = int(Read_Enrollments_Components().expiration_get_end_year())
        hour = str(Read_Enrollments_Components().expiration_get_end_hour())
        minute = int(Read_Enrollments_Components().expiration_get_end_minuet())
        req_period = str(Read_Enrollments_Components().expiration_get_end_am_pm_period())
        mon = month_to_num.get(month)

        if 1 <= date <= 9:
            date = "0" + str(date)

        exp_asser2 = "{mon}/{date}/{year} {hour}:{minu} {pe}"
        exp_asser2 = exp_asser2.format(mon=mon, date=date, year=year, hour=int(hour), minu=minute, pe=req_period)
        print("date format: ", exp_asser2)

        time.sleep(3)
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().expiration_filter_result_by_xpath())
        print("Expected data = " + exp_asser1)
        print("Actual data = " + ele.text)
        print("Expected data = " + exp_asser2)
        print("Actual data = " + ele.text)
        assert exp_asser1 in ele.text
        assert exp_asser2 in ele.text

    def handle_enrollment_start_or_end_date_calender(self, strategy):
        # click on the form calendar popup
        if strategy == "from":
            date = int(Read_Enrollments_Components().enroll_get_start_date())
            month = str(Read_Enrollments_Components().enroll_get_start_month())
            year = int(Read_Enrollments_Components().enroll_get_start_year())
            hour = str(Read_Enrollments_Components().enroll_get_start_hour())
            minute = int(Read_Enrollments_Components().enroll_get_start_minuet())
            req_period = str(Read_Enrollments_Components().enroll_get_start_am_pm_period())
            self.click_on_enrollment_start_date_checkBox()
            self.click_on_enrollment_start_date_inputBox()
        else:
            date = int(Read_Enrollments_Components().enroll_get_end_date())
            month = str(Read_Enrollments_Components().enroll_get_end_month())
            year = int(Read_Enrollments_Components().enroll_get_end_year())
            hour = str(Read_Enrollments_Components().enroll_get_end_hour())
            minute = int(Read_Enrollments_Components().enroll_get_end_minuet())
            req_period = str(Read_Enrollments_Components().enroll_get_end_am_pm_period())
            # click on calendar pop up
            self.click_on_enrollment_end_date_checkBox()
            self.click_on_enrollment_end_date_inputBox()

        # click on the clock icon
        calender_clock = self.d.find_element(By.XPATH, Read_Enrollments_Components().calender_timer_icon_by_xpath())
        calender_clock.click()

        time.sleep(3)

        # handle the hour and minute based on the strategy
        if strategy == "from":
            self.calender_handle_hour_minute_from(hour, minute)
        else:
            self.calender_handle_hour_minute_to(hour, minute)

        # select the period am or pm
        period = self.d.find_element(By.XPATH, Read_Enrollments_Components().period_by_xpath())
        if period.text == req_period:
            print("")
        else:
            period.click()

        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, Read_Enrollments_Components().calender_tick_icon_by_xpath())
        tick_icon.click()

        if strategy == "from":
            self.click_on_enrollment_start_date_inputBox()
        else:
            # click on calendar pop up
            self.click_on_enrollment_end_date_inputBox()

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
        month_year = self.d.find_element(By.XPATH, Read_Enrollments_Components().calender_month_year_by_xpath())
        ac_month = month_year.text.split(" ")[0]
        ac_year = int(month_year.text.split(" ")[1])

        # click on the back button
        while month_to_num.get(req_month) < month_to_num.get(ac_month) or req_year < ac_year:
            cal_back_button = self.d.find_element(By.XPATH,
                                                  Read_Enrollments_Components().calender_back_button_by_xpath())
            if cal_back_button.is_enabled():
                cal_back_button.click()
            time.sleep(1)
            month_year = self.d.find_element(By.XPATH,
                                             Read_Enrollments_Components().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])

        # click on the forward button
        while month_to_num.get(req_month) > month_to_num.get(ac_month) or req_year > ac_year:
            cal_back_button = self.d.find_element(By.XPATH,
                                                  Read_Enrollments_Components().calender_forward_button_by_xpath())
            if cal_back_button.is_enabled():
                cal_back_button.click()
            time.sleep(1)
            month_year = self.d.find_element(By.XPATH,
                                             Read_Enrollments_Components().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])

        # click on the required date
        date = self.d.find_element(By.XPATH,
                                   "(//td[@class='day' or @class='day weekend' or @class='day active' "
                                   "or @class='day active today'])[" + str(date) + "]")
        date.click()

        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, Read_Enrollments_Components().calender_tick_icon_by_xpath())
        tick_icon.click()

    def handle_expiration_start_or_end_date_calender(self, strategy):
        # click on the form calendar popup
        if strategy == "from":
            date = int(Read_Enrollments_Components().expiration_get_start_date())
            month = str(Read_Enrollments_Components().expiration_get_start_month())
            year = int(Read_Enrollments_Components().expiration_get_start_year())
            hour = str(Read_Enrollments_Components().expiration_get_start_hour())
            minute = int(Read_Enrollments_Components().expiration_get_start_minuet())
            req_period = str(Read_Enrollments_Components().expiration_get_start_am_pm_period())
            self.click_on_expiration_start_date_checkBox()
            self.click_on_expiration_start_date_inputBox()
        else:
            date = int(Read_Enrollments_Components().expiration_get_end_date())
            month = str(Read_Enrollments_Components().expiration_get_end_month())
            year = int(Read_Enrollments_Components().expiration_get_end_year())
            hour = str(Read_Enrollments_Components().expiration_get_end_hour())
            minute = int(Read_Enrollments_Components().expiration_get_end_minuet())
            req_period = str(Read_Enrollments_Components().expiration_get_end_am_pm_period())
            # click on calendar pop up
            self.click_on_expiration_end_date_checkBox()
            self.click_on_expiration_end_date_inputBox()

        # click on the clock icon
        calender_clock = self.d.find_element(By.XPATH, Read_Enrollments_Components().calender_timer_icon_by_xpath())
        calender_clock.click()

        time.sleep(3)

        # handle the hour and minute based on the strategy
        if strategy == "from":
            self.calender_handle_hour_minute_from(hour, minute)
        else:
            self.calender_handle_hour_minute_to(hour, minute)

        # select the period am or pm
        period = self.d.find_element(By.XPATH, Read_Enrollments_Components().period_by_xpath())
        if period.text == req_period:
            print("")
        else:
            period.click()

        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, Read_Enrollments_Components().calender_tick_icon_by_xpath())
        tick_icon.click()

        if strategy == "from":
            self.click_on_expiration_start_date_inputBox()
        else:
            # click on calendar pop up
            self.click_on_expiration_end_date_inputBox()

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
        month_year = self.d.find_element(By.XPATH, Read_Enrollments_Components().calender_month_year_by_xpath())
        ac_month = month_year.text.split(" ")[0]
        ac_year = int(month_year.text.split(" ")[1])

        # click on the back button
        while month_to_num.get(req_month) < month_to_num.get(ac_month) or req_year < ac_year:
            cal_back_button = self.d.find_element(By.XPATH,
                                                  Read_Enrollments_Components().calender_back_button_by_xpath())
            # if cal_back_button.is_enabled():
            #     cal_back_button.click()

            self.d.execute_script("arguments[0].click();", cal_back_button)
            time.sleep(1)
            month_year = self.d.find_element(By.XPATH,
                                             Read_Enrollments_Components().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])

        # click on the forward button
        while month_to_num.get(req_month) > month_to_num.get(ac_month) or req_year > ac_year:
            next_button = self.d.find_element(By.XPATH,
                                              Read_Enrollments_Components().calender_forward_button_by_xpath())
            # if next_button.is_enabled():
            #     next_button.click()

            self.d.execute_script("arguments[0].click();", next_button)
            time.sleep(1)

            month_year = self.d.find_element(By.XPATH,
                                             Read_Enrollments_Components().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])

        # click on the required date
        date = self.d.find_element(By.XPATH,
                                   "(//td[@class='day' or @class='day weekend' or @class='day active' "
                                   "or @class='day active today'])[" + str(date) + "]")
        date.click()

        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, Read_Enrollments_Components().calender_tick_icon_by_xpath())
        # tick_icon.click()
        self.d.execute_script("arguments[0].click();", tick_icon)

    def calender_handle_hour_minute_to(self, hour, minute):
        # set the minute
        current_min_ele = self.d.find_element(By.XPATH,
                                              Read_Enrollments_Components().current_minute_element_by_xpath())
        cur_min = int(current_min_ele.text)
        if int(minute) > int(cur_min):
            while int(cur_min) != int(minute):
                clock_up_button = self.d.find_element(By.XPATH, Read_Enrollments_Components()
                                                      .clock_min_up_button_by_xpath())
                clock_up_button.click()
                current_min_ele = self.d.find_element(By.XPATH, Read_Enrollments_Components()
                                                      .current_minute_element_by_xpath())
                cur_min = int(current_min_ele.text)
        else:
            while int(cur_min) != int(minute):
                clock_down_button = self.d.find_element(By.XPATH, Read_Enrollments_Components()
                                                        .clock_min_down_button_by_xpath())
                clock_down_button.click()
                current_min_ele = self.d.find_element(By.XPATH, Read_Enrollments_Components()
                                                      .current_minute_element_by_xpath())
                cur_min = int(current_min_ele.text)

        time.sleep(2)

        # set the hour
        current_hour_ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().current_hour_ele_by_xpath())
        cur_hour = int(current_hour_ele.text)

        while int(cur_hour) != int(hour):
            hour_down = self.d.find_element(By.XPATH, Read_Enrollments_Components().hour_down_by_xpath())
            hour_down.click()
            current_hour_ele = self.d.find_element(By.XPATH,
                                                   Read_Enrollments_Components().current_hour_ele_by_xpath())
            cur_hour = int(current_hour_ele.text)

    def calender_handle_hour_minute_from(self, hour, minute):

        # set the minute
        current_min_ele = self.d.find_element(By.XPATH, Read_Enrollments_Components()
                                              .current_minute_element_by_xpath())
        cur_min = int(current_min_ele.text)

        if int(minute) > int(cur_min):
            while int(cur_min) != int(minute):
                clock_up_button = self.d.find_element(By.XPATH, Read_Enrollments_Components()
                                                      .clock_min_up_button_by_xpath())
                clock_up_button.click()
                current_min_ele = self.d.find_element(By.XPATH, Read_Enrollments_Components()
                                                      .current_minute_element_by_xpath())
                cur_min = int(current_min_ele.text)
        else:
            while int(cur_min) != int(minute):
                clock_down_button = self.d.find_element(By.XPATH, Read_Enrollments_Components()
                                                        .clock_min_down_button_by_xpath())
                clock_down_button.click()
                current_min_ele = self.d.find_element(By.XPATH, Read_Enrollments_Components()
                                                      .current_minute_element_by_xpath())
                cur_min = int(current_min_ele.text)

        time.sleep(2)
        # set the hour
        current_hour_ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().current_hour_ele_by_xpath())
        cur_hour = int(current_hour_ele.text)

        # decrementHours
        while int(cur_hour) != int(hour):
            hour_down = self.d.find_element(By.XPATH, Read_Enrollments_Components().hour_down_by_xpath())
            hour_down.click()
            current_hour_ele = self.d.find_element(By.XPATH, Read_Enrollments_Components()
                                                   .current_hour_ele_by_xpath())
            cur_hour = int(current_hour_ele.text)

    def verify_if_match_found(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().no_match_search_filter_message())
        if ele.is_displayed():
            return False
        else:
            return True

    def validate_enrolled_on_is_displayed_from_the_match_list(self):
        result = True
        match_found_list_enrolled = self.d.find_elements(By.XPATH, Read_Enrollments_Components()
                                                         .match_list_enrolled_output())
        for ele in match_found_list_enrolled:
            if not ele.is_displayed():
                result = False
        assert result

    def validate_location_store_case_subject_from_match_list(self):
        result = True
        location_store_data = Read_Enrollments_Components().location_store_data_input()
        case_subject_data = Read_Enrollments_Components().case_subject_data_input()

        print(location_store_data, case_subject_data)
        match_found_list_location_store_case_subject = self.d \
            .find_elements(By.XPATH,
                           Read_Enrollments_Components().match_list_location_store_case_subject_output())
        for ele in match_found_list_location_store_case_subject:
            if not location_store_data and case_subject_data in ele.text:
                result = False
        assert result

    def validate_action_is_displayed_from_the_match_list(self):
        result = True
        match_found_list_action = self.d.find_elements(By.XPATH, Read_Enrollments_Components()
                                                       .match_list_action_output())
        for ele in match_found_list_action:
            if not ele.is_displayed():
                result = False
        assert result

    def validate_match_list_output(self, choice):
        """
        This function is used to validate the search filters criteria applied, from the list of enrollments matches
        \n choice 1 : validate enrolled on is displayed from match list
        \n choice 2 : validate location/store ,case/subject from match list
        \n choice 3 : validate action is displayed from the match list
        \n choice 4 : validate all search criteria from the match list

        :param choice:
        :return:
        """
        photo = self.d.find_element(By.XPATH, Read_Enrollments_Components().match_list_image_by_xpath())

        while not photo.is_displayed():
            time.sleep(Base_Class.three_second)

        match int(choice):
            case 1:
                self.validate_enrolled_on_is_displayed_from_the_match_list()

            case 2:
                self.validate_location_store_case_subject_from_match_list()

            case 3:
                self.validate_action_is_displayed_from_the_match_list()

            case 4:
                self.validate_enrolled_on_is_displayed_from_the_match_list()

                self.validate_location_store_case_subject_from_match_list()

                self.validate_action_is_displayed_from_the_match_list()
            case _:
                print("invalid input provided")
                assert False

    def verify_sort_key_location_store(self):
        data = Read_Enrollments_Components().sort_by_data_input_LOCATION_STORE()
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().sort_key_by_xpath())
        print("Expected data = " + data)
        print("Actual data = " + ele.text)
        assert data in ele.text

    def verify_sort_key_case_subject(self):
        data = Read_Enrollments_Components().sort_by_data_input_CASE_SUBJECT()
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().sort_key_by_xpath())
        print("Expected data = "+data)
        print("Actual data = "+ele.text)
        assert data.lower() in ele.text.lower()

    def close_all_panel_one_by_one(self):
        time.sleep(Base_Class.one_second)
        try:
            close_panel_list = self.d.find_elements(By.XPATH,
                                                    Read_Enrollments_Components().close_panel_one_by_one_list())
            for i in close_panel_list:
                i.click()
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
            logout_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().logout_btn_by_xpath())
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
