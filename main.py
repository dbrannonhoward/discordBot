from bot_logging.bot_logger import DiscordBotLog
from bot_memory.bot_brain import BotBrain
from SECRETS import MY_TOKEN
import discord

bot_logger = DiscordBotLog()
bot_brain = BotBrain()


class MyClient(discord.Client):
    async def on_ready(self):
        bot_brain.announce("logged on as {0}!".format(self.user))

    async def on_message(self, message):
        bot_brain.announce("message from {0.author}: {0.content}".format(message))
        if message.author == self.user:
            bot_logger.info_event("received message from self")
            return

        if ' ' in message.content:
            bot_logger.info_event("responding to message")
            await message.channel.send('i am not to be spoken with')


if __name__ == '__main__':
    client = MyClient()
    client.run(MY_TOKEN)
