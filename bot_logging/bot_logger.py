from bot_logging.LOG_CONSTANTS import LOG_FILE_EXTENSION
from bot_logging.LOG_CONSTANTS import LOG_FILE_PREFIX
from bot_logging.LOG_CONSTANTS import LOG_FORMAT_STRING
from bot_logging.LOG_CONSTANTS import TIME_FORMAT_STRING
from datetime import datetime
import logging
import os


class DiscordBotLog(logging.Logger):
    def __init__(self):
        super(DiscordBotLog, self).__init__('discordBot')
        self.logger = logging.getLogger('discordBot')
        self.logger.setLevel(logging.DEBUG)
        self.log_file_name = self.create_log_file_and_return_name()
        self.handler = logging.FileHandler(filename=self.log_file_name, encoding='utf-8', mode='w')
        self.handler.setFormatter(logging.Formatter(LOG_FORMAT_STRING))
        self.logger.addHandler(self.handler)

    def cleanup_log_directory(self):
        pass

    @staticmethod
    def create_log_file_and_return_name() -> str:
        ts = datetime.now()
        time_now = str(ts.strftime(TIME_FORMAT_STRING))
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
