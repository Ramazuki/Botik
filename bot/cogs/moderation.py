import discord
from discord.ext import commands
from discord.utils import get


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = None):
        if amount is None:
            await ctx.channel.purge(limit=2)
        else:
            try:
                int(amount)
            except:  # Error handler
                await ctx.send('Please enter a valid integer as amount.')
            else:
                await ctx.channel.purge(limit=amount + 1)

    '''BAN SECTION START'''

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, reason=None):
        if ctx.message.author == member:
            await ctx.send('ХИХИХИХИХИИХИХИХИИХ ОЧЕНЬ СМЕШНО')
        else:
            dm = await member.create_dm()
            await dm.send("You've been banned")
            await member.ban(reason=reason)
            await ctx.send(embed=discord.Embed(color=0x8f1b13, title="Отправлен отдыхать в бан",
                                               description=f"{member.mention} отправляется на отдых по причине: {reason} "
                                                           "<:disgusting:872606113718239312>"))

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member):
        banned = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(embed=discord.Embed(color=0x8f1b13, title="Произошёл разбан :exploding_head:",
                                                   description=f'{user} возвращается из небытия '
                                                               '<:isaac_like:872160976533864488> . Надеемся, что он '
                                                               'хорошо подумал о своём поведении'))

    '''BAN SECTION END'''

    '''MUTE SECTION'''

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, reason=None):
        muter = get(member.guild.roles, id=833340953687228417)
        if reason is None:
            reason = "По усмотрению модератора"
        await member.add_roles(muter)
        await ctx.send(f'{member.mention} в муте, клоун :clown: . По причине: {reason}')

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        muter = get(member.guild.roles, id=833340953687228417)
        await member.remove_roles(muter)
        await ctx.send(f'{member.mention}, говори!')


def setup(client):
    client.add_cog(Moderation(client))
    print('Moderation Cog loaded')
