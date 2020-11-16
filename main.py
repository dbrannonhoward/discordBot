from bot_configurator.bot_configuration import BotConfiguration
from bot_finder.bot_discovery import BotDiscovery
from bot_logger.bot_log import BotLog
from bot_memorizer.bot_memory import BotMemory
from bot_message_reader.bot_message_library import BotMessageLibrary
from SECRETS import MY_TOKEN
import discord


class MyClient(discord.Client):
    class Configuration(BotConfiguration):
        def __init__(self):
            super().__init__()

    class Discovery(BotDiscovery):
        def __init__(self):
            super().__init__()

    class Log(BotLog):
        def __init__(self):
            super().__init__()

    class Memory(BotMemory):
        def __init__(self):
            super().__init__()

    class MessageLibrary(BotMessageLibrary):
        def __init__(self):
            super().__init__()

    def __init__(self, **options):
        super().__init__(**options)
        self.Memory = self.Memory()
        self.Configuration = self.Configuration()
        self.Log = self.Log()
        self.MessageLibrary = self.MessageLibrary()
        # self.Vision = self.Vision()

    async def on_ready(self):
        event_logon = "logged on as user {0} with id {1}".format(self.user, self.user.id)
        self.Memory.announce(event_logon)

    async def on_message(self, message):
        if message.author == self.user:
            self.Log.info_event("bot sends : " + str(message.content))
            return

        if self.MessageLibrary.detects_shutdown(message):
            await message.channel.send(self.Memory.respond('SHUTDOWN'))
            exit()  # TODO this is a dirty shutdown
        if self.MessageLibrary.detects_a_space_in(message):
            await message.channel.send(self.Memory.respond('SPACE'))
        elif self.MessageLibrary.detects_question_mark_in(message):
            await message.channel.send(self.Memory.respond('QUESTION'))


if __name__ == '__main__':
    all_intents = discord.Intents.all()
    client = MyClient(intents=BotConfiguration.get_intent())
    client.run(MY_TOKEN)
