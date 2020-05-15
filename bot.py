import discord
from discord import utils
from discord.ext import commands
from discord.ext.commands import has_permissions
import config
import time
from discord.utils import get
import os

bot=commands.Bot(command_prefix=config.prefix)

@bot.event
async def on_ready():
    print("В сети")

@bot.event
async def on_message(message):
    channel=bot.get_channel(config.messagelog_channel)
    text = str(message.content)
    authormes=str(message.author.name)
    if message.author.bot==False:
        if message.channel.id != config.messagelog_channel:
            await channel.send(message.channel.name+": "+authormes+": "+text)
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    role = utils.get(member.guild.roles, id=config.join_role)
    await member.add_roles(role)
    channel=bot.get_channel(config.welcome_channel)
    await channel.send("Приветствуем "+member.name+" на нашем сервере")

@bot.command()
@has_permissions(manage_messages=True)
async def сказать(ctx, *,text):
    await ctx.message.delete()
    await ctx.send(text)

@bot.command(pass_context=True)
@has_permissions(manage_messages=True)
async def очистить(ctx, amount=1000):
    cleared=await ctx.channel.purge(limit=amount)
    cleared_count=str(len(cleared))
    message_bot=await ctx.send("Удалено "+cleared_count+" сообщений")
    channel_delete=message_bot.channel.id
    time.sleep(4)
    await bot.http.delete_message(channel_delete, message_bot.id)

@bot.command()
@has_permissions(administrator=True)
async def мут(ctx, member: discord.Member,*,reason='Нарушение правил сервера'):
    if member.bot == False:
        role = utils.get(member.guild.roles,id=config.muted_role)
        if member.nick != None:
            membermuted = str(member.nick)
        else:
            membermuted = str(member.name)
        await member.add_roles(role)
        await ctx.send("Участник "+membermuted+" был замучен по причине "+reason)
        log_channel = bot.get_channel(config.log_channel)
        await log_channel.send("Пользователь " + membermuted + "(" + str(member.id) + ") " + " замучен по причине " + reason)

@bot.command()
@has_permissions(administrator=True)
async def размут(ctx, member: discord.Member,*,reason=''):
    if member.bot == False:
        role = utils.get(member.guild.roles,id=config.muted_role)
        if member.nick != None:
            memberunmuted = str(member.nick)
        else:
            memberunmuted = str(member.name)

        if reason=='':
            await ctx.send("Укажите причину")
            return
        await ctx.send("Участник "+memberunmuted+" был размучен по причине "+reason)
        await member.remove_roles(role)
        log_channel = bot.get_channel(config.log_channel)
        await log_channel.send("Пользователь " + memberunmuted + "(" + str(member.id) + ") " + " размучен по причине " + reason)

@bot.command()
@has_permissions(administrator=True)
async def спам(ctx, key, amount: int, *,text: str):
    if key == '1':
        for i in range(0, amount):
            await ctx.send(text)

@bot.command()
@has_permissions(ban_members=True)
async def бан(ctx, member: discord.Member, *, reason=''):
    if member.bot==False:
        if reason == '':
            await ctx.send("Укажите причину бана")
            return
        if member.nick != None:
            banned_member=str(member.nick)
        else:
            banned_member=str(member.name)
        log_channel = bot.get_channel(config.log_channel)
        await ctx.guild.ban(member, reason=reason)
        await ctx.send(banned_member+" был забанен за "+reason)
        await log_channel.send("Пользователь " + banned_member + "(" + str(member.id) + ") " + " забанен по причине " + reason)
        await member.send("Вы были забанены на нашем сервере по причине " + reason)



@bot.command()
@has_permissions(kick_members=True)
async def кик(ctx, member: discord.Member, *,reason=''):
    if member.bot == False:
        if reason == '':
            await ctx.send("Укажите причину кика")
            return
        if member.nick != None:
            kicked_member = str(member.nick)
        else:
            kicked_member = str(member.name)
        await ctx.guild.kick(member, reason=reason)
        await ctx.send(kicked_member+" был кикнут с сервера за "+reason)
        log_channel = bot.get_channel(config.log_channel)
        await log_channel.send("Пользователь " + kicked_member + "(" + str(member.id) + ") " + " кикнут по причине " + reason)
        await member.send("Вы были кикнуты с нашего сервера по причине " + reason)

@bot.command()
async def писатьвлс(ctx, member: discord.Member, *, text):
    await member.send("С вами хочет связаться "+str(ctx.message.author)+". Текст: "+str(text))

@bot.command()
async def связаться(ctx, *, text):
    channel=bot.get_channel(config.message_from_users_channel)
    await channel.send("Обращение от "+str(ctx.message.author)+": "+text)

@bot.command()
@has_permissions(manage_roles=True)
async def выдатьроль(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(str(member.name)+" выдана роль "+str(role.name))

@bot.command()
@has_permissions(manage_roles=True)
async def снятьроль(ctx, member: discord.Member, role: discord.Role):
    await member.remove_roles(role)
    await ctx.send("С участника "+str(member.name)+" снята роль "+str(role.name))

OPERATIONS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

@bot.command()
async def калк(ctx, a, operator, b):
    await ctx.send("Ответ: " + str(OPERATIONS[operator](int(a), int(b))))

#командо помощь
@bot.command()
async def помощь(ctx):#команда
    await ctx.send(config.o1) #текст который выведеться

#команда /прав2
@bot.command()
async def прав2(ctx):#команда
    await ctx.send(config.p2) #текст который выведеться

#команда/прав1
@bot.command()
async def прав1(ctx):#команда
    await ctx.send(config.p1) #текст который выведеться


#команда /прав
@bot.command()
async def правила(ctx):#команда
    await ctx.send(config.PRAV1) #текст который выведеться


#bot.run("")
token = os.environ.get("BOT_TOKEN")     
bot.run(str(token))
