from pathlib import Path

import pytest

from All_POM_Package.Notes_Module.Notes_Search_Filter_Combination_POM import Notes_search_filter_combination_pom
from All_Test_Cases_Package.conftest import Base_Class


class Test_Notes_Search_Filter_Combination(Base_Class):
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
    def test_TC_NSFC_01(self):
        self.logger.info("test_TC_NSFC_01 execution started..")
        if Notes_search_filter_combination_pom().notes_with_no_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_01.png")
            assert False

    @pytest.mark.p1
    def test_TC_NSFC_02(self):
        self.logger.info("test_TC_NSFC_02 execution started..")
        if Notes_search_filter_combination_pom().notes_with_sort_by_Case_Subject_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_02.png")
            assert False

    @pytest.mark.p1
    def test_TC_NSFC_03(self):
        self.logger.info("test_TC_NSFC_03 execution started..")
        if Notes_search_filter_combination_pom().notes_with_sort_by_location_store_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_03.png")
            assert False

    @pytest.mark.p1
    def test_TC_NSFC_04(self):
        self.logger.info("test_TC_NSFC_04 execution started..")
        if Notes_search_filter_combination_pom(). \
                notes_with_Sort_by_Location_Store_and_Sort_by_Case_Subject_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_04.png")
            assert False

    @pytest.mark.p1
    def test_TC_NSFC_05(self):
        self.logger.info("test_TC_NSFC_05 execution started..")
        if Notes_search_filter_combination_pom().notes_with_Case_Subject_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_05.png")
            assert False

    @pytest.mark.p1
    def test_TC_NSFC_06(self):
        self.logger.info("test_TC_NSFC_06 execution started..")
        if Notes_search_filter_combination_pom().notes_with_Case_Subject_and_Sort_by_Case_Subject_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_06.png")
            assert False

    @pytest.mark.p1
    def test_TC_NSFC_07(self):
        self.logger.info("test_TC_NSFC_07 execution started..")
        if Notes_search_filter_combination_pom().\
                notes_with_filter_Case_Subject_and_Sort_by_Location_Store_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_07.png")
            assert False

    @pytest.mark.p1
    def test_TC_NSFC_08(self):
        self.logger.info("test_TC_NSFC_08 execution started..")
        if Notes_search_filter_combination_pom(). \
                notes_with_Case_Subject_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_08.png")
            assert False

    @pytest.mark.p1
    def test_TC_NSFC_09(self):
        self.logger.info("test_TC_NSFC_09 execution started..")
        if Notes_search_filter_combination_pom(). \
                notes_with_Location_Store_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_09.png")
            assert False

    @pytest.mark.p1
    def test_TC_NSFC_010(self):
        self.logger.info("test_TC_NSFC_010 execution started..")
        if Notes_search_filter_combination_pom(). \
                notes_with_Location_Store_and_Sort_by_Case_Subject_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_010.png")
            assert False

    @pytest.mark.p1
    def test_TC_NSFC_011(self):
        self.logger.info("test_TC_NSFC_011 execution started..")
        if Notes_search_filter_combination_pom(). \
                notes_with_Location_Store_and_Sort_by_Location_Store_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_011.png")
            assert False

    @pytest.mark.p1
    def test_TC_NSFC_012(self):
        self.logger.info("test_TC_NSFC_012 execution started..")
        if Notes_search_filter_combination_pom(). \
                notes_with_Location_Store_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_012.png")
            assert False

    @pytest.mark.p1
    def test_TC_NSFC_013(self):
        self.logger.info("test_TC_NSFC_013 execution started..")
        if Notes_search_filter_combination_pom(). \
                notes_with_Location_Store_and_Case_Subject_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_013.png")
            assert False

    @pytest.mark.p1
    def test_TC_NSFC_014(self):
        self.logger.info("test_TC_NSFC_014 execution started..")
        if Notes_search_filter_combination_pom(). \
                notes_with_Location_Store_Case_Subject_and_Sort_by_Case_Subject_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_014.png")
            assert False

    @pytest.mark.p1
    def test_TC_NSFC_015(self):
        self.logger.info("test_TC_NSFC_015 execution started..")
        if Notes_search_filter_combination_pom(). \
                notes_with_Location_Store_Case_Subject_and_Sort_by_Location_Store_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_015.png")
            assert False

    @pytest.mark.p1
    def test_TC_NSFC_016(self):
        self.logger.info("test_TC_NSFC_016 execution started..")
        if Notes_search_filter_combination_pom().\
                notes_with_Location_Store_Case_Subject_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_016.png")
            assert False

