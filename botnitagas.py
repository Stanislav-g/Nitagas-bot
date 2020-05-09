import discord
from discord.ext import commands
import datetime
from discord.utils import get
import asyncio
from time import sleep
from colorsys import hls_to_rgb
import youtube_dl
import os
import random
from random import randint, choice, choices
import io
import sqlite3
import random as r
import io





client = commands.Bot( command_prefix = '-')
client.remove_command('help')
@client.event

async def on_redy():
    print( 'Bot connected')
    await client.change_presence( status = discord.Status.online, activity = discord.Game( '-help' ) )
    await ctx.send( f'Hello' )







#hello
@client.command( pass_context = True )

async def hello( ctx ):
    author = ctx.message.author
    
    await ctx.send( f' { author.mention } Hello' )

#info
@client.command( pass_context = True )

async def info( ctx ):
    emb = discord.Embed( title = 'HELP', colour = discord.Color.red() )
    emb.add_field( name = 'Commands',value = 'Welcome to our server, it is designed for communication, sharing memes and also supports the themes of games, youtube and everything related to it. There are currently six bots on our server, and the commands for them are listed below.                                                                                           :arrow_right:pls help:arrow_left: :arrow_right:_help:arrow_left::arrow_right:.help:arrow_left:                                                      :arrow_right:/help:arrow_left::arrow_right:!help:arrow_left:')
    await ctx.send( embed = emb )


#help
@client.command( pass_context = True )

async def help( ctx ):
    emb = discord.Embed( title = 'HELP', colour = discord.Color.red() )
    emb.add_field( name = 'Commands',value = ' info- Информация\nserverinfo- информация о сервере\nbotinfo- информация о боте\nuserinfo- информация о пользователе\nhello- Приветствие \navatar- фото профиля\ncovid\ntime- Время\n j- Добавить бота в голосовой канал\n l- Удалить бота из голового канала\nnum- рандомное число от 1-101\n \n Games\n\nугадайка- угадай число от 1 до 20\n sapper- сапер\nknb- камень, ножницы, бумага\nrps- камень, ножницы, бумага с ботом\ncoinflip- орел или решка?\n\n\nTEXT\n \nsend_m- отправить сообщение другому участнику через бота\nping\nmath- калькулятор\nslap- ударить рандомного участника\nunion- узнать ник\n slapperson- ударить определенного игрока\nroles- узнать роли игрока\nadd- суммировать числа\nwordnum- количество слов в тексте\ntext2- ???\nytn- рандомное видео с канала Nitagas\nyt,yt2,yt3...yt7- видео с канала nitagas\nemoji_random- рандомное эмоджи\nsearch- поиск\nyoutube_search- поиск в youtube\nwiki- поиск в википедия\nyandex- поиск в яндекс\ngoogle- поиск в гугл\nkill\n \n ')
    await ctx.send( embed = emb )

#help
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def helpadmin( ctx ):
    await ctx.channel.purge( limit = 1 )
    emb = discord.Embed( title = 'HELP', colour = discord.Color.red() )
    emb.add_field( name = 'Commands',value = ' info- Информация\n\n Для админов \n \n text- писать от бота\nclear\n ban\n unban\n kick\nrainbow\n youtube- видео с nitagas\n\nchanging_name- изменить ник\nevent_roles- розогрыш ролей\ntempban s m h d\ntmute- voice mute\ntemp_add_role +time @ role\nadd_role +@ +role\ntempmute +time @ arg\nchannel_create +name\nvoice_create +name\nemojie +id message + emoji\nsuggest +arg')
    await ctx.send( embed = emb )

token = os.environ.get('BOT_TOKEN')
client.run(token)


