from pathlib import Path

import pytest

from All_POM_Package.Visitors_Module.Visitors_Search_Filter_Combination_POM import \
    Visitors_Search_Filter_Combination_POM
from All_Test_Cases_Package.conftest import Base_Class


class Test_visitors_search_filter_combination(Base_Class):
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
            # self.logger = Base_Class.logger_object()
            self.screenshots_path = f"{Path(__file__).parent.parent.parent}\\Reports\\Screenshots"
            print("\nsetup end")

        except Exception as ex:
            print("\nException in Test_Deployment_Manager_Test_Cases/setup_method: ", ex)

    # @pytest.mark.p1
    # def test1(self):
    #     if Visitors_Module_pom().trial():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_0032.png")
    #         assert False

    def test_TC_SVF_01(self):
        if Visitors_Search_Filter_Combination_POM().search_visitors_with_no_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_01.png")
            assert False

    def test_TC_SVF_02(self):
        if Visitors_Search_Filter_Combination_POM().search_visitors_with_hierarchy_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_03.png")
            assert False

    def test_TC_SVF_03(self):
        if Visitors_Search_Filter_Combination_POM().search_visitors_with_gender_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_03.png")
            assert False

    def test_TC_SVF_04(self):
        if Visitors_Search_Filter_Combination_POM().search_visitors_with_gender_and_hierarchy_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_01.png")
            assert False

    def test_TC_SVF_05(self):
        if Visitors_Search_Filter_Combination_POM().search_visitors_with_age_range_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_05.png")
            assert False

    def test_TC_SVF_06(self):
        if Visitors_Search_Filter_Combination_POM().search_visitors_with_age_range_and_hierarchy_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_06.png")
            assert False

    def test_TC_SVF_07(self):
        if Visitors_Search_Filter_Combination_POM().search_visitors_with_age_range_and_gender_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_07.png")
            assert False

    def test_TC_SVF_08(self):
        if Visitors_Search_Filter_Combination_POM()\
                .search_visitors_with_age_range_gender_and_hierarchy_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_08.png")
            assert False

    def test_TC_SVF_09(self):
        if Visitors_Search_Filter_Combination_POM().search_visitors_with_datetime_range_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_09.png")
            assert False

    def test_TC_SVF_10(self):
        if Visitors_Search_Filter_Combination_POM().search_visitors_with_datetime_range_and_hierarchy_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_10.png")
            assert False

    def test_TC_SVF_11(self):
        if Visitors_Search_Filter_Combination_POM().search_visitors_with_datetime_range_and_gender_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_11.png")
            assert False

    def test_TC_SVF_12(self):
        if Visitors_Search_Filter_Combination_POM()\
                .search_visitors_with_datetime_range_gender_and_hierarchy_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_12.png")
            assert False

    def test_TC_SVF_13(self):
        if Visitors_Search_Filter_Combination_POM().search_visitors_with_datetime_and_age_range_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_13.png")
            assert False

    def test_TC_SVF_14(self):
        if Visitors_Search_Filter_Combination_POM()\
                .search_visitors_with_datetime_age_range_and_hierarchy_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_14.png")
            assert False

    def test_TC_SVF_15(self):
        if Visitors_Search_Filter_Combination_POM()\
                .search_visitors_with_datetime_age_range_and_gender_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_15.png")
            assert False

    def test_TC_SVF_16(self):
        if Visitors_Search_Filter_Combination_POM()\
                .search_visitors_with_datetime_age_range_gender_and_hierarchy_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SVF_16.png")
            assert False



