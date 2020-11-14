from bot_logging.LOG_CONSTANTS import *
from datetime import datetime
import logging
import os


class DiscordBotLog:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.log_file_name = self.create_log_file_and_return_name()
        self.handler = logging.FileHandler(filename=self.log_file_name,
                                           encoding=LOG_ENCODING,
                                           mode=LOG_HANDLER_MODE)
        self.handler.setFormatter(logging.Formatter(LOG_FORMAT))
        self.logger.addHandler(self.handler)

    def cleanup_log_directory(self):
        pass

    @staticmethod
    def create_log_file_and_return_name() -> str:
        ts = datetime.now()
        time_now = str(ts.strftime(TIME_FORMAT))
        log_file_name = LOG_FILE_PREFIX + str(time_now) + LOG_FILE_EXTENSION
        try:
            if not os.path.exists(log_file_name):
                os.mknod(log_file_name)
            return log_file_name
        except OSError:
            raise OSError

    def debug_event(self, event_description):
        self.logger.log(logging.DEBUG, event_description)

    def info_event(self, event_description):
        self.logger.log(logging.INFO, event_description)


def main():
    log = DiscordBotLog()
    log.debug_event("debug event")
    log.info_event("info event")


if __name__ == '__main__':
    main()
