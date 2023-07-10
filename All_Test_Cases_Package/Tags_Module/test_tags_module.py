from pathlib import Path

import pytest
from All_POM_Package.Tags_Module.Tags_Module_POM import Tags_Module_pom
from All_Test_Cases_Package.conftest import Base_Class


class Test_Tags_Module(Base_Class):
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
    def test_TC_TAG_01(self):
        self.logger.info("test_TC_TAG_01 execution started..")
        if Tags_Module_pom().create_tags_for_serious_event():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_01.png")
            assert False

    @pytest.mark.p1
    def test_TC_TAG_02(self):
        self.logger.info("test_TC_TAG_02 execution started..")
        if Tags_Module_pom().create_tags_for_non_serious_event():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_02.png")
            assert False

    @pytest.mark.p1
    def test_TC_TAG_03(self):
        self.logger.info("test_TC_TAG_03 execution started..")
        if Tags_Module_pom().tags_search_functionality():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_03_verify.png")
            assert False

    @pytest.mark.p1
    def test_TC_TAG_04(self):
        self.logger.info("test_TC_TAG_04 execution started..")
        if Tags_Module_pom().filter_serious_event_tags_varify_it():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_04.png")
            assert False

    @pytest.mark.p1
    def test_TC_TAG_05(self):
        self.logger.info("test_TC_TAG_05 execution started..")
        if Tags_Module_pom().filter_non_serious_event_tags_varify_it():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_05.png")
            assert False

    @pytest.mark.p1
    def test_TC_TAG_06(self):
        self.logger.info("test_TC_TAG_06 execution started..")
        if Tags_Module_pom().duplicate_tags_not_create_validation():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_06.png")
            assert False

    @pytest.mark.p1
    def test_TC_TAG_07(self):
        self.logger.info("test_TC_TAG_07 execution started..")
        if Tags_Module_pom().update_serious_event_tag_name():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_07.png")
            assert False

    @pytest.mark.p1
    def test_TC_TAG_08(self):
        self.logger.info("test_TC_TAG_08 execution started..")
        if Tags_Module_pom().delete_all_tags():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_08.png")
            assert False

    @pytest.mark.p1
    def test_TC_TAG_09(self):
        self.logger.info("test_TC_TAG_09 execution started..")
        if Tags_Module_pom().verify_deterred_tag_is_present_at_first():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_09.png")
            assert False

    @pytest.mark.p2
    def test_TC_TAG_10(self):
        self.logger.info("test_TC_TAG_010 execution started..")
        if Tags_Module_pom().close_panel_and_discard_changes_verify():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_010.png")
            assert False
