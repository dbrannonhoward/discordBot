from bot_logger.bot_log import BotLog
from SECRETS import SHUTDOWN


class BotMessageLibrary:
    class Log(BotLog):
        def __init__(self):
            super().__init__()

    def __init__(self):
        self.Log = self.Log()
        self.Log.info_event("MessageReader initialized..")
        self.author = ""
        self.content = ""

    def detects_a_space_in(self, message):
        if ' ' in message.content:
            self.Log.info_event("bot detected space in message : " + str(message.content))
            return True
        return False

    def detects_question_mark_in(self, message):
        if '?' in message.content:
            self.Log.info_event("bot detected '?' in message : " + str(message.content))
            return True
        return False

    def detects_shutdown(self, message):
        if SHUTDOWN in message.content:
            self.Log.info_event("bot detected shutdown phrase in message : " + str(message.content))
            return True
        return False

    def get_content_from_message(self, message):
        content = str(message.content)
        self.content = content

    def get_message_details(self, message):
        self.get_author_from_message(message)
        self.get_content_from_message(message)
        message_details = [self.author, self.content]
        self.Log.info_event(message_details)
        return " ".join(message_details)

    def get_author_from_message(self, message):
        author = str(message.author)
        self.author = author
