from bot_log_.LOG_CONSTANTS import *
from CONSTANTS import STRFTIME_FORMAT
from datetime import datetime
import logging
import os


class LogMgmt:
    def __init__(self):
        self.logger = logging.getLogger(BOT_NAME)
        self.logger.setLevel(logging.DEBUG)
        self.log_directory = self.get_log_directory()
        self.cleanup_log_directory()
        self.log_file_name = self.create_log_file_and_return_name()
        self.handler = logging.FileHandler(filename=self.log_file_name,
                                           encoding=LOG_ENCODING,
                                           mode=LOG_HANDLER_MODE)
        self.handler.setFormatter(logging.Formatter(LOG_FORMAT))
        self.logger.addHandler(self.handler)
        self.info_event("DiscordBotLog initialized..")

    def cleanup_log_directory(self):
        self.delete_files_with_extension(LOG_FILE_EXTENSION)

    @staticmethod
    def create_log_file_and_return_name() -> str:
        ts = datetime.now()
        time_now = str(ts.strftime(STRFTIME_FORMAT))
        log_file_name = LOG_FILE_PREFIX + str(time_now) + LOG_FILE_EXTENSION
        try:
            if not os.path.exists(log_file_name):
                os.mknod(log_file_name)
            return log_file_name
        except OSError:
            raise OSError

    def debug_event(self, event_description):
        self.logger.log(logging.DEBUG, event_description)

    def delete_files_with_extension(self, extension):
        # TODO known bug if .log file is in this directory..
        try:
            for root, dirs, files in os.walk(self.log_directory):
                for file in files:
                    # file_abs_path = os.path.abspath(file)
                    if file.endswith(LOG_FILE_EXTENSION):
                        os.remove(file)
        except OSError:
            raise OSError

    @staticmethod
    def get_log_directory():
        return os.getcwd()

    def info_event(self, event_description: str):
        self.logger.log(logging.INFO, event_description)


def main():
    log = LogMgmt()
    log.debug_event("debug event")
    log.info_event("info event")


if __name__ == '__main__':
    main()
