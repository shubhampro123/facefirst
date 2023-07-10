from pathlib import Path

import pytest

from All_POM_Package.Visitor_Search_Jobs_Module.VisitorSearchJob_Filter_combination_POM import \
    VisitorSearchJob_Filter_combination_pom
from All_Test_Cases_Package.conftest import Base_Class


class Test_Visitor_Search_Jobs_Module_Filter_Combination(Base_Class):
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
    def test_TC_VSJ_01(self):
        if VisitorSearchJob_Filter_combination_pom().visitor_search_jobs_with_no_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VSJ_01.png")
            assert False

    @pytest.mark.p1
    def test_TC_VSJ_02(self):
        if VisitorSearchJob_Filter_combination_pom() \
                .visitor_search_jobs_with_include_jobs_for_all_user_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VSJ_02.png")
            assert False

    @pytest.mark.p1
    def test_TC_VSJ_03(self):
        if VisitorSearchJob_Filter_combination_pom() \
                .visitor_search_jobs_with_include_jobs_with_deleted_results_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VSJ_03.png")
            assert False

    @pytest.mark.p1
    def test_TC_VSJ_04(self):
        if VisitorSearchJob_Filter_combination_pom() \
                .visitor_search_jobs_with_include_jobs_with_deleted_results_and_for_all_users_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VSJ_04.png")
            assert False

    @pytest.mark.p1
    def test_TC_VSJ_05(self):
        if VisitorSearchJob_Filter_combination_pom() \
                .visitor_search_jobs_with_only_incomplete_jobs_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VSJ_05.png")
            assert False

    @pytest.mark.p1
    def test_TC_VSJ_06(self):
        if VisitorSearchJob_Filter_combination_pom() \
                .visitor_search_jobs_with_only_incomplete_jobs_and_jobs_for_all_users_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VSJ_06.png")
            assert False

    @pytest.mark.p1
    def test_TC_VSJ_07(self):
        if VisitorSearchJob_Filter_combination_pom() \
                .visitor_search_jobs_with_only_incomplete_jobs_and_jobs_with_deleted_users_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VSJ_07.png")
            assert False

    @pytest.mark.p1
    def test_TC_VSJ_08(self):
        if VisitorSearchJob_Filter_combination_pom()\
                .visitor_search_jobs_with_incomplete_jobs_deleted_users_jobs_for_all_users_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VSJ_08.png")
            assert False

    @pytest.mark.p1
    def test_TC_VSJ_09(self):
        if VisitorSearchJob_Filter_combination_pom() \
                .visitor_search_jobs_with_date_range_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VSJ_09.png")
            assert False

    @pytest.mark.p1
    def test_TC_VSJ_10(self):
        if VisitorSearchJob_Filter_combination_pom() \
                .visitor_search_jobs_with_date_range_and_include_jobs_all_users_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VSJ_10.png")
            assert False

    @pytest.mark.p1
    def test_TC_VSJ_11(self):
        if VisitorSearchJob_Filter_combination_pom() \
                .visitor_search_jobs_with_date_range_and_include_jobs_deleted_users_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VSJ_11.png")
            assert False

    @pytest.mark.p1
    def test_TC_VSJ_12(self):
        if VisitorSearchJob_Filter_combination_pom() \
                .visitor_search_jobs_with_date_range_include_jobs_deleted_and_all_users_filter_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VSJ_12.png")
            assert False

    @pytest.mark.p1
    def test_TC_VSJ_13(self):
        if VisitorSearchJob_Filter_combination_pom() \
                .visitor_search_jobs_with_date_range_and_only_incomplete_jobs_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VSJ_13.png")
            assert False

    @pytest.mark.p1
    def test_TC_VSJ_14(self):
        if VisitorSearchJob_Filter_combination_pom() \
                .visitor_search_jobs_with_date_range_incomplete_jobs_and_jobs_all_users_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VSJ_14.png")
            assert False

    @pytest.mark.p1
    def test_TC_VSJ_15(self):
        if VisitorSearchJob_Filter_combination_pom() \
                .visitor_search_jobs_with_date_range_incomplete_jobs_and_jobs_deleted_users_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VSJ_15.png")
            assert False
