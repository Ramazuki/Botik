from discord.ext import commands
from bot.main import client as bot
from discord import FFmpegPCMAudio
import random
import discord
import time


class Talking_Ben(commands.Cog):
    def __init__(self, client):
        self.voice = None
        self.caller = None
        self.client = client
        self.state = False

    @commands.command(description="Напишите эту команду и начните разговор с Беном!\n"
                                  "Одновременно Бен отвечает только одному человеку",
                      brief="Начать разговор с Беном", aliases=['Позвонить_Бену', 'Call_Ben', 'Звонок_Бену'])
    async def phonecall(self, ctx):
        if self.caller is None:
            if ctx.author.voice:
                self.caller = ctx.message.author
                channel = ctx.message.author.voice.channel
                self.voice = await channel.connect()
                emb = discord.Embed(title="*Phone call*", colour=discord.Colour.dark_gold())
                emb.set_image(
                    url="https://i.pinimg.com/564x/8f/63/2f/8f632fbf33ddc93a168999fa91525cb2.jpg")
                await ctx.send(embed=emb)
                source = FFmpegPCMAudio('./Content/Talking Ben/PhoneCall_Ben.wav')
                self.voice.play(source)
            else:
                await ctx.send("Вы не находитесь в голосовом канале")
        else:
            await ctx.send("Сейчас Бен занят")


    @commands.command(description="Завершить ваш незабываемый опыт общения с говорящей собакой",
                      brief="Завершить разговор с Беном",aliases=['Пока', 'До_связи', 'Пока-пока', 'До_свидания'])
    async def bye(self, ctx):
        if self.caller == ctx.message.author:
            self.state = False
            source = FFmpegPCMAudio('./Content/Talking Ben/NoAnswer_Ben.wav')
            if ctx.voice_client:
                emb = discord.Embed(title="*Bye*", colour=discord.Colour.dark_gold())
                emb.set_image(
                    url="https://i.pinimg.com/564x/10/49/13/104913dd057d53b9aa25f6a8cade4c99.jpg")
                self.voice.play(source)
                time.sleep(1)
                await ctx.send(embed=emb)
                time.sleep(1)
                await ctx.guild.voice_client.disconnect()
                self.caller = None
            else:
                await ctx.send("Я не в голосовом канале")

        else:
            await ctx.send("Сейчас Бен занят")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == bot.user:
            return
        if (message.author == self.caller) and (message.content.startswith('?') == False):
            sounds = ['Eeu_Ben', 'HoHoHo_Ben', 'No_Ben', 'Yes_Ben']
            pick = random.choice(sounds)
            source = FFmpegPCMAudio('./Content/Talking Ben/' + pick + '.wav')
            self.voice.play(source)

def setup(client):
    client.add_cog(Talking_Ben(client))
    print('Ben is active')
