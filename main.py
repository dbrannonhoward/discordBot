from bot_configuration.bot_configurator import Configurator
from bot_eyes.bot_vision import Vision
from bot_logging.bot_logger import DiscordBotLog
from bot_memory.bot_brain import Brain
from message_parsing.message_reader import MessageReader
from SECRETS import MY_TOKEN
import discord

bot_L = DiscordBotLog()
bot_B = Brain()
bot_C = Configurator()
bot_MR = MessageReader()
bot_V = Vision()


class MyClient(discord.Client):
    async def on_ready(self):
        event_logon = "logged on as user {0} with id {1}".format(self.user, self.user.id)
        bot_B.announce(event_logon)

    async def on_message(self, message):
        if message.author == self.user:
            bot_L.info_event("bot sends : " + str(message.content))
            return

        if bot_MR.detects_shutdown(message):
            await message.channel.send(bot_B.respond('SHUTDOWN'))
            exit()

        if bot_MR.detects_a_space_in(message):
            await message.channel.send(bot_B.respond('SPACE'))
        elif bot_MR.detects_question_mark_in(message):
            await message.channel.send(bot_B.respond('QUESTION'))


if __name__ == '__main__':
    all_intents = discord.Intents.all()
    client = MyClient(intents=bot_C.get_intent())
    client.run(MY_TOKEN)
