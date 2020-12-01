from bot_log_.bot_log import LogMgmt
from SECRETS import USERLIST
from SECRETS import SHUTDOWN


class MessageParser:
    def __init__(self):
        self.LM = LogMgmt()
        self.LM.info_event("MessageReader initialized..")
        self.author = ""
        self.content = ""

    def detects_a_space_in(self, message):
        if ' ' in message.content:
            self.LM.info_event("bot detected space in message : " + str(message.content))
            return True
        return False

    def detects_question_mark_in(self, message):
        if '?' in message.content:
            self.LM.info_event("bot detected '?' in message : " + str(message.content))
            return True
        return False

    def detects_shutdown(self, message):
        if SHUTDOWN in message.content:
            self.LM.info_event("bot detected shutdown phrase in message : " + str(message.content))
            return True
        return False

    def detects_user_list_request(self, message):
        if USERLIST in message.content:
            event_info = "bot detected user list phrase in message : " + str(message.content)
            self.LM.info_event(event_info)
            return True
        return False

    @staticmethod
    def get_message_detail(message, detail: str):
        if detail == 'author' and hasattr(message, detail):
            return str(message.author)
        if detail == 'content' and hasattr(message, detail):
            return str(message.content)
        raise RuntimeError

    def parse_message(self, message, discord_client_object):
        self.author = self.get_message_detail(message, 'author')
        self.content = self.get_message_detail(message, 'content')
        if message.author == discord_client_object.user:
            self.LM.info_event("bot sends : " + str(message.content))
            return None
        if self.detects_shutdown(message):
            return message.channel.send(discord_client_object.EH.respond(message, 'SHUTDOWN'))
        if self.detects_a_space_in(message):
            return message.channel.send(discord_client_object.EH.respond(message, 'SPACE'))
        elif self.detects_user_list_request(message):
            member_list_generator_and_sender = list()
            for member in discord_client_object.get_all_members():
                member_list_generator_and_sender.append(message.channel.send(str(member)))
            return member_list_generator_and_sender
        if self.detects_question_mark_in(message):
            return message.channel.send(discord_client_object.EH.respond(message, 'QUESTION'))
        else:
            return message.channel.send(discord_client_object.EH.respond(message, 'DUMB'))
