import configparser
from pathlib import Path


class Read_Tags_Components:
    def __init__(self):

        self.config = configparser.RawConfigParser()

        try:
            portal_menu_ini_file_path = f'{Path(__file__).parent.parent.parent}\\Test_Data\\Data_From_INI\\Tags.ini'
            print("dm url path: ", portal_menu_ini_file_path)
            print("File location: ", portal_menu_ini_file_path)
            # Base_Class.logger.info("File location: ", deployment_manager_ini_file_path)
            self.config.read(portal_menu_ini_file_path)
        except Exception as ex:
            print("config file got an exception", ex)

    def action_btn_by_xpath(self):
        try:
            action_btn_by_xpath = self.config.get("LOCATORS", "action_btn_by_xpath")
            print("action button by xpath: ", action_btn_by_xpath)
            return action_btn_by_xpath
        except Exception as ex:
            print("action_btn_by_xpath : ", ex)

    def create_tags_btn_by_xpath(self):
        try:
            create_tags_btn_by_xpath = self.config.get("LOCATORS", "create_tag_btn_by_xpath")
            print("action button by xpath: ", create_tags_btn_by_xpath)
            return create_tags_btn_by_xpath
        except Exception as ex:
            print("create_tags_btn_by_xpath : ", ex)

    def get_tag_name_field_by_xpath(self):
        try:
            tag_name_field_by_xpath = self.config.get("LOCATORS", "tag_name_field_by_xpath")
            print("tag name field by xpath: ", tag_name_field_by_xpath)
            return tag_name_field_by_xpath
        except Exception as ex:
            print("tag_name_field_by_xpath : ", ex)

    def get_commit_changes_actual_msg_by_xpath(self):
        try:
            get_commit_changes_actual_msg_by_xpath = self.config.get("LOCATORS", "commit_changes_actual_msg_by_xpath")
            print("get commit changes actual msg by xpath: ", get_commit_changes_actual_msg_by_xpath)
            return get_commit_changes_actual_msg_by_xpath
        except Exception as ex:
            print("get_commit_changes_actual_msg_by_xpath : ", ex)

    def get_commit_changes_expected_msg_by_xpath(self):
        try:
            get_commit_changes_expected_msg_by_xpath = self.config.get("ASSERTIONS",
                                                                       "commit_changes_validation_expected_msg")
            print("get commit changes expected msg by xpath: ", get_commit_changes_expected_msg_by_xpath)
            return get_commit_changes_expected_msg_by_xpath
        except Exception as ex:
            print("get_commit_changes_actual_msg_by_xpath : ", ex)

    def get_serious_event_checkbox_by_xpath(self):
        try:
            get_serious_event_checkbox_by_xpath = self.config.get("LOCATORS", "serious_event_check_box_by_xpath")
            print("serious event checkbox by xpath: ", get_serious_event_checkbox_by_xpath)
            return get_serious_event_checkbox_by_xpath
        except Exception as ex:
            print("get_serious_event_checkbox_by_xpath : ", ex)

    def get_save_btn_by_xpath(self):
        try:
            get_save_btn_by_xpath = self.config.get("LOCATORS", "save_btn_by_xpath")
            print("get save btn by xpath: ", get_save_btn_by_xpath)
            return get_save_btn_by_xpath
        except Exception as ex:
            print("get_save_btn_by_xpath : ", ex)

    def tag_create_success_msg_by_xpath(self):
        try:
            tag_create_success_msg_by_xpath = self.config.get("ASSERTIONS", "success_msg_by_xpath")
            print("tag create success msg by xpath ", tag_create_success_msg_by_xpath)
            return tag_create_success_msg_by_xpath
        except Exception as ex:
            print("tag_create_success_msg_by_xpath : ", ex)

    def close_create_tag_panel_by_xpath(self):
        try:
            close_create_tag_panel_by_xpath = self.config.get("LOCATORS", "close_create_tag_panel_by_xpath")
            print("close create tag panel by xpath ", close_create_tag_panel_by_xpath)
            return close_create_tag_panel_by_xpath
        except Exception as ex:
            print("close_create_tag_panel_by_xpath : ", ex)

    def list_of_all_tags_name_by_xpath(self):
        try:
            list_of_all_tags_name_by_xpath = self.config.get("ASSERTIONS", "list_of_all_tag_name_by_xpath")
            print("list of all tags name by xpath ", list_of_all_tags_name_by_xpath)
            return list_of_all_tags_name_by_xpath
        except Exception as ex:
            print("list_of_all_tags_name_by_xpath : ", ex)

    def filter_btn_by_xpath(self):
        try:
            filter_btn_by_xpath = self.config.get("LOCATORS", "filter_btn_by_path")
            print("filter btn by xpath ", filter_btn_by_xpath)
            return filter_btn_by_xpath
        except Exception as ex:
            print("filter_btn_by_xpath : ", ex)

    def serious_event_filter_btn_by_xpath(self):
        try:
            filter_btn_by_xpath = self.config.get("LOCATORS", "serious_yes_filter_by_xpath")
            print("filter btn by xpath ", filter_btn_by_xpath)
            return filter_btn_by_xpath
        except Exception as ex:
            print("filter_btn_by_xpath : ", ex)

    def tag_name_already_exists_validation_by_xpath(self):
        try:
            tag_name_already_exists_validation_by_xpath = self.config.get("ASSERTIONS",
                                                                          "Tag_name already_exists_validation_xpath")
            print("tag name already exists validation by xpath ", tag_name_already_exists_validation_by_xpath)
            return tag_name_already_exists_validation_by_xpath
        except Exception as ex:
            print("tag_name_already_exists_validation_by_xpath : ", ex)

    def close_panel_and_discard_changes_btn_by_xpath(self):
        try:
            close_panel_and_discard_changes_btn_by_xpath = self.config.get("LOCATORS",
                                                                           "close_panel_and_discard_changes")
            print("close panel and discard changes btn by xpath ", close_panel_and_discard_changes_btn_by_xpath)
            return close_panel_and_discard_changes_btn_by_xpath
        except Exception as ex:
            print("close_panel_and_discard_changes_btn_by_xpath : ", ex)

    def list_of_edit_tag_name_btn_by_xpath(self):
        try:
            list_of_edit_tag_name_btn_by_xpath = self.config.get("LOCATORS", "list_of_edit_tag_name_btn_by_xpath")
            print("list_of_edit_tag_name_btn_by_xpath ", list_of_edit_tag_name_btn_by_xpath)
            return list_of_edit_tag_name_btn_by_xpath
        except Exception as ex:
            print("list_of_edit_tag_name_btn_by_xpath : ", ex)

    def edit_tag_action_btn_by_xpath(self):
        try:
            tags_edit_panel_action_btn_by_xpath = self.config.get("LOCATORS", "tags_edit_panel_action_btn_by_xpath")
            print("tags_edit_panel_action_btn_by_xpath ", tags_edit_panel_action_btn_by_xpath)
            return tags_edit_panel_action_btn_by_xpath
        except Exception as ex:
            print("tags_edit_panel_action_btn_by_xpath : ", ex)

    def edit_btn_by_xpath(self):
        try:
            edit_btn_by_xpath = self.config.get("LOCATORS", "edit_btn_by_xpath")
            print("edit_btn_by_xpath ", edit_btn_by_xpath)
            return edit_btn_by_xpath
        except Exception as ex:
            print("edit_btn_by_xpath : ", ex)

    def tag_select_checkbox_list_by_xpath(self):
        try:
            tag_select_checkbox_btn_by_xpath = self.config.get("LOCATORS", "tags_select_checkbox_list")
            print("tag_select_checkbox_btn_by_xpath ", tag_select_checkbox_btn_by_xpath)
            return tag_select_checkbox_btn_by_xpath
        except Exception as ex:
            print("tag_select_checkbox_btn_by_xpath : ", ex)

    def delete_btn_by_xpath(self):
        try:
            delete_btn_by_xpath = self.config.get("LOCATORS", "delete_tag_btn_by_xpath")
            print("delete_btn_by_xpath ", delete_btn_by_xpath)
            return delete_btn_by_xpath
        except Exception as ex:
            print("delete_btn_by_xpath : ", ex)

    def close_tags_panel_by_xpath(self):
        try:
            close_tags_panel_by_xpath = self.config.get("LOCATORS", "portal_menu_panel_close")
            print("close_tags_panel_by_xpath ", close_tags_panel_by_xpath)
            return close_tags_panel_by_xpath
        except Exception as ex:
            print("delete_btn_by_xpath : ", ex)

    def yes_delete_selected(self):
        try:
            yes_delete_selected = self.config.get("LOCATORS", "yes_delete_selected")
            print("yes_delete_selected ", yes_delete_selected)
            return yes_delete_selected
        except Exception as ex:
            print("yes_delete_selected : ", ex)

    def tags_action_btn_by_xpath(self):
        try:
            tags_action_btn_by_xpath = self.config.get("LOCATORS", "tags_delete_action_btn_by_xpath")
            print("tags_action_btn_by_xpath ", tags_action_btn_by_xpath)
            return tags_action_btn_by_xpath
        except Exception as ex:
            print("tags_action_btn_by_xpath : ", ex)

    def filter_non_serious_btn_by_xpath(self):
        try:
            filter_non_serious_btn_by_xpath = self.config.get("LOCATORS", "serious_no_filter_by_xpath")
            print("filter_non_serious_btn_by_xpath", filter_non_serious_btn_by_xpath)
            return filter_non_serious_btn_by_xpath
        except Exception as ex:
            print("filter_non_serious_btn_by_xpath : ", ex)

    def tags_search_field_by_xpath(self):
        try:
            tags_search_field_by_xpath = self.config.get("LOCATORS", "tags_search_box")
            print("tags search field by xpath", tags_search_field_by_xpath)
            return tags_search_field_by_xpath
        except Exception as ex:
            print("tags_search_field_by_xpath : ", ex)

    def tags_present_validation_by_xpath(self):
        try:
            tags_present_validation_by_xpath = self.config.get("LOCATORS", "tags_present_validation")
            print("tags present validation by xpath", tags_present_validation_by_xpath)
            return tags_present_validation_by_xpath
        except Exception as ex:
            print("tags_present_validation_by_xpath : ", ex)

    def login_validation_by_xpath(self):
        try:
            login_validation_by_xpath = self.config.get("LOCATORS", "login_validation")
            print("login validation by xpath", login_validation_by_xpath)
            return login_validation_by_xpath
        except Exception as ex:
            print("login_validation_by_xpath : ", ex)

    def create_tag_success_msg_expected(self):
        try:
            create_tag_success_msg_expected = self.config.get("ASSERTIONS", "create_tag_success_msg")
            print("create_tag_success_msg_expected", create_tag_success_msg_expected)
            return create_tag_success_msg_expected
        except Exception as ex:
            print("create_tag_success_msg_expected : ", ex)

    def tag_search_result_expected(self):
        try:
            tag_search_result_expected = self.config.get("ASSERTIONS", "tags_search_expected")
            print("tag_search_result_expected", tag_search_result_expected)
            return tag_search_result_expected
        except Exception as ex:
            print("tag_search_result_expected : ", ex)

    def tag_search_input(self):
        try:
            tag_search_input = self.config.get("ASSERTIONS", "tags_search_input")
            print("tag_search_input", tag_search_input)
            return tag_search_input
        except Exception as ex:
            print("tag_search_input : ", ex)

    def expected_duplicate_tag_validation_msg(self):
        try:
            expected_duplicate_tag_validation_msg = self.config.get("ASSERTIONS",
                                                                    "expected_duplicate_tag_validation_msg")
            print("expected_duplicate_tag_validation_msg", expected_duplicate_tag_validation_msg)
            return expected_duplicate_tag_validation_msg
        except Exception as ex:
            print("expected_duplicate_tag_validation_msg : ", ex)

    def expected_deterred_tag(self):
        try:
            expected_deterred_tag = self.config.get("ASSERTIONS", "expected_deterred_tag")
            print("expected_deterred_tag", expected_deterred_tag)
            return expected_deterred_tag
        except Exception as ex:
            print("expected_deterred_tag : ", ex)

    def close_panel_and_discard_changes_input(self):
        try:
            close_panel_and_discard_changes_input = self.config.get("ASSERTIONS",
                                                                    "close_panel_and_discard_changes_input")
            print("close_panel_and_discard_changes_input", close_panel_and_discard_changes_input)
            return close_panel_and_discard_changes_input
        except Exception as ex:
            print("close_panel_and_discard_changes_input : ", ex)

    def update_tag_name_validation(self):
        try:
            update_tag_name_validation = self.config.get("ASSERTIONS", "update_tag_name_validation")
            print("update_tag_name_validation", update_tag_name_validation)
            return update_tag_name_validation
        except Exception as ex:
            print("update_tag_name_validation : ", ex)

    def close_and_discard_panel_btn(self):
        try:
            close_and_discard_panel_btn = self.config.get("LOCATORS", "close_and_discard_panel_btn")
            print("close_and_discard_panel_btn", close_and_discard_panel_btn)
            return close_and_discard_panel_btn
        except Exception as ex:
            print("close_and_discard_panel_btn : ", ex)

    def expected_discard_changes_warning_by_xpath(self):
        try:
            expected_discard_changes_warning_by_xpath = self.config.get("LOCATORS",
                                                                        "expected_discard_changes_warning_by_xpath")
            print("expected_discard_changes_warning_by_xpath", expected_discard_changes_warning_by_xpath)
            return expected_discard_changes_warning_by_xpath
        except Exception as ex:
            print("expected_discard_changes_warning_by_xpath : ", ex)

    def expected_uncommitted_changes_msg_by_xpath(self):
        try:
            expected_uncommitted_changes_msg_by_xpath = self.config.get("LOCATORS",
                                                                        "expected_uncommitted_changes_msg_by_xpath")
            print("expected_uncommitted_changes_msg_by_xpath", expected_uncommitted_changes_msg_by_xpath)
            return expected_uncommitted_changes_msg_by_xpath
        except Exception as ex:
            print("expected_uncommitted_changes_msg_by_xpath : ", ex)

    def close_panel_btn_text_validation(self):
        try:
            close_panel_btn_text_validation = self.config.get("LOCATORS", "close_panel_btn_text_validation")
            print("close_panel_btn_text_validation", close_panel_btn_text_validation)
            return close_panel_btn_text_validation
        except Exception as ex:
            print("close_panel_btn_text_validation : ", ex)

    def expected_discard_changes_warning(self):
        try:
            expected_discard_changes_warning = self.config.get("ASSERTIONS", "expected_discard_changes_warning")
            print("expected_discard_changes_warning", expected_discard_changes_warning)
            return expected_discard_changes_warning
        except Exception as ex:
            print("expected_discard_changes_warning : ", ex)

    def expected_uncommitted_changes_msg(self):
        try:
            expected_uncommitted_changes_msg = self.config.get("ASSERTIONS", "expected_uncommitted_changes_msg")
            print("expected_uncommitted_changes_msg", expected_uncommitted_changes_msg)
            return expected_uncommitted_changes_msg
        except Exception as ex:
            print("expected_uncommitted_changes_msg : ", ex)

    def expected_close_panel_btn_text(self):
        try:
            expected_close_panel_btn_text = self.config.get("ASSERTIONS", "expected_close_panel_btn_text")
            print("expected_close_panel_btn_text", expected_close_panel_btn_text)
            return expected_close_panel_btn_text
        except Exception as ex:
            print("expected_close_panel_btn_text : ", ex)

    def close_panel_one_by_one_list(self):
        try:
            close_panel_one_by_one_list = self.config.get("LOCATORS", "close_panel_one_by_one_list")
            print("close_panel_one_by_one_list", close_panel_one_by_one_list)
            return close_panel_one_by_one_list
        except Exception as ex:
            print("close_panel_one_by_one_list : ", ex)

    def tags_edit_button_by_xpath(self):
        try:
            tags_edit_button_by_xpath = self.config.get("LOCATORS", "tags_edit_button_by_xpath")
            print("tags_edit_button_by_xpath", tags_edit_button_by_xpath)
            return tags_edit_button_by_xpath
        except Exception as ex:
            print("tags_edit_button_by_xpath : ", ex)

    def filter_dropdown_by_xpath(self):
        try:
            filter_dropdown_by_xpath = self.config.get("LOCATORS", "filter_dropdown_by_xpath")
            print("filter_dropdown_by_xpath", filter_dropdown_by_xpath)
            return filter_dropdown_by_xpath
        except Exception as ex:
            print("filter_dropdown_by_xpath : ", ex)

    def non_serious_element_by_xpath(self):
        try:
            non_serious_element_by_xpath = self.config.get("LOCATORS", "non_serious_element_by_xpath")
            print("non_serious_element_by_xpath", non_serious_element_by_xpath)
            return non_serious_element_by_xpath
        except Exception as ex:
            print("non_serious_element_by_xpath : ", ex)
