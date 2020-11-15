from bot_logging.bot_logger import DiscordBotLog
from SECRETS import SHUTDOWN

message_logger = DiscordBotLog()


class MessageReader:
    def __init__(self):
        message_logger.info_event("MessageReader initialized..")
        self.author = ""
        self.content = ""

    @staticmethod
    def detects_a_space_in(message):
        if ' ' in message.content:
            message_logger.info_event("bot detected space in message : " + str(message.content))
            return True
        return False

    @staticmethod
    def detects_question_mark_in(message):
        if '?' in message.content:
            message_logger.info_event("bot detected '?' in message : " + str(message.content))
            return True
        return False

    @staticmethod
    def detects_shutdown(message):
        if SHUTDOWN in message.content:
            message_logger.info_event("bot detected shutdown phrase in message : " + str(message.content))
            return True
        return False

    def get_content_from_message(self, message) -> str:
        content = str(message.content)
        self.content = content

    def get_message_details(self, message):
        self.get_author_from_message(message)
        self.get_content_from_message(message)
        message_details = [self.author, self.content]
        message_logger.info_event(message_details)
        return " ".join(message_details)

    def get_author_from_message(self, message) -> str:
        author = str(message.author)
        self.author = author
