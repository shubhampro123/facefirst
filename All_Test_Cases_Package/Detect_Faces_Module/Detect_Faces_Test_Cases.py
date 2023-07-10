from pathlib import Path

import pytest

from All_POM_Package.Detect_Faces_Module.Detect_Faces_POM import Detect_Faces_pom
from All_POM_Package.Portal_Menu_Module.Portal_Menu_POM import Portal_Menu_pom
from All_Test_Cases_Package.conftest import Base_Class

@pytest.mark.detect_faces
class Test_Detect_Faces_Test_Cases(Base_Class):
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
    def test_user_login_in_potal(self):
        print("Test_Tags ff_01 execution started..")
        self.logger.info("testing test")
        Detect_Faces_pom().login_before()
        if Detect_Faces_pom().click_on_detect_faces_button():
            assert True
        else:
            print("login")

    @pytest.mark.p2
    def test_TC_TAG_02(self):
        print("test_TC_TAG_02 execution started..")
        self.logger.info("testing test")
        if Detect_Faces_pom().click_on_upload_photo() :
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_TAG_02.png")
            assert False

