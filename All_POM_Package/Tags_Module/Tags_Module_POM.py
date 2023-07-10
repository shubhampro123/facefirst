import time
from pathlib import Path

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from All_POM_Package.Portal_Menu_Module.Portal_Menu_POM import Portal_Menu_pom
from All_Test_Cases_Package.conftest import Base_Class
from Config_Package.Excel_Config_Files import XLUtils
from Config_Package.INI_Config_Files.Portal_Menu_Read_INI import Read_Portal_Menu_Components
from Config_Package.INI_Config_Files.Tags_Read_INI import Read_Tags_Components

test_data = "D://FaceFirst Project All Files\FF_Automation_python\Current Python Framework\FF_Automation_Project_1.0\Test_Data\Data_From_Excel\Test_Data_XLSX.xlsx"


# test_data = "Test_Data/Data_From_Excel/Test_Data_XLSX.xlsx"

class Tags_Module_pom:

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
            tags_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().portal_menu_tags_btn_by_xpath())
            tags_button.click()

        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\login_failed_for_portal_menu_pg_03.png")
                return False

    def create_tags_for_serious_event(self):
        rows = XLUtils.getRowCount(test_data, 'serious_event_tags_data')
        time.sleep(Base_Class.one_second)
        Tags_Module_pom().login_before()
        try:
            for r in range(3, rows + 1):
                tags_name = XLUtils.read_data(test_data, 'serious_event_tags_data', r, 2)
                action_button = self.d.find_element(By.XPATH, Read_Tags_Components().action_btn_by_xpath())
                time.sleep(Base_Class.one_second)
                action_button.click()
                time.sleep(Base_Class.one_second)
                create_button = self.d.find_element(By.XPATH, Read_Tags_Components().create_tags_btn_by_xpath())
                time.sleep(Base_Class.one_second)
                # self.d.execute_script("arguments[0].click();", create_button)
                create_button.click()
                time.sleep(Base_Class.one_second)
                tag_name = self.d.find_element(By.XPATH, Read_Tags_Components().get_tag_name_field_by_xpath())
                time.sleep(Base_Class.one_second)
                tag_name.send_keys(tags_name)
                time.sleep(Base_Class.one_second)
                commit = self.d.find_element(By.XPATH, Read_Tags_Components().get_commit_changes_actual_msg_by_xpath())
                commit.is_displayed()
                assert commit.text == Read_Tags_Components().get_commit_changes_expected_msg_by_xpath()
                serious_event_checkbox = self.d.find_element(By.XPATH,
                                                             Read_Tags_Components().
                                                             get_serious_event_checkbox_by_xpath())
                time.sleep(Base_Class.one_second)
                serious_event_checkbox.click()
                save = self.d.find_element(By.XPATH, Read_Tags_Components().get_save_btn_by_xpath())
                save.click()
                duplicate_tag = self.d.find_element(By.XPATH,
                                                    Read_Tags_Components().
                                                    tag_name_already_exists_validation_by_xpath())
                if duplicate_tag.is_displayed():
                    close_panel = self.d.find_element(By.XPATH,
                                                      Read_Tags_Components().close_create_tag_panel_by_xpath())
                    close_panel.click()
                    close_warning = self.d.find_element(By.XPATH,
                                                        Read_Tags_Components().
                                                        close_panel_and_discard_changes_btn_by_xpath())
                    close_warning.click()

                else:
                    success_msg = self.d.find_element(By.XPATH,
                                                      Read_Tags_Components().tag_create_success_msg_by_xpath())
                    tag_create_success_actual_validation_msg = success_msg.text
                    tag_create_success_expected_validation_msg = Read_Tags_Components(). \
                        create_tag_success_msg_expected()
                    assert tag_create_success_actual_validation_msg == tag_create_success_expected_validation_msg
                    close_panel = self.d.find_element(By.XPATH,
                                                      Read_Tags_Components().close_create_tag_panel_by_xpath())
                    close_panel.click()
                    time.sleep(Base_Class.one_second)
            Tags_Module_pom().close_all_panel_one_by_one()
            time.sleep(Base_Class.one_second)
            Portal_Menu_pom().click_on_logout_button()
            return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\create_tags_for_serious_event_failed_pg_03.png")
                return False

    def create_tags_for_non_serious_event(self):
        rows = XLUtils.getRowCount(test_data, 'non_serious_event_tags_data')

        try:
            time.sleep(Base_Class.one_second)
            Tags_Module_pom().login_before()
            self.d.refresh()
            tags_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().portal_menu_tags_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            tags_button.click()
            for r in range(3, rows + 1):
                tags_name = XLUtils.read_data(test_data, 'non_serious_event_tags_data', r, 2)
                action_button = self.d.find_element(By.XPATH, Read_Tags_Components().action_btn_by_xpath())
                time.sleep(Base_Class.one_second)
                action_button.click()
                create_button = self.d.find_element(By.XPATH, Read_Tags_Components().create_tags_btn_by_xpath())
                time.sleep(Base_Class.one_second)
                create_button.click()
                time.sleep(Base_Class.one_second)
                tag_name = self.d.find_element(By.XPATH, Read_Tags_Components().get_tag_name_field_by_xpath())
                time.sleep(Base_Class.one_second)
                tag_name.send_keys(tags_name)
                time.sleep(Base_Class.one_second)
                commit = self.d.find_element(By.XPATH, Read_Tags_Components().get_commit_changes_actual_msg_by_xpath())
                time.sleep(Base_Class.one_second)
                commit.is_displayed()
                time.sleep(Base_Class.one_second)
                assert commit.text == Read_Tags_Components().get_commit_changes_expected_msg_by_xpath()
                time.sleep(Base_Class.one_second)
                save = self.d.find_element(By.XPATH, Read_Tags_Components().get_save_btn_by_xpath())
                time.sleep(Base_Class.one_second)
                save.click()
                time.sleep(Base_Class.one_second)
                duplicate_tag = self.d.find_element(By.XPATH,
                                                    Read_Tags_Components().
                                                    tag_name_already_exists_validation_by_xpath())
                if duplicate_tag.is_displayed():
                    time.sleep(Base_Class.one_second)

                    close_panel = self.d.find_element(By.XPATH,
                                                      Read_Tags_Components().close_create_tag_panel_by_xpath())
                    time.sleep(Base_Class.one_second)
                    close_panel.click()
                    close_warning = self.d.find_element(By.XPATH,
                                                        Read_Tags_Components().
                                                        close_panel_and_discard_changes_btn_by_xpath())
                    time.sleep(Base_Class.one_second)
                    close_warning.click()

                else:
                    success_msg = self.d.find_element(By.XPATH,
                                                      Read_Tags_Components().tag_create_success_msg_by_xpath())
                    tag_create_success_actual_validation_msg = success_msg.text
                    tag_create_success_expected_validation_msg = Read_Tags_Components(). \
                        create_tag_success_msg_expected()
                    assert tag_create_success_actual_validation_msg == tag_create_success_expected_validation_msg
                    close_panel = self.d.find_element(By.XPATH,
                                                      Read_Tags_Components().close_create_tag_panel_by_xpath())
                    close_panel.click()
            Tags_Module_pom().close_all_panel_one_by_one()
            Portal_Menu_pom().click_on_logout_button()
            return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\create_tags_for_non_serious_event_failed_pg_03.png")
                return False

    def filter_serious_event_tags_varify_it(self):
        rows = XLUtils.getRowCount(test_data, 'serious_event_tags_data')

        try:
            time.sleep(Base_Class.one_second)
            Tags_Module_pom().login_before()
            self.d.refresh()
            tags_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().portal_menu_tags_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            tags_button.click()
            time.sleep(Base_Class.one_second)
            serious_event_tags_expected = []
            for r in range(2, rows + 1):
                tags_name = XLUtils.read_data(test_data, 'serious_event_tags_data', r, 2)
                serious_event_tags_expected.insert(r - 1, tags_name)
                serious_event_tags_expected = [x.lower() for x in serious_event_tags_expected]
                serious_event_tags_expected.sort()
            filter_btn = self.d.find_element(By.XPATH, Read_Tags_Components().filter_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            filter_btn.click()
            serious_event_filter = self.d.find_element(By.XPATH,
                                                       Read_Tags_Components().serious_event_filter_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            serious_event_filter.click()
            time.sleep(Base_Class.one_second)
            tags_name_list = self.d.find_elements(By.XPATH, Read_Tags_Components().list_of_all_tags_name_by_xpath())
            serious_event_tags_name_list_actual = []
            for r in tags_name_list:
                tag = r.text
                tag.lower()
                serious_event_tags_name_list_actual.append(tag)
                serious_event_tags_name_list_actual = [x.lower() for x in serious_event_tags_name_list_actual]
                serious_event_tags_name_list_actual.sort()
            time.sleep(Base_Class.one_second)
            assert serious_event_tags_expected == serious_event_tags_name_list_actual
            Tags_Module_pom().close_all_panel_one_by_one()
            time.sleep(Base_Class.one_second)
            Portal_Menu_pom().click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\tags_filter_serious_event_yes_failed_pg_03.png")
                return False

    def filter_non_serious_event_tags_varify_it(self):
        rows = XLUtils.getRowCount(test_data, 'non_serious_event_tags_data')

        try:
            time.sleep(Base_Class.one_second)
            Tags_Module_pom().login_before()
            self.d.refresh()
            tags_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().portal_menu_tags_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            tags_button.click()
            time.sleep(Base_Class.one_second)
            non_serious_event_tags_expected = []
            for r in range(2, rows + 1):
                tags_name = XLUtils.read_data(test_data, 'non_serious_event_tags_data', r, 2)
                non_serious_event_tags_expected.insert(r - 1, tags_name)
                non_serious_event_tags_expected = [x.lower() for x in non_serious_event_tags_expected]
                non_serious_event_tags_expected.sort()

            non_serious_event_tags_expected = non_serious_event_tags_expected[
                                              1:len(non_serious_event_tags_expected) + 1]
            print(len(non_serious_event_tags_expected), "data from excel")

            filter_dropdown = self.d.find_element(By.XPATH, Read_Tags_Components().filter_dropdown_by_xpath())
            time.sleep(Base_Class.one_second)
            filter_dropdown.click()
            time.sleep(3)
            non_serious_ele = self.d.find_element(By.XPATH, Read_Tags_Components().non_serious_element_by_xpath())
            time.sleep(Base_Class.one_second)
            non_serious_ele.click()
            time.sleep(3)
            tags_name_list = self.d.find_elements(By.XPATH, Read_Tags_Components().list_of_all_tags_name_by_xpath())
            serious_event_tags_name_list_actual = []
            for r in tags_name_list:
                tag = r.text.strip()
                tag = tag.lower()
                serious_event_tags_name_list_actual.append(tag)
            serious_event_tags_name_list_actual = serious_event_tags_name_list_actual[
                                                  1:len(serious_event_tags_name_list_actual) + 1]
            serious_event_tags_name_list_actual = [x.lower() for x in serious_event_tags_name_list_actual]
            serious_event_tags_name_list_actual.sort()
            time.sleep(Base_Class.one_second)

            print(non_serious_event_tags_expected)
            print(serious_event_tags_name_list_actual)
            assert non_serious_event_tags_expected == serious_event_tags_name_list_actual

            Tags_Module_pom().close_all_panel_one_by_one()
            time.sleep(Base_Class.one_second)
            Portal_Menu_pom().click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\tags_filter_serious_event_yes_failed_pg_03.png")
                return False

    def duplicate_tags_not_create_validation(self):
        rows = XLUtils.getRowCount(test_data, 'serious_event_tags_data')
        try:
            time.sleep(Base_Class.one_second)
            Tags_Module_pom().login_before()
            self.d.refresh()
            tags_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().portal_menu_tags_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            tags_button.click()
            time.sleep(Base_Class.one_second)
            for r in range(2, rows + 1):
                tags_name = XLUtils.read_data(test_data, 'serious_event_tags_data', r, 2)
                action_button = self.d.find_element(By.XPATH, Read_Tags_Components().action_btn_by_xpath())
                time.sleep(Base_Class.one_second)
                action_button.click()
                time.sleep(Base_Class.one_second)
                create_button = self.d.find_element(By.XPATH, Read_Tags_Components().create_tags_btn_by_xpath())
                time.sleep(Base_Class.one_second)
                create_button.click()
                time.sleep(Base_Class.one_second)
                tag_name = self.d.find_element(By.XPATH, Read_Tags_Components().get_tag_name_field_by_xpath())
                time.sleep(Base_Class.one_second)
                tag_name.send_keys(tags_name)
                commit = self.d.find_element(By.XPATH, Read_Tags_Components().get_commit_changes_actual_msg_by_xpath())
                time.sleep(Base_Class.one_second)
                commit.is_displayed()
                assert commit.text == Read_Tags_Components().get_commit_changes_expected_msg_by_xpath()
                serious_event_checkbox = self.d.find_element(By.XPATH,
                                                             Read_Tags_Components().
                                                             get_serious_event_checkbox_by_xpath())
                serious_event_checkbox.click()
                save = self.d.find_element(By.XPATH, Read_Tags_Components().get_save_btn_by_xpath())
                time.sleep(Base_Class.one_second)
                save.click()
                try:
                    tag_name_already_exists = self.d.find_element(By.XPATH,
                                                                  Read_Tags_Components().
                                                                  tag_name_already_exists_validation_by_xpath())
                    actual_duplicate_tag_validation_msg = tag_name_already_exists.text
                    expected_duplicate_tag_validation_msg = Read_Tags_Components(). \
                        expected_duplicate_tag_validation_msg()
                    print(expected_duplicate_tag_validation_msg)
                    if tag_name_already_exists.is_displayed():
                        time.sleep(Base_Class.one_second)
                        assert actual_duplicate_tag_validation_msg == expected_duplicate_tag_validation_msg
                        close_panel = self.d.find_element(By.XPATH,
                                                          Read_Tags_Components().close_create_tag_panel_by_xpath())
                        time.sleep(Base_Class.one_second)
                        close_panel.click()
                        close_panel_and_discard_changes_btn = self.d \
                            .find_element(By.XPATH,
                                          Read_Tags_Components().
                                          close_panel_and_discard_changes_btn_by_xpath())
                        time.sleep(Base_Class.one_second)
                        close_panel_and_discard_changes_btn.click()
                    else:
                        close_panel = self.d.find_element(By.XPATH,
                                                          Read_Tags_Components().close_create_tag_panel_by_xpath())
                        time.sleep(Base_Class.one_second)
                        close_panel.click()
                except Exception as ex:
                    str(ex)
            Tags_Module_pom().close_all_panel_one_by_one()
            time.sleep(Base_Class.one_second)
            Portal_Menu_pom().click_on_logout_button()
            return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\duplicate_tags_not_create_validation_failed_pg_03.png")
                return False

    def update_serious_event_tag_name(self):
        rows = XLUtils.getRowCount(test_data, 'serious_event_tags_data')
        try:
            time.sleep(Base_Class.one_second)
            Tags_Module_pom().login_before()
            exp_tag_name = []
            tags_name = []
            # edit_btn_list = []
            for r in range(2, rows + 1):
                exp_tag_name.insert(r - 2, XLUtils.read_data(test_data, 'serious_event_tags_data', r, 3))

            for r in range(2, rows + 1):
                tags_name.insert(r - 2, XLUtils.read_data(test_data, 'serious_event_tags_data', r, 2))

            exp_tag_name = exp_tag_name[1:len(exp_tag_name) + 1]
            tags_name = tags_name[1:len(tags_name) + 1]
            filter_btn = self.d.find_element(By.XPATH, Read_Tags_Components().filter_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            filter_btn.click()
            serious_event_filter = self.d.find_element(By.XPATH,
                                                       Read_Tags_Components().serious_event_filter_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            serious_event_filter.click()
            edit_btn_list = self.d.find_elements(By.XPATH,
                                                 Read_Tags_Components().tags_edit_button_by_xpath())

            time.sleep(3)
            time.sleep(Base_Class.one_second)
            for i in range(0, len(edit_btn_list)):

                try:
                    ac_tg_name = str(tags_name[i]).lower().strip()
                    time.sleep(Base_Class.one_second)
                    ele = self.d.find_element(By.XPATH, "//p[normalize-space(text())='"+str(
                        ac_tg_name)+"']/following-sibling::div[@class='right-margin-menu']/descendant::div["
                                    "@data-toggle='tooltip']")
                    time.sleep(Base_Class.one_second)
                    self.d.execute_script("arguments[0].click();", ele)
                    time.sleep(Base_Class.one_second)
                    time.sleep(2)
                    action_btn = self.d.find_element(By.XPATH,
                                                     Read_Tags_Components().edit_tag_action_btn_by_xpath())
                    time.sleep(Base_Class.one_second)
                    self.d.execute_script("arguments[0].click();", action_btn)
                    time.sleep(Base_Class.one_second)
                except Exception as ex:
                    str(ex)
                edit_btn = self.d.find_element(By.XPATH, Read_Tags_Components().edit_btn_by_xpath())
                time.sleep(Base_Class.one_second)
                self.d.execute_script("arguments[0].click();", edit_btn)
                time.sleep(Base_Class.one_second)
                tag_name_field = self.d.find_element(By.XPATH,
                                                     Read_Tags_Components().get_tag_name_field_by_xpath())
                time.sleep(Base_Class.one_second)
                tag_name_field.send_keys(Keys.CONTROL, 'a')
                time.sleep(Base_Class.one_second)
                tag_name_field.send_keys(Keys.DELETE)
                time.sleep(Base_Class.one_second)
                tag_name_field.send_keys(exp_tag_name[i])
                time.sleep(Base_Class.one_second)
                save = self.d.find_element(By.XPATH, Read_Tags_Components().get_save_btn_by_xpath())
                time.sleep(Base_Class.one_second)
                self.d.execute_script("arguments[0].click();", save)
                time.sleep(Base_Class.one_second)
                close_panel = self.d.find_element(By.XPATH,
                                                  Read_Tags_Components().close_create_tag_panel_by_xpath())
                time.sleep(Base_Class.one_second)
                close_panel.click()
            Portal_Menu_pom().click_on_logout_button()
            return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\update_serious_event_tag_name_failed_pg_03.png")
                return False

    def delete_all_tags(self):

        try:
            time.sleep(Base_Class.one_second)
            Tags_Module_pom().login_before()
            self.d.refresh()
            tags_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().portal_menu_tags_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            tags_button.click()
            time.sleep(Base_Class.one_second)
            tags_checkbox = self.d.find_elements(By.XPATH,
                                                 Read_Tags_Components().tag_select_checkbox_list_by_xpath())
            try:
                for i in range(2, len(tags_checkbox)):
                    tags_checkbox[i].click()
            except Exception as ex:
                str(ex)
            action_button = self.d.find_element(By.XPATH, Read_Tags_Components().tags_action_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            action_button.click()
            delete_btn = self.d.find_element(By.XPATH,
                                             Read_Tags_Components().delete_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            delete_btn.click()
            delete_yes_btn = self.d.find_element(By.XPATH,
                                                 Read_Tags_Components().yes_delete_selected())
            time.sleep(Base_Class.one_second)
            delete_yes_btn.click()
            Tags_Module_pom().close_all_panel_one_by_one()
            time.sleep(Base_Class.one_second)
            Portal_Menu_pom().click_on_logout_button()
            return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\delete_all_tags_failed_pg_03.png")
                return False

    def verify_deterred_tag_is_present_at_first(self):
        try:
            time.sleep(Base_Class.one_second)
            Tags_Module_pom().login_before()
            self.d.refresh()
            tags_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().portal_menu_tags_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            tags_button.click()
            time.sleep(Base_Class.one_second)
            deterred_tag = self.d.find_elements(By.XPATH, Read_Tags_Components().list_of_all_tags_name_by_xpath())
            time.sleep(Base_Class.one_second)
            actual_deterred_tag = deterred_tag[0].text
            time.sleep(Base_Class.one_second)
            expected_deterred_tag = Read_Tags_Components().expected_deterred_tag()
            time.sleep(Base_Class.one_second)
            assert actual_deterred_tag.lower() == expected_deterred_tag.lower()
            time.sleep(Base_Class.one_second)
            Tags_Module_pom().close_all_panel_one_by_one()
            time.sleep(Base_Class.one_second)
            Portal_Menu_pom().click_on_logout_button()
            return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\delete_all_tags_failed_pg_03.png")
                return False

    def tags_search_functionality(self):
        try:
            time.sleep(Base_Class.one_second)
            Tags_Module_pom().login_before()
            self.d.refresh()
            tags_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().portal_menu_tags_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            tags_button.click()
            search_box = self.d.find_element(By.XPATH, Read_Tags_Components().tags_search_field_by_xpath())
            search_box.send_keys(Read_Tags_Components().tag_search_input())
            time.sleep(Base_Class.one_second)
            # search_result = []
            search_result = self.d.find_elements(By.XPATH, Read_Tags_Components().list_of_all_tags_name_by_xpath())
            time.sleep(Base_Class.one_second)
            actual_tag_result = search_result[0].text
            expected_tag_result = Read_Tags_Components().tag_search_result_expected()
            assert actual_tag_result == expected_tag_result
            Tags_Module_pom().close_all_panel_one_by_one()
            time.sleep(Base_Class.one_second)
            Portal_Menu_pom().click_on_logout_button()
            return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\tags_search_functionality_failed_pg_03.png")
                return False

    def close_panel_and_discard_changes_verify(self):
        try:
            Tags_Module_pom().login_before()
            time.sleep(Base_Class.one_second)
            action_button = self.d.find_element(By.XPATH, Read_Tags_Components().close_and_discard_panel_btn())
            time.sleep(Base_Class.one_second)
            action_button.click()
            time.sleep(Base_Class.one_second)
            create_button = self.d.find_element(By.XPATH, Read_Tags_Components().create_tags_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            create_button.click()
            time.sleep(Base_Class.one_second)
            tag_name = self.d.find_element(By.XPATH, Read_Tags_Components().get_tag_name_field_by_xpath())
            time.sleep(Base_Class.one_second)
            tag_name.send_keys(Read_Tags_Components().close_panel_and_discard_changes_input())
            time.sleep(Base_Class.one_second)
            close_panel = self.d.find_element(By.XPATH, Read_Tags_Components().close_create_tag_panel_by_xpath())
            time.sleep(Base_Class.one_second)
            close_panel.click()
            time.sleep(Base_Class.one_second)
            warning_msg = self.d.find_element(By.XPATH,
                                              Read_Tags_Components().expected_discard_changes_warning_by_xpath())
            time.sleep(Base_Class.one_second)
            actual_warning_msg = warning_msg.text
            excepted_warning_msg = Read_Tags_Components().expected_discard_changes_warning()
            assert actual_warning_msg == excepted_warning_msg
            uncommitted_changes_msg = self.d.find_element(By.XPATH,
                                                          Read_Tags_Components().
                                                          expected_uncommitted_changes_msg_by_xpath())
            time.sleep(Base_Class.one_second)
            actual_uncommitted_changes_msg = uncommitted_changes_msg.text
            excepted_uncommitted_changes_msg = Read_Tags_Components().expected_uncommitted_changes_msg()
            assert actual_uncommitted_changes_msg == excepted_uncommitted_changes_msg
            close_panel_btn = self.d.find_element(By.XPATH,
                                                  Read_Tags_Components().close_panel_btn_text_validation())
            actual_close_panel_btn_text = close_panel_btn.text
            excepted_close_panel_btn_text = Read_Tags_Components().expected_close_panel_btn_text()
            assert actual_close_panel_btn_text == excepted_close_panel_btn_text
            close_panel_and_discard_changes_btn = self.d.find_element(By.XPATH,
                                                                      Read_Tags_Components().
                                                                      close_panel_and_discard_changes_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            close_panel_and_discard_changes_btn.click()
            time.sleep(Base_Class.one_second)

            logout = self.d.find_element(By.XPATH,
                                         Read_Portal_Menu_Components().logout_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            logout.click()
            return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\close_panel_and_discard_changes_verify_failed_pg_03.png")
                return False

    def create_tags_for_serious_event_without_login(self):
        rows = XLUtils.getRowCount(test_data, 'Tags_Data')
        time.sleep(Base_Class.one_second)
        try:
            for r in range(3, rows + 1):
                tags_name = XLUtils.read_data(test_data, 'Tags_Data', r, 2)
                action_button = self.d.find_element(By.XPATH, Read_Tags_Components().action_btn_by_xpath())
                time.sleep(Base_Class.one_second)

                action_button.click()
                time.sleep(Base_Class.one_second)
                create_button = self.d.find_element(By.XPATH, Read_Tags_Components().create_tags_btn_by_xpath())
                time.sleep(Base_Class.one_second)

                # self.d.execute_script("arguments[0].click();", create_button)
                create_button.click()
                time.sleep(Base_Class.one_second)
                tag_name = self.d.find_element(By.XPATH, Read_Tags_Components().get_tag_name_field_by_xpath())
                tag_name.send_keys(tags_name)
                commit = self.d.find_element(By.XPATH, Read_Tags_Components().get_commit_changes_actual_msg_by_xpath())
                time.sleep(Base_Class.one_second)

                commit.is_displayed()
                assert commit.text == Read_Tags_Components().get_commit_changes_expected_msg_by_xpath()
                serious_event_checkbox = self.d.find_element(By.XPATH,
                                                             Read_Tags_Components().
                                                             get_serious_event_checkbox_by_xpath())
                time.sleep(Base_Class.one_second)

                serious_event_checkbox.click()
                save = self.d.find_element(By.XPATH, Read_Tags_Components().get_save_btn_by_xpath())
                time.sleep(Base_Class.one_second)

                save.click()
                duplicate_tag = self.d.find_element(By.XPATH,
                                                    Read_Tags_Components().
                                                    tag_name_already_exists_validation_by_xpath())
                if duplicate_tag.is_displayed():
                    close_panel = self.d.find_element(By.XPATH,
                                                      Read_Tags_Components().close_create_tag_panel_by_xpath())
                    time.sleep(Base_Class.one_second)
                    close_panel.click()
                    close_warning = self.d.find_element(By.XPATH,
                                                        Read_Tags_Components().
                                                        close_panel_and_discard_changes_btn_by_xpath())
                    time.sleep(Base_Class.one_second)
                    close_warning.click()

                else:
                    time.sleep(Base_Class.one_second)
                    success_msg = self.d.find_element(By.XPATH, Read_Tags_Components().get_save_btn_by_xpath())
                    success_msg.is_displayed()
                    close_panel = self.d.find_element(By.XPATH,
                                                      Read_Tags_Components().close_create_tag_panel_by_xpath())
                    close_panel.click()
            return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\create_tags_for_serious_event_failed_pg_03.png")
                return False

    def close_all_panel(self):
        time.sleep(Base_Class.one_second)
        try:
            cloud_menu_button = self.d.find_element(By.XPATH,
                                                    Read_Portal_Menu_Components().portal_menu_cloud_menu_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            cloud_menu_button.click()
            time.sleep(Base_Class.one_second)
            closed_all_button = self.d.find_element(By.XPATH,
                                                    Read_Portal_Menu_Components().portal_menu_closed_all_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            closed_all_button.click()
            return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\close_all_panel_failed_pg_03.png")
                return False

    def close_all_panel_one_by_one(self):
        time.sleep(Base_Class.one_second)
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
                    f"{Path(__file__).parent.parent}\\Screenshots\\close_all_panel_failed_pg_03.png")
                return False
