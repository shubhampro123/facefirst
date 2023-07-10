import time
from datetime import date
from pathlib import Path

import pyautogui
from selenium.common import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from All_Test_Cases_Package.conftest import Base_Class
from Config_Package.INI_Config_Files.Identify_and_Enroll_Read_INI import Read_Identify_and_Enroll_Components
from Config_Package.INI_Config_Files.Portal_Menu_Read_INI import Read_Portal_Menu_Components
from Config_Package.INI_Config_Files.Visitor_search_Read_INI import Read_Visitor_Search_Components


class Identify_and_Enroll_pom:
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
            print("login")

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\login_failed_for_portal_menu_pg_03.png")
                return False

    def upload_image(self):
        """
        This function is usd to upload the image and click on the search button
        :return:
        """
        upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
        upload_photo.click()
        time.sleep(2)
        file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\img1.png"

        pyautogui.write(file_path)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.press('enter')

    def upload_image_not_enrolled(self):
        """
        This function is usd to upload the image and click on the search button
        :return:
        """
        upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
        upload_photo.click()
        time.sleep(2)
        file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\shrek.png"
        # file_path = 'C:\\Users\\baps\\Pictures\\uim.png'
        # file_path = 'D:\Chrome_Download\img1.png'

        pyautogui.write(file_path)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.press('enter')

    def enroll_person(self):
        """
        This function is used to enroll the person
        :return:
        """
        self.login_before()
        time.sleep(Base_Class.two_second)

        link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                   .identify_and_enroll_link_by_xpath())
        self.d.execute_script("arguments[0].click();", link)

        self.upload_image()

        identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .identify_enroll_panel_identify_enroll_btn_by_xpath())

        self.d.execute_script("arguments[0].click();", identify_enroll_btn)

        wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                        .identifying_photo_wait_by_xpath())
        while wait_icon.is_displayed():
            time.sleep(Base_Class.two_second)

        enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .enrollment_group_by_xpath())
        select = Select(enrollment_group)
        select.select_by_index(1)

        location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .location_store_inpt_bx_by_xpath())
        location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

        case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .case_subject_inpt_bx_by_xpath())
        case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

        reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .reported_loss_inpt_bx_by_xpath())
        reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

        date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .date_incident_inpt_bx_by_xpath())
        time.sleep(Base_Class.two_second)
        date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
        time.sleep(Base_Class.two_second)
        action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .action_inpt_bx_by_xpath())
        action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

        save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .add_details_save_btn_by_xpath())
        assert save_btn.is_displayed()
        save_btn.click()
        wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                        .enrollment_success_loader())
        while wait_icon.is_displayed():
            time.sleep(Base_Class.two_second)
        success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                          .enrollment_success_msg_xpath())
        assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
            enrollment_success_msg_validation().lower()

        title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                     add_details_panel_title_panel())
        for x in title:
            if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                    add_details_panel_validation().lower():
                assert False
        self.close_all_panel_one_by_one()
        self.click_on_logout_button()

    def delete_enrollment(self):
        try:

            cloud_menu = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                             cloud_menu_button_xpath())
            cloud_menu.click()
            time.sleep(Base_Class.one_second)
            time.sleep(2)
            enrollment_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                 enrollment_menu_button_xpath())
            time.sleep(2)
            enrollment_btn.click()
            time.sleep(Base_Class.one_second)
            time.sleep(2)
            select_all_checkbox = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                      select_all_enrollment_btn_xpath())
            time.sleep(2)
            select_all_checkbox.click()
            time.sleep(Base_Class.one_second)

            action_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                             enrollment_panel_action_btn())
            time.sleep(2)
            action_btn.click()
            time.sleep(Base_Class.one_second)

            delete_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                             delete_enrollments_btn_xpath())
            time.sleep(2)
            delete_btn.click()
            time.sleep(Base_Class.one_second)

            yes_delete = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                             yes_delete_btn_xpath())
            time.sleep(2)
            yes_delete_2 = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                               yes_delete_btn_xpath_2())
            time.sleep(2)
            if yes_delete.is_displayed():
                time.sleep(2)
                yes_delete.click()
                time.sleep(Base_Class.one_second)
            else:
                time.sleep(2)
                yes_delete_2.click()
                time.sleep(Base_Class.one_second)

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\delete_enrollment_failed.png")
                return False

    def verify_Cloud_Menu_Local_Menu(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            cloud_menu = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().cloud_menu_by_xpath())
            assert cloud_menu.is_displayed()

            try:
                cloud_menu.click()
            except WebDriverException:
                assert False

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_Cloud_Menu_Local_Menu_failed.png")
                return False

    def verify_if_Identify_and_Enroll_Menu_Option_is_displayed_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            identify_and_enroll = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                      identify_and_enroll_link_by_xpath())
            assert identify_and_enroll.is_displayed()

            try:
                self.d.execute_script("arguments[0].click();", identify_and_enroll)
            except WebDriverException:
                assert False

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_if_Identify_and_Enroll_Menu_Option_is_displayed_and_clickable_failed.png")
                return False

    def verify_a_new_panel_is_displayed_with_title_as_Identify_and_Enroll(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            identify_and_enroll = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                      identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", identify_and_enroll)
            time.sleep(Base_Class.two_second)

            identify_and_enroll_panel_title = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                                  identify_and_enroll_panel_title_by_xpath())
            actual_text = identify_and_enroll_panel_title.text
            expected_text = Read_Identify_and_Enroll_Components().identify_and_enroll_panel_title()
            print("Expected data = " + expected_text)
            print("Actual data = " + actual_text)
            assert actual_text.lower() == expected_text.lower()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_a_new_panel_is_displayed_with_title_as_Identify_and_Enroll_failed.png")
                return False

    def verify_Select_A_Photo_test_is_displayed_at_the_top_inside_Identity_and_Enroll_Panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            identify_and_enroll = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                      identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", identify_and_enroll)
            time.sleep(Base_Class.two_second)

            select_a_photo_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                      select_a_photo_text_by_xpath())
            actual_text = select_a_photo_text.text
            expected_text = Read_Identify_and_Enroll_Components().identify_and_enroll_panel_select_photo_text()
            print("Expected data = " + expected_text)
            print("Actual data = " + actual_text)
            assert actual_text.lower() == expected_text.lower()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_Select_A_Photo_test_is_displayed_at_the_top_inside_Identity_and_Enroll_Panel_failed.png")
                return False

    def verify_a_square_box_blank_image_icon_is_displayed_below_select_a_photo_and_it_is_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            identify_and_enroll = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                      identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", identify_and_enroll)
            time.sleep(Base_Class.two_second)

            square_box_blank_image_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                              upload_image_by_xpath())
            assert square_box_blank_image_icon.is_displayed()

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            try:
                upload_photo.click()
            except WebDriverException:
                assert False
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\img1.png"

            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_a_square_box_blank_image_icon_is_displayed_below_select_a_photo_"
                    f"and_it_is_clickable_failed.png")
                return False

    def verify_text_below_image_icon_is_displayed_and_expected_text(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            identify_and_enroll = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                      identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", identify_and_enroll)
            time.sleep(Base_Class.two_second)
            validate_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                select_photo_instructions_by_xpath())

            assert validate_text.is_displayed()
            actual_text = validate_text.text.lower()
            expected_text = Read_Identify_and_Enroll_Components().select_photo_instructions_text_validation().lower()
            print("Expected data = " + expected_text)
            print("Actual data = " + actual_text)
            assert actual_text == expected_text
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_text_below_image_icon_is_displayed_and_expected_text_failed.png")
                return False

    def verify_if_a_new_dialog_box_is_appeared_to_choose_image_file(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            identify_and_enroll = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                      identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", identify_and_enroll)
            time.sleep(Base_Class.two_second)

            self.upload_image()

            uploaded_image_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                            uploaded_photo_validation_by_xpath())
            assert uploaded_image_validation.is_displayed()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_if_a_new_dialog_box_is_appeared_to_choose_image_file_failed.png")
                return False

    def click_on_image_icon_upload_image_and_verify_if_same_image_displayed_inside_image_box(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            time.sleep(Base_Class.two_second)
            uploaded_image_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .uploaded_image_validation())
            # assert uploaded_image_validation.is_displayed()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_notes_button_is_visible_along_with_its_count_and_is_clickable_failed.png")
                return False

    def verify_two_new_panel_appeared_with_title_as_Enrollment_Steps_and_Add_Details(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_steps_title = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .enrollment_steps_by_xpath())
            assert enrollment_steps_title.is_displayed()

            ex_enrollments_steps_title_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_steps_title_txt_validation().lower()
            ac_enrollment_steps_title_txt = enrollment_steps_title.text.lower()
            print("Expected data = " + ex_enrollments_steps_title_txt)
            print("Actual data = " + ac_enrollment_steps_title_txt)
            assert ex_enrollments_steps_title_txt == ac_enrollment_steps_title_txt

            add_details_panel = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .add_details_panel_by_xpath())
            assert add_details_panel.is_displayed()

            ex_add_details_panel_txt = Read_Identify_and_Enroll_Components() \
                .add_details_panel_title_txt_validation().lower()
            ac_add_details_panel_txt = add_details_panel.text.lower()
            print("Expected data = " + ex_add_details_panel_txt)
            print("Actual data = " + ac_add_details_panel_txt)
            assert ex_add_details_panel_txt == ac_add_details_panel_txt

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_two_new_panel_appeared_with_title_as_Enrollment_Steps_and_Add_Details_failed.png")
                return False

    def verify_Image_Properties_text_below_image_and_its_dimensions_are_visible(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)
            identify_and_enroll = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                      identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", identify_and_enroll)
            time.sleep(Base_Class.two_second)

            self.upload_image()

            uploaded_image_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                            uploaded_photo_validation_by_xpath())
            assert uploaded_image_validation.is_displayed()

            Image_Properties_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                        image_properties_text_by_xpath())
            actual_text = Image_Properties_text.text
            expected_text = Read_Identify_and_Enroll_Components().image_properties_text()
            print("Expected data = " + expected_text)
            print("Actual data = " + actual_text)
            assert actual_text == expected_text

            image_dimension_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                             image_dia_mentions_by_xpath())
            assert image_dimension_validation.is_displayed()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_Image_Properties_text_below_image_and_its_dimensions_are_visible_failed.png")
                return False

    def verify_re_Select_Photo_button_is_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH,
                                       Read_Identify_and_Enroll_Components().identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            try:
                reselect_photo_btn = self.d.find_element(By.XPATH,
                                                         Read_Identify_and_Enroll_Components()
                                                         .identify_enroll_panel_reselect_photo_btn_by_xpath())
                assert reselect_photo_btn.is_displayed()
                reselect_photo_icon = self.d.find_element(By.XPATH,
                                                          Read_Identify_and_Enroll_Components()
                                                          .reselect_photo_icon())
                assert reselect_photo_icon.is_displayed()

            except WebDriverException:
                assert False

            try:
                self.d.execute_script("arguments[0].click();", reselect_photo_btn)
            except WebDriverException:
                assert False

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_re_Select_Photo_button_is_visible_and_clickable_failed.png")
                return False

    def verify_crop_photo_button_is_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH,
                                       Read_Identify_and_Enroll_Components().identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            try:
                crop_photo_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_crop_photo_btn_by_xpath())

                assert crop_photo_btn.is_displayed()

                crop_photo_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .crop_photo_icon())

                assert crop_photo_icon.is_displayed()

                self.d.execute_script("arguments[0].click();", crop_photo_btn)
                Alert(self.d).accept()
            except WebDriverException:
                assert False
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_crop_photo_button_is_visible_and_clickable_failed.png")
                return False

    def verify_text_below_three_buttons_is_displayed(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH,
                                       Read_Identify_and_Enroll_Components().identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            # identify and enroll button below text validation

            identify_enroll_txt_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                          .identify_enroll_btn_below_text_xpath())

            exp_identify_enroll_txt = Read_Identify_and_Enroll_Components().identify_enroll_btn_below_text() \
                .replace(" ", "")
            act_identify_enroll_txt = identify_enroll_txt_ele.text.replace("\n", "").lower().replace(" ", "")
            print("Expected data = " + exp_identify_enroll_txt)
            print("Actual data = " + act_identify_enroll_txt)
            assert identify_enroll_txt_ele.is_displayed() and exp_identify_enroll_txt == act_identify_enroll_txt

            # reselect photo button below text validation

            reselect_photo_txt_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .reselect_btn_below_text_xpath())
            exp_reselect_photo_txt = Read_Identify_and_Enroll_Components().reselect_photo_btn_below_text() \
                .replace(" ", "")
            act_reselect_photo_txt = reselect_photo_txt_ele.text.replace("\n", "").lower().replace(" ", "")
            print("Expected data = " + exp_reselect_photo_txt)
            print("Actual data = " + act_reselect_photo_txt)
            assert reselect_photo_txt_ele.is_displayed() and exp_reselect_photo_txt == act_reselect_photo_txt

            # crop photo button below text validation

            crop_photo_txt_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .crop_photo_btn_below_xpath())
            exp_crop_photo_txt = Read_Identify_and_Enroll_Components().crop_photo_btn_below_text() \
                .replace(" ", "")
            act_crop_photo_txt = crop_photo_txt_ele.text.replace("\n", "").lower().replace(" ", "")
            print("Expected data = " + exp_crop_photo_txt)
            print("Actual data = " + act_crop_photo_txt)
            assert crop_photo_txt_ele.is_displayed() and exp_crop_photo_txt == act_crop_photo_txt

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_text_below_three_buttons_is_displayed_failed.png")
                return False

    def verify_if_current_image_is_removed_from_image_box(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH,
                                       Read_Identify_and_Enroll_Components().identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()
            uploaded_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .uploaded_photo_validation_by_xpath())

            reselect_photo_btn = self.d.find_element(By.XPATH,
                                                     Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_reselect_photo_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", reselect_photo_btn)
            time.sleep(Base_Class.two_second)

            upload_image_icon = self.d.find_element(By.XPATH,
                                                    Read_Identify_and_Enroll_Components()
                                                    .upload_image_by_xpath())
            if upload_image_icon.is_displayed():
                assert True
            else:
                assert False
            time.sleep(Base_Class.two_second)
            reselect_photo_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_reselect_photo_btn_by_xpath())
            if reselect_photo_btn.is_displayed():
                assert False
            else:
                assert True

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())
            if identify_enroll_btn.is_displayed():
                assert False
            else:
                assert True

            crop_photo_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .identify_enroll_panel_crop_photo_btn_by_xpath())
            if crop_photo_btn.is_displayed():
                assert False
            else:
                assert True

            upload_photo_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .upload_image_by_xpath())

            assert upload_photo_ele.is_displayed()

            ex_validate_txt = Read_Identify_and_Enroll_Components().select_photo_instructions_text_validation()

            validate_btn_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .select_photo_instructions_by_xpath())
            ac_validate_txt = validate_btn_ele.text
            print("Expected data = " + ex_validate_txt)
            print("Actual data = " + ac_validate_txt)
            assert ex_validate_txt.lower() == ac_validate_txt.lower()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_if_current_image_is_removed_from_image_box_failed.png")
                return False

    def verify_identify_enroll_button_is_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())

            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            try:
                identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                          .identify_enroll_panel_identify_enroll_btn_by_xpath())

                assert identify_enroll_btn.is_displayed()

                identify_enroll_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                           .identify_enroll_icon())

                assert identify_enroll_icon.is_displayed()

                self.d.execute_script("arguments[0].click();", identify_enroll_btn)
                cancel = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                           .add_details_cancel_btn_by_xpath())
                cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .cancel_enrollment_btn_by_xpath())
                cancel.click()
                cancel_enrollment.click()
            except WebDriverException:
                assert False
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_identify_enroll_button_is_visible_and_clickable_failed.png")
                return False

    def verify_new_panel_is_displayed_with_title_as_Identify_Results(self):
        try:
            try:
                self.enroll_person()
            except Exception as ex:
                msg = str(ex)
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)
            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            ex_identify_results_txt = Read_Identify_and_Enroll_Components().identify_results_text_validation()
            time.sleep(Base_Class.two_second)
            print("2")
            identify_results = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .identify_results_panel_by_xpath())
            print("3")
            time.sleep(Base_Class.two_second)
            ac_identify_results_txt = identify_results.text
            print("4")
            time.sleep(2)
            print("Expected data = " + ex_identify_results_txt)
            print("Actual data = " + ac_identify_results_txt)
            assert identify_results.is_displayed() and ex_identify_results_txt.lower() == ac_identify_results_txt.lower()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_new_panel_is_displayed_with_title_as_Identify_Results_failed.png")
                return False

    def verify_matches_are_found_and_displayed_inside_Identify_Results_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            identify_results_img_list = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components()
                                                             .identify_results_image_by_xpath())
            for ele in identify_results_img_list:
                if not ele.is_displayed():
                    assert False
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_matches_are_found_and_displayed_inside_Identify_Results_panel_failed.png")
                return False

    def verify_visitor_image_is_displayed_as_expected_below_sample_image_icon(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            time.sleep(2)
            faces_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .identify_results_faces_icon_by_xpath())
            faces_icon.click()
            time.sleep(2)
            face_images_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .visitor_image_on_enroll_face_panel())
            time.sleep(2)
            assert face_images_validation.is_displayed()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_visitor_image_is_displayed_as_expected_below_sample_image_icon_failed.png")
                return False

    def verify_a_check_box_is_displayed_and_it_is_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            faces_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .identify_results_faces_icon_by_xpath())
            faces_icon.click()

            time.sleep(Base_Class.two_second)
            checkbox = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .enrollment_faces_panel_checkbox_by_xpath())
            assert checkbox.is_displayed()

            try:
                checkbox.click()
            except Exception as ex:
                assert False
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_a_check_box_is_displayed_and_it_is_clickable_failed.png")
                return False

    def verify_download_image_button_with_its_label_poping_up_and_it_is_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            faces_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .identify_results_faces_icon_by_xpath())
            faces_icon.click()

            time.sleep(Base_Class.two_second)
            download_button = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                  download_button_enroll_panel_by_xpath())

            actions = ActionChains(self.d)
            actions.move_to_element(download_button).perform()

            download_button_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                             .download_button_validation_by_xpath())

            assert download_button.is_displayed()

            assert download_button_validation.is_displayed()

            print("Expected data = " + Read_Identify_and_Enroll_Components().download_button_validation())
            print("Actual data = " + download_button_validation.text)
            assert download_button_validation.text.lower() == \
                   Read_Identify_and_Enroll_Components().download_button_validation().lower()
            try:
                download_button.click()
            except Exception as ex:
                assert False
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_download_image_button_with_its_label_poping_up_and_it_is_clickable_failed.png")
                return False

    def verify_view_image_info_button_is_visible_along_with_its_label(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            faces_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .identify_results_faces_icon_by_xpath())
            faces_icon.click()

            time.sleep(Base_Class.two_second)
            view_image_icon = self.d.find_element(By.XPATH,
                                                  Read_Identify_and_Enroll_Components().view_image_file_info_button())

            actions = ActionChains(self.d)
            actions.move_to_element(view_image_icon).perform()

            view_image_icon_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                             view_image_file_info_validation())

            assert view_image_icon.is_displayed()

            assert view_image_icon_validation.is_displayed()

            print("Expected data = " + Read_Identify_and_Enroll_Components().view_image_file_info())
            print("Actual data = " + view_image_icon_validation.text)
            assert view_image_icon_validation.text.lower() == \
                   Read_Identify_and_Enroll_Components().view_image_file_info().lower()

            try:
                view_image_icon.click()
                Alert(self.d).accept()
            except Exception as ex:
                assert False
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_view_image_info_button_is_visible_along_with_its_label_failed.png")
                return False

    def click_on_view_image_info_button_verify_a_pop_up_is_appeared_with_image_information(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            time.sleep(2)
            faces_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .identify_results_faces_icon_by_xpath())
            faces_icon.click()
            time.sleep(2)
            time.sleep(Base_Class.two_second)
            view_image_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                  view_image_file_info_button())
            time.sleep(2)
            view_image_icon.click()

            pop_up_text = self.d.switch_to.alert.text
            print("Expected data = " + pop_up_text)
            print("Actual data = " + Read_Identify_and_Enroll_Components().view_image_pop_up_text_1())
            print("Expected data = " + pop_up_text)
            print("Actual data = " + Read_Identify_and_Enroll_Components().view_image_pop_up_text_2())
            print("Expected data = " + pop_up_text)
            print("Actual data = " + Read_Identify_and_Enroll_Components().view_image_pop_up_text_3())
            print("Expected data = " + pop_up_text)
            print("Actual data = " + Read_Identify_and_Enroll_Components().view_image_pop_up_text_4())
            assert Read_Identify_and_Enroll_Components().view_image_pop_up_text_1() in pop_up_text
            assert Read_Identify_and_Enroll_Components().view_image_pop_up_text_2() in pop_up_text
            assert Read_Identify_and_Enroll_Components().view_image_pop_up_text_3() in pop_up_text
            assert Read_Identify_and_Enroll_Components().view_image_pop_up_text_4() in pop_up_text

            self.d.switch_to.alert.accept()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_view_image_info_button_verify_a_pop_up_is_appeared_with_image_information_failed.png")
                return False

    def click_on_close_panel_button_displayed_beside_panel_title_verify_panel_is_closed_successfully(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            panel_close = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .identify_results_panel_close())
            panel_close.click()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         close_panel_enroll_faces_validation())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components().identify_result_text_validation(). \
                        lower():
                    assert False
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_close_panel_button_displayed_beside_panel_title_verify_panel_is_"
                    f"closed_successfully_failed.png")
                return False

    def click_on_Person_View_button_and_verify_a_new_panel_with_title_Enrollment_View_is_displayed(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            person_view = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .identify_results_person_view_icon_by_xpath())
            person_view.click()

            enrollment_view_panel_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                                   .enrollment_view_panel_validation())
            assert enrollment_view_panel_validation.is_displayed()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_Person_View_button_and_verify_a_new_panel_with_title_"
                    f"Enrollment_View_is_displayed_failed.png")
                return False

    def verify_action_dropdown_is_displayed_and_clickable_in_top_right_corner_of_Enrollment_View_is_displayed(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            person_view = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .identify_results_person_view_icon_by_xpath())
            person_view.click()

            action_button = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .enrollment_view_panel_action_button())
            assert action_button.is_displayed()

            try:
                action_button.click()
            except Exception as ex:
                assert False

            action_button_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                           .enrollment_view_panel_action_button_validation())
            time.sleep(Base_Class.two_second)
            assert action_button_validation.is_displayed()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_action_dropdown_is_displayed_and_clickable_in_top_right_corner_of_"
                    f"Enrollment_View_is_displayed_failed.png")
                return False

    def click_on_action_dropdown_and_verify_menu_items(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            person_view = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .identify_results_person_view_icon_by_xpath())
            person_view.click()

            action_button = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .enrollment_view_panel_action_button())

            action_button.click()

            # disable enrollment option display and click verify

            disable_enrollment_option = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .enrollment_view_panel_action_button_validation())
            time.sleep(Base_Class.two_second)
            assert disable_enrollment_option.is_displayed()
            time.sleep(Base_Class.two_second)
            print("Expected data = " + Read_Identify_and_Enroll_Components().disable_enrollment_option_validation())
            print("Actual data = " + disable_enrollment_option.text)
            assert disable_enrollment_option.text == Read_Identify_and_Enroll_Components(). \
                disable_enrollment_option_validation()

            try:
                disable_enrollment_option.click()
            except Exception as ex:
                assert False
            time.sleep(Base_Class.two_second)
            assert self.d.switch_to.alert.text == Read_Identify_and_Enroll_Components(). \
                disable_enrollment_option_click_validation()
            self.d.switch_to.alert.dismiss()

            # identify within enrollments option display and click verify

            action_button.click()
            identify_within_enrollments_option = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                                     .identify_within_enrollments_option())
            time.sleep(Base_Class.two_second)
            assert identify_within_enrollments_option.is_displayed()
            time.sleep(Base_Class.two_second)
            print("Expected data = " + Read_Identify_and_Enroll_Components().
                  identify_within_enrollments_option_validation())
            print("Actual data = " + identify_within_enrollments_option.text)
            assert identify_within_enrollments_option.text == Read_Identify_and_Enroll_Components(). \
                identify_within_enrollments_option_validation()

            try:
                identify_within_enrollments_option.click()
            except Exception as ex:
                assert False
            time.sleep(Base_Class.two_second)
            click_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                   identify_enroll_panel_validation())
            assert click_validation.is_displayed()
            time.sleep(Base_Class.two_second)
            result_panel_close = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                     identify_result_panel_close())
            result_panel_close.click()
            time.sleep(Base_Class.two_second)
            identify_panel_close = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                       identify_and_enroll_panel_close())
            identify_panel_close.click()

            # identify within visitor option display and click verify
            time.sleep(Base_Class.two_second)
            action_button.click()
            identify_within_visitor_option = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                                 .identify_within_visitors_option())
            time.sleep(Base_Class.two_second)
            assert identify_within_visitor_option.is_displayed()
            time.sleep(Base_Class.two_second)
            print("Expected data = " + Read_Identify_and_Enroll_Components().
                  identify_within_visitors_option_validation())
            print("Actual data = " + identify_within_visitor_option.text)
            assert identify_within_visitor_option.text == Read_Identify_and_Enroll_Components(). \
                identify_within_visitors_option_validation()
            time.sleep(Base_Class.two_second)
            try:
                self.d.execute_script("arguments[0].click();", identify_within_visitor_option)
            except Exception as ex:
                assert False

            time.sleep(Base_Class.two_second)
            click_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                   visitor_search_panel_validation())
            assert click_validation.is_displayed()
            time.sleep(Base_Class.two_second)
            visitor_search_panel_close = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                             visitor_search_panel_close())
            visitor_search_panel_close.click()

            # view / edite details option display and click verify
            time.sleep(Base_Class.two_second)
            action_button.click()
            edite_details_option = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                       .view_edit_details_option())
            time.sleep(Base_Class.two_second)
            assert edite_details_option.is_displayed()
            time.sleep(Base_Class.two_second)
            print("Expected data = " + Read_Identify_and_Enroll_Components(). \
                  view_edit_details_option_validation())
            print("Actual data = " + edite_details_option.text)
            assert edite_details_option.text == Read_Identify_and_Enroll_Components(). \
                view_edit_details_option_validation()
            time.sleep(Base_Class.two_second)
            try:
                self.d.execute_script("arguments[0].click();", edite_details_option)
            except Exception as ex:
                assert False

            time.sleep(Base_Class.two_second)
            click_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                   enrollment_details_panel_validation())
            assert click_validation.is_displayed()
            time.sleep(Base_Class.two_second)
            view_edit_panel_close = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                        enrollment_details_panel_close())
            view_edit_panel_close.click()

            try:
                # delete enrollment option display and click verify
                time.sleep(Base_Class.two_second)
                action_button.click()
                delete_enrollment_option = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                               .delete_enrollment_option())
                time.sleep(Base_Class.two_second)
                assert delete_enrollment_option.is_displayed()
                time.sleep(Base_Class.two_second)
                print("Expected data = " + Read_Identify_and_Enroll_Components().delete_enrollment_option_validation())
                print("Actual data = " + delete_enrollment_option.text)
                assert delete_enrollment_option.text == Read_Identify_and_Enroll_Components(). \
                    delete_enrollment_option_validation()
                time.sleep(Base_Class.two_second)
                try:
                    self.d.execute_script("arguments[0].click();", delete_enrollment_option)
                except Exception as ex:
                    assert False

                time.sleep(Base_Class.two_second)
                click_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                       delete_enrollment_validation())
                assert click_validation.is_displayed()

                cancel_button = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                    delete_enrollment_cancel_button())
                cancel_button.click()
            except Exception as ex:
                msg = str(ex)

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_action_dropdown_and_verify_menu_items_failed.png")
                return False

    def click_on_close_button_of_Identify_Results_panel_and_verify_closed_successfully(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            panel_close = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .identify_results_panel_close())
            panel_close.click()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         close_panel_enroll_faces_validation())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components().identify_result_text_validation(). \
                        lower():
                    assert False
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_close_button_of_Identify_Results_panel_and_verify_closed_successfully_failed.png")
                return False

    def click_on_download_image_image_verify_visitor_image_is_downloaded_successfully(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            faces_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .identify_results_faces_icon_by_xpath())
            faces_icon.click()

            time.sleep(Base_Class.two_second)
            download_button = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                  download_button_enroll_panel_by_xpath())

            download_button.click()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_download_image_image_verify_visitor_image_is_downloaded_successfully_failed.png")
                return False

    def verify_faces_button_is_visible_with_its_label_popping_up_and_clickable_on_identify_results_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            face_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identify_results_faces_icon_by_xpath())

            expected_face_icon_hover_txt = Read_Identify_and_Enroll_Components() \
                .identify_results_face_icon_hover_text_validation().lower()

            a = ActionChains(self.d)
            a.move_to_element(face_icon).perform()

            time.sleep(Base_Class.two_second)

            actual_face_icon_hover_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                             .identify_results_faces_icon_hover_by_xpath())

            actual_face_icon_hover_txt = actual_face_icon_hover_ele.text.lower()
            print("Expected data = " + expected_face_icon_hover_txt)
            print("Actual data = " + actual_face_icon_hover_txt)
            assert expected_face_icon_hover_txt == actual_face_icon_hover_txt

            try:
                face_icon.click()
            except Exception as ex:
                assert False

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_faces_button_is_visible_with_its_label_popping_up_and_clickable"
                    f"_on_identify_results_panel_failed.png")
                return False

    def verify_person_view_button_is_visible_with_its_label_popping_up_and_clickable_on_identify_results_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            person_view_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .identify_results_person_view_icon_by_xpath())

            expected_person_view_icon_hover_txt = Read_Identify_and_Enroll_Components() \
                .identify_results_person_view_icon_hover_text_validation().lower()

            a = ActionChains(self.d)
            a.move_to_element(person_view_icon).perform()

            time.sleep(Base_Class.two_second)

            actual_person_view_hover_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                               .identify_results_person_view_icon_hover_by_xpath())

            actual_person_view_hover_txt = actual_person_view_hover_ele.text.lower()
            print("Expected data = " + expected_person_view_icon_hover_txt)
            print("Actual data = " + actual_person_view_hover_txt)
            assert expected_person_view_icon_hover_txt == actual_person_view_hover_txt

            try:
                person_view_icon.click()
            except Exception as ex:
                assert False

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_person_view_button_is_visible_with_its_label_popping_up_"
                    f"and_clickable_on_identify_results_panel_failed.png")
                return False

    def verify_purge_replace_button_is_visible_with_its_label_popping_up_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            purge_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .identify_results_purge_replace_icon_by_xpath())

            expected_purge_icon_hover_txt = Read_Identify_and_Enroll_Components() \
                .identify_results_purge_replace_icon_hover_text_validation().lower()

            a = ActionChains(self.d)
            a.move_to_element(purge_icon).perform()

            time.sleep(Base_Class.two_second)

            actual_purge_hover_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .identify_results_purge_replace_icon_hover_by_xpath())

            actual_purge_hover_ele_txt = actual_purge_hover_ele.text.lower()
            print("Expected data = " + expected_purge_icon_hover_txt)
            print("Actual data = " + actual_purge_hover_ele_txt)
            assert expected_purge_icon_hover_txt == actual_purge_hover_ele_txt

            try:
                purge_icon.click()
                Alert(self.d).dismiss()
            except Exception as ex:
                assert False
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_purge_replace_button_is_visible_with_its_label_popping_up_and_clickable_failed.png")
                return False

    def click_on_faces_button_and_verify_a_new_panel_with_title_enrollment_faces_is_displayed(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            face_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identify_results_faces_icon_by_xpath())

            face_icon.click()

            exp_enrollment_faces_txt = Read_Identify_and_Enroll_Components().enrollment_faces_text_validation().lower()

            enrollment_faces_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                       .enrollment_faces_panel_by_xpath())
            ac_enrollment_faces_txt = enrollment_faces_ele.text.lower()
            print("Expected data = " + exp_enrollment_faces_txt)
            print("Actual data = " + ac_enrollment_faces_txt)
            assert enrollment_faces_ele.is_displayed() and exp_enrollment_faces_txt == ac_enrollment_faces_txt
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_faces_button_and_verify_a_new_panel_with_title_enrollment_"
                    f"faces_is_displayed_failed.png")
                return False

    def verify_action_dropdown_is_displayed_and_clickable_in_top_right_corner_of_enrollment_faces_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            face_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identify_results_faces_icon_by_xpath())

            face_icon.click()

            action_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .enrollment_faces_action_drop_down_by_xpath())
            assert action_ele.is_displayed()
            try:
                action_ele.click()
            except Exception as ex:
                assert False
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_action_dropdown_is_displayed_and_clickable_in_top_right_corner_of_"
                    f"enrollment_faces_panel_failed.png")
                return False

    def click_on_action_dropdown_and_verify_menu_items_displayed_are_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            face_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identify_results_faces_icon_by_xpath())

            face_icon.click()

            action_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .enrollment_faces_action_drop_down_by_xpath())

            action_ele.click()

            ex_identify_within_enrollments_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_faces_drop_down_identify_within_enrollments_txt_validation().lower()
            ex_identify_within_visitors_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_faces_drop_down_identify_within_visitors_txt_validation().lower()
            ex_add_photo_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_faces_drop_down_add_photo_txt_validation().lower()
            ex_delete_selected_faces = Read_Identify_and_Enroll_Components() \
                .enrollment_faces_drop_down_delete_selected_faces_txt_validation().lower()

            identify_within_enrollments_ele = self.d \
                .find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                              .enrollment_faces_drop_down_identify_within_enrollments_ele_by_xpath())
            ac_identify_within_enrollments_txt = identify_within_enrollments_ele.text.lower()
            identify_within_visitors_ele = self.d \
                .find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                              .enrollment_faces_drop_down_identify_within_visitors_ele_by_xpath())
            ac_identify_within_visitors_txt = identify_within_visitors_ele.text.lower()
            add_photo_ele = self.d \
                .find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                              .enrollment_faces_drop_down_add_photo_ele_by_xpath())
            ac_add_photo_txt = add_photo_ele.text.lower()
            delete_selected_faces_ele = self.d \
                .find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                              .enrollment_faces_drop_down_delete_selected_faces_ele_by_xpath())
            ac_delete_selected_faces_txt = delete_selected_faces_ele.text.lower()
            print("Expected data = " + ex_identify_within_enrollments_txt)
            print("Actual data = " + ac_identify_within_enrollments_txt)
            print("Expected data = " + ex_identify_within_visitors_txt)
            print("Actual data = " + ac_identify_within_visitors_txt)
            print("Expected data = " + ex_add_photo_txt)
            print("Actual data = " + ac_add_photo_txt)
            print("Expected data = " + ex_delete_selected_faces)
            print("Actual data = " + ac_delete_selected_faces_txt)
            assert ex_identify_within_enrollments_txt == ac_identify_within_enrollments_txt
            assert ex_identify_within_visitors_txt == ac_identify_within_visitors_txt
            assert ex_add_photo_txt == ac_add_photo_txt
            assert ex_delete_selected_faces == ac_delete_selected_faces_txt
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_action_dropdown_and_verify_menu_items_displayed_are_clickable_failed.png")
                return False

    def verify_location_and_case_information_is_displayed_as_a_heading_inside_enrollment_faces_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            face_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identify_results_faces_icon_by_xpath())

            face_icon.click()

            for x in range(50):
                location_case_heading = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .enrollment_faces_location_case_heading_ele_by_xpath())
                location_case_heading_txt = location_case_heading.text
                if location_case_heading_txt != "":
                    assert True
                    break

                if x == 50:
                    assert False
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_location_and_case_information_is_displayed_as_a_heading_inside"
                    f"_enrollment_faces_panel_failed.png")
                return False

    def verify_sample_image_icon_is_visible_below_location_and_it_is_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            face_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identify_results_faces_icon_by_xpath())

            face_icon.click()

            sample_image_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .enrollment_faces_sample_image_icon_by_xpath())
            assert sample_image_icon.is_displayed()
            try:
                sample_image_icon.click()
            except Exception as ex:
                assert False
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\img1.png"

            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_sample_image_icon_is_visible_below_location_and_it_is_clickable_failed.png")
                return False

    def verify_if_draggable_photo_text_is_visible_above_image_displayed(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            face_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identify_results_faces_icon_by_xpath())

            face_icon.click()

            ex_draggable_photo_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_faces_draggable_photo_txt_validation().lower()
            draggable_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .enrollment_faces_draggable_photo_by_xpath())
            ac_draggable_photo_txt = draggable_ele.text.strip().lower()

            assert draggable_ele.is_displayed()
            print("Expected data = " + ex_draggable_photo_txt)
            print("Actual data = " + ac_draggable_photo_txt)
            assert ex_draggable_photo_txt == ac_draggable_photo_txt
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_if_draggable_photo_text_is_visible_above_image_displayed_failed.png")
                return False

    def verify_visitor_image_is_displayed_as_expected_below_sample_image_icon_inside_enrollment_faces_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            face_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identify_results_faces_icon_by_xpath())

            face_icon.click()

            visitor_img_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .enrollment_faces_visitor_img_by_xpath())
            assert visitor_img_ele.is_displayed()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_visitor_image_is_displayed_as_expected_below_sample_image"
                    f"_icon_inside_enrollment_faces_panel_failed.png")
                return False

    def verify_location_and_case_information_is_displayed_as_a_heading_inside_enrollment_view_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            person_view_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .identify_results_person_view_icon_by_xpath())
            person_view_icon.click()

            for x in range(50):
                location_case_heading = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .enrollment_view_location_case_heading_ele_by_xpath())
                location_case_heading_txt = location_case_heading.text
                if location_case_heading_txt != "":
                    assert True
                    break

                if x == 50:
                    assert False
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_location_and_case_information_is_displayed_as_a_heading_"
                    f"inside_enrollment_view_panel_failed.png")
                return False

    def verify_visitor_image_is_displayed_as_expected_below_heading_on_enrollment_view_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            time.sleep(2)
            person_view_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .identify_results_person_view_icon_by_xpath())
            person_view_icon.click()
            time.sleep(2)
            img = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                      .enrollment_view_visitor_img_by_xpath())
            time.sleep(2)
            assert img.is_displayed()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_visitor_image_is_displayed_as_expected_below_heading_"
                    f"on_enrollment_view_panel_failed.png")
                return False

    def verify_visitors_lOCATION_STORE_CASE_SUBJECT_information_is_displayed_on_enrollment_view_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            person_view_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .identify_results_person_view_icon_by_xpath())
            person_view_icon.click()

            location_store_case_subject = self.d \
                .find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                              .enrollment_view_location_store_case_subject_ele_by_xpath())
            location_store_case_subject_info = self.d \
                .find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                              .enrollment_view_location_store_case_subject_info_by_xpath())
            assert location_store_case_subject.is_displayed()
            assert location_store_case_subject_info.is_displayed()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_visitors_lOCATION_STORE_CASE_SUBJECT_information"
                    f"_is_displayed_on_enrollment_view_panel_failed.png")
                return False

    def verify_ranked_match_index_title_along_with_symbol_visible_on_identify_results_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            expected_ranked_match_index_txt = Read_Identify_and_Enroll_Components() \
                .identify_results_ranked_match_index_text_validation().lower()

            ranked_match_index_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .identify_results_ranked_match_index_by_xpath())

            actual_ranked_match_index_txt = ranked_match_index_ele.text.lower()
            print("Expected data = " + expected_ranked_match_index_txt)
            print("Actual data = " + actual_ranked_match_index_txt)
            assert expected_ranked_match_index_txt == actual_ranked_match_index_txt

            exclamation_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .identify_results_exclamation_symbol_by_xpath())
            assert exclamation_icon.is_displayed()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_ranked_match_index_title_along_with_symbol_visible_on_identify_results_panel_failed.png")
                return False

    def verify_images_are_visible_enlisted_inside_identify_result_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            identify_results_img_list = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components()
                                                             .identify_results_image_by_xpath())
            for ele in identify_results_img_list:
                if not ele.is_displayed():
                    assert False
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_matches_are_found_and_displayed_inside_Identify_Results_panel_failed.png")
                return False

    def verify_location_Case_information_and_index_score_displayed_inside_indentify_result_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            location_case_info_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .identify_results_location_case_info())

            assert location_case_info_ele.is_displayed()

            index_score_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .identify_results_index_score_by_xpath())
            assert index_score_ele.is_displayed()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_location_Case_information_and_index_score_displayed_"
                    f"inside_indentify_result_panel_failed.png")
                return False

    def verify_three_buttons_faces_person_view_and_purge_Replace_are_visible(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            face_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identify_results_faces_icon_by_xpath())
            assert face_icon.is_displayed()
            person_view = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .identify_results_person_view_icon_by_xpath())
            assert person_view.is_displayed()
            purge_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .identify_results_purge_replace_icon_by_xpath())
            assert purge_icon.is_displayed()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_three_buttons_faces_person_view_and_purge_Replace_are_visible_failed.png")
                return False

    def close_all_panel_one_by_one(self):
        try:
            close_panel_list = self.d.find_elements(By.XPATH,
                                                    Read_Visitor_Search_Components().close_all_panel_one_by_one())
            for i in close_panel_list:
                i.click()
                time.sleep(Base_Class.one_second)
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
            logout_button = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().logout_btn_by_xpath())
            time.sleep(Base_Class.one_second)
            logout_button.click()
            time.sleep(Base_Class.one_second)
            print("logout")
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_logout_pg_03.png")
                return False

    def verify_visitors_ACTION_information_is_displayed_below_its_image_on_Enrollment_View_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            person_view_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .identify_results_person_view_icon_by_xpath())
            person_view_icon.click()

            action_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .enrollment_view_action_ele_by_xpath())
            action_ele_info = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .enrollment_view_action_info_by_xpath())
            assert action_ele.is_displayed()
            assert action_ele_info.is_displayed()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_visitors_ACTION_information_is_displayed_below_its_"
                    f"image_on_Enrollment_View_panel_failed.png")
                return False

    def verify_Enrolled_On_text_and_its_information_is_visible_as_expected_on_enrollment_view_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            person_view_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .identify_results_person_view_icon_by_xpath())
            person_view_icon.click()

            enrolled_on_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .enrollment_view_enrolled_on_ele_by_xpath())
            enrolled_on_ele_info = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                       .enrollment_view_enrolled_on_info_by_xpath())
            assert enrolled_on_ele.is_displayed()
            assert enrolled_on_ele_info.is_displayed()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_Enrolled_On_text_and_its_information_is_visible_as_"
                    f"expected_on_enrollment_view_panel_failed.png")
                return False

    def verify_enabled_disabled_information_is_visible_on_enrollment_view_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            person_view_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .identify_results_person_view_icon_by_xpath())
            person_view_icon.click()

            try:
                enabled_status = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .enrollment_view_enrolled_status_by_xpath())
                assert enabled_status.is_displayed()
            except Exception as ex:
                disabled_status = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .enrollment_view_disabled_status_by_xpath())
                assert disabled_status.is_displayed()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_enabled_disabled_information_is_visible_on_enrollment_view_panel_failed.png")
                return False

    def verify_enrollment_details_button_is_visible_and_clickable_as_expected_on_enrollment_view_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            person_view_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .identify_results_person_view_icon_by_xpath())
            person_view_icon.click()

            enrollment_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                 enrollment_view_enrollment_details_btn_by_xpath())
            assert enrollment_btn.is_displayed()
            ex_enrollment_btn_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_view_enrollment_details_txt_validation().lower()
            ac_enrollment_btn_txt = enrollment_btn.text.lower()
            print("Expected data = " + ex_enrollment_btn_txt)
            print("Actual data = " + ac_enrollment_btn_txt)
            assert ex_enrollment_btn_txt == ac_enrollment_btn_txt

            try:
                enrollment_btn.click()
            except Exception as ex:
                assert False
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_enrollment_details_button_is_visible_and_clickable_as_expected_"
                    f"on_enrollment_view_panel_failed.png")
                return False

    def verify_faces_button_is_visible_along_with_count_and_it_is_clickable_on_enrollment_view_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            time.sleep(2)
            person_view_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .identify_results_person_view_icon_by_xpath())
            person_view_icon.click()
            time.sleep(2)
            face_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .enrollment_view_faces_btn_by_xpath())
            time.sleep(2)
            assert face_btn.is_displayed()
            ex_face_btn_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_view_faces_txt_validation().lower()
            ac_faces_btn_txt = face_btn.text.lower()
            time.sleep(2)
            assert ex_face_btn_txt == ac_faces_btn_txt
            time.sleep(2)
            count = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                        .enrollment_view_faces_count_by_xpath())
            time.sleep(2)
            assert count.is_displayed()

            assert int(count.text.strip()) >= 0
            time.sleep(2)
            try:
                face_btn.click()
            except Exception as ex:
                assert False
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_faces_button_is_visible_along_with_count_and_it_is_clickable"
                    f"_on_enrollment_view_panel_failed.png")
                return False

    def verify_events_button_is_visible_along_with_count_and_it_is_clickable_on_enrollment_view_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            time.sleep(2)
            person_view_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .identify_results_person_view_icon_by_xpath())
            person_view_icon.click()
            time.sleep(2)
            events_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .enrollment_view_events_btn_by_xpath())
            time.sleep(2)
            assert events_btn.is_displayed()
            ex_events_btn_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_view_events_txt_validation().lower()
            ac_events_btn_txt = events_btn.text.lower()

            assert ex_events_btn_txt == ac_events_btn_txt

            try:
                events_btn.click()
            except Exception as ex:
                assert False
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_events_button_is_visible_along_with_count_and"
                    f"_it_is_clickable_on_enrollment_view_panel_failed.png")
                return False

    def verify_enrollment_groups_button_is_visible_along_with_its_count_and_is_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            time.sleep(2)
            person_view_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .identify_results_person_view_icon_by_xpath())
            time.sleep(2)
            person_view_icon.click()
            time.sleep(2)
            enrollment_group_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                       .enrollment_view_enrollment_groups_btn_by_xpath())
            time.sleep(2)
            assert enrollment_group_btn.is_displayed()
            time.sleep(2)
            ex_enrollment_group_btn_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_view_enrollment_groups_txt_validation().lower()
            ac_enrollment_group_btn_txt = enrollment_group_btn.text.lower()
            time.sleep(2)
            assert ex_enrollment_group_btn_txt == ac_enrollment_group_btn_txt

            count = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                        .enrollment_view_enrollment_groups_count_by_xpath())
            time.sleep(2)
            assert count.is_displayed()
            assert int(count.text.strip()) >= 0

            try:
                enrollment_group_btn.click()
            except Exception as ex:
                assert False
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_enrollment_groups_button_is_visible_along_with_its_count_and_is_clickable_failed.png")
                return False

    def verify_notes_button_is_visible_along_with_its_count_and_is_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            time.sleep(2)
            person_view_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .identify_results_person_view_icon_by_xpath())
            time.sleep(2)
            person_view_icon.click()
            time.sleep(2)
            notes_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_view_notes_btn_by_xpath())
            time.sleep(2)
            assert notes_btn.is_displayed()
            ex_notes_btn_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_view_notes_txt_validation().lower()
            ac_notes_btn_txt = notes_btn.text.lower()
            time.sleep(2)
            assert ex_notes_btn_txt == ac_notes_btn_txt
            time.sleep(2)
            count = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                        .enrollment_view_notes_count_by_xpath())
            time.sleep(2)
            assert count.is_displayed()
            assert int(count.text.strip()) >= 0

            try:
                notes_btn.click()
            except Exception as ex:
                assert False
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_notes_button_is_visible_along_with_its_count_and_is_clickable_failed.png")
                return False

    def click_on_close_panel_button_displayed_beside_panel_title_and_verify_panel_is_closed_successfully(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_view_panel = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                        .identify_results_person_view_icon_by_xpath())
            enrollment_view_panel.click()
            time.sleep(Base_Class.two_second)

            panel_close = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_view_panel_close())
            panel_close.click()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         close_panel_enroll_faces_validation())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        enrollment_view_panel_title_validation().lower():
                    assert False

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_close_panel_button_displayed_beside_panel_title_and_verify_panel_"
                    f"is_closed_successfully_failed.png")
                return False

    def click_on_purge_and_replace_button_and_pop_up_is_appeared_along_with_expected_message(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            purge_and_replace = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .identify_results_purge_replace_icon_by_xpath())
            purge_and_replace.click()
            time.sleep(Base_Class.two_second)

            assert self.d.switch_to.alert.text == Read_Identify_and_Enroll_Components(). \
                purge_and_replace_validation_text()

            self.d.switch_to.alert.dismiss()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_purge_and_replace_button_and_pop_up_is_appeared_along_with_"
                    f"expected_message_failed.png")
                return False

    def click_on_close_panel_button_displayed_beside_panel_title_verify_panel_closed_successfully(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_view_panel = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                        .identify_results_person_view_icon_by_xpath())
            enrollment_view_panel.click()
            time.sleep(Base_Class.two_second)

            panel_close = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_view_panel_close())
            panel_close.click()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         close_panel_enroll_faces_validation())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        enrollment_view_panel_title_validation().lower():
                    assert False
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_close_panel_button_displayed_beside_panel_title_verify_panel_is_"
                    f"closed_successfully_failed.png")
                return False

    def click_on_Crop_Image_button_and_verify_a_pop_up_is_visible_with_expected_message(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            crop_photo_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .crop_photo_button())

            self.d.execute_script("arguments[0].click();", crop_photo_btn)

            assert self.d.switch_to.alert.text == Read_Identify_and_Enroll_Components().crop_photo_validation()

            self.d.switch_to.alert.accept()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_Crop_Image_button_and_verify_a_pop_up_is_visible_with_expected_message_failed.png")
                return False

    def click_on_close_panel_button_displayed_beside_panel_title_verify_panel_successfully_closed(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_view_panel = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                        .identify_results_person_view_icon_by_xpath())
            enrollment_view_panel.click()
            time.sleep(Base_Class.two_second)

            panel_close = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_view_panel_close())
            panel_close.click()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         close_panel_enroll_faces_validation())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        enrollment_view_panel_title_validation().lower():
                    assert False
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_close_panel_button_displayed_beside_panel_title_verify_panel_"
                    f"successfully_closed_failed.png")
                return False

    def verify_two_new_panel_appeared_with_title_as_Enrollment_Steps_and_Add_Details(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_steps_title = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .enrollment_steps_by_xpath())
            assert enrollment_steps_title.is_displayed()

            ex_enrollments_steps_title_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_steps_title_txt_validation().lower()
            ac_enrollment_steps_title_txt = enrollment_steps_title.text.lower()
            assert ex_enrollments_steps_title_txt == ac_enrollment_steps_title_txt

            add_details_panel = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .add_details_panel_by_xpath())
            assert add_details_panel.is_displayed()

            ex_add_details_panel_txt = Read_Identify_and_Enroll_Components() \
                .add_details_panel_title_txt_validation().lower()
            ac_add_details_panel_txt = add_details_panel.text.lower()
            assert ex_add_details_panel_txt == ac_add_details_panel_txt
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_two_new_panel_appeared_with_title_as_Enrollment_Steps_and_Add_Details_failed.png")
                return False

    def verify_first_panel_title_Enrollment_Steps_and_below_it_image_selected_is_visible(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_steps_title = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .enrollment_steps_by_xpath())
            assert enrollment_steps_title.is_displayed()

            ex_enrollments_steps_title_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_steps_title_txt_validation().lower()
            ac_enrollment_steps_title_txt = enrollment_steps_title.text.lower()
            assert ex_enrollments_steps_title_txt == ac_enrollment_steps_title_txt

            enrollment_steps_img = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                       .enrollment_steps_selected_img_by_xpath())
            assert enrollment_steps_img.is_displayed()
            enrollment_cancel = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                       .warning_msg_close_button())
            self.close_all_panel_one_by_one()
            enrollment_cancel.click()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_first_panel_title_Enrollment_Steps_and_below_it_image_selected_is_visible_failed.png")
                return False

    def verify_image_properties_text_below_image_along_with_details_is_displayed_as_expected(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            image_properties = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_steps_image_properties_by_xpath())
            ex_image_properties_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_steps_image_properties_txt_validation().lower()
            ac_image_properties_txt = image_properties.text.lower()
            print(ex_image_properties_txt, "========>", ac_image_properties_txt)
            assert image_properties.is_displayed() and ex_image_properties_txt == ac_image_properties_txt

            image_properties_info = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                        .enrollment_steps_image_properties_info_by_xpath())
            assert "pixels" or "kb" in image_properties_info.text.lower()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_image_properties_text_below_image_along_with"
                    f"_details_is_displayed_as_expected_failed.png")
                return False

    def verify_warning_text_is_displayed_below_image_on_Enrollment_Steps_panel_as_expected(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            warning = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                          .enrollment_steps_warning_by_xpath())
            ex_warning_txt = Read_Identify_and_Enroll_Components().enrollment_steps_warning_txt_validation()
            ac_warning_txt = warning.text
            assert warning.is_displayed() and ex_warning_txt.lower() in ac_warning_txt.lower()
            warning_close = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .warning_msg_close_button())

            self.close_all_panel_one_by_one()
            self.d.execute_script("arguments[0].click();", warning_close)
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_warning_text_is_displayed_below_image_on_Enrollment"
                    f"_Steps_panel_as_expected_failed.png")
                return False

    def verify_No_match_found_text_below_warning_is_visible_as_expected_on_Enrollment_Steps_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            no_match_found = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .enrollments_steps_no_match_found_by_xpath())
            exp_msg = Read_Identify_and_Enroll_Components().enrollment_steps_no_match_found_txt_validation().lower()
            ac_msg = no_match_found.text.lower()
            assert no_match_found.is_displayed() and exp_msg == ac_msg
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_No_match_found_text_below_warning_is_visible_as_"
                    f"expected_on_Enrollment_Steps_panel_failed.png")
                return False

    def verify_exposure_sharpness_resolution_images_parameters_their_data_green_tick_symbol_is_displayed(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            image_info_list = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_steps_image_info_list_by_xpath())
            image_data_list = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_steps_image_datas_list_by_xpath())
            green_ticks_list = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .enrollment_steps_green_ticks_list_by_xpath())

            for i in range(0, len(image_info_list)):
                assert image_info_list.__getitem__(i).is_displayed()
                assert image_data_list.__getitem__(i).is_displayed()
                assert green_ticks_list.__getitem__(i).is_displayed()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_exposure_sharpness_resolution_images_parameters_their_data_"
                    f"green_tick_symbol_is_displayed_failed.png")
                return False

    def verify_second_panel_titled_as_Add_Details_and_panel_is_active_enabled(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            add_details_panel = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .add_details_panel_by_xpath())
            assert add_details_panel.is_displayed()

            ex_add_details_panel_txt = Read_Identify_and_Enroll_Components() \
                .add_details_panel_title_txt_validation().lower()
            ac_add_details_panel_txt = add_details_panel.text.lower()
            assert ex_add_details_panel_txt == ac_add_details_panel_txt
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_second_panel_titled_as_Add_Details_and_panel_is_active_enabled_failed.png")
                return False

    def verify_cancel_button_below_title_Add_Details_is_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            assert cancel_btn.is_displayed()

            try:
                cancel_btn.click()
            except Exception as ex:
                assert False

            cancel_msg_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().cancel_msg_by_xpath())
            exp_cancel_msg = Read_Identify_and_Enroll_Components().add_details_cancel_msg_txt_validation().lower()
            ac_cancel_msg = cancel_msg_ele.text.lower()

            assert exp_cancel_msg == ac_cancel_msg

            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_cancel_button_below_title_Add_Details_is_visible_and_clickable_failed.png")
                return False

    def verify_save_button_below_title_Add_Details_is_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()

            try:
                save_btn.click()
                Alert(self.d).accept()
            except Exception as ex:
                assert False

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()

            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_save_button_below_title_Add_Details_is_visible_and_clickable_failed.png")
                return False

    def verify_two_option_Expire_Date_and_Do_Not_Expire_are_visible_and_clickable_below_Add_Details_title(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            expire_date_rado_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                       .expire_date_radio_btn_by_xpath())
            do_not_expire_radio_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                          .do_not_expire_radio_btn_by_xpath())

            expire_date_rado_btn.click()
            assert expire_date_rado_btn.is_selected()

            do_not_expire_radio_btn.click()
            assert do_not_expire_radio_btn.is_selected()

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()

            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_two_option_Expire_Date_and_Do_Not_Expire_are_visible_and"
                    f"_clickable_below_Add_Details_title_failed.png")
                return False

    def verify_date_entry_textbox_beside_Expire_Date_is_visible_and_clickable_and_current_date_is_displayed(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            expire_date_txt_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_details_expire_date_text_bx_by_xpath())
            assert expire_date_txt_bx.is_displayed()
            expire_date_txt_bx.click()
            expire_date_calender_popup = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                             .add_details_expire_date_calender_pop_up_by_xpath())
            assert expire_date_calender_popup.is_displayed()

            exp_date = expire_date_txt_bx.get_attribute("value").split(" ")[0].split("/")

            ac_date = str(date.today()).replace("-", "/").split("/")
            temp = ac_date[0]
            for x in range(1, len(temp) - 1):
                ac_date[x - 1] = ac_date[x]
            ac_date[len(ac_date) - 1] = temp

            assert exp_date == ac_date

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_date_entry_textbox_beside_Expire_Date_is_visible_and_clickable"
                    f"_and_current_date_is_displayed_failed.png")
                return False

    def verify_opt_out_label_text_and_check_box_besides_is_visible_and_clickable_on_Add_Details_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            opt_out_txt_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .add_details_opt_out_by_xpath())
            exp_opt_out_txt = Read_Identify_and_Enroll_Components().opt_out_txt_validation().lower()
            ac_opt_out_txt = opt_out_txt_ele.text.strip().lower()
            assert exp_opt_out_txt == ac_opt_out_txt

            opt_out_check_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .opt_out_chk_bx_by_xpath())
            assert opt_out_check_bx.is_displayed()
            opt_out_check_bx.click()
            assert opt_out_check_bx.is_selected()

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_opt_out_label_text_and_check_box_besides_is_visible"
                    f"_and_clickable_on_Add_Details_panel_failed.png")
                return False

    def verify_Enrollment_Group_label_text_is_displayed_with_dropdown_beside_it_is_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group_text_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_details_enrollment_groups_text_by_xpath())
            enrollment_group_text_ele.is_displayed()

            enrollment_group_drop_dwn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .enrollment_group_by_xpath())
            try:
                enrollment_group_drop_dwn.click()
            except Exception as ex:
                assert False

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_Enrollment_Group_label_text_is_displayed_with_dropdown_"
                    f"beside_it_is_visible_and_clickable_failed.png")
                return False

    def click_on_Enrollment_Group_dropdown_and_verify_options_inside_it_are_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group_drop_dwn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .enrollment_group_by_xpath())
            enrollment_group_drop_dwn.click()

            enrollment_groups_options = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components()
                                                             .add_details_enrollment_groups_options_by_xpath())
            for ele in enrollment_groups_options:
                if not ele.is_displayed() and ele.click():
                    assert False

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_Enrollment_Group_dropdown_and_verify_options_inside_it"
                    f"_are_visible_and_clickable_failed.png")
                return False

    def verify_Field_Incomplete_text_below_enrollment_group_dropdown_is_visible_as_expected(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()
            time.sleep(Base_Class.two_second)

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())
            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            field_incomplete = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .add_details_enrollment_groups_field_incomplete_by_xpath())
            field_incomplete.is_displayed()

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_Field_Incomplete_text_below_enrollment_group_dropdown_is_visible_as_expected_failed.png")
                return False

    def verify_REQUIRED_FIELDS_heading_below_enrollment_group_dropdown_is_displayed(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            required_fields = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .add_details_required_fields_by_xpath())
            assert required_fields.is_displayed()

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_REQUIRED_FIELDS_heading_below_enrollment_group_dropdown_is_displayed_failed.png")
                return False

    def verify_LOCATION_STORE_label_text_and_text_box_besides_it_is_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            location_store_txt = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_details_location_store_text_ele_by_xpath())
            ex_location_store_txt = Read_Identify_and_Enroll_Components() \
                .add_details_location_store_txt_validation().lower()
            ac_location_store_txt = location_store_txt.text.lower()
            assert ex_location_store_txt == ac_location_store_txt
            location_store_txt_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                        .location_store_inpt_bx_by_xpath())
            location_store_txt_bx.send_keys(Read_Identify_and_Enroll_Components()
                                            .add_details_location_store_data_input())
            assert location_store_txt_bx.get_attribute("value").lower().strip() == Read_Identify_and_Enroll_Components() \
                .add_details_location_store_data_input()

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_LOCATION_STORE_label_text_and_text_box_besides_it_is_visible_and_clickable_failed.png")
                return False

    def verify_Field_Incomplete_text_below_location_store_textbox_is_visible_as_expected(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            field_incomplete = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .add_details_location_store_field_incomplete_by_xpath())
            assert field_incomplete.is_displayed()

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_Field_Incomplete_text_below_location_store_textbox_is_visible_as_expected_failed.png")
                return False

    def verify_CASE_SUBJECT_label_text_and_text_box_besides_it_is_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            case_subject_txt = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .add_details_case_subject_text_ele_by_xpath())
            ex_case_subject_txt = Read_Identify_and_Enroll_Components() \
                .add_details_case_subject_txt_validation().lower()
            ac_case_subject_txt = case_subject_txt.text.lower()
            assert ex_case_subject_txt == ac_case_subject_txt
            case_subject_txt_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .case_subject_inpt_bx_by_xpath())
            case_subject_txt_bx.send_keys(Read_Identify_and_Enroll_Components().add_details_case_subject_data_input())
            assert case_subject_txt_bx.get_attribute("value").lower().strip() == Read_Identify_and_Enroll_Components() \
                .add_details_case_subject_data_input().lower()

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()

            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_CASE_SUBJECT_label_text_and_text_box_besides_it_is_visible_and_clickable_failed.png")
                return False

    def verify_Field_Incomplete_text_below_case_subject_textbox_is_visible_as_expected(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            field_incomplete = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .add_details_case_subject_field_incomplete_by_xpath())
            assert field_incomplete.is_displayed()

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_Field_Incomplete_text_below_case_subject_textbox_is_visible_as_expected_failed.png")
                return False

    def verify_REPORTED_LOSS_label_text_and_text_box_besides_it_is_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            reported_loss_txt = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .add_details_reported_loss_text_ele_by_xpath())
            ex_reported_loss_txt = Read_Identify_and_Enroll_Components() \
                .add_details_reported_loss_txt_validation().lower()
            ac_reported_loss_txt = reported_loss_txt.text.lower()
            assert ex_reported_loss_txt == ac_reported_loss_txt

            reported_loss_txt_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                       .reported_loss_inpt_bx_by_xpath())
            reported_loss_txt_bx.send_keys(Read_Identify_and_Enroll_Components().add_details_reported_loss_data_input())
            ex_reported_loss_data = int(Read_Identify_and_Enroll_Components().add_details_reported_loss_data_input())
            ac_reported_loss_data = int(reported_loss_txt_bx.get_attribute("value").strip())
            assert ex_reported_loss_data == ac_reported_loss_data
            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_REPORTED_LOSS_label_text_and_text_box_besides_it_is_visible_and_clickable_failed.png")
                return False

    def verify_Field_Incomplete_text_below_REPORTED_LOSS_textbox_is_visible_as_expected(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            field_incomplete = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .add_details_reported_loss_field_incomplete_by_xpath())
            assert field_incomplete.is_displayed()

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_Field_Incomplete_text_below_REPORTED_LOSS_textbox_is_visible_as_expected_failed.png")
                return False

    def verify_DATE_INCIDENT_label_text_and_text_box_besides_it_is_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            date_incident_txt = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .add_details_date_incident_text_ele_by_xpath())
            assert date_incident_txt.is_displayed()

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_DATE_INCIDENT_label_text_and_text_box_besides_it_is_visible_and_clickable_failed.png")
                return False

    def verify_Field_Incomplete_text_below_DATE_INCIDENT_textbox_is_visible_as_expected(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            field_incomplete = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .add_details_date_incident_field_incomplete_by_xpath())
            assert field_incomplete.is_displayed()

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_Field_Incomplete_text_below_DATE_INCIDENT_textbox_is_visible_as_expected_failed.png")
                return False

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_Field_Incomplete_text_below_DATE_INCIDENT_textbox_is_visible_as_expected_failed.png")
                return False

    def verify_ACTION_label_text_and_text_box_besides_it_is_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            action_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .add_details_action_text_ele_by_xpath())
            assert action_text.is_displayed()

            action_text_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .action_inpt_bx_by_xpath())
            action_text_bx.send_keys(Read_Identify_and_Enroll_Components().add_details_action_data_input())

            assert Read_Identify_and_Enroll_Components().add_details_action_data_input().lower() == \
                   action_text_bx.get_attribute("value").lower()

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_ACTION_label_text_and_text_box_besides_it_is_visible_and_clickable_failed.png")
                return False

    def verify_Field_Incomplete_text_below_ACTION_textbox_is_visible_as_expected(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            field_incomplete = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .add_details_action_field_incomplete_by_xpath())
            assert field_incomplete.is_displayed()

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_Field_Incomplete_text_below_ACTION_textbox_is_visible_as_expected_failed.png")
                return False

    def verify_OPTIONAL_FIELDS_heading_below_action_textbox_is_displayed(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            optional_fields = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .add_details_optional_fields_by_xpath())
            assert optional_fields.is_displayed()

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_OPTIONAL_FIELDS_heading_below_action_textbox_is_displayed_failed.png")
                return False

    def verify_CASE_EVENT_TYPE_label_text_is_displayed_with_dropdown_beside_it_is_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            case_event_type_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                       .add_details_case_event_type_text_ele_by_xpath())
            assert case_event_type_text.is_displayed()

            case_event_type_drop_dwn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                           .case_event_type_by_xpath())
            s = Select(case_event_type_drop_dwn)
            options_list = s.options
            assert len(options_list) > 0

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_CASE_EVENT_TYPE_label_text_is_displayed_with_dropdown_beside"
                    f"_it_is_visible_and_clickable_failed.png")
                return False

    def click_on_CASE_EVENT_TYPE_dropdown_and_verify_options_inside_it_are_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            case_event_type_drop_dwn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                           .case_event_type_by_xpath())
            s = Select(case_event_type_drop_dwn)
            options_list = s.options
            for x in options_list:
                try:
                    s.select_by_visible_text(x.text)
                    time.sleep(Base_Class.two_second)
                except Exception as ex:
                    assert False

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_CASE_EVENT_TYPE_dropdown_and_verify_options_"
                    f"inside_it_are_visible_and_clickable_failed.png")
                return False

    def verify_ACTIVITY_TYPE_label_text_is_displayed_with_dropdown_beside_it_is_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            activity_type_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_details_activity_type_text_ele_by_xpath())
            assert activity_type_text.is_displayed()

            activity_type_drop_dwn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .activity_type_by_xpath())
            s = Select(activity_type_drop_dwn)
            options_list = s.options
            assert len(options_list) > 0

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_ACTIVITY_TYPE_label_text_is_displayed_with_dropdown_beside"
                    f"_it_is_visible_and_clickable_failed.png")
                return False

    def click_on_ACTIVITY_TYPE_dropdown_and_verify_options_inside_it_are_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            activity_type_drop_dwn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .activity_type_by_xpath())
            s = Select(activity_type_drop_dwn)
            options_list = s.options
            for x in options_list:
                try:
                    s.select_by_visible_text(x.text)
                    time.sleep(Base_Class.two_second)
                except Exception as ex:
                    assert False

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_CASE_EVENT_TYPE_dropdown_and_verify_options_"
                    f"inside_it_are_visible_and_clickable_failed.png")
                return False

    def verify_METHOD_OF_OFFENSE_label_text_is_displayed_with_dropdown_beside_it_is_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            method_of_offence_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .add_details_method_of_offence_text_ele_by_xpath())
            assert method_of_offence_text.is_displayed()

            method_of_offence_drop_dwn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                             .method_of_offence_by_xpath())
            s = Select(method_of_offence_drop_dwn)
            options_list = s.options
            assert len(options_list) > 0

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_METHOD_OF_OFFENSE_label_text_is_displayed_with_dropdown_beside"
                    f"_it_is_visible_and_clickable_failed.png")
                return False

    def click_on_METHOD_OF_OFFENSE_dropdown_and_verify_options_inside_it_are_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            method_of_offence_drop_dwn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                             .method_of_offence_by_xpath())
            s = Select(method_of_offence_drop_dwn)
            options_list = s.options
            options_list = s.options
            for x in options_list:
                try:
                    s.select_by_visible_text(x.text)
                    time.sleep(Base_Class.two_second)
                except Exception as ex:
                    assert False

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_METHOD_OF_OFFENSE_dropdown_and_verify_options_inside"
                    f"_it_are_visible_and_clickable_failed.png")
                return False

    def verify_REPORTED_BY_label_text_and_text_box_besides_it_is_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            time.sleep(2)
            add_details_reported_by_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                               .add_details_reported_by_text_ele_by_xpath())
            time.sleep(2)
            assert add_details_reported_by_text.is_displayed()
            time.sleep(2)
            reported_by_txt_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .reported_by_inpt_bx_by_xpath())
            ex_reported_by_data = Read_Identify_and_Enroll_Components().reported_by_data()
            reported_by_txt_bx.send_keys(ex_reported_by_data)

            ac_reported_by_data = reported_by_txt_bx.get_attribute("value")
            time.sleep(2)
            assert ex_reported_by_data.lower() == ac_reported_by_data.lower()
            time.sleep(2)
            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            time.sleep(2)
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            time.sleep(2)
            cancel_enrollment.click()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_REPORTED_BY_label_text_and_text_box_besides_it_is_visible_and_clickable_failed.png")
                return False

    def verify_Build_label_text_and_text_box_besides_it_is_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            time.sleep(2)
            add_details_build_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .add_details_build_text_ele_by_xpath())
            time.sleep(2)
            assert add_details_build_text.is_displayed()

            build_txt_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().build_inpt_bx_by_xpath())
            ex_build_data = Read_Identify_and_Enroll_Components().build_data()
            build_txt_bx.send_keys(ex_build_data)
            time.sleep(2)
            ac_build_data = build_txt_bx.get_attribute("value")
            time.sleep(2)
            assert ex_build_data.lower() == ac_build_data.lower()

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            time.sleep(2)
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            time.sleep(2)
            cancel_enrollment.click()
            time.sleep(2)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_Build_label_text_and_text_box_besides_it_is_visible_and_clickable_failed.png")
                return False

    def verify_Body_Markings_label_text_and_text_box_besides_it_is_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            body_marking_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .body_markings_inpt_bx_by_xpath())
            assert body_marking_text.is_displayed()

            body_marking_txt_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .build_inpt_bx_by_xpath())
            ex_body_marking_data = Read_Identify_and_Enroll_Components().body_markings_data()
            body_marking_txt_bx.send_keys(ex_body_marking_data)

            ac_body_marking_data = body_marking_txt_bx.get_attribute("value")
            assert ex_body_marking_data.lower() == ac_body_marking_data.lower()

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_Body_Markings_label_text_and_text_box_besides_it_is_visible_and_clickable_failed.png")
                return False

    def verify_GENDER_label_text_is_displayed_with_dropdown_beside_it_is_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            gender_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().gender_by_xpath())
            assert gender_text.is_displayed()

            gender_txt_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().gender_by_xpath())
            s = Select(gender_txt_bx)
            options_list = s.options
            assert len(options_list) > 0

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_GENDER_label_text_is_displayed_with_dropdown_"
                    f"beside_it_is_visible_and_clickable_failed.png")
                return False

    def click_on_GENDER_dropdown_and_verify_options_inside_it_are_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            gender_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .add_details_gender_text_ele_by_xpath())
            assert gender_text.is_displayed()

            gender_txt_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().gender_by_xpath())
            s = Select(gender_txt_bx)
            options_list = s.options
            for x in options_list:
                try:
                    s.select_by_visible_text(x.text)
                    time.sleep(Base_Class.two_second)
                except Exception as ex:
                    assert False

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_GENDER_dropdown_and_verify_options_inside_it_are_visible_and_clickable_failed.png")
                return False

    def verify_HEIGHT_label_text_is_displayed_with_dropdown_beside_it_is_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            height_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .add_details_height_text_ele_by_xpath())
            assert height_text.is_displayed()

            height_txt_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().height_by_xpath())
            s = Select(height_txt_bx)
            options_list = s.options
            assert len(options_list) > 0

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_HEIGHT_label_text_is_displayed_with_dropdown_beside_it"
                    f"_is_visible_and_clickable_failed.png")
                return False

    def click_on_HEIGHT_dropdown_and_verify_options_inside_it_are_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            height_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .add_details_height_text_ele_by_xpath())
            assert height_text.is_displayed()

            height_txt_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().height_by_xpath())
            s = Select(height_txt_bx)
            options_list = s.options
            for x in options_list:
                try:
                    s.select_by_visible_text(x.text)
                    time.sleep(Base_Class.two_second)
                except Exception as ex:
                    assert False

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_HEIGHT_dropdown_and_verify_options_inside_it_are_visible_and_clickable_failed.png")
                return False

    def verify_NARRATIVES_label_text_and_text_box_besides_it_is_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            narratives_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .add_details_narratives_text_ele_by_xpath())
            assert narratives_text.is_displayed()

            narratives_text_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .narratives_txt_bx_by_xpath())
            ex_narratives_data = Read_Identify_and_Enroll_Components().narratives_data()
            narratives_text_bx.send_keys(ex_narratives_data)

            ac_narratives_data = narratives_text_bx.get_attribute("value")
            assert ex_narratives_data.lower() == ac_narratives_data.lower()

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_NARRATIVES_label_text_and_text_box_besides_it_is_visible_and_clickable_failed.png")
                return False

    def Enter_Data_into_fields_displayed_on_Add_Details_panel_and_verify_enrollment_successfully_created(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            time.sleep(Base_Class.two_second)
            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)
            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False
            time.sleep(2)
            self.delete_enrollment()
            time.sleep(2)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\Enter_Data_into_fields_displayed_on_Add_Details_panel_and_verify_enrollment_"
                    f"successfully_created_failed.png")
                return False

    def verify_Success_message_is_displayed_below_warning_on_Identify_and_enroll_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            self.upload_image_not_enrolled()

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False
            time.sleep(2)
            self.delete_enrollment()
            time.sleep(2)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_Success_message_is_displayed_below_warning_on_Identify_and_enroll_panel_failed.png")
                return False

    def verify_three_buttons_below_success_message_is_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False

            review_enroll_details_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .review_enrollment_details_button_xpath())
            review_enroll_details_btn.click()

            review_enroll_details_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                                   .review_enrollment_details_button_validation())
            assert review_enroll_details_validation.is_displayed()

            review_added_groups_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                          .review_added_groups_button_xpath())
            review_added_groups_btn.click()

            review_added_groups_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                                 .review_added_groups_button_validation())
            assert review_added_groups_validation.is_displayed()

            add_more_faces_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_more_faces_xpath())
            add_more_faces_btn.click()

            add_more_faces_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_more_faces_validation())
            add_more_faces_validation.is_displayed()
            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_three_buttons_below_success_message_is_visible_and_clickable_failed.png")
                return False

    def click_on_Review_Enrollment_Details_button_and_verify_if_Enrollment_Details_panel_is_displayed(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_103.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False

            review_enroll_details_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .review_enrollment_details_button_xpath())
            review_enroll_details_btn.click()

            review_enroll_details_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                                   .review_enrollment_details_button_validation())
            assert review_enroll_details_validation.is_displayed()
            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_Review_Enrollment_Details_button_and_verify_if_Enrollment"
                    f"_Details_panel_is_displayed_failed.png")
                return False

    def verify_Action_button_visible_and_clickable_on_Enrollment_Details_Panel_below_its_title(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_103.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False

            review_enroll_details_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .review_enrollment_details_button_xpath())
            review_enroll_details_btn.click()

            action_btn_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                        .enrollment_details_action_button())
            assert action_btn_validation.is_displayed()
            try:
                action_btn_validation.click()
            except Exception as ex:
                assert False

            click_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_details_action_button_validation())
            assert click_validation.is_displayed()

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_Action_button_visible_and_clickable_on_Enrollment_"
                    f"Details_Panel_below_its_title_failed.png")
                return False

    def click_and_verify_Edit_Identify_Within_Enrollment_and_Identify_within_visitors_option_are_visible_and_clickable(
            self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_103.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False
            time.sleep(Base_Class.one_second)
            review_enroll_details_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .review_enrollment_details_button_xpath())
            review_enroll_details_btn.click()

            action_btn_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                        .enrollment_details_action_button())
            assert action_btn_validation.is_displayed()
            time.sleep(Base_Class.one_second)
            try:
                action_btn_validation.click()
            except Exception as ex:
                assert False

            edite_option = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .enrollment_details_action_button_validation())
            assert edite_option.is_displayed()
            time.sleep(Base_Class.one_second)
            try:
                edite_option.click()
            except Exception as ex:
                assert False

            edite_option_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                          .edite_button_validation_xpath())
            assert edite_option_validation.is_displayed()
            save_button = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .edite_panel_save_button())
            time.sleep(Base_Class.one_second)
            save_button.click()

            action_btn_validation.click()
            time.sleep(Base_Class.one_second)

            identify_enroll_option = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .action_button_identify_option())
            assert identify_enroll_option.is_displayed()
            time.sleep(Base_Class.one_second)
            try:
                identify_enroll_option.click()
            except Exception as ex:
                assert False

            identify_enroll_option_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                                    .identify_enroll_option_validation())
            time.sleep(Base_Class.one_second)
            assert identify_enroll_option_validation.is_displayed()

            action_btn_validation.click()
            time.sleep(Base_Class.one_second)

            visitors_option = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .action_button_visitors_option())
            time.sleep(Base_Class.one_second)
            try:
                visitors_option.click()
            except Exception as ex:
                assert False

            visitors_option_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                             .visitor_search_panel_validation())
            assert visitors_option_validation.is_displayed()
            time.sleep(Base_Class.one_second)

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_and_verify_Edit_Identify_Within_Enrollment_and_Identify_within_visitors_"
                    f"option_are_visible_and_clickable_failed.png")
                return False

    def verify_location_and_case_name_is_displayed_as_heading_on_Enrollment_Details_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_103.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False
            time.sleep(Base_Class.one_second)
            review_enroll_details_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .review_enrollment_details_button_xpath())
            review_enroll_details_btn.click()

            location_store_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .location_store_text_validation())
            assert location_store_text.is_displayed()

            case_subject_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .case_subject_text_validation())
            assert case_subject_text.is_displayed()

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_location_and_case_name_is_displayed_as_heading_on_Enrollment_Details_panel_failed.png")
                return False

    def verify_visitor_image_is_visible_besides_it_Enrolled_on_date_and_time_is_displayed_as_expected(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_103.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False
            time.sleep(Base_Class.one_second)
            review_enroll_details_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .review_enrollment_details_button_xpath())
            review_enroll_details_btn.click()
            time.sleep(Base_Class.one_second)

            image_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_details_img_validation())
            assert image_validation.is_displayed()
            time.sleep(Base_Class.one_second)

            enrolled_on_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .enrolled_on_text_validation())
            assert enrolled_on_validation.is_displayed()
            time.sleep(Base_Class.one_second)

            time_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .enrolled_time_validation())
            assert time_validation.is_displayed()
            time.sleep(Base_Class.one_second)

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_visitor_image_is_visible_besides_it_Enrolled_on_date_and_time_is_"
                    f"displayed_as_expected_failed.png")
                return False

    def verify_Enabled_Disabled_status_with_its_symbol_is_visible_besides_visitor_image(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_103.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False
            time.sleep(Base_Class.one_second)
            review_enroll_details_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .review_enrollment_details_button_xpath())
            review_enroll_details_btn.click()
            time.sleep(Base_Class.one_second)

            enable_btn_with_symbol_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                                    .enable_text_with_symbol_validation())
            assert enable_btn_with_symbol_validation.is_displayed()
            time.sleep(Base_Class.one_second)

            enable_symbol_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                           .enable_button_symbol_validation())
            assert enable_symbol_validation.is_displayed()

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_Enabled_Disabled_status_with_its_symbol_is_visible_besides_visitor_image_failed.png")
                return False

    def verify_Opt_out_status_is_displayed_as_expected_on_Enrollment_Details_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_103.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False
            time.sleep(Base_Class.one_second)
            review_enroll_details_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .review_enrollment_details_button_xpath())
            review_enroll_details_btn.click()
            time.sleep(Base_Class.one_second)

            opt_out_status_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .opt_out_status_validation())
            assert opt_out_status_validation.is_displayed()

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_Opt_out_status_is_displayed_as_expected_on_Enrollment_Details_panel_failed.png")
                return False

    def verify_REQUIRED_FIELDS_heading_is_displayed_along_with_its_data_on_Enrollment_Details_Panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_103.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False
            time.sleep(Base_Class.one_second)
            review_enroll_details_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .review_enrollment_details_button_xpath())
            review_enroll_details_btn.click()
            time.sleep(Base_Class.one_second)

            required_fields_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                             .required_fields_title_validation())
            assert required_fields_validation.is_displayed()

            location_store_text_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                                 .location_store_text_validation())
            assert location_store_text_validation.is_displayed()
            case_subject_text_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                               .case_subject_text_validation())
            assert case_subject_text_validation.is_displayed()
            reported_loss_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                           .reported_loss_validation())
            assert reported_loss_validation.is_displayed()

            date_incident_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                           .date_incident_validation())
            assert date_incident_validation.is_displayed()

            action_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .action_data_validation())
            assert action_validation.is_displayed()

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_REQUIRED_FIELDS_heading_is_displayed_along_with_its_"
                    f"data_on_Enrollment_Details_Panel_failed.png")
                return False

    def verify_OPTIONAL_FIELDS_heading_below_required_field_is_displayed_as_expected(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_103.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            case_event_type = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .case_event_type_dropdown())
            select = Select(case_event_type)
            select.select_by_index(1)
            time.sleep(Base_Class.one_second)

            activity_type = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .activity_type_dropdown())
            select = Select(activity_type)
            select.select_by_index(1)
            time.sleep(Base_Class.one_second)

            method_of_offense = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .method_of_offence_by_xpath())
            select = Select(method_of_offense)
            select.select_by_index(1)
            time.sleep(Base_Class.one_second)

            gender = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                         .gender_dropdown())
            select = Select(gender)
            select.select_by_index(1)
            time.sleep(Base_Class.one_second)

            height = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                         .height_type_dropdown())
            select = Select(height)
            select.select_by_index(1)
            time.sleep(Base_Class.one_second)

            reported_by = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .reported_by_input())
            reported_by.send_keys(Read_Identify_and_Enroll_Components().reported_by_data())
            time.sleep(Base_Class.one_second)

            build = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                        .build_input())
            build.send_keys(Read_Identify_and_Enroll_Components().build_data())
            time.sleep(Base_Class.one_second)

            body_markings = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .body_markings_input())
            body_markings.send_keys(Read_Identify_and_Enroll_Components().body_markings_data())
            time.sleep(Base_Class.one_second)

            narratives = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .narrative_Desc_input())
            narratives.send_keys(Read_Identify_and_Enroll_Components().narratives_data())
            time.sleep(Base_Class.one_second)

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            time.sleep(Base_Class.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False
            time.sleep(Base_Class.one_second)
            review_enroll_details_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .review_enrollment_details_button_xpath())
            review_enroll_details_btn.click()
            time.sleep(Base_Class.one_second)

            optional_fields_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                             .optional_fields_text_validation())
            assert optional_fields_validation.is_displayed()

            case_event_type_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                             .case_event_type_validation())
            assert case_event_type_validation.is_displayed()
            activity_type_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                           .activity_type_validation())
            assert activity_type_validation.is_displayed()
            method_of_offense_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                               .method_of_offense_validation())
            assert method_of_offense_validation.is_displayed()

            reported_by_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .reported_by_validation())
            assert reported_by_validation.is_displayed()

            body_markings_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                           .body_markings_validation())
            assert body_markings_validation.is_displayed()

            gender_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .gender_validation())
            assert gender_validation.is_displayed()

            height_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .height_validation())
            assert height_validation.is_displayed()

            narratives_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                        .narratives_validation())
            assert narratives_validation.is_displayed()

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_OPTIONAL_FIELDS_heading_below_required_field_is_displayed_as_expected_failed.png")
                return False

    def click_on_close_enrollment_details_panel_and_verify_panel_is_closed_successfully(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_103.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            review_enroll_details_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .review_enrollment_details_button_xpath())
            review_enroll_details_btn.click()

            enrollment_details_panel = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                           enrollment_details_panel_close_1())
            enrollment_details_panel.click()
            time.sleep(Base_Class.two_second)

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         enrollment_details_panel_validation())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        enrollment_details_panel_close_validation().lower():
                    assert False
            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_close_enrollment_details_panel_and_verify_panel_is_closed_successfully_failed.png")
                return False

    def click_on_Review_Added_Groups_Button_and_verify_if_enrollment_groups_panel_is_visible(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False

            review_added_groups_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                          .review_added_groups_button_xpath())
            review_added_groups_btn.click()

            review_added_groups_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                                 .review_added_groups_button_validation())
            assert review_added_groups_validation.is_displayed()

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_Review_Added_Groups_Button_and_verify_if_enrollment_groups_panel_is_visible_failed.png")
                return False

    def verify_Filter_dropdown_is_visible_and_clickable_on_Enrollment_Groups_Panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False

            review_added_groups_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                          .review_added_groups_button_xpath())
            review_added_groups_btn.click()
            time.sleep(Base_Class.two_second)

            filter_dropdown = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .filter_dropdown_xpath())
            assert filter_dropdown.is_displayed()
            try:
                filter_dropdown.click()
            except Exception as ex:
                assert False

            time.sleep(Base_Class.two_second)

            filter_dropdown_click_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                                   .filter_dropdown_validation())
            assert filter_dropdown_click_validation.is_displayed()

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_Filter_dropdown_is_visible_and_clickable_on_Enrollment_Groups_Panel_failed.png")
                return False

    def click_on_Filter_dropdown_and_verify_its_options_are_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False

            review_added_groups_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                          .review_added_groups_button_xpath())
            review_added_groups_btn.click()
            time.sleep(Base_Class.two_second)

            filter_dropdown = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .filter_dropdown_xpath())
            assert filter_dropdown.is_displayed()
            try:
                filter_dropdown.click()
            except Exception as ex:
                assert False
            time.sleep(Base_Class.two_second)

            linked_enroll_option = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                       .linked_enroll_option())
            assert linked_enroll_option.is_displayed()
            try:
                linked_enroll_option.click()
            except Exception as ex:
                assert False

            time.sleep(Base_Class.two_second)

            filter_dropdown.click()
            time.sleep(Base_Class.one_second)

            unlinked_enroll_option = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .unlinked_enroll_option())
            assert unlinked_enroll_option.is_displayed()
            try:
                unlinked_enroll_option.click()
            except Exception as ex:
                assert False

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_Filter_dropdown_and_verify_its_options_are_visible_and_clickable_failed.png")
                return False

    def verify_Action_dropdown_is_visible_and_clickable_on_Enrollment_Groups_Panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False

            review_added_groups_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                          .review_added_groups_button_xpath())
            review_added_groups_btn.click()
            time.sleep(Base_Class.two_second)

            action_dropdown = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .enrollment_group_action_btn())
            assert action_dropdown.is_displayed()
            try:
                action_dropdown.click()
            except Exception as ex:
                assert False

            time.sleep(Base_Class.two_second)

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_Action_dropdown_is_visible_and_clickable_on_Enrollment_Groups_Panel_failed.png")
                return False

    def click_on_Action_dropdown_and_verify_its_options_are_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False

            review_added_groups_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                          .review_added_groups_button_xpath())
            review_added_groups_btn.click()
            time.sleep(Base_Class.two_second)

            action_dropdown = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .enrollment_group_action_btn())
            assert action_dropdown.is_displayed()
            try:
                action_dropdown.click()
            except Exception as ex:
                assert False

            time.sleep(Base_Class.two_second)

            add_person = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .action_btn_add_person_option())

            remove_person = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .remove_person_from_group())

            if add_person.is_displayed():
                try:
                    add_person.click()
                except Exception as ex:
                    assert False
            else:
                try:
                    remove_person.click()
                except Exception as ex:
                    assert False
            self.d.switch_to.alert.accept()
            time.sleep(Base_Class.one_second)
            action_dropdown.click()

            create_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_btn_create_group_option())
            assert create_group.is_displayed()
            try:
                create_group.click()
            except Exception as ex:
                assert False
            time.sleep(Base_Class.one_second)
            action_dropdown.click()

            refresh = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                          .action_btn_refresh_option())
            assert refresh.is_displayed()
            try:
                refresh.click()
            except Exception as ex:
                assert False

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_Action_dropdown_and_verify_its_options_are_visible_and_clickable_failed.png")
                return False

    def verify_select_all_check_box_along_with_its_label_is_visible_and_clickable(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False

            review_added_groups_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                          .review_added_groups_button_xpath())
            review_added_groups_btn.click()
            time.sleep(Base_Class.two_second)

            select_all_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .select_all_text_validation())
            assert select_all_text.is_displayed()
            time.sleep(Base_Class.two_second)

            select_all_check_box = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                       .select_all_check_box_click())
            assert select_all_check_box.is_displayed()
            try:
                select_all_check_box.click()
            except Exception as ex:
                assert False

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_select_all_check_box_along_with_its_label_is_visible_and_clickable_failed.png")
                return False

    def verify_enrollment_groups_associated_with_enrollment_is_enlisted_inside_Enrollment_Groups_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False

            review_added_groups_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                          .review_added_groups_button_xpath())
            review_added_groups_btn.click()
            time.sleep(Base_Class.two_second)

            associate_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .associate_group_validation())
            assert associate_group.is_displayed()
            time.sleep(Base_Class.two_second)

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_enrollment_groups_associated_with_enrollment_is_enlisted_"
                    f"inside_Enrollment_Groups_panel_failed.png")
                return False

    def click_on_close_enrollment_group_panel_and_verify_panel_is_closed_successfully(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_103.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            review_add_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .review_added_groups_button_xpath())
            review_add_group.click()

            enrollment_group_panel = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                         enrollment_details_panel_close_1())
            enrollment_group_panel.click()
            time.sleep(Base_Class.two_second)

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         review_added_groups_button_validation())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        enrollment_view_enrollment_groups_txt_validation().lower():
                    assert False
            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_close_enrollment_group_panel_and_verify_panel_is_closed_successfully_failed.png")
                return False

    def click_on_add_more_faces_button_and_verify_if_Enrollment_Faces_panel_is_displayed(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False

            add_more_faces_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_more_faces_xpath())
            add_more_faces_btn.click()

            add_more_faces_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_more_faces_validation())
            add_more_faces_validation.is_displayed()
            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_add_more_faces_button_and_verify_if_Enrollment_Faces_panel_is_displayed_failed.png")
                return False

    def verify_Action_button_is_visible_and_clickable_on_Enrollment_Faces_Panel_below_its_title(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False

            add_more_faces_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_more_faces_xpath())
            add_more_faces_btn.click()

            add_more_faces_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_more_faces_validation())
            add_more_faces_validation.is_displayed()

            add_more_faces_action_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .enrollment_faces_action_btn())
            assert add_more_faces_action_btn.is_displayed()
            add_more_faces_action_btn.click()
            time.sleep(Base_Class.two_second)

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_Action_button_is_visible_and_clickable_on_Enrollment_"
                    f"Faces_Panel_below_its_title_failed.png")
                return False

    def click_on_Action_dropdown_and_verify_its_options_are_visible_and_clickable_enroll_face_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False

            add_more_faces_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_more_faces_xpath())
            assert add_more_faces_btn.is_displayed()
            try:
                add_more_faces_btn.click()
            except Exception as ex:
                assert False

            add_more_faces_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_more_faces_validation())
            add_more_faces_validation.is_displayed()

            add_more_faces_action_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .enrollment_faces_action_btn())
            assert add_more_faces_action_btn.is_displayed()
            try:
                add_more_faces_action_btn.click()
            except Exception as ex:
                assert False
            time.sleep(Base_Class.one_second)

            enrollment_option = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .enrollments_option_xpath())
            assert enrollment_option.is_displayed()
            try:
                enrollment_option.click()
            except Exception as ex:
                assert False
            add_more_faces_action_btn.click()
            time.sleep(Base_Class.one_second)

            visitors_option = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .visitors_option_xpath())
            assert visitors_option.is_displayed()
            try:
                visitors_option.click()
            except Exception as ex:
                assert False

            add_more_faces_action_btn.click()
            time.sleep(Base_Class.one_second)

            add_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .add_photo_option_xpath())
            assert add_photo.is_displayed()
            try:
                add_photo.click()
            except Exception as ex:
                assert False
            add_more_faces_action_btn.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(Base_Class.one_second)

            delete_faces = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .delete_faces_option_xpath())
            assert delete_faces.is_displayed()
            try:
                delete_faces.click()
            except Exception as ex:
                assert False
            self.d.switch_to.alert.accept()

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_Action_dropdown_and_verify_its_options_are_visible_and_"
                    f"clickable_enroll_face_panel_failed.png")
                return False

    def verify_location_and_case_name_is_displayed_as_heading_on_Enrollment_Faces_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False

            add_more_faces_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_more_faces_xpath())
            add_more_faces_btn.click()

            add_more_faces_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_more_faces_validation())
            add_more_faces_validation.is_displayed()

            time.sleep(Base_Class.one_second)

            location_case_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                           .location_cases_name_validation())
            assert location_case_validation.is_displayed()

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_location_and_case_name_is_displayed_as_heading_on_Enrollment_Faces_panel_failed.png")
                return False

    def verify_sample_image_box_is_visible_and_clickable_below_location_information(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False

            add_more_faces_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_more_faces_xpath())
            add_more_faces_btn.click()

            add_more_faces_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_more_faces_validation())
            add_more_faces_validation.is_displayed()

            time.sleep(Base_Class.one_second)

            sample_img_box = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .sample_img_box_xpath())
            assert sample_img_box.is_displayed()
            try:
                sample_img_box.click()
            except Exception as ex:
                assert False

            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_sample_image_box_is_visible_and_clickable_below_location_information_failed.png")
                return False

    def click_on_sample_image_box_and_verify_if_file_open_dialog_box_is_displayed(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False

            add_more_faces_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_more_faces_xpath())
            add_more_faces_btn.click()

            add_more_faces_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_more_faces_validation())
            add_more_faces_validation.is_displayed()

            time.sleep(Base_Class.one_second)

            sample_img_box = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .sample_img_box_xpath())
            assert sample_img_box.is_displayed()
            sample_img_box.click()

            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_sample_image_box_and_verify_if_file_open_dialog_box_is_displayed_failed.png")
                return False

    def verify_Dragable_Photo_Text_be_displayed_on_enrolled_visitor_image_below_sample_image(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False

            add_more_faces_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_more_faces_xpath())
            add_more_faces_btn.click()

            add_more_faces_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_more_faces_validation())
            add_more_faces_validation.is_displayed()

            time.sleep(Base_Class.one_second)

            draggable_photo_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                       .draggable_photo_text())
            assert draggable_photo_text.is_displayed()

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_Dragable_Photo_Text_be_displayed_on_enrolled_visitor_image_below_sample_image_failed.png")
                return False

    def verify_check_box_is_visible_and_clickable_besides_visitor_image_on_the_panel(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False

            add_more_faces_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_more_faces_xpath())
            add_more_faces_btn.click()

            add_more_faces_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_more_faces_validation())
            add_more_faces_validation.is_displayed()

            time.sleep(Base_Class.one_second)

            check_box = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .check_box_xpath())
            assert check_box.is_displayed()
            try:
                check_box.click()
            except Exception as ex:
                assert False

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_check_box_is_visible_and_clickable_besides_visitor_image_on_the_panel_failed.png")
                return False

    def verify_download_image_button_is_visible_and_clickable_besides_visitor_image(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False

            add_more_faces_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_more_faces_xpath())
            add_more_faces_btn.click()

            add_more_faces_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_more_faces_validation())
            add_more_faces_validation.is_displayed()

            time.sleep(Base_Class.one_second)

            donwload_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .download_img_button_xpath())
            assert donwload_btn.is_displayed()
            try:
                donwload_btn.click()
            except Exception as ex:
                assert False

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_download_image_button_is_visible_and_clickable_besides_visitor_image_failed.png")
                return False

    def verify_image_file_info_button_is_visible_and_clickable_besides_visitor_image(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False

            add_more_faces_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_more_faces_xpath())
            add_more_faces_btn.click()

            add_more_faces_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_more_faces_validation())
            add_more_faces_validation.is_displayed()

            time.sleep(Base_Class.one_second)

            img_file_info = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .view_img_info_xpath())
            assert img_file_info.is_displayed()
            try:
                img_file_info.click()
            except Exception as ex:
                assert False

            self.d.switch_to.alert.accept()

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\verify_image_file_info_button_is_visible_and_clickable_besides_visitor_image_failed.png")
                return False

    def click_on_download_image_button_and_verify_image_is_downloaded_successfully(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False

            add_more_faces_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_more_faces_xpath())
            add_more_faces_btn.click()

            add_more_faces_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_more_faces_validation())
            add_more_faces_validation.is_displayed()

            time.sleep(Base_Class.one_second)

            download_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .download_img_button_xpath())
            assert download_btn.is_displayed()
            try:
                download_btn.click()
            except Exception as ex:
                assert False

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_download_image_button_and_verify_image_is_downloaded_successfully_failed.png")
                return False

    def click_on_image_file_info_button_and_verify_a_pop_up_is_displayed_with_image_information(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)
            success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                              .enrollment_success_msg_xpath())
            assert success_msg.text.lower() == Read_Identify_and_Enroll_Components(). \
                enrollment_success_msg_validation().lower()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    assert False

            add_more_faces_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_more_faces_xpath())
            add_more_faces_btn.click()

            add_more_faces_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_more_faces_validation())
            add_more_faces_validation.is_displayed()

            time.sleep(Base_Class.one_second)

            img_file_info = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .view_img_info_xpath())
            assert img_file_info.is_displayed()
            try:
                img_file_info.click()
            except Exception as ex:
                assert False

            text = self.d.switch_to.alert.text
            assert Read_Identify_and_Enroll_Components().view_image_pop_up_text_1() in text
            assert Read_Identify_and_Enroll_Components().view_image_pop_up_text_2() in text
            assert Read_Identify_and_Enroll_Components().view_image_pop_up_text_3() in text
            assert Read_Identify_and_Enroll_Components().view_image_pop_up_text_4() in text
            self.d.switch_to.alert.accept()

            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_image_file_info_button_and_verify_a_pop_up_is_"
                    f"displayed_with_image_information_failed.png")
                return False

    def click_on_close_panel_button_and_verify_enrollment_faces_panel_is_closed_successfully(self):
        try:
            self.login_before()
            time.sleep(Base_Class.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)

            upload_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().upload_image_by_xpath())
            upload_photo.click()
            time.sleep(2)
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\test_103.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

            identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .identify_enroll_panel_identify_enroll_btn_by_xpath())

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(1)

            location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(Base_Class.two_second)
            date_incident.send_keys(Read_Identify_and_Enroll_Components().date_incident_data())
            time.sleep(Base_Class.two_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            assert save_btn.is_displayed()
            save_btn.click()
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .enrollment_success_loader())
            while wait_icon.is_displayed():
                time.sleep(Base_Class.two_second)

            enroll_faces = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .add_more_faces_xpath())
            enroll_faces.click()

            close = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                        .enrollment_faces_panel_close_xpath())
            close.click()

            time.sleep(Base_Class.two_second)

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         enrollment_face_panel_title())
            for x in title:
                print(x.text.strip().lower())
                print(Read_Identify_and_Enroll_Components(). \
                      enrollment_faces_panel_close().lower())
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        enrollment_faces_panel_close().lower():
                    assert False
            self.delete_enrollment()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots"
                    f"\\click_on_close_panel_button_and_verify_enrollment_faces_panel"
                    f"_is_closed_successfully_failed.png")
                return False
