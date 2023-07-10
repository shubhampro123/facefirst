import configparser
from pathlib import Path


class Read_Visitor_Search_jobs_filter_Components:
    def __init__(self):

        self.config = configparser.RawConfigParser()

        try:
            portal_menu_ini_file_path = f'{Path(__file__).parent.parent.parent}\\Test_Data\\Data_From_INI' \
                                        f'\\VisitorSearchJob_Filter_combination.ini'
            # Base_Class.logger.info("File location: ", deployment_manager_ini_file_path)
            self.config.read(portal_menu_ini_file_path)
        except Exception as ex:
            print("config file got an exception", ex)

    def matches_found_by_xpath(self):
        try:
            matches_found_by_xpath = self.config.get("LOCATORS", "matches_found_by_xpath")
            return matches_found_by_xpath
        except Exception as ex:
            print("matches_found_by_xpath : ", ex)

    def job_progress_title_by_xpath(self):
        try:
            job_progress_title_by_xpath = self.config.get("LOCATORS", "job_progress_title_by_xpath")
            return job_progress_title_by_xpath
        except Exception as ex:
            print("job_progress_title_by_xpath : ", ex)

    def start_date_by_xpath(self):
        try:
            start_date_by_xpath = self.config.get("LOCATORS", "start_date_by_xpath")
            return start_date_by_xpath
        except Exception as ex:
            print("start_date_by_xpath : ", ex)

    def end_date_by_xpath(self):
        try:
            end_date_by_xpath = self.config.get("LOCATORS", "end_date_by_xpath")
            return end_date_by_xpath
        except Exception as ex:
            print("end_date_by_xpath : ", ex)

    def search_constraints_by_xpath(self):
        try:
            search_constraints_by_xpath = self.config.get("LOCATORS", "search_constraints_by_xpath")
            return search_constraints_by_xpath
        except Exception as ex:
            print("search_constraints_by_xpath : ", ex)

    def view_results_by_xpath(self):
        try:
            view_results_by_xpath = self.config.get("LOCATORS", "view_results_by_xpath")
            return view_results_by_xpath
        except Exception as ex:
            print("view_results_by_xpath : ", ex)

    def select_all_by_xpath(self):
        try:
            select_all_by_xpath = self.config.get("LOCATORS", "select_all_by_xpath")
            return select_all_by_xpath
        except Exception as ex:
            print("select_all_by_xpath : ", ex)

    def search_by_xpath(self):
        try:
            search_by_xpath = self.config.get("LOCATORS", "search_by_xpath")
            return search_by_xpath
        except Exception as ex:
            print("search_by_xpath : ", ex)

    def action_by_xpath(self):
        try:
            action_by_xpath = self.config.get("LOCATORS", "action_by_xpath")
            return action_by_xpath
        except Exception as ex:
            print("action_by_xpath : ", ex)

    def delete_jobs_by_xpath(self):
        try:
            delete_jobs_by_xpath = self.config.get("LOCATORS", "delete_jobs_by_xpath")
            return delete_jobs_by_xpath
        except Exception as ex:
            print("delete_jobs_by_xpath : ", ex)

    def delete_job_confirmation_by_xpath(self):
        try:
            delete_job_confirmation_by_xpath = self.config.get("LOCATORS", "delete_job_confirmation_by_xpath")
            return delete_job_confirmation_by_xpath
        except Exception as ex:
            print("delete_job_confirmation_by_xpath : ", ex)

    def cancel_delete_job_confirmation_by_xpath(self):
        try:
            cancel_delete_job_confirmation_by_xpath = self.config.get("LOCATORS",
                                                                      "cancel_delete_job_confirmation_by_xpath")
            return cancel_delete_job_confirmation_by_xpath
        except Exception as ex:
            print("cancel_delete_job_confirmation_by_xpath : ", ex)

    def cancel_jobs_by_xpath(self):
        try:
            cancel_jobs_by_xpath = self.config.get("LOCATORS", "cancel_jobs_by_xpath")
            return cancel_jobs_by_xpath
        except Exception as ex:
            print("cancel_jobs_by_xpath : ", ex)

    def refresh_link_by_xpath(self):
        try:
            refresh_link_by_xpath = self.config.get("LOCATORS", "refresh_link_by_xpath")
            return refresh_link_by_xpath
        except Exception as ex:
            print("refresh_link_by_xpath : ", ex)

    def blank_page_msg_by_xpath(self):
        try:
            blank_page_msg_by_xpath = self.config.get("LOCATORS", "blank_page_msg_by_xpath")
            return blank_page_msg_by_xpath
        except Exception as ex:
            print("blank_page_msg_by_xpath : ", ex)

    def only_incomplete_jobs_yes_radio_btn_by_xpath(self):
        try:
            only_incomplete_jobs_yes_radio_btn_by_xpath = self.config.get("LOCATORS",
                                                                          "only_incomplete_jobs_yes_radio_btn_by_xpath")
            return only_incomplete_jobs_yes_radio_btn_by_xpath
        except Exception as ex:
            print("only_incomplete_jobs_yes_radio_btn_by_xpath : ", ex)

    def only_incomplete_jobs_no_radio_btn_by_xpath(self):
        try:
            only_incomplete_jobs_no_radio_btn_by_xpath = self.config.get("LOCATORS",
                                                                         "only_incomplete_jobs_no_radio_btn_by_xpath")
            return only_incomplete_jobs_no_radio_btn_by_xpath
        except Exception as ex:
            print("only_incomplete_jobs_no_radio_btn_by_xpath : ", ex)

    def include_jobs_deleted_results_jobs_yes_radio_btn_by_xpath(self):
        try:
            include_jobs_deleted_results_jobs_yes_radio_btn_by_xpath = self.config.get("LOCATORS",
                                                                                       "include_jobs_deleted_results_"
                                                                                       "jobs_yes_radio_btn_by_xpath")
            return include_jobs_deleted_results_jobs_yes_radio_btn_by_xpath
        except Exception as ex:
            print("include_jobs_deleted_results_jobs_yes_radio_btn_by_xpath : ", ex)

    def include_jobs_deleted_results_jobs_no_radio_btn_by_xpath(self):
        try:
            include_jobs_deleted_results_jobs_no_radio_btn_by_xpath = self.config.get("LOCATORS",
                                                                                      "include_jobs_deleted_"
                                                                                      "results_jobs_no_radio"
                                                                                      "_btn_by_xpath")

            return include_jobs_deleted_results_jobs_no_radio_btn_by_xpath
        except Exception as ex:
            print("include_jobs_deleted_results_jobs_no_radio_btn_by_xpath : ", ex)

    def include_jobs_all_users_yes_radio_btn_by_xpath(self):
        try:
            include_jobs_all_users_yes_radio_btn_by_xpath = self.config.get("LOCATORS", "include_jobs_all_users_"
                                                                                        "yes_radio_btn_by_xpath")
            return include_jobs_all_users_yes_radio_btn_by_xpath
        except Exception as ex:
            print("include_jobs_all_users_yes_radio_btn_by_xpath : ", ex)

    def include_jobs_all_users_no_radio_btn_by_xpath(self):
        try:
            include_jobs_all_users_no_radio_btn_by_xpath = self.config.get("LOCATORS", "include_jobs_all_users"
                                                                                       "_no_radio_btn_by_xpath")
            return include_jobs_all_users_no_radio_btn_by_xpath
        except Exception as ex:
            print("include_jobs_all_users_no_radio_btn_by_xpath : ", ex)

    def search_dropdown_clear_btn_by_xpath(self):
        try:
            search_dropdown_clear_btn_by_xpath = self.config.get("LOCATORS", "search_dropdown_clear_btn_by_xpath")

            return search_dropdown_clear_btn_by_xpath
        except Exception as ex:
            print("search_dropdown_clear_btn_by_xpath : ", ex)

    def search_dropdown_search_btn_by_xpath(self):
        try:
            search_dropdown_search_btn_by_xpath = self.config.get("LOCATORS", "search_dropdown_search_btn_by_xpath")

            return search_dropdown_search_btn_by_xpath
        except Exception as ex:
            print("search_dropdown_search_btn_by_xpath : ", ex)

    def visitor_search_job_btn_by_xpath(self):
        try:
            visitor_search_job_btn_by_xpath = self.config.get("LOCATORS", "visitor_search_job_btn_by_xpath")

            return visitor_search_job_btn_by_xpath
        except Exception as ex:
            print("visitor_search_job_btn_by_xpath : ", ex)

    def start_date_input_tbx_by_xpath(self):
        try:
            start_date_input_tbx_by_xpath = self.config.get("LOCATORS", "start_date_input_tbx_by_xpath")

            return start_date_input_tbx_by_xpath
        except Exception as ex:
            print("start_date_input_tbx_by_xpath : ", ex)

    def end_date_input_tbx_by_xpath(self):
        try:
            end_date_input_tbx_by_xpath = self.config.get("LOCATORS", "end_date_input_tbx_by_xpath")

            return end_date_input_tbx_by_xpath
        except Exception as ex:
            print("end_date_input_tbx_by_xpath : ", ex)

    def start_date_data(self):
        try:
            start_date = self.config.get("DATA", "start_date")

            return start_date
        except Exception as ex:
            print("start_date : ", ex)

    def end_date_data(self):
        try:
            end_date = self.config.get("DATA", "end_date")

            return end_date
        except Exception as ex:
            print("end_date : ", ex)

    def incomplete_status_by_xpath(self):
        try:
            incomplete_status_by_xpath = self.config.get("LOCATORS", "incomplete_status_by_xpath")

            return incomplete_status_by_xpath
        except Exception as ex:
            print("incomplete_status_by_xpath : ", ex)

    def jobs_list_by_xpath(self):
        try:
            jobs_list_by_xpath = self.config.get("LOCATORS", "jobs_list_by_xpath")

            return jobs_list_by_xpath
        except Exception as ex:
            print("jobs_list_by_xpath : ", ex)

    def match_list_first_check_bx_by_xpath(self):
        try:
            match_list_first_check_bx_by_xpath = self.config.get("LOCATORS", "match_list_first_check_bx_by_xpath")

            return match_list_first_check_bx_by_xpath
        except Exception as ex:
            print("match_list_first_check_bx_by_xpath : ", ex)

    def match_list_action_by_xpath(self):
        try:
            match_list_action_by_xpath = self.config.get("LOCATORS", "match_list_action_by_xpath")

            return match_list_action_by_xpath
        except Exception as ex:
            print("match_list_action_by_xpath : ", ex)

    def delete_selected_visitor_by_xpath(self):
        try:
            delete_selected_visitor_by_xpath = self.config.get("LOCATORS", "delete_selected_visitor_by_xpath")

            return delete_selected_visitor_by_xpath
        except Exception as ex:
            print("delete_selected_visitor_by_xpath : ", ex)

    def including_deleted_criteria_by_xpath(self):
        try:
            including_deleted_criteria_by_xpath = self.config.get("LOCATORS", "including_deleted_criteria_by_xpath")

            return including_deleted_criteria_by_xpath
        except Exception as ex:
            print("including_deleted_criteria_by_xpath : ", ex)

    def only_incomplete_jobs_by_xpath(self):
        try:
            only_incomplete_jobs_by_xpath = self.config.get("LOCATORS", "only_incomplete_jobs_by_xpath")

            return only_incomplete_jobs_by_xpath
        except Exception as ex:
            print("only_incomplete_jobs_by_xpath : ", ex)

    def all_users_job_by_xpath(self):
        try:
            all_users_job_by_xpath = self.config.get("LOCATORS", "all_users_job_by_xpath")

            return all_users_job_by_xpath
        except Exception as ex:
            print("all_users_job_by_xpath : ", ex)




