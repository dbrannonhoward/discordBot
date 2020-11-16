from bot_configurator.bot_configuration import BotConfiguration
from bot_finder.bot_discovery import BotDiscovery
from bot_logger.bot_log import BotLog
from bot_brain.bot_memory import BotMemory
from bot_message_reader.bot_message_library import BotMessageLibrary
from SECRETS import MY_TOKEN
import asyncio
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
        self.Configuration = self.Configuration()
        self.Discovery = self.Discovery()  # TODO not used at this time
        self.Log = self.Log()
        self.Memory = self.Memory()
        self.MessageLibrary = self.MessageLibrary()

    async def on_ready(self):
        event_logon = "logged on as user {0} with id {1}".format(self.user, self.user.id)
        self.Memory.announce(event_logon)

    async def on_message(self, message):
        if message.author == self.user:
            self.Log.info_event("bot sends : " + str(message.content))
            return

        if self.MessageLibrary.detects_shutdown(message):
            await message.channel.send(self.Memory.respond(message, 'SHUTDOWN'))
            exit()  # TODO this is a dirty shutdown
        if self.MessageLibrary.detects_a_space_in(message):
            await message.channel.send(self.Memory.respond(message, 'SPACE'))
        elif self.MessageLibrary.detects_user_list_request(message):
            for member in self.get_all_members():
                self.Memory.respond(message, str(member))
                await message.channel.send(str(member))
                await asyncio.sleep(1)
        elif self.MessageLibrary.detects_question_mark_in(message):
            await message.channel.send(self.Memory.respond(message, 'QUESTION'))
        else:
            await message.channel.send(self.Memory.respond(message, 'DUMB'))


if __name__ == '__main__':
    all_intents = discord.Intents.all()
    client = MyClient(intents=BotConfiguration.get_intent())
    client.run(MY_TOKEN)
