from bot_logging.bot_logger import DiscordBotLog
from bot_memory.MEMORY_STRUCTURE import memories
from CONSTANTS import STRFTIME_FORMAT
from datetime import datetime


brain_logger = DiscordBotLog()


class BotBrain:
    def __init__(self):
        brain_logger.info_event("BotBrain initialized..")
        self.memory = memories

    @staticmethod
    def announce(announcement: str):
        brain_logger.info_event(announcement)
        print(announcement)

    def create_memory(self):
        brain_logger.info_event("creating memory..")
        print("bot_brain recalling..")

    @staticmethod
    def get_timestamp():
        time_now = datetime.now()
        return time_now.strftime(STRFTIME_FORMAT)

    def read_memory(self, memory_key):
        brain_logger.info_event("reading memory..")
        print("bot_brain remembering..")
        try:
            return self.memory[memory_key]
        except KeyError:
            raise KeyError

    def get_last_user_spoken_to(self):
        return self.memory["last_user_spoken_to"]

    def get_time_initialized(self):
        return self.memory["time_initialized"]

    def get_time_last_message_received(self):
        return self.memory["time_last_message_received"]

    def get_time_last_message_sent(self):
        return self.memory["time_last_message_sent"]

    def set_last_user_spoken_to(self, username):
        self.memory["last_user_spoken_to"] = username

    def set_time_initialized(self):
        self.memory["time_initialized"] = self.get_timestamp()

    def set_time_last_message_received(self):
        self.memory["time_last_message_received"] = self.get_timestamp()

    def set_time_last_message_sent(self):
        self.memory["time_last_message_sent"] = self.get_timestamp()


def main():
    bb = BotBrain()


if __name__ == '__main__':
    main()
