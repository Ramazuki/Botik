from discord.ext import commands
import discord
import random
import io
import time


class DuelModule(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.duelist1 = None
        self.duelist2 = None
        self.word = None
        #self.state = False #If duel actually happened
        self.game = False #If game in proccess


    @commands.command(aliases=['дуэль'],
                      description='Вызови своего друга на дуэль!\nПобеждает тот, кто первый напишет заданное слово в чат',
                      brief='Словесная дуэль!!!')
    async def duel(self, ctx, member: discord.Member):
        if member == ctx.message.author:
            return

        if self.duelist1 is None and self.duelist2 is None:
            #self.state = False
            self.duelist1 = ctx.message.author
            self.duelist2 = member
            invitation = discord.Embed(title="Вам брошен вызов", description=f'{member.mention} вам был брошен вызов от {ctx.message.author.mention}\n'
                                                                             f'?accept - принять    ?deny - отклонить', color=0xe3003d)
            await ctx.send(embed=invitation)
        else:
            await ctx.send("Кто-то сейчас дуэлится")


    @commands.command(aliases=['принять',"подтвердить"],
                      description="Принять вызов на дуэль",
                      brief="Принять вызов")
    async def accept(self, ctx):
        if self.duelist1 is None or self.duelist2 is None or self.duelist2 != ctx.message.author:
            await ctx.send("Вам не брошен вызов")
            return

        #self.state = True
        self.game = True
        #Pick random russian noun
        with io.open("bot/data/russian_nouns.txt", encoding="utf-8", mode='r') as ru:
            text = ru.readlines()

        self.word = random.choice(text).strip()
        await ctx.send("Дуэль начинается, готовьте свою клавиатуру")
        time.sleep(2)
        await ctx.send(embed=discord.Embed(title=f'{self.word}', colour=0xe3003d))

    @commands.command(aliases=['отклонить'],
                      description='Отклонить вызов на дуэль',
                      brief='Отклонить вызов')
    async def deny(self, ctx):
        if (self.duelist1 == ctx.message.author or self.duelist2 == ctx.message.author) and self.game == False :
            #self.state = True
            self.duelist1 = None
            self.duelist2 = None
            await ctx.send('Дуэль отклонена!')
        elif self.game == True:
            await ctx.send('Не пытайся сбежать с дуэли')
        else:
            await ctx.send('Вам не брошен вызов')

    @commands.Cog.listener()
    async def on_message(self, message):
        if (self.duelist1 == message.author or self.duelist2 == message.author) and self.game == True and not message.content.startswith(r'?'):
            if message.content == self.word:
                self.word = None
                self.game = False
                await message.channel.send(f'{message.author.mention} победил!')
                self.duelist1 = None
                self.duelist2 = None
            else:
                await message.channel.send(f'Слово написано не верно, {message.author.mention}')



def setup(client):
    client.add_cog(DuelModule(client))
    print("Duels loaded")