from bot_log_.bot_log import LogMgmt
from bot_message_.MESSAGE_STRINGS import *
from SECRETS import USERLIST
from SECRETS import SHUTDOWN


class MessageHandler:
    class Log(LogMgmt):
        def __init__(self):
            super().__init__()

    def __init__(self):
        self.Log = self.Log()
        self.Log.info_event("MessageReader initialized..")
        self.author = ""
        self.content = ""

    def announce(self, message_string):
        self.Log.info_event(message_string)
        self.print_to_console(message_string)

    def detects_a_space_in(self, message):
        if ' ' in message.content:
            self.Log.info_event("bot detected space in message : " + str(message.content))
            return True
        return False

    def detects_user_list_request(self, message):
        if USERLIST in message.content:
            event_info = "bot detected user list phrase in message : " + str(message.content)
            self.Log.info_event(event_info)
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

    def log_on(self, user_, user_id_):
        message_log_on = "logged on as user {0} with id {1}".format(user_, user_id_)
        self.Log.info_event(message_log_on)

    @staticmethod
    def print_to_console(message_string):
        print(message_string)

    def respond(self, message, quote_key):
        # TODO rewrite
        event_info = "responding to {0.content} sent by {0.author} with ".\
                         format(message) + str(quote_key)
        if quote_key in self.MSG_STR.keys():
            self.Log.info_event(event_info)
            print(event_info)
            return self.memory[quote_key]
        print(event_info)
        return "NO KEY : " + str(quote_key)
