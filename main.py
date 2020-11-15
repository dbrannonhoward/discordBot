from bot_logging.bot_logger import DiscordBotLog
from bot_memory.bot_brain import Brain
from message_parsing.message_reader import MessageReader
from SECRETS import MY_TOKEN
import discord

bot_L = DiscordBotLog()
bot_B = Brain()
bot_MR = MessageReader()


class MyClient(discord.Client):
    async def on_ready(self):
        bot_B.announce("logged on as {0}!".format(self.user))

    async def on_message(self, message):
        # bot_brain.announce("message from {0.author}: {0.content}".format(message))
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
    client = MyClient()
    client.run(MY_TOKEN)
