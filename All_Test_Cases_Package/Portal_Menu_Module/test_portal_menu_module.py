from pathlib import Path

import pytest

from All_POM_Package.Portal_Menu_Module.Portal_Menu_POM import Portal_Menu_pom
from All_Test_Cases_Package.conftest import Base_Class


class Test_Portal_Menu_Test_Cases(Base_Class):
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

    @pytest.mark.p1
    def test_TC_PM_24(self):
        self.logger.info("test_TC_PM_24 execution started..")
        if Portal_Menu_pom().reset_password():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_rest_password.png")
            assert False

    # @pytest.mark.p1
    # def test_TC_PM_26(self):
    #     self.logger.info("test_TC_PM_26 execution started..")
    #     if Portal_Menu_pom().current_and_new_password_not_same_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(
    #             f"{self.screenshots_path}\\test_verify_current_and_new_password_not_same_validation.png")
    #         assert False
    # 
    # @pytest.mark.p2
    # def test_TC_PM_27(self):
    #     self.logger.info("test_TC_PM_27 execution started..")
    #     if Portal_Menu_pom().set_upper_case_password():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_upper_case_password.png")
    #         assert False
    # 
    # @pytest.mark.p2
    # def test_TC_PM_28(self):
    #     self.logger.info("test_TC_PM_28 execution started..")
    #     if Portal_Menu_pom().set_lower_case_password():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_lower_case_password.png")
    #         assert False
    # 
    # @pytest.mark.p2
    # def test_TC_PM_29(self):
    #     self.logger.info("test_TC_PM_29 execution started..")
    #     if Portal_Menu_pom().set_special_character_password():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_special_character_password.png")
    #         assert False
    # 
    # @pytest.mark.p2
    # def test_TC_PM_30(self):
    #     self.logger.info("test_TC_PM_30 execution started..")
    #     if Portal_Menu_pom().set_less_than_eight_character_password():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_special_character_password.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_1(self):
    #     self.logger.info("test_TC_PM_1 execution started..")
    #     if Portal_Menu_pom().event_button_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_event_button.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_2(self):
    #     self.logger.info("test_TC_PM_2 execution started..")
    #     if Portal_Menu_pom().tags_button_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_tags_button.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_3(self):
    #     self.logger.info("test_TC_PM_3 execution started..")
    #     if Portal_Menu_pom().identify_enroll_button_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_identify_enroll_button.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_4(self):
    #     self.logger.info("test_TC_PM_4 execution started..")
    #     if Portal_Menu_pom().detect_faces_button_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_detect_faces_button.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_5(self):
    #     self.logger.info("test_TC_PM_5 execution started..")
    #     if Portal_Menu_pom().enrollments_button_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_enrollments_button.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_6(self):
    #     self.logger.info("test_TC_PM_6 execution started..")
    #     if Portal_Menu_pom().enrollments_groups_button_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_enrollments_groups_button.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_7(self):
    #     self.logger.info("test_TC_PM_7 execution started..")
    #     if Portal_Menu_pom().notification_groups_button_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_notification_groups_button.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_8(self):
    #     self.logger.info("test_TC_PM_8 execution started..")
    #     if Portal_Menu_pom().visitors_button_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_visitors_button.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_9(self):
    #     self.logger.info("test_TC_PM_9 execution started..")
    #     if Portal_Menu_pom().visitors_search_button_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_visitors_search_button.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_10(self):
    #     self.logger.info("test_TC_PM_10 execution started..")
    #     if Portal_Menu_pom().visitors_search_button_job_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_visitors_search_job_button.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_11(self):
    #     self.logger.info("test_TC_PM_11 execution started..")
    #     if Portal_Menu_pom().notes_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_notes_button.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_12(self):
    #     self.logger.info("test_TC_PM_12 execution started..")
    #     if Portal_Menu_pom().locations_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_locations_button.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_13(self):
    #     self.logger.info("test_TC_PM_13 execution started..")
    #     if Portal_Menu_pom().users_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_users_button.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_14(self):
    #     self.logger.info("test_TC_PM_14 execution started..")
    #     if Portal_Menu_pom().users_roles_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_users_roles_button.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_15(self):
    #     self.logger.info("test_TC_PM_15 execution started..")
    #     if Portal_Menu_pom().zones_button_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_zones_button.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_16(self):
    #     self.logger.info("test_TC_PM_16 execution started..")
    #     if Portal_Menu_pom().account_button_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_account_button.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_17(self):
    #     self.logger.info("test_TC_PM_17 execution started..")
    #     if Portal_Menu_pom().reporting_button_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_reporting_button.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_18(self):
    #     self.logger.info("test_TC_PM_18 execution started..")
    #     if Portal_Menu_pom().notifier_button_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_notifier_button.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_19(self):
    #     self.logger.info("test_TC_PM_19 execution started..")
    #     if Portal_Menu_pom().dashboard_button_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_dashboard_button.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_31(self):
    #     self.logger.info("test_TC_PM_31 execution started..")
    #     if Portal_Menu_pom().audit_reports_button_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_dashboard_button.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_20(self):
    #     self.logger.info("test_TC_PM_20 execution started..")
    #     if Portal_Menu_pom().close_all_panel_button():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_close_all_panel.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_21(self):
    #     self.logger.info("test_TC_PM_21 execution started..")
    #     if Portal_Menu_pom().copyright_button_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_copyright_button.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_22(self):
    #     self.logger.info("test_TC_PM_22 execution started..")
    #     if Portal_Menu_pom().profile_button_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_profile_button.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_23(self):
    #     self.logger.info("test_TC_PM_23 execution started..")
    #     if Portal_Menu_pom().face_first_logo_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_logo.png")
    #         assert False
    # 
    # @pytest.mark.p1
    # def test_TC_PM_25(self):
    #     self.logger.info("test_TC_PM_25 execution started..")
    #     if Portal_Menu_pom().logout_button_validation():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_verify_logout_button.png")
    #         assert False
