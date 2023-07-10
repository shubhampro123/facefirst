import time
from pathlib import Path
from selenium.webdriver.common.by import By
from All_Test_Cases_Package.conftest import Base_Class
from Config_Package.INI_Config_Files.Portal_Menu_Read_INI import Read_Portal_Menu_Components
from Config_Package.INI_Config_Files.Tags_Read_INI import Read_Tags_Components


class Portal_Menu_pom:

    def __init__(self):
        self.d = Base_Class.d

    def login_before(self):

        try:
            # self.d.get(Read_Portal_Menu_Components().get_url())
            print("login")
            # time.sleep(Base_Class.one_second)
            # username = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_usernameField())
            # username.send_keys(Read_Portal_Menu_Components().get_username())
            # password = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_passwordField())
            # password.send_keys(Read_Portal_Menu_Components().get_password())
            # time.sleep(Base_Class.one_second)
            # login_btn = self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton())
            # self.d.execute_script("arguments[0].click();", login_btn)

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\login_failed_for_portal_menu_pg_03.png")
                return False

    def login_before_one(self):

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
                    f"{Path(__file__).parent.parent}\\Screenshots\\login_failed_for_portal_menu_pg_03.png")
                return False

    def click_on_event_button(self):
        try:
            time.sleep(Base_Class.one_second)
            event_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().portal_menu_event_btn_by_xpath())
            self.d.execute_script("arguments[0].click();", event_button)
            time.sleep(Base_Class.one_second)
            # event_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_portal_menu_event_pg_03.png")
                return False

    def event_button_validation(self):
        try:
            Portal_Menu_pom().login_before()
            Portal_Menu_pom().click_on_event_button()
            time.sleep(Base_Class.one_second)
            event_validation = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().portal_menu_event_validation_by_xpath()
                                                   )
            actual_event_panel_text = event_validation.text
            expected_event_panel_text = Read_Portal_Menu_Components().event_panel_validation_text()
            assert actual_event_panel_text == expected_event_panel_text
            time.sleep(Base_Class.one_second)
            if event_validation.is_displayed():
                Portal_Menu_pom().close_all_panel_one_by_one()
                time.sleep(Base_Class.one_second)
                Portal_Menu_pom().click_on_logout_button()
                return True

            else:
                Portal_Menu_pom().close_all_panel_one_by_one()
                time.sleep(Base_Class.one_second)
                Portal_Menu_pom().click_on_logout_button()
                return False

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\menu_event_validation_failed_pg_03.png")
                return False

    def click_on_tags_button(self):
        try:
            time.sleep(Base_Class.one_second)
            tags_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().portal_menu_tags_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            self.d.execute_script("arguments[0].click();", tags_button)
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_portal_menu_tags_pg_03.png")
                return False

    def tags_button_validation(self):
        try:
            Portal_Menu_pom().login_before()
            Portal_Menu_pom().click_on_tags_button()
            time.sleep(Base_Class.one_second)
            tags_validation = self.d.find_element(By.XPATH,
                                                  Read_Portal_Menu_Components().portal_menu_tags_validation_by_xpath())
            actual_tags_panel_text = tags_validation.text
            expected_tags_panel_text = Read_Portal_Menu_Components().tags_panel_validation_text()
            assert actual_tags_panel_text == expected_tags_panel_text
            time.sleep(Base_Class.one_second)
            if tags_validation.is_displayed():
                Portal_Menu_pom().close_all_panel_one_by_one()
                Portal_Menu_pom().click_on_logout_button()
                return True
            else:
                Portal_Menu_pom().close_all_panel_one_by_one()
                Portal_Menu_pom().click_on_logout_button()
                return False
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\menu_tags_validation_failed_pg_03.png")
                return False

    def click_on_identify_enroll_button(self):
        try:
            time.sleep(Base_Class.one_second)
            identify_enroll_button = self.d.find_element(By.XPATH,
                                                         Read_Portal_Menu_Components().
                                                         portal_menu_identify_enroll_btn_by_xpath())
            identify_enroll_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\Button_not_clickable_portal_menu_identify_enroll_pg_03.png")
                return False

    def identify_enroll_button_validation(self):
        try:
            Portal_Menu_pom().login_before()
            Portal_Menu_pom().click_on_identify_enroll_button()
            time.sleep(Base_Class.one_second)
            identify_enroll_validation = self.d.find_element(By.XPATH,
                                                             Read_Portal_Menu_Components().
                                                             portal_menu_indentify_enroll_validation_by_xpath())
            actual_identify_enroll_validation_text = identify_enroll_validation.text
            expected_identify_enroll_validation_text = Read_Portal_Menu_Components(). \
                identify_and_enroll_panel_validation_text()
            assert actual_identify_enroll_validation_text == expected_identify_enroll_validation_text
            time.sleep(Base_Class.one_second)
            if identify_enroll_validation.is_displayed():
                Portal_Menu_pom().close_all_panel_one_by_one()
                Portal_Menu_pom().click_on_logout_button()
                return True
            else:
                Portal_Menu_pom().close_all_panel_one_by_one()
                Portal_Menu_pom().click_on_logout_button()
                return False
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\identify_enroll_validation_failed_pg_03.png")
                return False

    def click_on_detect_faces_button(self):
        try:
            time.sleep(Base_Class.one_second)
            detect_faces_button = self.d.find_element(By.XPATH,
                                                      Read_Portal_Menu_Components().
                                                      portal_menu_detect_faces_btn_by_xpath())
            detect_faces_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\Button_not_clickable_portal_menu_detect_faces_pg_03.png")
                return False

    def detect_faces_button_validation(self):
        try:
            Portal_Menu_pom().login_before()
            Portal_Menu_pom().click_on_detect_faces_button()
            time.sleep(Base_Class.one_second)
            detect_faces_validation = self.d.find_element(By.XPATH,
                                                          Read_Portal_Menu_Components().
                                                          portal_menu_detect_faces_validation_by_xpath())
            actual_detect_faces_validation = detect_faces_validation.text
            expected_detect_faces_validation = Read_Portal_Menu_Components().detect_faces_validation_text()
            assert actual_detect_faces_validation == expected_detect_faces_validation
            time.sleep(Base_Class.one_second)
            if detect_faces_validation.is_displayed():
                Portal_Menu_pom().close_all_panel_one_by_one()
                Portal_Menu_pom().click_on_logout_button()
                return True
            else:
                Portal_Menu_pom().close_all_panel_one_by_one()
                Portal_Menu_pom().click_on_logout_button()
                return False
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\detect_faces_validation_failed_pg_03.png")
                return False

    def click_on_enrollments_button(self):
        try:
            time.sleep(Base_Class.one_second)
            enrollments_button = self.d.find_element(By.XPATH,
                                                     Read_Portal_Menu_Components().
                                                     portal_menu_enrollments_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            enrollments_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_portal_menu_enrollments_pg_03"
                    f".png")
                return False

    def enrollments_button_validation(self):
        try:
            Portal_Menu_pom().login_before()
            Portal_Menu_pom().click_on_enrollments_button()
            time.sleep(Base_Class.one_second)
            enrollments_validation = self.d.find_element(By.XPATH,
                                                         Read_Portal_Menu_Components().
                                                         portal_menu_enrollments_validation_by_xpath())
            actual_enrollments_validation = enrollments_validation.text
            expected_enrollments_validation = Read_Portal_Menu_Components().enrollments_panel_validation_text()
            assert actual_enrollments_validation == expected_enrollments_validation
            time.sleep(Base_Class.one_second)
            if enrollments_validation.is_displayed():
                Portal_Menu_pom().close_all_panel_one_by_one()
                Portal_Menu_pom().click_on_logout_button()
                return True
            else:
                Portal_Menu_pom().close_all_panel_one_by_one()
                Portal_Menu_pom().click_on_logout_button()
                return False
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\enrollments_validation_failed_pg_03.png")
                return False

    def click_on_enrollments_groups_button(self):
        try:
            time.sleep(Base_Class.one_second)
            enrollments_groups_button = self.d.find_element(By.XPATH,
                                                            Read_Portal_Menu_Components().
                                                            portal_menu_enrollments_groups_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            enrollments_groups_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\Button_not_clickable_portal_menu_enrollments_groups_pg_03.png")
                return False

    def enrollments_groups_button_validation(self):
        try:
            Portal_Menu_pom().login_before()
            Portal_Menu_pom().click_on_enrollments_groups_button()
            time.sleep(Base_Class.one_second)
            enrollments_groups_validation = self.d.find_element(By.XPATH,
                                                                Read_Portal_Menu_Components().
                                                                portal_menu_enrollments_groups_validation_by_xpath())
            actual_enrollments_groups_validation = enrollments_groups_validation.text
            expected_enrollments_groups_validation = Read_Portal_Menu_Components(). \
                enrollments_groups_panel_validation_text()
            assert actual_enrollments_groups_validation == expected_enrollments_groups_validation
            time.sleep(Base_Class.one_second)
            if enrollments_groups_validation.is_displayed():
                Portal_Menu_pom().close_all_panel_one_by_one()
                Portal_Menu_pom().click_on_logout_button()
                return True
            else:
                Portal_Menu_pom().close_all_panel_one_by_one()
                Portal_Menu_pom().click_on_logout_button()
                return False
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\enrollments_groups_validation_failed_pg_03.png")
                return False

    def click_on_notification_groups_button(self):
        try:
            time.sleep(Base_Class.one_second)
            notification_groups_button = self.d.find_element(By.XPATH,
                                                             Read_Portal_Menu_Components().
                                                             portal_menu_notification_groups_btn_by_xpath())
            notification_groups_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\Button_not_clickable_portal_menu_notification_groups_pg_03.png")
                return False

    def notification_groups_button_validation(self):
        try:
            Portal_Menu_pom().login_before()
            Portal_Menu_pom().click_on_notification_groups_button()
            time.sleep(Base_Class.one_second)
            notification_groups_validation = self.d.find_element(By.XPATH,
                                                                 Read_Portal_Menu_Components().
                                                                 portal_menu_notification_groups_validation_by_xpath())
            actual_notification_groups_validation = notification_groups_validation.text
            expected_notification_groups_validation = Read_Portal_Menu_Components(). \
                notification_groups_panel_validation_text()
            assert actual_notification_groups_validation == expected_notification_groups_validation
            time.sleep(Base_Class.one_second)
            if notification_groups_validation.is_displayed():
                Portal_Menu_pom().close_all_panel_one_by_one()
                time.sleep(Base_Class.one_second)
                Portal_Menu_pom().click_on_logout_button()
                return True
            else:
                Portal_Menu_pom().close_all_panel_one_by_one()
                time.sleep(Base_Class.one_second)
                Portal_Menu_pom().click_on_logout_button()
                return False
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\notification_groups_validation_failed_pg_03.png")
                return False

    def click_on_visitors_button(self):
        try:
            time.sleep(Base_Class.one_second)
            visitors_button = self.d.find_element(By.XPATH,
                                                  Read_Portal_Menu_Components().portal_menu_visitors_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            visitors_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_portal_menu_visitors_pg_03.png")
                return False

    def visitors_button_validation(self):
        try:
            Portal_Menu_pom().login_before()
            Portal_Menu_pom().click_on_visitors_button()
            time.sleep(Base_Class.one_second)
            visitors_validation = self.d.find_element(By.XPATH,
                                                      Read_Portal_Menu_Components().
                                                      portal_menu_visitors_validation_by_xpath())
            actual_visitors_validation = visitors_validation.text
            expected_visitors_validation = Read_Portal_Menu_Components().visitors_panel_validation_text()
            assert actual_visitors_validation == expected_visitors_validation
            time.sleep(Base_Class.one_second)
            if visitors_validation.is_displayed():
                Portal_Menu_pom().close_all_panel_one_by_one()
                time.sleep(Base_Class.one_second)
                Portal_Menu_pom().click_on_logout_button()
                return True
            else:
                Portal_Menu_pom().close_all_panel_one_by_one()
                time.sleep(Base_Class.one_second)
                Portal_Menu_pom().click_on_logout_button()
                return False
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\notification_visitors_validation_failed_pg_03.png")
                return False

    def click_on_visitors_search_button(self):
        try:
            time.sleep(Base_Class.one_second)
            visitors_search_button = self.d.find_element(By.XPATH,
                                                         Read_Portal_Menu_Components().
                                                         portal_menu_visitors_search_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            visitors_search_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\Button_not_clickable_portal_menu_visitors_search_pg_03.png")
                return False

    def visitors_search_button_validation(self):
        try:
            Portal_Menu_pom().login_before()
            Portal_Menu_pom().click_on_visitors_search_button()
            time.sleep(Base_Class.one_second)
            visitors_search_validation = self.d.find_element(By.XPATH,
                                                             Read_Portal_Menu_Components().
                                                             portal_menu_visitors_search_validation_by_xpath())
            actual_visitors_search_validation = visitors_search_validation.text
            expected_visitors_search_validation = Read_Portal_Menu_Components().visitor_search_panel_validation_text()
            assert actual_visitors_search_validation == expected_visitors_search_validation
            time.sleep(Base_Class.one_second)
            if visitors_search_validation.is_displayed():
                Portal_Menu_pom().close_all_panel_one_by_one()
                Portal_Menu_pom().click_on_logout_button()
                return True
            else:
                Portal_Menu_pom().close_all_panel_one_by_one()
                Portal_Menu_pom().click_on_logout_button()
                return False
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\notification_visitors_search_validation_failed_pg_03.png")
                return False

    def click_on_visitors_search_job_button(self):
        try:
            time.sleep(Base_Class.one_second)
            visitors_search_job_button = self.d.find_element(By.XPATH,
                                                             Read_Portal_Menu_Components().
                                                             portal_menu_visitors_search_job_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            visitors_search_job_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\Button_not_clickable_portal_menu_visitors_search_job_pg_03.png")
                return False

    def visitors_search_button_job_validation(self):
        try:
            Portal_Menu_pom().login_before()
            Portal_Menu_pom().click_on_visitors_search_job_button()
            time.sleep(Base_Class.one_second)
            visitors_search_job_validation = self.d.find_element(By.XPATH,
                                                                 Read_Portal_Menu_Components().
                                                                 portal_menu_visitors_search_job_validation_by_xpath())
            actual_visitors_search_job_validation = visitors_search_job_validation.text
            expected_visitors_search_job_validation = Read_Portal_Menu_Components().visitor_search_jobs_panel_text()
            assert actual_visitors_search_job_validation == expected_visitors_search_job_validation
            time.sleep(Base_Class.one_second)
            if visitors_search_job_validation.is_displayed():
                Portal_Menu_pom().close_all_panel_one_by_one()
                time.sleep(Base_Class.one_second)
                Portal_Menu_pom().click_on_logout_button()
                return True
            else:
                Portal_Menu_pom().close_all_panel_one_by_one()
                time.sleep(Base_Class.one_second)
                Portal_Menu_pom().click_on_logout_button()
                return False
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\notification_visitors_search_job_validation_failed_pg_03.png")
                return False

    def click_on_notes_button(self):
        try:
            time.sleep(Base_Class.one_second)
            notes_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().portal_menu_notes_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            notes_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_portal_menu_notes_pg_03.png")
                return False

    def notes_validation(self):
        try:
            Portal_Menu_pom().login_before()
            Portal_Menu_pom().click_on_notes_button()
            time.sleep(Base_Class.one_second)
            notes_validation = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().
                                                   portal_menu_notes_validation_by_xpath())
            actual_notes_validation = notes_validation.text
            expected_notes_validation = Read_Portal_Menu_Components().notes_panel_validation_text()
            assert actual_notes_validation == expected_notes_validation
            time.sleep(Base_Class.one_second)
            if notes_validation.is_displayed():
                Portal_Menu_pom().close_all_panel_one_by_one()
                time.sleep(Base_Class.one_second)
                Portal_Menu_pom().click_on_logout_button()
                return True
            else:
                Portal_Menu_pom().close_all_panel_one_by_one()
                time.sleep(Base_Class.one_second)
                Portal_Menu_pom().click_on_logout_button()
                return False
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\notification_notes_validation_failed_pg_03.png")
                return False

    def click_on_locations_button(self):
        try:
            time.sleep(Base_Class.one_second)
            locations_button = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().portal_menu_locations_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            locations_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_portal_menu_locations_pg_03.png"
                )
                return False

    def locations_validation(self):
        try:
            Portal_Menu_pom().login_before()
            Portal_Menu_pom().click_on_locations_button()
            time.sleep(Base_Class.one_second)
            locations_validation = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().
                                                       portal_menu_locations_validation_by_xpath())
            cancel_button = self.d.find_element(By.XPATH,
                                                Read_Portal_Menu_Components().
                                                location_cancel_button())
            actual_locations_validation = locations_validation.text
            expected_locations_validation = Read_Portal_Menu_Components().locations_panel_validation_text()
            print(actual_locations_validation)
            print(expected_locations_validation)
            assert actual_locations_validation == expected_locations_validation
            time.sleep(Base_Class.one_second)
            if locations_validation.is_displayed():
                time.sleep(Base_Class.one_second)
                self.d.execute_script("arguments[0].click();", cancel_button)
                Portal_Menu_pom().close_all_panel_one_by_one()
                time.sleep(Base_Class.one_second)
                Portal_Menu_pom().click_on_logout_button()
                return True
            else:
                time.sleep(Base_Class.one_second)
                self.d.execute_script("arguments[0].click();", cancel_button)
                Portal_Menu_pom().close_all_panel_one_by_one()
                time.sleep(Base_Class.one_second)
                Portal_Menu_pom().click_on_logout_button()
                return False
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\notification_locations_validation_failed_pg_03.png")
                return False

    def click_on_users_button(self):
        try:
            time.sleep(Base_Class.one_second)
            users_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().portal_menu_users_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            users_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_portal_menu_users_pg_03.png")
                return False

    def users_validation(self):
        try:
            Portal_Menu_pom().login_before()
            Portal_Menu_pom().click_on_users_button()
            time.sleep(Base_Class.one_second)
            users_validation = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().portal_menu_users_validation_by_xpath()
                                                   )
            actual_users_validation = users_validation.text
            expected_users_validation = Read_Portal_Menu_Components().user_panel_validation_text()
            assert actual_users_validation == expected_users_validation
            time.sleep(Base_Class.one_second)
            if users_validation.is_displayed():
                Portal_Menu_pom().close_all_panel_one_by_one()
                time.sleep(Base_Class.one_second)
                Portal_Menu_pom().click_on_logout_button()
                return True
            else:
                Portal_Menu_pom().close_all_panel_one_by_one()
                time.sleep(Base_Class.one_second)
                Portal_Menu_pom().click_on_logout_button()
                return False
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\notification_users_validation_failed_pg_03.png")
                return False

    def click_on_users_role_button(self):
        try:
            time.sleep(Base_Class.one_second)
            users_roles_button = self.d.find_element(By.XPATH,
                                                     Read_Portal_Menu_Components().
                                                     portal_menu_users_roles_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            users_roles_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_portal_menu_users_roles_pg_03"
                    f".png")
                return False

    def users_roles_validation(self):
        try:
            Portal_Menu_pom().login_before()
            Portal_Menu_pom().click_on_users_role_button()
            time.sleep(Base_Class.one_second)
            users_roles_validation = self.d.find_element(By.XPATH,
                                                         Read_Portal_Menu_Components().
                                                         portal_menu_users_roles_validation_by_xpath())
            actual_users_roles_validation = users_roles_validation.text
            expected_users_roles_validation = Read_Portal_Menu_Components().user_roles_validation_text()
            assert actual_users_roles_validation == expected_users_roles_validation
            time.sleep(Base_Class.one_second)
            if users_roles_validation.is_displayed():
                Portal_Menu_pom().close_all_panel_one_by_one()
                time.sleep(Base_Class.one_second)
                Portal_Menu_pom().click_on_logout_button()
                return True
            else:
                Portal_Menu_pom().close_all_panel_one_by_one()
                time.sleep(Base_Class.one_second)
                Portal_Menu_pom().click_on_logout_button()
                return False
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\notification_users_roles_validation_failed_pg_03.png"
                )
                return False

    def click_on_zones_button(self):
        try:
            time.sleep(Base_Class.one_second)
            zones_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().portal_menu_zones_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            zones_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_portal_menu_zones_pg_03.png")
                return False

    def zones_button_validation(self):
        try:
            Portal_Menu_pom().login_before()
            Portal_Menu_pom().click_on_zones_button()
            time.sleep(Base_Class.one_second)
            zones_validation = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().portal_menu_zones_validation_by_xpath()
                                                   )
            actual_zones_validation = zones_validation.text
            expected_zones_validation = Read_Portal_Menu_Components().zones_panel_validation_text()
            assert actual_zones_validation == expected_zones_validation
            time.sleep(Base_Class.one_second)
            if zones_validation.is_displayed():
                Portal_Menu_pom().close_all_panel_one_by_one()
                time.sleep(Base_Class.one_second)
                Portal_Menu_pom().click_on_logout_button()
                return True
            else:
                Portal_Menu_pom().close_all_panel_one_by_one()
                time.sleep(Base_Class.one_second)
                Portal_Menu_pom().click_on_logout_button()
                return False
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\notification_zones_validation_failed_pg_03.png")
                return False

    def click_on_account_button(self):
        try:
            time.sleep(Base_Class.one_second)
            account_button = self.d.find_element(By.XPATH,
                                                 Read_Portal_Menu_Components().portal_menu_account_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            account_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_portal_menu_account_pg_03.png")
                return False

    def account_button_validation(self):
        try:
            Portal_Menu_pom().login_before()
            Portal_Menu_pom().click_on_account_button()
            time.sleep(Base_Class.one_second)
            account_validation = self.d.find_element(By.XPATH,
                                                     Read_Portal_Menu_Components().
                                                     portal_menu_account_validation_by_xpath())
            actual_account_validation = account_validation.text
            expected_account_validation = Read_Portal_Menu_Components().account_panel_validation_text()
            assert actual_account_validation == expected_account_validation
            time.sleep(Base_Class.one_second)
            if account_validation.is_displayed():
                Portal_Menu_pom().close_all_panel_one_by_one()
                time.sleep(Base_Class.one_second)
                Portal_Menu_pom().click_on_logout_button()
                return True
            else:
                Portal_Menu_pom().close_all_panel_one_by_one()
                time.sleep(Base_Class.one_second)
                Portal_Menu_pom().click_on_logout_button()
                return False
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\notification_account_validation_failed_pg_03.png")
                return False

    def click_on_reporting_button(self):
        try:
            time.sleep(Base_Class.one_second)
            reporting_button = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().portal_menu_reporting_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            reporting_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_portal_menu_reporting_pg_03.png"
                )
                return False

    def reporting_button_validation(self):
        try:
            Portal_Menu_pom().login_before()
            Portal_Menu_pom().click_on_reporting_button()
            time.sleep(Base_Class.one_second)
            reporting_validation = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().
                                                       portal_menu_reporting_validation_by_xpath())
            actual_reporting_validation = reporting_validation.text
            expected_reporting_validation = Read_Portal_Menu_Components().reporting_validation_text()
            assert actual_reporting_validation == expected_reporting_validation
            time.sleep(Base_Class.one_second)
            if reporting_validation.is_displayed():
                Portal_Menu_pom().close_all_panel_one_by_one()
                Portal_Menu_pom().click_on_logout_button()
                return True
            else:
                Portal_Menu_pom().close_all_panel_one_by_one()
                Portal_Menu_pom().click_on_logout_button()
                return False
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\notification_account_validation_failed_pg_03.png")
                return False

    def click_on_notifier_button(self):
        try:
            time.sleep(Base_Class.one_second)
            notifier_button = self.d.find_element(By.XPATH,
                                                  Read_Portal_Menu_Components().portal_menu_notifier_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            notifier_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_portal_menu_notifier_pg_03.png")
                return False

    def notifier_button_validation(self):
        try:
            Portal_Menu_pom().login_before()
            Portal_Menu_pom().click_on_notifier_button()
            time.sleep(Base_Class.one_second)
            notifier_validation = self.d.find_element(By.XPATH,
                                                      Read_Portal_Menu_Components().
                                                      portal_menu_notifier_validation_by_xpath())
            close = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().
                                        notifier_close_button())
            actual_notifier_validation = notifier_validation.text
            expected_notifier_validation = Read_Portal_Menu_Components().notifier_panel_validation_text()
            assert actual_notifier_validation == expected_notifier_validation
            time.sleep(Base_Class.one_second)
            if notifier_validation.is_displayed():
                close.click()
                Portal_Menu_pom().click_on_logout_button()
                return True
            else:
                close.click()
                Portal_Menu_pom().click_on_logout_button()
                return False
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\notification_notifier_validation_failed_pg_03.png")
                return False

    def click_on_dashboard_button(self):
        try:
            time.sleep(Base_Class.one_second)
            dashboard_button = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().portal_menu_dashboard_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            dashboard_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_portal_menu_dashboard_pg_03.png"
                )
                return False

    def dashboard_button_validation(self):
        try:
            Portal_Menu_pom().login_before()
            Portal_Menu_pom().click_on_dashboard_button()
            time.sleep(Base_Class.one_second)
            self.d.switch_to.window(self.d.window_handles[1])
            dashboard_validation = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().
                                                       portal_menu_dashboard_validation_by_xpath())
            actual_dashboard_validation = dashboard_validation.text
            excepted_dashboard_validation = Read_Portal_Menu_Components().dashboard_panel_validation_text()
            assert actual_dashboard_validation == excepted_dashboard_validation
            time.sleep(Base_Class.one_second)
            if dashboard_validation.is_displayed():
                self.d.close()
                self.d.switch_to.window(self.d.window_handles[0])
                Portal_Menu_pom().click_on_logout_button()
                return True
            else:
                self.d.close()
                self.d.switch_to.window(self.d.window_handles[0])
                Portal_Menu_pom().click_on_logout_button()
                return False
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\notification_dashboard_validation_failed_pg_03.png")
                return False

    def click_on_audit_report_button(self):
        try:
            time.sleep(Base_Class.one_second)
            audit_report_button = self.d.find_element(By.XPATH,
                                                      Read_Portal_Menu_Components().audit_log_reports_btn_xpath())
            time.sleep(Base_Class.one_second)
            audit_report_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_portal_menu_audit_"
                    f"report_pg_03.png"
                )
                return False

    def audit_reports_button_validation(self):
        try:
            self.login_before()
            self.click_on_audit_report_button()
            time.sleep(Base_Class.one_second)
            self.d.switch_to.window(self.d.window_handles[1])
            audit_report_validation = self.d.find_element(By.XPATH,
                                                          Read_Portal_Menu_Components().
                                                          audit_log_reports_validation())
            if audit_report_validation.is_displayed():
                self.d.close()
                self.d.switch_to.window(self.d.window_handles[0])
                Portal_Menu_pom().click_on_logout_button()
                return True
            else:
                self.d.close()
                self.d.switch_to.window(self.d.window_handles[0])
                Portal_Menu_pom().click_on_logout_button()
                return False
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\notification_dashboard_validation_failed_pg_03.png")
                return False

    def click_on_copyright_button(self):
        try:
            time.sleep(Base_Class.one_second)
            copyright_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().copyright_btn_by_xpath())
            # self.d.execute_script("arguments[0].click();", copyright_button)
            time.sleep(Base_Class.one_second)
            copyright_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_copyright_pg_03.png")
                return False

    def copyright_button_validation(self):
        try:
            Portal_Menu_pom().login_before()
            Portal_Menu_pom().click_on_copyright_button()
            time.sleep(Base_Class.one_second)
            copyright_validation = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().copyright_validation_by_xpath())
            assert copyright_validation.text.__contains__(
                Read_Portal_Menu_Components().copyright_version_text_validation())
            assert copyright_validation.text.__contains__(
                Read_Portal_Menu_Components().copyright_year_text_validation())
            Portal_Menu_pom().close_all_panel_one_by_one()
            Portal_Menu_pom().click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\notification_copyright_validation_failed_pg_03.png")
                return False

    def click_on_profile_button(self):
        try:
            time.sleep(Base_Class.one_second)
            profile_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().profile_btn_by_xpath())
            profile_button.click()
            time.sleep(Base_Class.one_second)
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_profile_pg_03.png")
                return False

    def profile_button_validation(self):
        try:
            Portal_Menu_pom().login_before()
            Portal_Menu_pom().click_on_profile_button()
            time.sleep(Base_Class.one_second)
            profile_validation = self.d.find_element(By.XPATH,
                                                     Read_Portal_Menu_Components().profile_validation_by_xpath())
            actual_profile_validation = profile_validation.text
            excepted_profile_validation = Read_Portal_Menu_Components().validation_user_panel_text()
            assert actual_profile_validation == excepted_profile_validation
            time.sleep(Base_Class.one_second)
            if profile_validation.is_displayed():
                Portal_Menu_pom().close_all_panel_one_by_one()
                Portal_Menu_pom().click_on_logout_button()
                return True
            else:
                Portal_Menu_pom().close_all_panel_one_by_one()
                Portal_Menu_pom().click_on_logout_button()
                return False
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\notification_profile_validation_failed_pg_03.png")
                return False

    def click_on_logout_button(self):
        try:
            # time.sleep(Base_Class.one_second)
            # logout_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().logout_btn_by_xpath())
            # time.sleep(Base_Class.one_second)
            # logout_button.click()
            # time.sleep(Base_Class.one_second)
            print("logout")
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_logout_pg_03.png")
                return False

    def face_first_logo_validation(self):
        try:
            Portal_Menu_pom().login_before()
            time.sleep(Base_Class.one_second)
            logo = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().logo_by_xpath())
            p = self.d.execute_script(
                "return arguments[0].complete " + "&& typeof arguments[0].naturalWidth != \"undefined\" " + "&& arguments[0].naturalWidth > 0",
                logo)
            result = p
            if result:
                Portal_Menu_pom().click_on_logout_button()
                return True
            else:
                Portal_Menu_pom().click_on_logout_button()
                return False
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\logo_validation_failed_pg_03.png")
                return False

    def logout_button_validation(self):
        try:
            Portal_Menu_pom().login_before()
            Portal_Menu_pom().click_on_logout_button()
            time.sleep(Base_Class.one_second)
            logout_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().logout_btn_by_xpath())
            actual_logout_button_text = logout_button.text
            expected_logout_button_text = Read_Portal_Menu_Components().logout_button_expected_text()
            assert actual_logout_button_text == expected_logout_button_text
            self.d.execute_script("arguments[0].click();", logout_button)
            return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\notification_logout_validation_failed_pg_03.png")
                return False

    def reset_password(self):
        try:
            Portal_Menu_pom().login_before_one()
            time.sleep(Base_Class.one_second)

            password = [Read_Portal_Menu_Components().new_password(), Read_Portal_Menu_Components().get_password(),
                        Read_Portal_Menu_Components().new_password()]
            for i in range(2):
                Portal_Menu_pom().click_on_profile_button()
                action_button = self.d.find_element(By.XPATH,
                                                    Read_Portal_Menu_Components().user_profile_action_btn_by_xpath())
                action_button.click()
                time.sleep(Base_Class.one_second)
                edit_button = self.d.find_element(By.XPATH,
                                                  Read_Portal_Menu_Components().user_profile_edit_btn_by_xpath())
                edit_button.click()
                name_field = self.d.find_element(By.XPATH,
                                                 Read_Portal_Menu_Components().rest_password_first_name_input())
                last_name_field = self.d.find_element(By.XPATH,
                                                      Read_Portal_Menu_Components().rest_password_last_name_input())
                if name_field.get_attribute("value") is "":
                    name_field.send_keys(Read_Portal_Menu_Components().first_name())
                if last_name_field.get_attribute("value") is "":
                    last_name_field.send_keys(Read_Portal_Menu_Components().last_name())
                current_password = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().current_password_filed_by_xpath())
                current_password.send_keys(password[i + 1])
                new_password = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().new_password_filed_by_xpath())
                new_password.send_keys(password[i])
                confirm_password = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().confirm_password_filed_by_xpath())
                confirm_password.send_keys(password[i])
                time.sleep(Base_Class.one_second)
                save_btn = self.d.find_element(By.XPATH,
                                               Read_Portal_Menu_Components().save_new_password())
                save_btn.click()
                password_updated = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().password_change_validation())
                actual_password_change_success_msg = password_updated.text
                expected_password_change_success_msg = Read_Portal_Menu_Components(). \
                    rest_password_success_msg_validation_text()
                assert actual_password_change_success_msg == expected_password_change_success_msg
                password_updated.is_displayed()
                Portal_Menu_pom().close_all_panel_one_by_one()
            Portal_Menu_pom().click_on_logout_button()
            return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\notification_users_validation_failed_pg_03.png")
                return False

    def current_and_new_password_not_same_validation(self):
        try:
            Portal_Menu_pom().login_before()
            time.sleep(Base_Class.one_second)

            # password = [Read_Portal_Menu_Components().new_password()]

            Portal_Menu_pom().click_on_profile_button()
            action_button = self.d.find_element(By.XPATH,
                                                Read_Portal_Menu_Components().user_profile_action_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            action_button.click()
            time.sleep(Base_Class.one_second)
            edit_button = self.d.find_element(By.XPATH,
                                              Read_Portal_Menu_Components().user_profile_edit_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            edit_button.click()
            current_password = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().current_password_filed_by_xpath())
            name_field = self.d.find_element(By.XPATH,
                                             Read_Portal_Menu_Components().rest_password_first_name_input())
            last_name_field = self.d.find_element(By.XPATH,
                                                  Read_Portal_Menu_Components().rest_password_last_name_input())
            if name_field.get_attribute("value") is "":
                name_field.send_keys(Read_Portal_Menu_Components().first_name())
            if last_name_field.get_attribute("value") is "":
                last_name_field.send_keys(Read_Portal_Menu_Components().last_name())
            current_password.send_keys(Read_Portal_Menu_Components().get_password())
            new_password = self.d.find_element(By.XPATH,
                                               Read_Portal_Menu_Components().new_password_filed_by_xpath())
            new_password.send_keys(Read_Portal_Menu_Components().get_password())
            confirm_password = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().confirm_password_filed_by_xpath())
            confirm_password.send_keys(Read_Portal_Menu_Components().get_password())
            time.sleep(Base_Class.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Read_Portal_Menu_Components().save_new_password())
            save_btn.click()
            validation_msg = self.d.find_element(By.XPATH,
                                                 Read_Portal_Menu_Components().
                                                 current_and_new_password_not_same_validation())
            actual_validation_msg = validation_msg.text
            expected_validation_msg = Read_Portal_Menu_Components().current_psw_and_new_psw_not_same_validation()
            assert actual_validation_msg == expected_validation_msg
            cancel_btn = self.d.find_element(By.XPATH,
                                             Read_Portal_Menu_Components().user_panel_cancel_btn())
            time.sleep(Base_Class.one_second)
            cancel_btn.click()
            closed_button = self.d.find_element(By.XPATH,
                                                Read_Portal_Menu_Components().user_panel_close_btn())
            time.sleep(Base_Class.one_second)
            closed_button.click()
            Portal_Menu_pom().click_on_logout_button()
            return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\notification_users_validation_failed_pg_03.png")
                return False

    def set_upper_case_password(self):
        try:
            Portal_Menu_pom().login_before()
            time.sleep(Base_Class.one_second)

            password = [Read_Portal_Menu_Components().get_upper_case_password(),
                        Read_Portal_Menu_Components().get_password(),
                        Read_Portal_Menu_Components().get_upper_case_password()]
            for i in range(2):
                Portal_Menu_pom().click_on_profile_button()
                action_button = self.d.find_element(By.XPATH,
                                                    Read_Portal_Menu_Components().user_profile_action_btn_by_xpath())
                time.sleep(Base_Class.one_second)
                action_button.click()
                time.sleep(Base_Class.one_second)
                edit_button = self.d.find_element(By.XPATH,
                                                  Read_Portal_Menu_Components().user_profile_edit_btn_by_xpath())
                time.sleep(Base_Class.one_second)
                edit_button.click()
                name_field = self.d.find_element(By.XPATH,
                                                 Read_Portal_Menu_Components().rest_password_first_name_input())
                last_name_field = self.d.find_element(By.XPATH,
                                                      Read_Portal_Menu_Components().rest_password_last_name_input())
                if name_field.get_attribute("value") is "":
                    name_field.send_keys(Read_Portal_Menu_Components().first_name())
                if last_name_field.get_attribute("value") is "":
                    last_name_field.send_keys(Read_Portal_Menu_Components().last_name())
                current_password = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().current_password_filed_by_xpath())
                current_password.send_keys(password[i + 1])
                new_password = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().new_password_filed_by_xpath())
                new_password.send_keys(password[i])
                confirm_password = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().confirm_password_filed_by_xpath())
                confirm_password.send_keys(password[i])
                time.sleep(Base_Class.one_second)
                save_btn = self.d.find_element(By.XPATH,
                                               Read_Portal_Menu_Components().save_new_password())
                time.sleep(Base_Class.one_second)
                save_btn.click()
                password_updated = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().password_change_validation())
                actual_password_change_success_msg = password_updated.text
                expected_password_change_success_msg = Read_Portal_Menu_Components(). \
                    rest_password_success_msg_validation_text()
                assert actual_password_change_success_msg == expected_password_change_success_msg
                Portal_Menu_pom().close_all_panel_one_by_one()
            Portal_Menu_pom().click_on_logout_button()
            return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\upper_case_password_failed_pg_03.png")
                return False

    def set_lower_case_password(self):
        try:
            Portal_Menu_pom().login_before()
            time.sleep(Base_Class.one_second)

            password = [Read_Portal_Menu_Components().get_lower_case_password(),
                        Read_Portal_Menu_Components().get_password(),
                        Read_Portal_Menu_Components().get_lower_case_password()]
            for i in range(2):
                Portal_Menu_pom().click_on_profile_button()
                action_button = self.d.find_element(By.XPATH,
                                                    Read_Portal_Menu_Components().user_profile_action_btn_by_xpath())
                action_button.click()
                time.sleep(Base_Class.one_second)
                edit_button = self.d.find_element(By.XPATH,
                                                  Read_Portal_Menu_Components().user_profile_edit_btn_by_xpath())
                time.sleep(Base_Class.one_second)
                edit_button.click()
                name_field = self.d.find_element(By.XPATH,
                                                 Read_Portal_Menu_Components().rest_password_first_name_input())
                last_name_field = self.d.find_element(By.XPATH,
                                                      Read_Portal_Menu_Components().rest_password_last_name_input())
                if name_field.get_attribute("value") is "":
                    name_field.send_keys(Read_Portal_Menu_Components().first_name())
                if last_name_field.get_attribute("value") is "":
                    last_name_field.send_keys(Read_Portal_Menu_Components().last_name())
                current_password = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().current_password_filed_by_xpath())
                current_password.send_keys(password[i + 1])
                new_password = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().new_password_filed_by_xpath())
                new_password.send_keys(password[i])
                confirm_password = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().confirm_password_filed_by_xpath())
                confirm_password.send_keys(password[i])
                time.sleep(Base_Class.one_second)
                save_btn = self.d.find_element(By.XPATH,
                                               Read_Portal_Menu_Components().save_new_password())
                time.sleep(Base_Class.one_second)
                save_btn.click()
                password_updated = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().password_change_validation())
                actual_password_change_success_msg = password_updated.text
                expected_password_change_success_msg = Read_Portal_Menu_Components(). \
                    rest_password_success_msg_validation_text()
                assert actual_password_change_success_msg == expected_password_change_success_msg
                Portal_Menu_pom().close_all_panel_one_by_one()
            Portal_Menu_pom().click_on_logout_button()
            return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\lower_case_password_failed_pg_03.png")
                return False

    def set_special_character_password(self):
        try:
            Portal_Menu_pom().login_before()
            time.sleep(Base_Class.one_second)

            password = [Read_Portal_Menu_Components().get_special_character_password(),
                        Read_Portal_Menu_Components().get_password(),
                        Read_Portal_Menu_Components().get_special_character_password()]
            for i in range(2):
                Portal_Menu_pom().click_on_profile_button()
                action_button = self.d.find_element(By.XPATH,
                                                    Read_Portal_Menu_Components().user_profile_action_btn_by_xpath())
                action_button.click()
                time.sleep(Base_Class.one_second)
                edit_button = self.d.find_element(By.XPATH,
                                                  Read_Portal_Menu_Components().user_profile_edit_btn_by_xpath())
                time.sleep(Base_Class.one_second)
                edit_button.click()
                name_field = self.d.find_element(By.XPATH,
                                                 Read_Portal_Menu_Components().rest_password_first_name_input())
                last_name_field = self.d.find_element(By.XPATH,
                                                      Read_Portal_Menu_Components().rest_password_last_name_input())
                if name_field.get_attribute("value") is "":
                    name_field.send_keys(Read_Portal_Menu_Components().first_name())
                if last_name_field.get_attribute("value") is "":
                    last_name_field.send_keys(Read_Portal_Menu_Components().last_name())
                current_password = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().current_password_filed_by_xpath())
                current_password.send_keys(password[i + 1])
                new_password = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().new_password_filed_by_xpath())
                new_password.send_keys(password[i])
                confirm_password = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().confirm_password_filed_by_xpath())
                confirm_password.send_keys(password[i])
                time.sleep(Base_Class.one_second)
                save_btn = self.d.find_element(By.XPATH,
                                               Read_Portal_Menu_Components().save_new_password())
                time.sleep(Base_Class.one_second)
                save_btn.click()
                password_updated = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().password_change_validation())
                actual_password_change_success_msg = password_updated.text
                expected_password_change_success_msg = Read_Portal_Menu_Components(). \
                    rest_password_success_msg_validation_text()
                assert actual_password_change_success_msg == expected_password_change_success_msg
                Portal_Menu_pom().close_all_panel_one_by_one()
            Portal_Menu_pom().click_on_logout_button()
            return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\lower_case_password_failed_pg_03.png")
                return False

    def set_less_than_eight_character_password(self):
        try:
            Portal_Menu_pom().login_before()
            time.sleep(Base_Class.one_second)

            # password = [Read_Portal_Menu_Components().get_less_than_eight_character_password(),
            # Read_Portal_Menu_Components().get_password()]

            Portal_Menu_pom().click_on_profile_button()
            action_button = self.d.find_element(By.XPATH,
                                                Read_Portal_Menu_Components().user_profile_action_btn_by_xpath())
            action_button.click()
            time.sleep(Base_Class.one_second)
            edit_button = self.d.find_element(By.XPATH,
                                              Read_Portal_Menu_Components().user_profile_edit_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            edit_button.click()
            name_field = self.d.find_element(By.XPATH,
                                             Read_Portal_Menu_Components().rest_password_first_name_input())
            last_name_field = self.d.find_element(By.XPATH,
                                                  Read_Portal_Menu_Components().rest_password_last_name_input())
            if name_field.get_attribute("value") is "":
                name_field.send_keys(Read_Portal_Menu_Components().first_name())
            if last_name_field.get_attribute("value") is "":
                last_name_field.send_keys(Read_Portal_Menu_Components().last_name())
            current_password = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().current_password_filed_by_xpath())
            current_password.send_keys(Read_Portal_Menu_Components().get_password())
            new_password = self.d.find_element(By.XPATH,
                                               Read_Portal_Menu_Components().new_password_filed_by_xpath())
            new_password.send_keys(Read_Portal_Menu_Components().get_less_than_eight_character_password())
            confirm_password = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().confirm_password_filed_by_xpath())
            confirm_password.send_keys(Read_Portal_Menu_Components().get_less_than_eight_character_password())
            time.sleep(Base_Class.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Read_Portal_Menu_Components().save_new_password())
            time.sleep(Base_Class.one_second)
            save_btn.click()
            less_char_validation = self.d.find_element(By.XPATH,
                                                       Read_Portal_Menu_Components().
                                                       less_than_eight_character_validation_password())
            actual_less_char_validation = less_char_validation.text
            expected_less_char_validation = Read_Portal_Menu_Components().less_than_eight_char_password_validation()
            assert actual_less_char_validation == expected_less_char_validation
            cancel_btn = self.d.find_element(By.XPATH,
                                             Read_Portal_Menu_Components().user_panel_cancel_btn())
            cancel_btn.click()
            closed_button = self.d.find_element(By.XPATH,
                                                Read_Portal_Menu_Components().user_panel_close_btn())
            closed_button.click()

            Portal_Menu_pom().click_on_logout_button()
            return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\lower_case_password_failed_pg_03.png")
                return False

    def close_all_panel_one_by_one(self):
        try:
            close_panel_list = self.d.find_elements(By.XPATH,
                                                    Read_Tags_Components().close_panel_one_by_one_list())
            for i in close_panel_list:
                i.click()
            return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\close_panel_one_by_one.png")
                return False

    def close_all_panel_button(self):
        try:
            Portal_Menu_pom().login_before()
            time.sleep(Base_Class.one_second)
            self.click_on_enrollments_button()
            cloud_menu_button = self.d.find_element(By.XPATH,
                                                    Read_Portal_Menu_Components().portal_menu_cloud_menu_btn_by_xpath())
            cloud_menu_button.click()
            self.click_on_tags_button()
            time.sleep(Base_Class.one_second)
            cloud_menu_button.click()
            self.click_on_visitors_search_button()
            cloud_menu_button = self.d.find_element(By.XPATH,
                                                    Read_Portal_Menu_Components().portal_menu_cloud_menu_btn_by_xpath())
            cloud_menu_button.click()
            closed_all_button = self.d.find_element(By.XPATH,
                                                    Read_Portal_Menu_Components().portal_menu_closed_all_btn_by_xpath())
            actual_closed_all_panel_text = closed_all_button.text
            expected_closed_all_panel_text = Read_Portal_Menu_Components().close_all_panel_expected_text()
            assert actual_closed_all_panel_text == expected_closed_all_panel_text
            closed_all_button.click()
            time.sleep(Base_Class.one_second)
            Portal_Menu_pom().click_on_logout_button()
            return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\close_panel_one_by_one.png")
                return False
