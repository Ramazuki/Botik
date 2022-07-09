import discord
from discord.ext import commands
from bot.main import client as bot

class ReactionRoles(commands.Cog):
    def __init__(self, client):
        self.client = client

    @bot.event
    async def on_raw_reaction_add(payload):
        message_id = payload.message_id
        if message_id == 978707785808236564:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)

            if payload.emoji.name == 'peepoNerd':
                role = discord.utils.get(guild.roles, name = 'PeepoNerd')
            elif payload.emoji.name == 'dat_ass':
                role = discord.utils.get(guild.roles, name = 'Gigachad')
            else:
                role = discord.utils.get(guild.roles, name = payload.emoji.name)

            if role is not None:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                print(guild.members)
                if member is not None:
                    await member.add_roles(role)

    @bot.event
    async def on_raw_reaction_remove(payload):
        message_id = payload.message_id
        if message_id == 978707785808236564:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)

            if payload.emoji.name == 'peepoNerd':
                role = discord.utils.get(guild.roles, name='PeepoNerd')
            elif payload.emoji.name == 'dat_ass':
                role = discord.utils.get(guild.roles, name='Gigachad')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)

def setup(client):
    client.add_cog(ReactionRoles(client))
    print('Reaction Roles Cog loaded')
