import discord
from discord.ext import commands
from discord import utils
import os
from discord.ext.commands import has_permissions
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

@bot.command(pass_context=True)
@has_permissions(manage_messages=True)
async def очистить(ctx, amount=100):
    await ctx.channel.purge(limit=amount)

@bot.command(pass_context=True)
@has_permissions(manage_messages=True)
async def озв(ctx, arg = 'ПРИВЕТ, Я РОБОТ DayKitStart`а'):
    await ctx.send(arg)
    await ctx.message.delete()

#поле для токена бота
#bot.run(config.TOKEN)

token = os.environ.get("BOT_TOKEN")     
bot.run(str(token))
