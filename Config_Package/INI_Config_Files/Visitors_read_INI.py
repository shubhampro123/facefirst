import configparser
from pathlib import Path

class Read_Visitors_Components:
    def __init__(self):

        self.config = configparser.RawConfigParser()

        try:
            portal_menu_ini_file_path = f'{Path(__file__).parent.parent.parent}\\Test_Data\\Data_From_INI' \
                                        f'\\Visitors.ini'
            # Base_Class.logger.info("File location: ", deployment_manager_ini_file_path)
            self.config.read(portal_menu_ini_file_path)
        except Exception as ex:
            print("config file got an exception", ex)

    def start_date_check_bx_by_xpath(self):
        try:
            start_date_check_bx_by_xpath = self.config.get("LOCATORS", "start_date_check_bx_by_xpath")
            return start_date_check_bx_by_xpath
        except Exception as ex:
            print("start_date_check_bx_by_xpath : ", ex)

    def end_date_check_bx_by_xpath(self):
        try:
            end_date_check_bx_by_xpath = self.config.get("LOCATORS", "end_date_check_bx_by_xpath")
            return end_date_check_bx_by_xpath
        except Exception as ex:
            print("end_date_check_bx_by_xpath : ", ex)

    def visitors_link_by_xpath(self):
        try:
            visitors_link_by_xpath = self.config.get("LOCATORS", "visitors_link_by_xpath")
            return visitors_link_by_xpath
        except Exception as ex:
            print("visitors_link_by_xpath : ", ex)

    def search_drop_down_search_btn_by_xpath(self):
        try:
            search_drop_down_search_btn_by_xpath = self.config.get("LOCATORS", "search_drop_down_search_btn_by_xpath")
            return search_drop_down_search_btn_by_xpath
        except Exception as ex:
            print("search_drop_down_search_btn_by_xpath : ", ex)

    def search_drop_down_by_xpath(self):
        try:
            search_drop_down_by_xpath = self.config.get("LOCATORS", "search_drop_down_by_xpath")
            return search_drop_down_by_xpath
        except Exception as ex:
            print("search_drop_down_by_xpath : ", ex)

    def start_date_txt_bx_by_xpath(self):
        try:
            start_date_txt_bx_by_xpath = self.config.get("LOCATORS", "start_date_txt_bx_by_xpath")
            return start_date_txt_bx_by_xpath
        except Exception as ex:
            print("search_drop_down_by_xpath : ", ex)

    def end_date_txt_bx_by_xpath(self):
        try:
            end_date_txt_bx_by_xpath = self.config.get("LOCATORS", "end_date_txt_bx_by_xpath")
            return end_date_txt_bx_by_xpath
        except Exception as ex:
            print("end_date_txt_bx_by_xpath : ", ex)

    def clock_min_up_button_by_xpath(self):
        try:
            clock_min_up_button_by_xpath = self.config.get("LOCATORS", "clock_min_up_button_by_xpath")
            return clock_min_up_button_by_xpath
        except Exception as ex:
            print("clock_min_up_button_by_xpath : ", ex)

    def start_age_by_xpath(self):
        try:
            start_age_by_xpath = self.config.get("LOCATORS", "start_age_by_xpath")
            return start_age_by_xpath
        except Exception as ex:
            print("start_age_by_xpath : ", ex)

    def end_age_by_xpath(self):
        try:
            end_age_by_xpath = self.config.get("LOCATORS", "end_age_by_xpath")
            return end_age_by_xpath
        except Exception as ex:
            print("end_age_by_xpath : ", ex)

    def zone_data_input(self):
        try:
            zone_data_input = self.config.get("DATA", "zone_data_input")
            return zone_data_input
        except Exception as ex:
            print("zone_data_input : ", ex)

    def zone_selection_by_xpath(self):
        try:
            zone_selection_by_xpath = self.config.get("LOCATORS", "zone_selection_by_xpath")
            return zone_selection_by_xpath
        except Exception as ex:
            print("zone_selection_by_xpath : ", ex)

    def zone_check_bx_list_by_xpath(self):
        try:
            zone_check_bx_list_by_xpath = self.config.get("LOCATORS", "zone_check_bx_list_by_xpath")
            return zone_check_bx_list_by_xpath
        except Exception as ex:
            print("zone_check_bx_list_by_xpath : ", ex)

    def zone_text_list_by_xpath(self):
        try:
            zone_text_list_by_xpath = self.config.get("LOCATORS", "zone_text_list_by_xpath")
            return zone_text_list_by_xpath
        except Exception as ex:
            print("zone_text_list_by_xpath : ", ex)

    def save_button_by_xpath(self):
        try:
            save_button_by_xpath = self.config.get("LOCATORS", "save_button_by_xpath")
            return save_button_by_xpath
        except Exception as ex:
            print("save_button_by_xpath : ", ex)

    def close_button_by_xpath(self):
        try:
            close_button_by_xpath = self.config.get("LOCATORS", "close_button_by_xpath")
            return close_button_by_xpath
        except Exception as ex:
            print("close_button_by_xpath : ", ex)

    def clear_button_by_xpath(self):
        try:
            clear_button_by_xpath = self.config.get("LOCATORS", "clear_button_by_xpath")
            return clear_button_by_xpath
        except Exception as ex:
            print("clear_button_by_xpath : ", ex)

    def zone_result_by_xpath(self):
        try:
            zone_result_by_xpath = self.config.get("LOCATORS", "zone_result_by_xpath")
            return zone_result_by_xpath
        except Exception as ex:
            print("zone_result_by_xpath : ", ex)

    def gender_result_by_xpath(self):
        try:
            gender_result_by_xpath = self.config.get("LOCATORS", "gender_result_by_xpath")
            return gender_result_by_xpath
        except Exception as ex:
            print("gender_result_by_xpath : ", ex)

    def age_result_by_xpath(self):
        try:
            age_result_by_xpath = self.config.get("LOCATORS", "age_result_by_xpath")
            return age_result_by_xpath
        except Exception as ex:
            print("age_result_by_xpath : ", ex)

    def date_result_by_xpath(self):
        try:
            date_result_by_xpath = self.config.get("LOCATORS", "date_result_by_xpath")
            return date_result_by_xpath
        except Exception as ex:
            print("date_result_by_xpath : ", ex)

    def gender_data_input(self):
        try:
            gender_data_input = self.config.get("DATA", "gender_data_input")
            return gender_data_input
        except Exception as ex:
            print("gender_data_input : ", ex)

    def start_age_by_xpath(self):
        try:
            start_age_by_xpath = self.config.get("LOCATORS", "start_age_by_xpath")
            return start_age_by_xpath
        except Exception as ex:
            print("start_age_by_xpath : ", ex)

    def end_age_by_xpath(self):
        try:
            end_age_by_xpath = self.config.get("LOCATORS", "end_age_by_xpath")
            return end_age_by_xpath
        except Exception as ex:
            print("end_age_by_xpath : ", ex)

    def select_gender_by_xpath(self):
        try:
            select_gender_by_xpath = self.config.get("LOCATORS", "select_gender_by_xpath")
            return select_gender_by_xpath
        except Exception as ex:
            print("select_gender_by_xpath : ", ex)

    def get_start_date(self):
        try:
            get_start_date = self.config.get("DATA", "start_date")
            return get_start_date
        except Exception as ex:
            print("get_start_date : ", ex)

    def get_start_month(self):
        try:
            get_start_month = self.config.get("DATA", "start_month")
            return get_start_month
        except Exception as ex:
            print("get_start_month : ", ex)

    def get_start_year(self):
        try:
            get_start_year = self.config.get("DATA", "start_year")
            return get_start_year
        except Exception as ex:
            print("get_start_year : ", ex)

    def get_start_hour(self):
        try:
            get_start_hour = self.config.get("DATA", "start_hour")
            return get_start_hour
        except Exception as ex:
            print("get_start_hour : ", ex)

    def get_start_minuet(self):
        try:
            get_start_minuet = self.config.get("DATA", "start_minuet")
            return get_start_minuet
        except Exception as ex:
            print("get_start_minuet : ", ex)

    def get_start_am_pm_period(self):
        try:
            get_start_am_pm_period = self.config.get("DATA", "start_am_pm_period")
            return get_start_am_pm_period
        except Exception as ex:
            print("get_start_am_pm_period : ", ex)

    def get_end_date(self):
        try:
            get_end_date = self.config.get("DATA", "end_date")
            return get_end_date
        except Exception as ex:
            print("get_end_date : ", ex)

    def get_end_month(self):
        try:
            get_end_month = self.config.get("DATA", "end_month")
            return get_end_month
        except Exception as ex:
            print("get_end_month : ", ex)

    def get_end_year(self):
        try:
            get_end_year = self.config.get("DATA", "end_year")
            return get_end_year
        except Exception as ex:
            print("get_end_year : ", ex)

    def get_end_hour(self):
        try:
            get_end_hour = self.config.get("DATA", "end_hour")
            return get_end_hour
        except Exception as ex:
            print("get_end_hour : ", ex)

    def get_end_minuet(self):
        try:
            get_end_minuet = self.config.get("DATA", "end_minuet")
            return get_end_minuet
        except Exception as ex:
            print("get_end_minuet : ", ex)

    def get_end_am_pm_period(self):
        try:
            get_end_am_pm_period = self.config.get("DATA", "end_am_pm_period")
            return get_end_am_pm_period
        except Exception as ex:
            print("get_end_am_pm_period : ", ex)

    def calender_timer_icon_by_xpath(self):
        try:
            calender_timer_icon_by_xpath = self.config.get("LOCATORS", "calender_timer_icon_by_xpath")
            return calender_timer_icon_by_xpath
        except Exception as ex:
            print("calender_timer_icon_by_xpath : ", ex)

    def period_by_xpath(self):
        try:
            period_by_xpath = self.config.get("LOCATORS", "period_by_xpath")
            return period_by_xpath
        except Exception as ex:
            print("period_by_xpath : ", ex)

    def calender_tick_icon_by_xpath(self):
        try:
            calender_tick_icon_by_xpath = self.config.get("LOCATORS", "calender_tick_icon_by_xpath")
            return calender_tick_icon_by_xpath
        except Exception as ex:
            print("calender_tick_icon_by_xpath : ", ex)

    def calender_back_button_by_xpath(self):
        try:
            calender_back_button_by_xpath = self.config.get("LOCATORS", "calender_back_button_by_xpath")
            return calender_back_button_by_xpath
        except Exception as ex:
            print("calender_back_button_by_xpath : ", ex)

    def calender_month_year_by_xpath(self):
        try:
            calender_month_year_by_xpath = self.config.get("LOCATORS", "calender_month_year_by_xpath")
            return calender_month_year_by_xpath
        except Exception as ex:
            print("calender_month_year_by_xpath : ", ex)

    def calender_forward_button_by_xpath(self):
        try:
            calender_forward_button_by_xpath = self.config.get("LOCATORS", "calender_forward_button_by_xpath")
            return calender_forward_button_by_xpath
        except Exception as ex:
            print("calender_forward_button_by_xpath : ", ex)

    def current_minute_element_by_xpath(self):
        try:
            current_minute_element_by_xpath = self.config.get("LOCATORS", "current_minute_element_by_xpath")
            return current_minute_element_by_xpath
        except Exception as ex:
            print("current_minute_element_by_xpath : ", ex)

    def current_hour_ele_by_xpath(self):
        try:
            current_hour_ele_by_xpath = self.config.get("LOCATORS", "current_hour_ele")
            return current_hour_ele_by_xpath
        except Exception as ex:
            print("current_hour_ele_by_xpath : ", ex)

    def hour_down_by_xpath(self):
        try:
            hour_down_by_xpath = self.config.get("LOCATORS", "hour_down_by_xpath")
            return hour_down_by_xpath
        except Exception as ex:
            print("hour_down_by_xpath : ", ex)

    def clock_min_down_button_by_xpath(self):
        try:
            clock_min_down_button_by_xpath = self.config.get("LOCATORS", "clock_min_down_button_by_xpath")
            return clock_min_down_button_by_xpath
        except Exception as ex:
            print("clock_min_down_button_by_xpath : ", ex)

    def start_age_data_input(self):
        try:
            start_age_data_input = self.config.get("DATA", "start_age_data_input")
            return start_age_data_input
        except Exception as ex:
            print("start_age_data_input : ", ex)

    def end_age_data_input(self):
        try:
            end_age_data_input = self.config.get("DATA", "end_age_data_input")
            return end_age_data_input
        except Exception as ex:
            print("end_age_data_input : ", ex)
