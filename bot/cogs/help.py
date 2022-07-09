from discord.ext import commands
import discord
from main import client as bot


class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            embed = discord.Embed(name="Help", description=page, colour=0x4e4e91)
            await destination.send(embed=embed)


class BetterHelp(commands.Cog):
    def __init__(self, client):
        self._original_help_command = client.help_command
        client.help_command = MyHelpCommand()
        client.help_command.cog = self

    def cog_unload(self):
        bot.help_command = self._original_help_command


def setup(client):
    client.add_cog(BetterHelp(client))
