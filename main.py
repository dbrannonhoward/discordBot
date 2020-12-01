from bot_config_.bot_configuration import Configurator
from bot_event_.event_handler_ import EventHandler
from bot_log_.bot_log import LogMgmt
from bot_message_.message_parser_ import MessageParser
from bot_server_.server_parser_ import ServerParser
from SECRETS import MY_TOKEN
import asyncio
import discord


class DiscordClient(discord.Client):
    def __init__(self, **options):
        super().__init__(**options)
        self.Cfg, self.EH, self.LM, self.MP, self.SP = \
            Configurator(), EventHandler(), LogMgmt(), MessageParser(), ServerParser()
        self.actor = None

    async def on_ready(self):
        event_logon = "logged on as user {0} with id {1}".format(self.user, self.user.id)
        self.EH.announce(event_logon)

    async def on_message(self, message):
        self.LM.info_event("parsing message : " + str(message.content) + ", sent by : " + str(message.author))
        self.actor = self.MP.parse_message(message, self)
        if self.actor is None:
            return  # TODO does this work as intended? skips rest of function..?
        if isinstance(self.actor, list):
            for actor_ in self.actor:
                await actor_
                await asyncio.sleep(1)
            return
        await self.actor


if __name__ == '__main__':
    all_intents = discord.Intents.all()
    client = DiscordClient(intents=Configurator.get_intent())
    client.run(MY_TOKEN)
