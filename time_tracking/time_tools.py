from CONSTANTS import STRFTIME_FORMAT
from datetime import datetime


class TimeTools:
    def __init__(self):
        pass

    @staticmethod
    def get_timestamp():
        time_now = datetime.now()
        return time_now.strftime(STRFTIME_FORMAT)
