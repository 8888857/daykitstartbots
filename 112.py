import discord
from discord.ext import commands
from discord import utils
import os
#импорт папки конфигов
import config

#установить префикс
bot = commands.Bot(command_prefix='/')

#команда /прав
@bot.command()
async def прав(ctx):#команда
    await ctx.send(config.PRAV1) #текст который выведеться

#команда/прав1
@bot.command()
async def прав1(ctx):#команда
    await ctx.send(config.p1) #текст который выведеться

#команда /прав2
@bot.command()
async def прав2(ctx):#команда
    await ctx.send(config.p2) #текст который выведеться

#командо помощь
@bot.command()
async def помощь(ctx):#команда
    await ctx.send(config.o1) #текст который выведеться

#команда /обр1
@bot.command()
async def обр1(ctx):#команда
    await ctx.send(config.ob1) #текст который выведеться

#команда /обр2
@bot.command()
async def обр2(ctx):#команда
    await ctx.send(config.ob2) #текст который выведеться

#команда /обр3
@bot.command()
async def обр3(ctx):#команда
    await ctx.send(config.ob3) #текст который выведеться

#команда /обр
@bot.command()
async def обр(ctx):#команда
    await ctx.send(config.ob) #текст который выведеться

#поле для токена бота
#bot.run(config.TOKEN)

token = os.enverion.get('BOT_TOKEN')

bot.run(token)