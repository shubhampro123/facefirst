import configparser
from pathlib import Path


class read_event_filter_ini:
    def __init__(self):
        self.config = configparser.RawConfigParser()

        try:
            file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\Data_From_INI\\Event_filter.ini"

            # print("config_file path: ", file_path)
            self.config.read(file_path)
            # print(config.get("LOGIN_PAGE_AFTER_REGISTRATION", "url"))
        except Exception as ex:
            print(ex)

    def menu_event_button_by_xpath(self):
        menu_event_button_by_xpath = self.config.get("LOCATOR", "menu_event_button_by_xpath")
        return menu_event_button_by_xpath

    def menu_enrollment_group_by_xpath(self):
        menu_enrollment_group_by_xpath = self.config.get("LOCATOR", "menu_enrollment_group_by_xpath")
        return menu_enrollment_group_by_xpath

    def event_search_button_by_xpath(self):
        event_search_button_by_xpath = self.config.get("LOCATOR", "event_search_button_by_xpath")
        return event_search_button_by_xpath

    def event_search_start_date_checkbox(self):
        event_search_start_date_checkbox = self.config.get("LOCATOR", "event_search_start_date_checkbox")
        return event_search_start_date_checkbox

    def event_search_start_date_input(self):
        event_search_start_date_input = self.config.get("LOCATOR", "event_search_start_date_input")
        return event_search_start_date_input

    def event_search_end_date_checkbox(self):
        event_search_end_date_checkbox = self.config.get("LOCATOR", "event_search_end_date_checkbox")
        return event_search_end_date_checkbox

    def event_search_end_date_input(self):
        event_search_end_date_input = self.config.get("LOCATOR", "event_search_end_date_input")
        return event_search_end_date_input

    def enrollment_group_drop_down(self):
        enrollment_group_drop_down = self.config.get("LOCATOR", "enrollment_group_drop_down")
        return enrollment_group_drop_down

    def enrollment_group_checkbox_list(self):
        enrollment_group_checkbox_list = self.config.get("LOCATOR", "enrollment_group_checkbox_list")
        return enrollment_group_checkbox_list

    def enrollment_group_name_list(self):
        enrollment_group_name_list = self.config.get("LOCATOR", "enrollment_group_name_list")
        return enrollment_group_name_list

    def clear_button_by_xpath(self):
        clear_button_by_xpath = self.config.get("LOCATOR", "clear_button_by_xpath")
        return clear_button_by_xpath

    def close_button_by_xpath(self):
        close_button_by_xpath = self.config.get("LOCATOR", "close_button_by_xpath")
        return close_button_by_xpath

    def save_button_by_xpath(self):
        save_button_by_xpath = self.config.get("LOCATOR", "save_button_by_xpath")
        return save_button_by_xpath

    def zone_selection_drop_down(self):
        zone_selection_drop_down = self.config.get("LOCATOR", "zone_selection_drop_down")
        return zone_selection_drop_down

    def zones_checkbox_list(self):
        zones_checkbox_list = self.config.get("LOCATOR", "zones_checkbox_list")
        return zones_checkbox_list

    def zones_text_list(self):
        zones_text_list = self.config.get("LOCATOR", "zones_text_list")
        return zones_text_list

    def save_zone_button_by_xpath(self):
        save_zone_button_by_xpath = self.config.get("LOCATOR", "save_zone_button_by_xpath")
        return save_zone_button_by_xpath

    def close_zone_button_by_xpath(self):
        close_zone_button_by_xpath = self.config.get("LOCATOR", "close_zone_button_by_xpath")
        return close_zone_button_by_xpath

    def clear_zone_button_by_xpath(self):
        clear_zone_button_by_xpath = self.config.get("LOCATOR", "clear_zone_button_by_xpath")
        return clear_zone_button_by_xpath

    def tag_selection_drop_down(self):
        tag_selection_drop_down = self.config.get("LOCATOR", "tag_selection_drop_down")
        return tag_selection_drop_down

    def tags_checkbox_list(self):
        tags_checkbox_list = self.config.get("LOCATOR", "tags_checkbox_list")
        return tags_checkbox_list

    def tags_text_list(self):
        tags_text_list = self.config.get("LOCATOR", "tags_text_list")
        return tags_text_list

    def tags_clear_button_by_xpath(self):
        tags_clear_button_by_xpath = self.config.get("LOCATOR", "tags_clear_button_by_xpath")
        return tags_clear_button_by_xpath

    def tags_save_button_by_xpath(self):
        tags_save_button_by_xpath = self.config.get("LOCATOR", "tags_save_button_by_xpath")
        return tags_save_button_by_xpath

    def tags_close_button_by_xpath(self):
        tags_close_button_by_xpath = self.config.get("LOCATOR", "tags_close_button_by_xpath")
        return tags_close_button_by_xpath

    def sort_by_date_by_xpath(self):
        sort_by_date_by_xpath = self.config.get("LOCATOR", "sort_by_date_by_xpath")
        return sort_by_date_by_xpath

    def wait_icon_xpath(self):
        wait_icon_xpath = self.config.get("LOCATOR", "wait_icon_xpath")
        return wait_icon_xpath

    def clear_even_filter_button(self):
        clear_even_filter_button = self.config.get("LOCATOR", "clear_even_filter_button")
        return clear_even_filter_button

    def location_search_button_by_xpath(self):
        location_search_button_by_xpath = self.config.get("LOCATOR", "location_search_button_by_xpath")
        return location_search_button_by_xpath

    def event_filter_search_button_by_xpath(self):
        event_filter_search_button_by_xpath = self.config.get("LOCATOR", "event_filter_search_button_by_xpath")
        return event_filter_search_button_by_xpath

    def date_list_range_result_validation(self):
        date_list_range_result_validation = self.config.get("VALIDATION", "date_list_range_result_validation")
        return date_list_range_result_validation

    def tags_search_result_validation(self):
        tags_search_result_validation = self.config.get("VALIDATION", "tags_search_result_validation")
        return tags_search_result_validation

    def date_search_result_validation(self):
        date_search_result_validation = self.config.get("VALIDATION", "date_search_result_validation")
        return date_search_result_validation

    def enrollment_group_search_result_validation(self):
        enrollment_group_search_result_validation = self.config.get("VALIDATION",
                                                                    "enrollment_group_search_result_validation")
        return enrollment_group_search_result_validation

    def zone_search_result_validation(self):
        zone_search_result_validation = self.config.get("VALIDATION",
                                                        "zone_search_result_validation")
        return zone_search_result_validation

    def tags_search_result_second_validation(self):
        tags_search_result_second_validation = self.config.get("VALIDATION",
                                                        "tags_search_result_second_validation")
        return tags_search_result_second_validation

    def get_enrollment_group(self):
        get_enrollment_group = self.config.get("DATA", "enrollment_group")
        return get_enrollment_group

    def get_zone(self):
        get_zone = self.config.get("DATA", "zone")
        return get_zone

    def get_tags(self):
        get_tags = self.config.get("DATA", "tags")
        return get_tags

    def get_start_date(self):
        get_start_date = self.config.get("DATA", "start_date")
        return get_start_date

    def get_start_month(self):
        get_start_month = self.config.get("DATA", "start_month")
        return get_start_month

    def get_start_year(self):
        get_start_year = self.config.get("DATA", "start_year")
        return get_start_year

    def get_start_hour(self):
        get_start_hour = self.config.get("DATA", "start_hour")
        return get_start_hour

    def get_start_minuet(self):
        get_start_minuet = self.config.get("DATA", "start_minuet")
        return get_start_minuet

    def get_start_am_pm_period(self):
        get_start_am_pm_period = self.config.get("DATA", "start_am_pm_period")
        return get_start_am_pm_period

    def get_end_date(self):
        get_end_date = self.config.get("DATA", "end_date")
        return get_end_date

    def get_end_month(self):
        get_end_month = self.config.get("DATA", "end_month")
        return get_end_month

    def get_end_year(self):
        get_end_year = self.config.get("DATA", "end_year")
        return get_end_year

    def get_end_hour(self):
        get_end_hour = self.config.get("DATA", "end_hour")
        return get_end_hour

    def get_end_minuet(self):
        get_end_minuet = self.config.get("DATA", "end_minuet")
        return get_end_minuet

    def get_end_am_pm_period(self):
        get_end_am_pm_period = self.config.get("DATA", "end_am_pm_period")
        return get_end_am_pm_period

    def root_zone_validation(self):
        root_zone_validation = self.config.get("VALIDATION", "root_zone_validation")
        return root_zone_validation



