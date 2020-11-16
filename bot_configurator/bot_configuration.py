import discord


class BotConfiguration:
    def __init__(self):
        pass

    @staticmethod
    def get_intent():
        return discord.Intents.all()
