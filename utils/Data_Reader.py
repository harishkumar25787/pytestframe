import os
import traceback
import pyexcel as exc
from utils.configutility import ConfigUtility
from configparser import ConfigParser

class DataReader:
    """
    This class includes basic reusable data helpers.
    """
    config = ConfigUtility()

    def __init__(self):
        self.cur_path = os.path.abspath(os.path.dirname(__file__))

    def load_test_data(self):

        records = None

        # noinspection PyBroadException
        prop = self.config.load_properties_file()
        base_test_data = prop.get('RAFT', 'base_test_data')
        ui_file_path = os.path.join(self.cur_path, r"../TestData/{}.xlsx".format(base_test_data))

        try:
            if ui_file_path is not None:
                records = exc.iget_records(file_name=ui_file_path)
        except Exception as ex:
            traceback.print_exc(ex)

        return records

    def get_data(self, tc_name, column_name):
        """
        This method is used for returning column data specific to ui test case name
        :param tc_name: it takes test case name as input parameter
        :param column_name: it takes the name of the column for which value has to be returned
        :return:
        """
        value = None
        excel_records = self.load_test_data()

        # noinspection PyBroadException

        try:
            if excel_records is not None:
                for record in excel_records:
                    if record['TC_Name'] == tc_name:
                        value = record[column_name]
                        break
                    else:
                        continue

        except Exception as ex:
            traceback.print_exc(ex)

        return value