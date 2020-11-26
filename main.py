from bot_config_.bot_configuration import Configurator
from bot_event_.event_handler_ import EventHandler
from bot_log_.bot_log import LogMgmt
from bot_message_.message_handler_ import MessageHandler
from bot_server_.server_parser_ import ServerParser
from SECRETS import MY_TOKEN
import asyncio
import discord


class DiscordClient(discord.Client):
    def __init__(self, **options):
        super().__init__(**options)
        self.Cfg, self.EH, self.LM, self.MH, self.SP = \
            Configurator(), EventHandler(), LogMgmt(), MessageHandler(), ServerParser()

    async def on_ready(self):
        user_, user_id_ = self.user, self.user.id
        self.MP.log_on(user_, user_id_)
        self.EH.announce(event_logon)

    async def on_message(self, message):
        if message.author == self.user:
            self.LM.info_event("bot sends : " + str(message.content))
            return

        if self.MP.detects_shutdown(message):
            await message.channel.send(self.EH.respond(message, 'SHUTDOWN'))
            exit()  # TODO this is a dirty shutdown
        if self.MP.detects_a_space_in(message):
            await message.channel.send(self.EH.respond(message, 'SPACE'))
        elif self.MP.detects_user_list_request(message):
            for member in self.get_all_members():
                self.EH.respond(message, str(member))
                await message.channel.send(str(member))
                await asyncio.sleep(1)
        elif self.MP.detects_question_mark_in(message):
            await message.channel.send(self.EH.respond(message, 'QUESTION'))
        else:
            await message.channel.send(self.EH.respond(message, 'DUMB'))


if __name__ == '__main__':
    all_intents = discord.Intents.all()
    client = DiscordClient(intents=Configurator.get_intent())
    client.run(MY_TOKEN)
