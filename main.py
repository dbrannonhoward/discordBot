from CONSTANTS import MY_TOKEN
import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))


if __name__ == '__main__':
    client = MyClient()
    client.run(MY_TOKEN)
