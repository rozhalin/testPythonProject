import json
from builtins import SystemError
from datetime import datetime, timedelta

from BusinessError import BusinessError
from BusinessProcess import BusinessProcess


class Robot:

    def __init__(self):
        print("Init")

        self.transaction = None
        self.process_start_date_time = datetime.now()

        self.__config()
        self.__init_applications()
        self.data = self.__get_transaction_data()

    def start(self):
        print("Start")
        while True:
            try:
                # robot working time check
                if self.__is_processing_time_over(self.config["processing_minutes"]): break
                # stop request check
                if self.__is_stop_requested(): break

                self.transaction = self.__get_transaction()
                if self.transaction is None:
                    break

                self.__process()
                self.__set_transaction_status(None)

            except SystemError as se:
                print("system exception")
                self.__set_transaction_status(se)
                self.__kill_all_processes()
                self.__init_applications()

            except BusinessError as be:
                print("business exception")
                self.__set_transaction_status(be)

    def __config(self):
        with open('data/config.json', 'r', encoding='utf-8') as fh:
            self.config = json.load(fh)

    def __process(self):
        print("process")
        BusinessProcess(self.config, self.transaction).run()

    def __init_applications(self):
        print("init applications")

    def __get_transaction_data(self):
        print("get transaction data")
        return ["1", "2", "3"]

    def __get_transaction(self):
        print("get transaction")
        return "New Transaction"

    def __set_transaction_status(self, exception):
        print("set transaction status")
        if exception is None:
            print("Success")
        elif isinstance(exception, SystemError):
            print("System Exception")
        elif isinstance(exception, BusinessError):
            print("Business Error")
        else:
            raise TypeError("Unsupported type of exception")

    def __kill_all_processes(self):
        print("kill all processes")

    def __is_processing_time_over(self, minutes):
        return (self.process_start_date_time + timedelta(minutes=minutes)) < datetime.now()

    def __is_stop_requested(self):
        # todo
        return False
