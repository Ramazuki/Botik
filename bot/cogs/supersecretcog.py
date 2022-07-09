import re
from main import client
from discord.ext import commands
import random
import discord


class SuperSecret(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['аватар'])
    async def supersecretcommand(self, ctx):
        author = ctx.message.author
        supersecretlist = [f'{author.mention}, любит, когда волосатые мужики обмазываются маслом!',
                           f'{client.user.name} успешно заскамил мамонта - {author.mention}!',
                           f'{author.mention}, постирай свои трусы уже',
                           f'Появляется дикий {author.mention}',
                           f'{client.user.name} сел в машину и сгорел.']
        await ctx.send(random.choice(supersecretlist))

    @commands.command(aliases=['нос'])
    async def nose(self, ctx, member: discord.Member = None):
        author = ctx.message.author
        if member is None:
            await ctx.send(f'{client.user.mention} украл нос у {author.mention}')
        else:
            await ctx.send(f'{author.mention} украл нос у {member.mention}')

    @commands.Cog.listener()
    async def on_message(self, message):
        content = message.content
        if re.search(r'гигачад|Гигачад|Гига чад|гига чад', content):
            print(content)
            embed = discord.Embed(color=0x404e57)
            embed.set_image(
                url="https://melmagazine.com/wp-content/uploads/2021/01/66f-1.jpg")
            await message.channel.send(embed=embed)


def setup(client):
    client.add_cog(SuperSecret(client))
    print("Secret loaded")
