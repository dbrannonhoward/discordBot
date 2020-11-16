from bot_logger.bot_log import BotLog
from bot_brain.MEMORY_STRUCTURE import memories
from time_tracking.time_tools import TimeTools


time_tool = TimeTools()


class BotMemory:
    class Log(BotLog):
        def __init__(self):
            super().__init__()

    def __init__(self):
        self.Log = self.Log()
        self.Log.info_event("BotBrain initialized..")
        self.memory = memories

    def announce(self, announcement: str):
        self.Log.info_event(announcement)
        print(announcement)

    # def create_memory(self):
    #     brain_logger.info_event("creating memory..")
    #     print("bot_brain recalling..")

    def get_last_user_spoken_to(self):
        return self.memory["last_user_spoken_to"]

    def get_time_initialized(self):
        return self.memory["time_initialized"]

    def get_time_last_message_received(self):
        return self.memory["time_last_message_received"]

    def get_time_last_message_sent(self):
        return self.memory["time_last_message_sent"]

    def read_memory(self, memory_key):
        self.Log.info_event("reading memory..")
        print("bot_brain remembering..")
        try:
            return self.memory[memory_key]
        except KeyError:
            raise KeyError

    def respond(self, message, quote_key):
        # TODO ugly quickfix, rewrite
        event_info = "responding to {0.content} sent by {0.author} with ".\
                         format(message) + str(quote_key)
        if quote_key in self.memory.keys():
            self.Log.info_event(event_info)
            print(event_info)
            return self.memory[quote_key]
        print(event_info)
        return "NO KEY : " + str(quote_key)

    def set_last_user_spoken_to(self, username):
        self.memory["last_user_spoken_to"] = username

    def set_time_initialized(self):
        self.memory["time_initialized"] = time_tool.get_timestamp()

    def set_time_last_message_received(self):
        self.memory["time_last_message_received"] = time_tool.get_timestamp()

    def set_time_last_message_sent(self):
        self.memory["time_last_message_sent"] = time_tool.get_timestamp()


def main():
    bb = BotMemory()


if __name__ == '__main__':
    main()
