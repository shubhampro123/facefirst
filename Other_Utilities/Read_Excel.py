import pandas as pd
from pathlib import Path


class Read_excel:

    @staticmethod
    def get_registration_form_data_df():
        try:
            file_path = f"{Path(__file__).parent.parent}\\Test_Data\\Data_From_Excel\\Test_Data_XLSX.xlsx"
            df = pd.read_excel(file_path, sheet_name='Registration_Form_Data')
            return df
        except Exception as ex:
            print(ex)
