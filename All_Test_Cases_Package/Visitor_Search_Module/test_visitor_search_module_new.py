from pathlib import Path

import pytest

from All_POM_Package.Visitor_Search_Module.visitor_search_module_POM_new import Visitor_Search_Module_pom_new
from All_Test_Cases_Package.conftest import Base_Class


class Test_Visitor_Search_Module(Base_Class):
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

    ############################ Visitor Search with image using NATS (Demographics Enabled) #######################

    # @pytest.mark.p2
    # def test_TC_VS_001(self):
    #     self.logger.info("Visitor search module = test_TC_VS_001 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_no_search_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_001.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_VS_002(self):
    #     self.logger.info("Visitor search module = test_TC_VS_002 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_region_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_002.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_VS_003(self):
    #     self.logger.info("Visitor search module = test_TC_VS_003 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_gender_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_003.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_VS_004(self):
    #     self.logger.info("Visitor search module = test_TC_VS_004 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_region_and_gender_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_004.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_VS_005(self):
    #     self.logger.info("Visitor search module = test_TC_VS_005 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_age_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_005.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_VS_006(self):
    #     self.logger.info("Visitor search module = test_TC_VS_006 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_region_and_age_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_006.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_VS_007(self):
    #     self.logger.info("Visitor search module = test_TC_VS_007 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_age_and_gender_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_007.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_VS_008(self):
    #     self.logger.info("Visitor search module = test_TC_VS_008 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_region_age_and_gender_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_008.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_009(self):
    #     self.logger.info("Visitor search module = test_TC_VS_009 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_only_date_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_009.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_010(self):
    #     self.logger.info("Visitor search module = test_TC_VS_010 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_date_and_region_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_010.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_011(self):
    #     self.logger.info("Visitor search module = test_TC_VS_011 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_only_date_and_gender_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_011.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_012(self):
    #     self.logger.info("Visitor search module = test_TC_VS_012 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_date_and_region_and_gender_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_012.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_013(self):
    #     self.logger.info("Visitor search module = test_TC_VS_013 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_date_and_age_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_013.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_014(self):
    #     self.logger.info("Visitor search module = test_TC_VS_014 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_date_region_and_age_range_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_014.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_015(self):
    #     self.logger.info("Visitor search module = test_TC_VS_015 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_date_age_and_gender_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_015.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_016(self):
    #     self.logger.info("Visitor search module = test_TC_VS_016 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_date_region_age_range_and_gender_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_016.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_017(self):
    #     self.logger.info("Visitor search module = test_TC_VS_017 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_and_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_017.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_018(self):
    #     self.logger.info("Visitor search module = test_TC_VS_018 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_and_region_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_018.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_019(self):
    #     self.logger.info("Visitor search module = test_TC_VS_019 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_and_gender_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_019.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_020(self):
    #     self.logger.info("Visitor search module = test_TC_VS_020 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_region_and_gender_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_020.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_021(self):
    #     self.logger.info("Visitor search module = test_TC_VS_021 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_and_age_range_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_021.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_022(self):
    #     self.logger.info("Visitor search module = test_TC_VS_022 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_region_and_age_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_022.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_023(self):
    #     self.logger.info("Visitor search module = test_TC_VS_023 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_region_age_and_gender_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_023.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_024(self):
    #     self.logger.info("Visitor search module = test_TC_VS_024 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_age_and_gender_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_024.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_025(self):
    #     self.logger.info("Visitor search module = test_TC_VS_025 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_and_date_range_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_025.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_026(self):
    #     self.logger.info("Visitor search module = test_TC_VS_026 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_and_region_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_026.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_027(self):
    #     self.logger.info("Visitor search module = test_TC_VS_027 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_and_gender_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_027.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_028(self):
    #     self.logger.info("Visitor search module = test_TC_VS_028 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_region_and_gender_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_028.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_029(self):
    #     self.logger.info("Visitor search module = test_TC_VS_029 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_and_age_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_029.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_030(self):
    #     self.logger.info("Visitor search module = test_TC_VS_030 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_region_and_age_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_030.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_031(self):
    #     self.logger.info("Visitor search module = test_TC_VS_031 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_age_and_gender_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_031.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_032(self):
    #     self.logger.info("Visitor search module = test_TC_VS_032 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_date_range_region_age_and_gender_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_032.png")
    #         assert False
    #
    # ############# Visitor Search with Metadata using NATS (Demographics Enabled) ##################
    #
    # @pytest.mark.p2
    # def test_TC_VS_033(self):
    #     self.logger.info("Visitor search module = test_TC_VS_033 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_no_search_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_033.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_VS_034(self):
    #     self.logger.info("Visitor search module = test_TC_VS_034 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_region_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_034.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_VS_035(self):
    #     self.logger.info("Visitor search module = test_TC_VS_035 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_gender_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_035.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_VS_036(self):
    #     self.logger.info("Visitor search module = test_TC_VS_036 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_region_and_gender_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_036.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_VS_037(self):
    #     self.logger.info("Visitor search module = test_TC_VS_037 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_age_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_037.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_VS_038(self):
    #     self.logger.info("Visitor search module = test_TC_VS_038 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_region_and_age_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_038.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_VS_039(self):
    #     self.logger.info("Visitor search module = test_TC_VS_039 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_age_and_gender_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_039.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_VS_040(self):
    #     self.logger.info("Visitor search module = test_TC_VS_040 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_region_age_and_gender_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_040.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_041(self):
    #     self.logger.info("Visitor search module = test_TC_VS_041 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_only_date_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_041.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_042(self):
    #     self.logger.info("Visitor search module = test_TC_VS_042 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_date_and_region_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_042.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_043(self):
    #     self.logger.info("Visitor search module = test_TC_VS_043 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_only_date_and_gender_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_043.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_044(self):
    #     self.logger.info("Visitor search module = test_TC_VS_044 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_date_and_region_and_gender_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_044.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_045(self):
    #     self.logger.info("Visitor search module = test_TC_VS_045 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_date_and_age_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_045.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_046(self):
    #     self.logger.info("Visitor search module = test_TC_VS_046 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_date_region_and_age_range_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_046.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_047(self):
    #     self.logger.info("Visitor search module = test_TC_VS_047 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_date_age_and_gender_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_047.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_048(self):
    #     self.logger.info("Visitor search module = test_TC_VS_048 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_date_region_age_range_and_gender_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_048.png")
    #         assert False
    #
    # ################ Visitor Search with Image and Metadata with Nats (Demographics Enabled) #######################
    #
    # @pytest.mark.p1
    # def test_TC_VS_049(self):
    #     self.logger.info("Visitor search module = test_TC_VS_049 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_and_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_049.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_050(self):
    #     self.logger.info("Visitor search module = test_TC_VS_050 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_and_max_match_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_050.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_051(self):
    #     self.logger.info("Visitor search module = test_TC_VS_051 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_and_thresh_hold_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_051.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_052(self):
    #     self.logger.info("Visitor search module = test_TC_VS_052 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_thresh_hold_and_max_count_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_052.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_053(self):
    #     self.logger.info("Visitor search module = test_TC_VS_053 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_and_gender_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_053.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_054(self):
    #     self.logger.info("Visitor search module = test_TC_VS_054 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_gender_and_max_count_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_134.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_055(self):
    #     self.logger.info("Visitor search module = test_TC_VS_055 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_gender_and_thresh_hold_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_055.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_056(self):
    #     self.logger.info("Visitor search module = test_TC_VS_056 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_gender_thresh_hold_and_max_count_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_056.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_057(self):
    #     self.logger.info("Visitor search module = test_TC_VS_057 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_and_age_range_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_057.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_058(self):
    #     self.logger.info("Visitor search module = test_TC_VS_058 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_age_range_and_max_match_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_058.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_059(self):
    #     self.logger.info("Visitor search module = test_TC_VS_059 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_age_range_and_thresh_hold_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_059.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_060(self):
    #     self.logger.info("Visitor search module = test_TC_VS_060 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_age_range_and_max_matches_thresh_hold_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_060.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_061(self):
    #     self.logger.info("Visitor search module = test_TC_VS_061 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_age_range_and_gender_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_061.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_062(self):
    #     self.logger.info("Visitor search module = test_TC_VS_062 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_age_range_gender_and_max_matches_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_062.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_063(self):
    #     self.logger.info("Visitor search module = test_TC_VS_063 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_age_range_gender_and_thresh_hold_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_063.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_064(self):
    #     self.logger.info("Visitor search module = test_TC_VS_064 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_age_range_gender_thresh_hold_and_max_matches_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_064.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_065(self):
    #     self.logger.info("Visitor search module = test_TC_VS_065 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_and_region_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_065.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_066(self):
    #     self.logger.info("Visitor search module = test_TC_VS_066 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_region_and_max_match_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_066.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_067(self):
    #     self.logger.info("Visitor search module = test_TC_VS_067 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_region_and_thresh_hold_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_067.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_068(self):
    #     self.logger.info("Visitor search module = test_TC_VS_068 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_region_thresh_hold_and_max_count_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_068.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_069(self):
    #     self.logger.info("Visitor search module = test_TC_VS_069 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_region_and_gender_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_069.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_070(self):
    #     self.logger.info("Visitor search module = test_TC_VS_070 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_region_gender_and_max_count_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_070.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_071(self):
    #     self.logger.info("Visitor search module = test_TC_VS_071 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_region_gender_and_thresh_hold_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_071.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_072(self):
    #     self.logger.info("Visitor search module = test_TC_VS_072 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_region_gender_thresh_hold_and_max_count_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_072.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_073(self):
    #     self.logger.info("Visitor search module = test_TC_VS_073 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_region_and_age_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_073.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_074(self):
    #     self.logger.info("Visitor search module = test_TC_VS_074 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_region_age_and_max_matches_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_074.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_075(self):
    #     self.logger.info("Visitor search module = test_TC_VS_075 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_region_age_and_thresh_hold_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_075.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_076(self):
    #     self.logger.info("Visitor search module = test_TC_VS_076 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_region_age_thresh_hold_and_max_matches_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_076.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_077(self):
    #     self.logger.info("Visitor search module = test_TC_VS_077 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_region_age_and_gender_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_077.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_078(self):
    #     self.logger.info("Visitor search module = test_TC_VS_078 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_region_age_gender_and_max_match_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_078.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_079(self):
    #     self.logger.info("Visitor search module = test_TC_VS_079 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_region_age_gender_and_thresh_hold_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_159.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_080(self):
    #     self.logger.info("Visitor search module = test_TC_VS_080 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_region_age_gender_thresh_hold_and_max_match_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_080.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_081(self):
    #     self.logger.info("Visitor search module = test_TC_VS_081 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_and_date_range_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_081.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_082(self):
    #     self.logger.info("Visitor search module = test_TC_VS_082 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_and_max_count_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_082.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_083(self):
    #     self.logger.info("Visitor search module = test_TC_VS_083 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_and_thresh_hold_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_083.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_084(self):
    #     self.logger.info("Visitor search module = test_TC_VS_084 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_date_range_thresh_hold_and_max_matches_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_084.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_085(self):
    #     self.logger.info("Visitor search module = test_TC_VS_085 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_and_gender_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_085.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_086(self):
    #     self.logger.info("Visitor search module = test_TC_VS_086 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_date_range_gender_criteria_and_max_matches_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_086.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_087(self):
    #     self.logger.info("Visitor search module = test_TC_VS_087 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_date_range_gender_criteria_and_threshold_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_087.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_088(self):
    #     self.logger.info("Visitor search module = test_TC_VS_088 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_date_range_gender_criteria_threshold_and_max_match_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_088.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_089(self):
    #     self.logger.info("Visitor search module = test_TC_VS_089 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_and_age_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_089.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_090(self):
    #     self.logger.info("Visitor search module = test_TC_VS_090 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_age_and_max_matches_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_090.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_091(self):
    #     self.logger.info("Visitor search module = test_TC_VS_091 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_age_and_threshold_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_091.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_VS_092(self):
    #     self.logger.info("Visitor search module = test_TC_VS_092 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_date_range_age_threshold_and_max_matches_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_092.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_093(self):
    #     self.logger.info("Visitor search module = test_TC_VS_093 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_age_and_gender_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_093.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_094(self):
    #     self.logger.info("Visitor search module = test_TC_VS_094 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_age_gender_and_max_matches_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_094.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_095(self):
    #     self.logger.info("Visitor search module = test_TC_VS_095 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_age_gender_and_threshold_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_095.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_096(self):
    #     self.logger.info("Visitor search module = test_TC_VS_096 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_date_range_age_gender_threshold_and_max_matches_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_096.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_097(self):
    #     self.logger.info("Visitor search module = test_TC_VS_097 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_and_region_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_097.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_098(self):
    #     self.logger.info("Visitor search module = test_TC_VS_098 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_region_and_max_matches_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_098.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_099(self):
    #     self.logger.info("Visitor search module = test_TC_VS_099 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_region_and_threshold_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_099.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_100(self):
    #     self.logger.info("Visitor search module = test_TC_VS_100 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_date_range_region_threshold_and_max_matches_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_100.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_101(self):
    #     self.logger.info("Visitor search module = test_TC_VS_101 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_region_and_gender_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_101.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_102(self):
    #     self.logger.info("Visitor search module = test_TC_VS_102 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_date_range_region_gender_and_max_matches_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_102.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_103(self):
    #     self.logger.info("Visitor search module = test_TC_VS_103 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_region_gender_and_threshold_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_103.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_104(self):
    #     self.logger.info("Visitor search module = test_TC_VS_104 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_date_range_region_gender_threshold_and_max_matches_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_104.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_105(self):
    #     self.logger.info("Visitor search module = test_TC_VS_105 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_region_and_age_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_105.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_106(self):
    #     self.logger.info("Visitor search module = test_TC_VS_106 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_date_range_region_age_and_max_count_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_106.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_107(self):
    #     self.logger.info("Visitor search module = test_TC_VS_107 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_date_range_region_age_and_thresh_hold_criteria_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_107.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_108(self):
    #     self.logger.info("Visitor search module = test_TC_VS_108 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_date_range_region_age_thresh_hold_and_max_matches_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_108.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_109(self):
    #     self.logger.info("Visitor search module = test_TC_VS_109 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_date_range_region_age_and_gender_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_109.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_110(self):
    #     self.logger.info("Visitor search module = test_TC_VS_110 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_date_range_region_age_gender_and_max_matches_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_110.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_111(self):
    #     self.logger.info("Visitor search module = test_TC_VS_111 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_date_range_region_age_gender_and_thresh_hold_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_111.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_112(self):
    #     self.logger.info("Visitor search module = test_TC_VS_112 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_date_range_region_age_gender_thresh_hold_and_max_matches_criteria_with_NATS(
    #     ):
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_112.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_VS_113(self):
    #     self.logger.info("Visitor search module = test_TC_VS_113 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_no_search_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_113.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_VS_114(self):
    #     self.logger.info("Visitor search module = test_TC_VS_114 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             Visitor_search_with_no_image_and_should_not_display_Max_of_Matches_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_114.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_VS_115(self):
    #     self.logger.info("Visitor search module = test_TC_VS_115 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             Visitor_search_with_no_image_and_should_not_display_Threshold_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_115.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_VS_116(self):
    #     self.logger.info("Visitor search module = test_TC_VS_116 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             Visitor_search_with_no_image_and_should_not_display_Threshold_max_matches_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_116.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_VS_117(self):
    #     self.logger.info("Visitor search module = test_TC_VS_117 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_region_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_117.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_VS_118(self):
    #     self.logger.info("Visitor search module = test_TC_VS_118 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             Visitor_search_with_no_image_and_Max_of_Matches_not_display_and_region_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_118.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_VS_119(self):
    #     self.logger.info("Visitor search module = test_TC_VS_119 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             Visitor_search_with_no_image_and_threshold_not_display_and_region_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_119.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_VS_120(self):
    #     self.logger.info("Visitor search module = test_TC_VS_120 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             Visitor_search_with_no_image_and_threshold_max_matches_not_display_and_region_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_120.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_121(self):
    #     self.logger.info("Visitor search module = test_TC_VS_121 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_only_date_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_121.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_122(self):
    #     self.logger.info("Visitor search module = test_TC_VS_122 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             Visitor_search_with_no_image_and_Max_of_Matches_not_display_and_date_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_122.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_123(self):
    #     self.logger.info("Visitor search module = test_TC_VS_123 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             Visitor_search_with_no_image_and_threshold_not_display_and_date_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_123.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_124(self):
    #     self.logger.info("Visitor search module = test_TC_VS_124 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             Visitor_search_with_no_image_and_max_matches_threshold_not_display_and_date_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_124.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_125(self):
    #     self.logger.info("Visitor search module = test_TC_VS_125 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_date_and_region_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_125.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_126(self):
    #     self.logger.info("Visitor search module = test_TC_VS_126 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             Visitor_search_with_no_image_and_max_matches_not_display_and_date_and_region_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_126.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_127(self):
    #     self.logger.info("Visitor search module = test_TC_VS_127 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             Visitor_search_with_no_image_and_threshold_not_display_and_date_and_region_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_127.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_128(self):
    #     self.logger.info("Visitor search module = test_TC_VS_128 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #         Visitor_search_with_no_image_and_max_matches_threshold_not_display_and_date_and_region_criteria_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_128.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_129(self):
    #     self.logger.info("Visitor search module = test_TC_VS_129 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_and_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_129.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_130(self):
    #     self.logger.info("Visitor search module = test_TC_VS_130 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_and_max_match_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_130.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_131(self):
    #     self.logger.info("Visitor search module = test_TC_VS_131 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_and_thresh_hold_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_131.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_132(self):
    #     self.logger.info("Visitor search module = test_TC_VS_132 execution started..")
    #     if Visitor_Search_Module_pom_new() \
    #             .visitor_search_with_image_thresh_hold_and_max_count_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_132.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_133(self):
    #     self.logger.info("Visitor search module = test_TC_VS_133 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_and_region_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_133.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_134(self):
    #     self.logger.info("Visitor search module = test_TC_VS_134 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_region_and_max_match_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_134.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_135(self):
    #     self.logger.info("Visitor search module = test_TC_VS_135 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_region_and_thresh_hold_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_135.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_136(self):
    #     self.logger.info("Visitor search module = test_TC_VS_136 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_region_thresh_hold_and_max_count_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_136.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_137(self):
    #     self.logger.info("Visitor search module = test_TC_VS_137 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_and_date_range_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_137.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_138(self):
    #     self.logger.info("Visitor search module = test_TC_VS_138 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_and_max_count_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_138.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_139(self):
    #     self.logger.info("Visitor search module = test_TC_VS_139 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_and_thresh_hold_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_139.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_140(self):
    #     self.logger.info("Visitor search module = test_TC_VS_140 execution started..")
    #     if Visitor_Search_Module_pom_new(). \
    #             visitor_search_with_image_date_range_thresh_hold_and_max_matches_with_NATS_criteria():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_140.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_141(self):
    #     self.logger.info("Visitor search module = test_TC_VS_141 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_and_region_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_141.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_142(self):
    #     self.logger.info("Visitor search module = test_TC_VS_142 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_region_and_max_matches_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_142.png")
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_VS_143(self):
    #     self.logger.info("Visitor search module = test_TC_VS_143 execution started..")
    #     if Visitor_Search_Module_pom_new().visitor_search_with_image_date_range_region_and_threshold_with_NATS():
    #         assert True
    #     else:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_143.png")
    #         assert False

    # @pytest.mark.p1
    def test_TC_VS_144(self):
        self.logger.info("Visitor search module = test_TC_VS_144 execution started..")
        if Visitor_Search_Module_pom_new(). \
                visitor_search_with_image_date_range_region_threshold_and_max_matches_with_NATS():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_144.png")
            assert False
