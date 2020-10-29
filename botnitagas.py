import discord
from discord.ext import commands
import datetime
from discord.utils import get
import asyncio
from time import sleep
from colorsys import hls_to_rgb
import youtube_dl
import os
import requests
import random
from random import randint, choice, choices
import io
import sqlite3
import random as r
import requests
import io
import typing
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
client = commands.Bot( command_prefix = '-')
client.remove_command('help')

	     				
@client.event
async def on_redy():
    print( 'Bot connected')

@client.command()
@commands.has_permissions( administrator = True )
async def web(ctx, arg, urll, * , text):
    await ctx.channel.purge( limit = 1 )
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url('https://discordapp.com/api/webhooks/753667884399722527/JOjqOcGEDPPLCxTwswJLpqEKf7u6onIZ0IFb0qsYoXPeBJ1eCZ2V58liVyRMfSIuqPGH', adapter=AsyncWebhookAdapter(session))
        emb = discord.Embed( title = arg, description = f"**{text}**\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", colour = discord.Colour.red(), url = urll, timestamp=ctx.message.created_at)
        await webhook.send(embed=emb)  

	
@client.command()
async def country(ctx):      

    randomflag2 = random.choice(['🏳️‍🌈','🇺🇳','🇦🇫','🇦🇱','🇩🇪','🇦🇩','🇦🇴 ',' 🇦🇮 ',' 🇦🇶 ',' 🇦🇬 ',' 🇸🇦 ',' 🇩🇿 ',' 🇦🇷 ',' 🇦🇲 ',' 🇦🇼 ',' 🇦🇺 ',' 🇦🇹 ',' 🇦🇿 ',' 🇧🇸 ',' 🇧🇩 ',' 🇧🇧 ',' 🇧🇭 ',' 🇧🇪 ',' 🇧🇿 ',' 🇧🇯 ',' 🇧🇲 ',' 🇧🇾 ',' 🇧🇴 ',' 🇧🇦 ',' 🇧🇼 ',' 🇧🇷 ',' 🇧🇳 ',' 🇧🇬 ',' 🇧🇫 ',' 🇧🇮 ',' 🇧🇹 ',' 🇨🇻 ',' 🇰🇭 ',' 🇨🇲 ',' 🇨🇦 ',' 🇮🇨 ',' 🇧🇶 ',' 🇶🇦 ',' 🇹🇩 ',' 🇨🇿 ',' 🇨🇱 ',' 🇨🇳 ',' 🇨🇾 ',' 🇻🇦 ',' 🇨🇴 ',' 🇰🇲 ',' 🇨🇬 ',' 🇰🇵 ',' 🇰🇷 ',' 🇨🇷 ',' 🇨🇮 ',' 🇭🇷 ',' 🇨🇺 ',' 🇨🇼 ',' 🇩🇰 ',' 🇩🇲 ',' 🇪🇨 ',' 🇪🇬 ',' 🇸🇻 ',' 🇦🇪 ',' 🇪🇷 ',' 🇸🇰 ',' 🇸🇮 ',' 🇪🇸 ',' 🇺🇸 ',' 🇪🇪 ',' 🇸🇿 ',' 🇪🇹 ',' 🇵🇭 ',' 🇫🇮 ',' 🇫🇯 ',' 🇫🇷 ',' 🇬🇦 ',' 🇬🇲 ',' 🇬🇪 ',' 🇬🇭 ',' 🇬🇮 ',' 🇬🇩 ',' 🇬🇷 ',' 🇬🇱 ',' 🇬🇵 ',' 🇬🇺 ',' 🇬🇹 ',' 🇬🇫 ',' 🇬🇬 ',' 🇬🇳 ',' 🇬🇶 ',' 🇬🇼 ',' 🇬🇾 ',' 🇭🇹 ',' 🇭🇳 ',' 🇭🇰 ',' 🇭🇺 ',' 🇮🇳 ',' 🇮🇩 ',' 🇮🇶 ',' 🇮🇷 ',' 🇮🇪 ',' 🇮🇲 ',' 🇨🇽 ',' 🇳🇫 ',' 🇮🇸 ',' 🇦🇽 ',' 🇰🇾 ',' 🇨🇨 ',' 🇨🇰 ',' 🇫🇴 ',' 🇬🇸 ',' 🇫🇰 ',' 🇲🇵 ',' 🇲🇭 ',' 🇵🇳 ',' 🇸🇧 ',' 🇹🇨 ',' 🇻🇬 ',' 🇻🇮 ',' 🇮🇱 ',' 🇮🇹 ',' 🇯🇲 ',' 🇯🇵 ',' 🇯🇪 ',' 🇯🇴 ',' 🇰🇿 ',' 🇰🇪 ',' 🇰🇬 ',' 🇰🇮 ',' 🇽🇰 ',' 🇰🇼 ',' 🇱🇦 ',' 🇱🇸 ',' 🇱🇻 ',' 🇱🇧 ',' 🇱🇷 ',' 🇱🇾 ',' 🇱🇮 ',' 🇱🇹 ',' 🇱🇺 ',' 🇲🇴 ',' 🇲🇰 ',' 🇲🇬 ',' 🇲🇾 ',' 🇲🇼 ',' 🇲🇻 ',' 🇲🇱 ',' 🇲🇹 ',' 🇲🇦 ',' 🇲🇶 ',' 🇲🇺 ',' 🇲🇷 ',' 🇾🇹 ',' 🇲🇽 ',' 🇫🇲 ',' 🇲🇩 ',' 🇲🇨 ',' 🇲🇳 ',' 🇲🇪 ',' 🇲🇸 ',' 🇲🇿 ',' 🇲🇲 ',' 🇳🇦 ',' 🇳🇷 ',' 🇳🇵 ',' 🇳🇮 ',' 🇳🇪 ',' 🇳🇬 ',' 🇳🇺 ',' 🇳🇴 ',' 🇳🇨 ',' 🇳🇿 ',' 🇴🇲 ',' 🇳🇱 ',' 🇵🇰 ',' 🇵🇼 ',' 🇵🇦 ',' 🇵🇬 ',' 🇵🇾 ',' 🇵🇪 ',' 🇵🇫 ',' 🇵🇱 ',' 🇵🇹 ',' 🇵🇷 ',' 🇬🇧 ',' 🏴󠁧󠁢󠁥󠁮󠁧󠁿 ',' 🏴󠁧󠁢󠁳󠁣󠁴󠁿 ',' 🏴󠁧󠁢󠁷󠁬󠁳󠁿 ',' 🇨🇫 ',' 🇨🇩 ',' 🇩🇴 ',' 🇷🇪 ',' 🇷🇼 ',' 🇷🇴 ',' 🇷🇺 ',' 🇪🇭 ',' 🇼🇸 ',' 🇦🇸 ',' 🇧🇱 ',' 🇰🇳 ',' 🇸🇲 ',' 🇵🇲 ',' 🇻🇨 ',' 🇸🇭 ',' 🇱🇨 ',' 🇸🇹 ',' 🇸🇳 ',' 🇷🇸 ',' 🇸🇨 ',' 🇸🇱 ',' 🇸🇬 ',' 🇸🇽 ',' 🇸🇾 ',' 🇸🇴 ',' 🇱🇰 ',' 🇿🇦 ',' 🇸🇩 ',' 🇸🇸 ',' 🇸🇪 ',' 🇨🇭 ',' 🇸🇷 ',' 🇹🇭 ',' 🇹🇼 ',' 🇹🇿 ',' 🇹🇯 ',' 🇮🇴 ',' 🇹🇫 ',' 🇵🇸 ',' 🇹🇱 ',' 🇹🇬 ',' 🇹🇰 ',' 🇹🇴 ',' 🇹🇹 ',' 🇹🇳 ',' 🇹🇲 ',' 🇹🇷 ',' 🇹🇻 ',' 🇺🇦 ',' 🇺🇬 ',' 🇺🇾 ',' 🇺🇿 ',' 🇻🇺 ',' 🇻🇪 ',' 🇻🇳 ',' 🇼🇫 ',' 🇾🇪 ',' 🇩🇯 ',' 🇿🇲 ',' 🇿🇼'

])
    randomflag3 = random.choice(['🏳️‍🌈','🇺🇳','🇦🇫','🇦🇱','🇩🇪','🇦🇩','🇦🇴 ',' 🇦🇮 ',' 🇦🇶 ',' 🇦🇬 ',' 🇸🇦 ',' 🇩🇿 ',' 🇦🇷 ',' 🇦🇲 ',' 🇦🇼 ',' 🇦🇺 ',' 🇦🇹 ',' 🇦🇿 ',' 🇧🇸 ',' 🇧🇩 ',' 🇧🇧 ',' 🇧🇭 ',' 🇧🇪 ',' 🇧🇿 ',' 🇧🇯 ',' 🇧🇲 ',' 🇧🇾 ',' 🇧🇴 ',' 🇧🇦 ',' 🇧🇼 ',' 🇧🇷 ',' 🇧🇳 ',' 🇧🇬 ',' 🇧🇫 ',' 🇧🇮 ',' 🇧🇹 ',' 🇨🇻 ',' 🇰🇭 ',' 🇨🇲 ',' 🇨🇦 ',' 🇮🇨 ',' 🇧🇶 ',' 🇶🇦 ',' 🇹ð© ',' 🇨🇿 ',' 🇨🇱 ',' 🇨🇳 ',' 🇨🇾 ',' 🇻🇦 ',' 🇨🇴 ',' 🇰🇲 ',' 🇨🇬 ',' 🇰🇵 ',' 🇰🇷 ',' 🇨🇷 ',' 🇨🇮 ',' 🇭🇷 ',' 🇨🇺 ',' 🇨🇼 ',' 🇩🇰 ',' 🇩🇲 ',' 🇪🇨 ',' 🇪🇬 ',' 🇸🇻 ',' 🇦🇪 ',' 🇪🇷 ',' 🇸🇰 ',' 🇸🇮 ',' 🇪🇸 ',' 🇺🇸 ',' 🇪🇪 ',' 🇸🇿 ',' 🇪🇹 ',' 🇵🇭 ',' 🇫🇮 ',' 🇫🇯 ',' 🇫🇷 ',' 🇬🇦 ',' 🇬🇲 ',' 🇬🇪 ',' 🇬🇭 ',' 🇬🇮 ',' 🇬🇩 ',' 🇬🇷 ',' 🇬🇱 ',' 🇬🇵 ',' 🇬🇺 ',' 🇬🇹 ',' 🇬🇫 ',' 🇬🇬 ',' 🇬🇳 ',' 🇬🇶 ',' 🇬🇼 ',' 🇬🇾 ',' 🇭🇹 ',' 🇭🇳 ',' 🇭🇰 ',' 🇭🇺 ',' 🇮🇳 ',' 🇮🇩 ',' 🇮🇶 ',' 🇮🇷 ',' 🇮🇪 ',' 🇮🇲 ',' 🇨🇽 ',' 🇳🇫 ',' 🇮🇸 ',' 🇦🇽 ',' 🇰🇾 ',' 🇨🇨 ',' 🇨🇰 ',' 🇫🇴 ',' 🇬🇸 ',' 🇫🇰 ',' 🇲🇵 ',' 🇲🇭 ',' 🇵🇳 ',' 🇸🇧 ',' 🇹🇨 ',' 🇻🇬 ',' 🇻🇮 ',' 🇮🇱 ',' 🇮🇹 ',' 🇯🇲 ',' 🇯🇵 ',' 🇯🇪 ',' 🇯🇴 ',' 🇰🇿 ',' 🇰🇪 ',' 🇰🇬 ',' 🇰🇮 ',' 🇽🇰 ',' 🇰🇼 ',' 🇱🇦 ',' 🇱🇸 ',' 🇱🇻 ',' 🇱🇧 ',' 🇱🇷 ',' 🇱🇾 ',' 🇱🇮 ',' 🇱🇹 ',' 🇱🇺 ',' 🇲🇴 ',' 🇲🇰 ',' 🇲🇬 ',' 🇲🇾 ',' 🇲🇼 ',' 🇲🇻 ',' 🇲🇱 ',' 🇲🇹 ',' 🇲🇦 ',' 🇲🇶 ',' 🇲🇺 ',' 🇲🇷 ',' 🇾🇹 ',' 🇲🇽 ',' 🇫🇲 ',' 🇲🇩 ',' 🇲🇨 ',' 🇲🇳 ',' 🇲🇪 ',' 🇲🇸 ',' 🇲🇿 ',' 🇲🇲 ',' 🇳🇦 ',' 🇳🇷 ',' 🇳🇵 ',' 🇳🇮 ',' 🇳🇪 ',' 🇳🇬 ',' 🇳🇺 ',' 🇳🇴 ',' 🇳🇨 ',' 🇳🇿 ',' 🇴🇲 ',' 🇳🇱 ',' 🇵🇰 ',' 🇵🇼 ',' 🇵🇦 ',' 🇵🇬 ',' 🇵🇾 ',' 🇵🇪 ',' 🇵🇫 ',' 🇵🇱 ',' 🇵🇹 ',' 🇵🇷 ',' 🇬🇧 ',' 🏴󠁧󠁢󠁥󠁮󠁧󠁿 ',' 🏴󠁧󠁢󠁳󠁣󠁴󠁿 ',' 🏴󠁧󠁢󠁷󠁬󠁳󠁿 ',' 🇨🇫 ',' 🇨🇩 ',' 🇩🇴 ',' 🇷🇪 ',' 🇷🇼 ',' 🇷🇴 ',' 🇷🇺 ',' 🇪🇭 ',' 🇼🇸 ',' 🇦🇸 ',' 🇧🇱 ',' 🇰🇳 ',' 🇸🇲 ',' 🇵🇲 ',' 🇻🇨 ',' 🇸🇭 ',' 🇱🇨 ',' 🇸🇹 ',' 🇸🇳 ',' 🇷🇸 ',' 🇸🇨 ',' 🇸🇱 ',' 🇸🇬 ',' 🇸🇽 ',' 🇸🇾 ',' 🇸🇴 ',' 🇱🇰 ',' 🇿🇦 ',' 🇸🇩 ',' 🇸🇸 ',' 🇸🇪 ',' 🇨🇭 ',' 🇸🇷 ',' 🇹🇭 ',' 🇹🇼 ',' 🇹🇿 ',' 🇹🇯 ',' 🇮🇴 ',' 🇹🇫 ',' 🇵🇸 ',' 🇹🇱 ',' 🇹🇬 ',' 🇹🇰 ',' 🇹🇴 ',' 🇹🇹 ',' 🇹🇳 ',' 🇹🇲 ',' 🇹🇷 ',' 🇹🇻 ',' 🇺🇦 ',' 🇺🇬 ',' 🇺🇾 ',' 🇺🇿 ',' 🇻🇺 ',' 🇻🇪 ',' 🇻🇳 ',' 🇼🇫 ',' 🇾🇪 ',' 🇩🇯 ',' 🇿🇲 ',' 🇿🇼'

])
    randomflag = random.choice(['🏳️‍🌈','🇺🇳','🇦🇫','🇦🇱','🇩🇪','🇦🇩','🇦🇴 ',' 🇦🇮 ',' 🇦🇶 ',' 🇦🇬 ',' 🇸🇦 ',' 🇩🇿 ',' 🇦🇷 ',' 🇦🇲 ',' 🇦🇼 ',' 🇦🇺 ',' 🇦🇹 ',' 🇦🇿 ',' 🇧🇸 ',' 🇧🇩 ',' 🇧🇧 ',' 🇧🇭 ',' 🇧🇪 ',' 🇧🇿 ',' 🇧🇯 ',' 🇧🇲 ',' 🇧🇾 ',' 🇧🇴 ',' 🇧🇦 ',' 🇧🇼 ',' 🇧🇷 ',' 🇧🇳 ',' 🇧🇬 ',' 🇧🇫 ',' 🇧🇮 ',' 🇧🇹 ',' 🇨🇻 ',' 🇰🇭 ',' 🇨🇲 ',' 🇨🇦 ',' 🇮🇨 ',' 🇧🇶 ',' 🇶🇦 ',' 🇹🇩 ',' 🇨🇿 ',' 🇨🇱 ',' 🇨🇳 ',' 🇨🇾 ',' 🇻🇦 ',' 🇨🇴 ',' 🇰🇲 ',' 🇨🇬 ',' 🇰🇵 ',' 🇰🇷 ',' 🇨🇷 ',' 🇨🇮 ',' 🇭🇷 ',' 🇨🇺 ',' 🇨🇼 ',' 🇩🇰 ',' 🇩🇲 ',' 🇪🇨 ',' 🇪🇬 ',' 🇸🇻 ',' 🇦🇪 ',' 🇪🇷 ',' 🇸🇰 ',' 🇸🇮 ',' 🇪🇸 ',' 🇺🇸 ',' 🇪🇪 ',' 🇸🇿 ',' 🇪🇹 ',' 🇵🇭 ',' 🇫🇮 ',' 🇫🇯 ',' 🇫🇷 ',' 🇬🇦 ',' 🇬🇲 ',' 🇬🇪 ',' 🇬🇭 ',' 🇬🇮 ',' 🇬🇩 ',' 🇬🇷 ',' 🇬🇱 ',' 🇬🇵 ',' 🇬🇺 ',' 🇬🇹 ',' 🇬🇫 ',' 🇬🇬 ',' 🇬🇳 ',' 🇬🇶 ',' 🇬🇼 ',' 🇬🇾 ',' 🇭🇹 ',' 🇭🇳 ',' 🇭🇰 ',' 🇭🇺 ',' 🇮🇳 ',' 🇮🇩 ',' 🇮🇶 ',' 🇮🇷 ',' 🇮🇪 ',' 🇮🇲 ',' 🇨🇽 ',' 🇳🇫 ',' 🇮🇸 ',' 🇦🇽 ',' 🇰🇾 ',' 🇨🇨 ',' 🇨🇰 ',' 🇫🇴 ',' 🇬🇸 ',' 🇫🇰 ',' 🇲🇵 ',' 🇲🇭 ',' 🇵🇳 ',' 🇸🇧 ',' 🇹🇨 ',' 🇻🇬 ',' 🇻🇮 ',' 🇮🇱 ',' 🇮🇹 ',' 🇯🇲 ',' 🇯🇵 ',' 🇯🇪 ',' 🇯🇴 ',' 🇰🇿 ',' 🇰🇪 ',' 🇰🇬 ',' 🇰🇮 ',' 🇽🇰 ',' 🇰🇼 ',' 🇱🇦 ',' 🇱🇸 ',' 🇱🇻 ',' 🇱🇧 ',' 🇱🇷 ',' 🇱🇾 ',' 🇱🇮 ',' 🇱🇹 ',' 🇱🇺 ',' 🇲🇴 ',' 🇲🇰 ',' 🇲🇬 ',' 🇲🇾 ',' 🇲🇼 ',' 🇲🇻 ',' 🇲🇱 ',' 🇲🇹 ',' 🇲🇦 ',' 🇲🇶 ',' 🇲🇺 ',' 🇲🇷 ',' 🇾🇹 ',' 🇲🇽 ',' 🇫🇲 ',' 🇲🇩 ',' 🇲🇨 ',' 🇲🇳 ',' 🇲🇪 ',' 🇲🇸 ',' 🇲🇿 ',' 🇲🇲 ',' 🇳🇦 ',' 🇳🇷 ',' 🇳🇵 ',' 🇳🇮 ',' 🇳🇪 ',' 🇳🇬 ',' 🇳🇺 ',' 🇳🇴 ',' 🇳🇨 ',' 🇳🇿 ',' 🇴🇲 ',' 🇳🇱 ',' 🇵🇰 ',' 🇵🇼 ',' 🇵🇦 ',' 🇵🇬 ',' 🇵🇾 ',' 🇵🇪 ',' 🇵🇫 ',' 🇵🇱 ',' 🇵🇹 ',' 🇵🇷 ',' 🇬🇧 ',' 🏴󠁧󠁢󠁥󠁮󠁧󠁿 ',' 🏴󠁧󠁢󠁳󠁣󠁴󠁿 ',' 🏴󠁧󠁢󠁷󠁬󠁳󠁿 ',' 🇨🇫 ',' 🇨🇩 ',' 🇩🇴 ',' 🇷🇪 ',' 🇷🇼 ',' 🇷🇴 ',' 🇷🇺 ',' 🇪🇭 ',' 🇼🇸 ',' 🇦🇸 ',' 🇧🇱 ',' 🇰🇳 ',' 🇸🇲 ',' 🇵🇲 ',' 🇻🇨 ',' 🇸🇭 ',' 🇱🇨 ',' 🇸🇹 ',' 🇸🇳 ',' 🇷🇸 ',' 🇸🇨 ',' 🇸🇱 ',' 🇸🇬 ',' 🇸🇽 ',' 🇸🇾 ',' 🇸🇴 ',' 🇱🇰 ',' 🇿🇦 ',' 🇸🇩 ',' 🇸🇸 ',' 🇸🇪 ',' 🇨🇭 ',' 🇸🇷 ',' 🇹🇭 ',' 🇹🇼 ',' 🇹🇿 ',' 🇹🇯 ',' 🇮🇴 ',' 🇹🇫 ',' 🇵🇸 ',' 🇹🇱 ',' 🇹🇬 ',' 🇹🇰 ',' 🇹🇴 ',' 🇹🇹 ',' 🇹🇳 ',' 🇹🇲 ',' 🇹🇷 ',' 🇹🇻 ',' 🇺🇦 ',' 🇺🇬 ',' 🇺🇾 ',' 🇺🇿 ',' 🇻🇺 ',' 🇻🇪 ',' 🇻🇳 ',' 🇼🇫 ',' 🇾🇪 ',' 🇩🇯 ',' 🇿🇲 ',' 🇿🇼'

])
    num = random.randint(1,80)
    while randomflag == randomflag2 or randomflag == randomflag3 or randomflag3 == randomflag2 or randomflag3 == randomflag or randomflag2 == randomflag3 or randomflag2 == randomflag:
        randomflag2 = random.choice(['🏳️‍🌈','🇺🇳','🇦🇫','🇦🇱','🇩🇪','🇦🇩','🇦🇴 ',' 🇦🇮 ',' 🇦🇶 ',' 🇦🇬 ',' 🇸🇦 ',' 🇩🇿 ',' 🇦🇷 ',' 🇦🇲 ',' 🇦🇼 ',' 🇦🇺 ',' 🇦🇹 ',' 🇦🇿 ',' 🇧🇸 ',' 🇧🇩 ',' 🇧🇧 ',' 🇧🇭 ',' 🇧🇪 ',' 🇧🇿 ',' 🇧🇯 ',' 🇧🇲 ',' 🇧🇾 ',' 🇧🇴 ',' 🇧🇦 ',' 🇧🇼 ',' 🇧🇷 ',' 🇧🇳 ',' 🇧🇬 ',' 🇧🇫 ',' 🇧🇮 ',' 🇧🇹 ',' 🇨🇻 ',' 🇰🇭 ',' 🇨🇲 ',' 🇨🇦 ',' 🇮🇨 ',' 🇧🇶 ',' 🇶🇦 ',' 🇹🇩 ',' 🇨🇿 ',' 🇨🇱 ',' 🇨🇳 ',' 🇨🇾 ',' 🇻🇦 ',' 🇨🇴 ',' 🇰🇲 ',' 🇨🇬 ',' 🇰🇵 ',' 🇰🇷 ',' 🇨🇷 ',' 🇨🇮 ',' 🇭🇷 ',' 🇨🇺 ',' 🇨🇼 ',' 🇩🇰 ',' 🇩🇲 ',' 🇪🇨 ',' 🇪🇬 ',' 🇸🇻 ',' 🇦🇪 ',' 🇪🇷 ',' 🇸🇰 ',' 🇸🇮 ',' 🇪🇸 ',' 🇺🇸 ',' 🇪🇪 ',' 🇸🇿 ',' 🇪🇹 ',' 🇵🇭 ',' 🇫🇮 ',' 🇫🇯 ',' 🇫🇷 ',' 🇬🇦 ',' 🇬🇲 ',' 🇬🇪 ',' 🇬🇭 ',' 🇬🇮 ',' 🇬🇩 ',' 🇬🇷 ',' 🇬🇱 ',' 🇬🇵 ',' 🇬🇺 ',' 🇬🇹 ',' 🇬🇫 ',' 🇬🇬 ',' 🇬🇳 ',' 🇬🇶 ',' 🇬🇼 ',' 🇬🇾 ',' 🇭🇹 ',' 🇭🇳 ',' 🇭🇰 ',' 🇭🇺 ',' 🇮🇳 ',' 🇮🇩 ',' 🇮🇶 ',' 🇮🇷 ',' 🇮🇪 ',' 🇮🇲 ',' 🇨🇽 ',' 🇳🇫 ',' 🇮🇸 ',' 🇦🇽 ',' 🇰🇾 ',' 🇨🇨 ',' 🇨🇰 ',' 🇫🇴 ',' 🇬🇸 ',' 🇫🇰 ',' 🇲🇵 ',' 🇲🇭 ',' 🇵🇳 ',' 🇸🇧 ',' 🇹🇨 ',' 🇻🇬 ',' 🇻🇮 ',' 🇮🇱 ',' 🇮🇹 ',' 🇯🇲 ',' 🇯🇵 ',' 🇯🇪 ',' 🇯🇴 ',' 🇰🇿 ',' 🇰🇪 ',' 🇰🇬 ',' 🇰🇮 ',' 🇽🇰 ',' 🇰🇼 ',' 🇱🇦 ',' 🇱🇸 ',' 🇱🇻 ',' 🇱🇧 ',' 🇱🇷 ',' 🇱🇾 ',' 🇱🇮 ',' 🇱🇹 ',' 🇱🇺 ',' 🇲🇴 ',' 🇲🇰 ',' 🇲🇬 ',' 🇲🇾 ',' 🇲🇼 ',' 🇲🇻 ',' 🇲🇱 ',' 🇲🇹 ',' 🇲🇦 ',' 🇲🇶 ',' 🇲🇺 ',' 🇲🇷 ',' 🇾🇹 ',' 🇲🇽 ',' 🇫🇲 ',' 🇲🇩 ',' 🇲🇨 ',' 🇲🇳 ',' 🇲🇪 ',' 🇲🇸 ',' 🇲🇿 ',' 🇲🇲 ',' 🇳🇦 ',' 🇳🇷 ',' 🇳🇵 ',' 🇳🇮 ',' 🇳🇪 ',' 🇳🇬 ',' 🇳🇺 ',' 🇳🇴 ',' 🇳🇨 ',' 🇳🇿 ',' 🇴🇲 ',' 🇳🇱 ',' 🇵🇰 ',' 🇵🇼 ',' 🇵🇦 ',' 🇵🇬 ',' 🇵🇾 ',' 🇵🇪 ',' 🇵🇫 ',' 🇵🇱 ',' 🇵🇹 ',' 🇵🇷 ',' 🇬🇧 ',' 🏴󠁧󠁢󠁥󠁮󠁧󠁿 ',' 🏴󠁧󠁢󠁳󠁣󠁴󠁿 ',' 🏴󠁧󠁢󠁷󠁬󠁳󠁿 ',' 🇨🇫 ',' 🇨🇩 ',' 🇩🇴 ',' 🇷🇪 ',' 🇷🇼 ',' 🇷🇴 ',' 🇷🇺 ',' 🇪🇭 ',' 🇼🇸 ',' 🇦🇸 ',' 🇧🇱 ',' 🇰🇳 ',' 🇸🇲 ',' 🇵🇲 ',' 🇻🇨 ',' 🇸🇭 ',' 🇱🇨 ',' 🇸🇹 ',' 🇸🇳 ',' 🇷🇸 ',' 🇸🇨 ',' 🇸🇱 ',' 🇸🇬 ',' 🇸🇽 ',' 🇸🇾 ',' 🇸🇴 ',' 🇱🇰 ',' 🇿🇦 ',' 🇸🇩 ',' 🇸🇸 ',' 🇸🇪 ',' 🇨🇭 ',' 🇸🇷 ',' 🇹🇭 ',' 🇹🇼 ',' 🇹🇿 ',' 🇹🇯 ',' 🇮🇴 ',' 🇹🇫 ',' 🇵🇸 ',' 🇹🇱 ',' 🇹🇬 ',' 🇹🇰 ',' 🇹🇴 ',' 🇹🇹 ',' 🇹🇳 ',' 🇹🇲 ',' 🇹🇷 ',' 🇹🇻 ',' 🇺🇦 ',' 🇺🇬 ',' 🇺🇾 ',' 🇺🇿 ',' 🇻🇺 ',' 🇻🇪 ',' 🇻🇳 ',' 🇼🇫 ',' 🇾🇪 ',' 🇩🇯 ',' 🇿🇲 ',' 🇿🇼'

])
        randomflag3 = random.choice(['🏳️‍🌈','🇺🇳','🇦🇫','🇦🇱','🇩🇪','🇦🇩','🇦🇴 ',' 🇦🇮 ',' 🇦🇶 ',' 🇦🇬 ',' 🇸🇦 ',' 🇩🇿 ',' 🇦🇷 ',' 🇦🇲 ',' 🇦🇼 ',' 🇦🇺 ',' 🇦🇹 ',' 🇦🇿 ',' 🇧🇸 ',' 🇧🇩 ',' 🇧🇧 ',' 🇧🇭 ',' 🇧🇪 ',' 🇧🇿 ',' 🇧🇯 ',' 🇧🇲 ',' 🇧🇾 ',' 🇧🇴 ',' 🇧🇦 ',' 🇧🇼 ',' 🇧🇷 ',' 🇧🇳 ',' 🇧🇬 ',' 🇧🇫 ',' 🇧🇮 ',' 🇧🇹 ',' 🇨🇻 ',' 🇰🇭 ',' 🇨🇲 ',' 🇨🇦 ',' 🇮🇨 ',' 🇧🇶 ',' 🇶🇦 ',' 🇹🇩 ',' 🇨🇿 ',' 🇨🇱 ',' 🇨🇳 ',' 🇨🇾 ',' 🇻🇦 ',' 🇨🇴 ',' 🇰🇲 ',' 🇨🇬 ',' 🇰🇵 ',' 🇰🇷 ',' 🇨🇷 ',' 🇨🇮 ',' 🇭🇷 ',' 🇨🇺 ',' 🇨🇼 ',' 🇩🇰 ',' 🇩🇲 ',' 🇪🇨 ',' 🇪🇬 ',' 🇸🇻 ',' 🇦🇪 ',' 🇪🇷 ',' 🇸🇰 ',' 🇸🇮 ',' 🇪🇸 ',' 🇺🇸 ',' 🇪🇪 ',' 🇸🇿 ',' 🇪🇹 ',' 🇵🇭 ',' 🇫🇮 ',' 🇫🇯 ',' 🇫🇷 ',' 🇬🇦 ',' 🇬🇲 ',' 🇬🇪 ',' 🇬🇭 ',' 🇬🇮 ',' 🇬🇩 ',' 🇬🇷 ',' 🇬🇱 ',' 🇬🇵 ',' 🇬🇺 ',' 🇬🇹 ',' 🇬🇫 ',' 🇬🇬 ',' 🇬🇳 ',' 🇬🇶 ',' 🇬🇼 ',' 🇬🇾 ',' 🇭🇹 ',' 🇭🇳 ',' 🇭🇰 ',' 🇭🇺 ',' 🇮🇳 ',' 🇮🇩 ',' 🇮🇶 ',' 🇮🇷 ',' 🇮🇪 ',' 🇮🇲 ',' 🇨🇽 ',' 🇳🇫 ',' 🇮🇸 ',' 🇦🇽 ',' 🇰🇾 ',' 🇨🇨 ',' 🇨🇰 ',' 🇫🇴 ',' 🇬🇸 ',' 🇫🇰 ',' 🇲🇵 ',' 🇲🇭 ',' 🇵🇳 ',' 🇸🇧 ',' 🇹🇨 ',' 🇻🇬 ',' 🇻🇮 ',' 🇮🇱 ',' 🇮🇹 ',' 🇯🇲 ',' 🇯🇵 ',' 🇯🇪 ',' 🇯🇴 ',' 🇰🇿 ',' 🇰🇪 ',' 🇰🇬 ',' 🇰🇮 ',' 🇽🇰 ',' 🇰🇼 ',' 🇱🇦 ',' 🇱🇸 ',' 🇱🇻 ',' 🇱🇧 ',' 🇱🇷 ',' 🇱🇾 ',' 🇱🇮 ',' 🇱🇹 ',' 🇱🇺 ',' 🇲🇴 ',' 🇲🇰 ',' 🇲🇬 ',' 🇲🇾 ',' 🇲🇼 ',' 🇲🇻 ',' 🇲🇱 ',' 🇲🇹 ',' 🇲🇦 ',' 🇲🇶 ',' 🇲🇺 ',' 🇲🇷 ',' 🇾🇹 ',' 🇲🇽 ',' 🇫🇲 ',' 🇲🇩 ',' 🇲🇨 ',' 🇲🇳 ',' 🇲🇪 ',' 🇲🇸 ',' 🇲🇿 ',' 🇲🇲 ',' 🇳🇦 ',' 🇳🇷 ',' 🇳🇵 ',' 🇳🇮 ',' 🇳🇪 ',' 🇳🇬 ',' 🇳🇺 ',' 🇳🇴 ',' 🇳🇨 ',' 🇳🇿 ',' 🇴🇲 ',' 🇳🇱 ',' 🇵🇰 ',' 🇵🇼 ',' 🇵🇦 ',' 🇵🇬 ',' 🇵🇾 ',' 🇵🇪 ',' 🇵🇫 ',' 🇵🇱 ',' 🇵🇹 ',' 🇵🇷 ',' 🇬🇧 ',' 🏴󠁧󠁢󠁥󠁮󠁧󠁿 ',' 🏴󠁧󠁢󠁳󠁣󠁴󠁿 ',' 🏴󠁧󠁢󠁷󠁬󠁳󠁿 ',' 🇨🇫 ',' 🇨🇩 ',' 🇩🇴 ',' 🇷🇪 ',' 🇷🇼 ',' 🇷🇴 ',' 🇷🇺 ',' 🇪🇭 ',' 🇼🇸 ',' 🇦🇸 ',' 🇧🇱 ',' 🇰🇳 ',' 🇸🇲 ',' 🇵🇲 ',' 🇻🇨 ',' 🇸🇭 ',' 🇱🇨 ',' 🇸🇹 ',' 🇸🇳 ',' 🇷🇸 ',' 🇸🇨 ',' 🇸🇱 ',' 🇸🇬 ',' 🇸🇽 ',' 🇸🇾 ',' 🇸🇴 ',' 🇱🇰 ',' 🇿🇦 ',' 🇸🇩 ',' 🇸🇸 ',' 🇸🇪 ',' 🇨🇭 ',' 🇸🇷 ',' 🇹🇭 ',' 🇹🇼 ',' 🇹🇿 ',' 🇹🇯 ',' 🇮🇴 ',' 🇹🇫 ',' 🇵🇸 ',' 🇹🇱 ',' 🇹🇬 ',' 🇹🇰 ',' 🇹🇴 ',' 🇹🇹 ',' 🇹🇳 ',' 🇹🇲 ',' 🇹🇷 ',' 🇹🇻 ',' 🇺🇦 ',' 🇺🇬 ',' 🇺🇾 ',' 🇺🇿 ',' 🇻🇺 ',' 🇻🇪 ',' 🇻🇳 ',' 🇼🇫 ',' 🇾🇪 ',' 🇩🇯 ',' 🇿🇲 ',' 🇿🇼'

])
        randomflag = random.choice(['🏳️‍🌈','🇺🇳','🇦🇫','🇦🇱','🇩🇪','🇦🇩','🇦🇴 ',' 🇦🇮 ',' 🇦🇶 ',' 🇦🇬 ',' 🇸🇦 ',' 🇩🇿 ',' 🇦🇷 ',' 🇦🇲 ',' 🇦🇼 ',' 🇦🇺 ',' 🇦🇹 ',' 🇦🇿 ',' 🇧🇸 ',' 🇧🇩 ',' 🇧🇧 ',' 🇧🇭 ',' 🇧🇪 ',' 🇧🇿 ',' 🇧🇯 ',' 🇧🇲 ',' 🇧🇾 ',' 🇧🇴 ',' 🇧🇦 ',' 🇧🇼 ',' 🇧🇷 ',' 🇧🇳 ',' 🇧🇬 ',' 🇧🇫 ',' 🇧🇮 ',' 🇧🇹 ',' 🇨🇻 ',' 🇰🇭 ',' 🇨🇲 ',' 🇨🇦 ',' 🇮🇨 ',' 🇧🇶 ',' 🇶🇦 ',' 🇹🇩 ',' 🇨🇿 ',' 🇨🇱 ',' 🇨🇳 ',' 🇨🇾 ',' 🇻🇦 ',' 🇨🇴 ',' 🇰🇲 ',' 🇨🇬 ',' 🇰🇵 ',' 🇰🇷 ',' 🇨🇷 ',' 🇨🇮 ',' 🇭🇷 ',' 🇨🇺 ',' 🇨🇼 ',' 🇩🇰 ',' 🇩🇲 ',' 🇪🇨 ',' 🇪🇬 ',' 🇸🇻 ',' 🇦🇪 ',' 🇪🇷 ',' 🇸🇰 ',' 🇸🇮 ',' 🇪🇸 ',' 🇺🇸 ',' 🇪🇪 ',' 🇸🇿 ',' 🇪🇹 ',' 🇵🇭 ',' 🇫🇮 ',' 🇫🇯 ',' 🇫🇷 ',' 🇬🇦 ',' 🇬🇲 ',' 🇬🇪 ',' 🇬🇭 ',' 🇬🇮 ',' 🇬🇩 ',' 🇬🇷 ',' 🇬🇱 ',' 🇬🇵 ',' 🇬🇺 ',' 🇬🇹 ',' 🇬🇫 ',' 🇬🇬 ',' 🇬🇳 ',' 🇬🇶 ',' 🇬🇼 ',' 🇬🇾 ',' 🇭🇹 ',' 🇭🇳 ',' 🇭🇰 ',' 🇭🇺 ',' 🇮🇳 ',' 🇮🇩 ',' 🇮🇶 ',' 🇮🇷 ',' 🇮🇪 ',' 🇮🇲 ',' 🇨🇽 ',' 🇳🇫 ',' 🇮🇸 ',' 🇦🇽 ',' 🇰🇾 ',' 🇨🇨 ',' 🇨🇰 ',' 🇫🇴 ',' 🇬🇸 ',' 🇫🇰 ',' 🇲🇵 ',' 🇲🇭 ',' 🇵🇳 ',' 🇸🇧 ',' 🇹🇨 ',' 🇻🇬 ',' 🇻🇮 ',' 🇮🇱 ',' 🇮🇹 ',' 🇯🇲 ',' 🇯🇵 ',' 🇯🇪 ',' 🇯🇴 ',' 🇰🇿 ',' 🇰🇪 ',' 🇰🇬 ',' 🇰🇮 ',' 🇽🇰 ',' 🇰🇼 ',' 🇱🇦 ',' 🇱🇸 ',' 🇱🇻 ',' 🇱🇧 ',' 🇱🇷 ',' 🇱🇾 ',' 🇱🇮 ',' 🇱🇹 ',' 🇱🇺 ',' 🇲🇴 ',' 🇲🇰 ',' 🇲🇬 ',' 🇲🇾 ',' 🇲🇼 ',' 🇲🇻 ',' 🇲🇱 ',' 🇲🇹 ',' 🇲🇦 ',' 🇲🇶 ',' 🇲🇺 ',' 🇲🇷 ',' 🇾🇹 ',' 🇲🇽 ',' 🇫🇲 ',' 🇲🇩 ',' 🇲🇨 ',' 🇲🇳 ',' 🇲🇪 ',' 🇲🇸 ',' 🇲🇿 ',' 🇲🇲 ',' 🇳🇦 ',' 🇳🇷 ',' 🇳🇵 ',' 🇳🇮 ',' 🇳🇪 ',' 🇳🇬 ',' 🇳🇺 ',' 🇳🇴 ',' 🇳🇨 ',' 🇳🇿 ',' 🇴🇲 ',' 🇳🇱 ',' 🇵🇰 ',' 🇵🇼 ',' 🇵🇦 ',' 🇵🇬 ',' 🇵🇾 ',' 🇵🇪 ',' 🇵🇫 ',' 🇵🇱 ',' 🇵🇹 ',' 🇵🇷 ',' 🇬🇧 ',' 🏴󠁧󠁢󠁥󠁮󠁧󠁿 ',' 🏴󠁧󠁢󠁳󠁣󠁴󠁿 ',' 🏴󠁧󠁢󠁷󠁬󠁳󠁿 ',' 🇨🇫 ',' 🇨🇩 ',' 🇩🇴 ',' 🇷🇪 ',' 🇷🇼 ',' 🇷🇴 ',' 🇷🇺 ',' 🇪🇭 ',' 🇼🇸 ',' 🇦🇸 ',' 🇧🇱 ',' 🇰🇳 ',' 🇸🇲 ',' 🇵🇲 ',' 🇻🇨 ',' 🇸🇭 ',' 🇱🇨 ',' 🇸🇹 ',' 🇸🇳 ',' 🇷🇸 ',' 🇸🇨 ',' 🇸🇱 ',' 🇸🇬 ',' 🇸🇽 ',' 🇸🇾 ',' 🇸🇴 ',' 🇱🇰 ',' 🇿🇦 ',' 🇸🇩 ',' 🇸🇸 ',' ð¸🇪 ',' 🇨🇭 ',' 🇸🇷 ',' 🇹🇭 ',' 🇹🇼 ',' 🇹🇿 ',' 🇹🇯 ',' 🇮🇴 ',' 🇹🇫 ',' 🇵🇸 ',' 🇹🇱 ',' 🇹🇬 ',' 🇹🇰 ',' 🇹🇴 ',' 🇹🇹 ',' 🇹🇳 ',' 🇹🇲 ',' 🇹🇷 ',' 🇹🇻 ',' 🇺🇦 ',' 🇺🇬 ',' 🇺🇾 ',' 🇺🇿 ',' 🇻🇺 ',' 🇻🇪 ',' 🇻🇳 ',' 🇼🇫 ',' 🇾🇪 ',' 🇩🇯 ',' 🇿🇲 ',' 🇿🇼'

])
    files = []
    for file in ctx.message.attachments:
        fp = io.BytesIO()
        await file.save(fp)
        if file in ctx.message.attachments:
            files.append(discord.File(fp, filename = file.filename, spoiler = file.is_spoiler()))
            await ctx.send(files = files)
            if num < 100:
                between = int(100 - num)
                num2 = random.randint(1,between)
                summa = (num + num2)
                    
                if summa <= 100:
                        
                    allnums = int(num + num2)
                    between_second = (100 - allnums)
                    num3 = between_second
                    if num > num2:   
                        if num > num3:   
                            if num2 > num3:
                                
                                embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'1 {randomflag} {num}%\n2 {randomflag2} {num2}%\n3 {randomflag3} {num3}%')
                                embed.set_footer(text = f'© Copyright 2020 Topian Team | Все права защищены', icon_url = ctx.author.avatar_url)
                                await ctx.send(embed=embed)
         

                            else:
                                embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'1 {randomflag} {num}%\n2 {randomflag2} {num3}%\n3 {randomflag3} {num2}%')                        
                                embed.set_footer(text = f'© Copyright 2020 Topian Team | Все права защищены', icon_url = ctx.author.avatar_url)
                                await ctx.send(embed=embed)  

                        else:
                            embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'1 {randomflag} {num3}%\n2 {randomflag2} {num}%\n3 {randomflag3} {num2}%')                        
                            embed.set_footer(text = f'© Copyright 2020 Topian Team | Все права защищены', icon_url = ctx.author.avatar_url)
                            await ctx.send(embed=embed)

                            
                    elif num2 > num:
                        if num2 > num3:
                            if num > num3:
                                embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'1 {randomflag} {num2}%\n2 {randomflag2} {num}%\n3 {randomflag3} {num3}%')                        
                                embed.set_footer(text = f'© Copyright 2020 Topian Team | Все права защищены', icon_url = ctx.author.avatar_url)
                                await ctx.send(embed=embed)


                            else:
                                embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'1 {randomflag} {num2}%\n2 {randomflag2} {num3}%\n3 {randomflag3} {num}%')                        
                                embed.set_footer(text = f'© Copyright 2020 Topian Team | Все права защищены', icon_url = ctx.author.avatar_url)
                                await ctx.send(embed=embed)

              

                        else:
                            embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'1 {randomflag} {num3}%\n2 {randomflag2} {num2}%\n3 {randomflag3} {num}%')                        
                            embed.set_footer(text = f'© Copyright 2020 Topian Team | Все права защищены', icon_url = ctx.author.avatar_url)
                            await ctx.send(embed=embed)


                                 
                    elif num3 > num:
                        if num3 > num3:
                            if num > num3:
                                embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'1 {randomflag} {num3}%\n2 {randomflag2} {num}%\n3 {randomflag3} {num2}%')                        
                                embed.set_footer(text = f'© Copyright 2020 Topian Team | Все права защищены', icon_url = ctx.author.avatar_url)
                                await ctx.send(embed=embed)


                            else:
                                embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'1 {randomflag} {num3}%\n2 {randomflag2} {num2}%\n3 {randomflag3} {num}%')                        
                                embed.set_footer(text = f'© Copyright 2020 Topian Team | Все права защищены', icon_url = ctx.author.avatar_url)
                                await ctx.send(embed=embed)
                                


                        else:
                            embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'1 {randomflag} {num2}%\n2 {randomflag2} {num3}%\n3 {randomflag3} {num}%')                        
                            embed.set_footer(text = f'© Copyright 2020 Topian Team | Все права защищены', icon_url = ctx.author.avatar_url)
                            await ctx.send(embed=embed)

        else:
            await ctx.send(f"Вы не прикрепили картинку")

#join to channel
@client.command()
async def j(ctx):
    global voise
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    voice = await channel.connect()
    await ctx.send(f'Бот присоеденился к каналу: {channel}')
#leave from channel
@client.command()
async def l(ctx):
    global voise
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        voice = await channel.connect()
        await ctx.send(f'Бот отключился от канала: {channel}')
	
	

	    
#hello
@client.command( pass_context = True )
async def hello( ctx ):
    author = ctx.message.author
    await ctx.send( f' { author.mention } Hello' )
	
@client.command()
async def w(ctx, * , text):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url('https://discordapp.com/api/webhooks/752220541288579183/jJ1yFfSh5em3SWgbIYx9KNton7BL1_3ufA7VfflDDOrq4GS_1R8aJozIIQDLep_her3n', adapter=AsyncWebhookAdapter(session))
        name = ctx.author.name
        avt = ctx.author.avatar_url
        await webhook.send(text, username= name, avatar_url = avt)
#info
@client.command( pass_context = True )
async def info( ctx ):
    await ctx.channel.purge( limit = 1 )
    emb = discord.Embed( title = 'INFO', colour = discord.Color.red() )
    emb.add_field( name = 'Commands',value = 'Welcome to our server, it is designed for communication, sharing memes and also supports the themes of games, youtube and everything related to it. There are currently six bots on our server, and the commands for them are listed below.                                                                                           :arrow_right:pls help:arrow_left: :arrow_right:_help:arrow_left::arrow_right:.help:arrow_left:                                                      :arrow_right:/help:arrow_left::arrow_right:!help:arrow_left:')
    await ctx.author.send( embed = emb )




@client.command()
async def timeup(ctx):
    startTime = time.time()
    timeUp = time.time() - startTime
    hoursUp = round(timeUp) // 3600
    timeUp %= 3600
    minutesUp = round(timeUp) // 60
    timeUp = round(timeUp % 60)
    msg = "Бот запустился: **{0}** час. **{1}** мин. **{2}** сек. назад".format(hoursUp, minutesUp, timeUp)
    await ctx.send(f"{msg}")

@client.command()
async def status(ctx):
    await ctx.channel.purge( limit = 1 )
    while True:      
        activity = discord.Activity(name= len(client.guilds), type=discord.ActivityType.watching)
        await client.change_presence(activity=activity)
        await asyncio.sleep(60)
        activity = discord.Activity(name='канал Nitagas', type=discord.ActivityType.watching)
        await client.change_presence(activity=activity)
        await asyncio.sleep(60)     
        activity = discord.Activity(name='-help', type=discord.ActivityType.watching)
        await client.change_presence(activity=activity)
        await asyncio.sleep(60)
        activity = discord.Activity(name='канал Nitagas', type=discord.ActivityType.watching)
        await client.change_presence(activity=activity)
        await asyncio.sleep(60)
        activity = discord.Activity(name='-help', type=discord.ActivityType.watching)
        await client.change_presence(activity=activity)
     

#mute
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def mute( ctx, member: discord.Member ):
    await ctx.channel.purge( limit = 1 )
    mute_role = discord.utils.get( ctx.message.guild.roles, name = 'mute')
    await member.add_roles( mute_role )
    await ctx.send( f'У {member.mention}, ограничение чата за нарушение прав!')


    
#clear
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )
@commands.has_permissions( manage_messages= True )
async def clear( ctx, amount : int ):
    await ctx.channel.purge( limit = amount)
    embed = discord.Embed(description = f'Было удалено {amount} сообщений.\nКоманду вызвал {ctx.author.mention}', color=0x0c0c0c)
    embed.set_footer(text=f"ID Пользователя: {ctx.author.id}")
    await ctx.send(embed=embed) 
    
 
#send_a
@client.command()
@commands.has_permissions(administrator = True)
async def send_m(ctx, member: discord.Member, *, arg):
    await ctx.channel.purge(limit = 1)
    await member.send('```' + arg + '```')        
       
    
    
#kick
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def kick( ctx, member: discord.Member, *, reason = None):
    emb = discord.Embed( title = 'Kick', colour = discord.Color.red() )
    await ctx.channel.purge( limit = 1 )

    await member.kick( reason = reason )


    embed = discord.Embed(description = f':shield: Пользователь {member.mention} был кикнут. \n📖 По причине: {reason}\n🧐 Кикнул {ctx.author.mention}', color=0x0c0c0c)
    embed.set_footer(text=f"ID Пользователя: {ctx.author.id}")
    await ctx.send(embed=embed)  
    channel = client.get_channel( 747764481559494686 )
    embedd = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**{member} was kicked**')
    embedd.set_author(name=member, icon_url=str(member.avatar_url_as(static_format='png', size=2048)))
    embedd.set_footer(text=f"Member ID: {member.id}")
    await channel.send(embed=embedd)

#ban
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def ban( ctx, member: discord.Member, *, reason = None):
    emb = discord.Embed( title = 'Ban', colour = discord.Color.red() )
    await ctx.channel.purge( limit = 1 )

    await member.ban( reason = reason )
    embed = discord.Embed(description = f':shield: Пользователь {member.mention} был забанен. \n📖 По причине: {reason}\n🧐 Забанил {ctx.author.mention}', color=0x0c0c0c)
    embed.set_footer(text=f"ID Пользователя: {ctx.author.id}")
    await ctx.send(embed=embed)  

#unban
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def unban( ctx, *, member ):
    emb.set_author( name = member.name, icon_url = member.avatar_url)
    emb = discord.Embed( title = 'unban', colour = discord.Color.red() )
    await ctx.channel.purge( limit = 1)
    banned_users = await ctx.guild.bans()
    embed = discord.Embed(description = f':shield: Пользователь {member.mention} был разбанен. \n📖 По причине: {reason}\n🧐 Разбанил {ctx.author.mention}', color=0x0c0c0c)
    embed.set_footer(text=f"ID Пользователя: {ctx.author.id}")
    await ctx.send(embed=embed)  

    for ban_entry in banned_users:
        user = ban_entry.user

        await ctx.guild.unban ( user)
       
        await ctx.send( f'Unbanned user {user.mention }' )

        return

#help    
@client.command( pass_context = True )

async def helptwo( ctx ):
    await ctx.channel.purge( limit = 1 )
    
    emb = discord.Embed( title = 'HELP', colour = discord.Color.red() )
    emb.add_field( name = 'Commands',value = ' info- Информация\nserverinfo - информация о сервере\nbotinfo - информация о боте\nuserinfo - информация о пользователе\nhello - Приветствие \navatar- фото профиля\ncovid\ntime- Время\nnum- рандомное число от 1-101\n \n Games\n\nугадайка - угадай число от 1 до 20\n sapper- сапер\nknb - камень, ножницы, бумага\nrps - камень, ножницы, бумага с ботом\ncoinflip - орел или решка?\nball - шар предсказаний\n\n\nTEXT\n \nsend_m - отправить сообщение другому участнику через бота\nping - пинг\nmath - калькулятор\nslap - ударить рандомного участника\nunion - узнать ник\n slapperson - ударить определенного игрока\nroles - узнать роли игрока\nadd - суммировать числа\nwordnum - количество слов в тексте\ntext2 - ???\nytn - рандомное видео с канала Nitagas\nyt,yt2,yt3...yt7 - видео с канала nitagas\nemoji_random - рандомное эмоджи\nsearch - поиск\nyoutube_search - поиск в youtube\nwiki - поиск в википедия\nyandex - поиск в яндекс\ngoogle - поиск в гугл\nkill\n \n ')
    await ctx.author.send( embed = emb )


#help
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def helpadmin( ctx ):
    await ctx.channel.purge( limit = 1 )
    emb = discord.Embed( title = 'HELP', colour = discord.Color.red() )
    emb.add_field( name = 'Commands',value = ' info- Информация\n\n Для админов \n \n text- писать от бота\nclear\n ban\n unban\n kick\nrainbow\n youtube- видео с nitagas\n\nchanging_name- изменить ник\nevent_roles- розогрыш ролей\ntempban s m h d\ntmute- voice mute\ntemp_add_role +time @ role\nadd_role +@ +role\ntempmute +time @ arg\nchannel_create +name\nvoice_create +name\nemoji +id message + emoji\nsuggest +arg')
    await ctx.author.send( embed = emb )
#time
@client.command( pass_context = True )


async def time( ctx ):
    emb = discord.Embed( title = 'Time', colour = discord.Colour.red(), url = 'http://www.unn.ru/time/')

    emb.set_author( name = client.user.name, icon_url = client.user.avatar_url )
    emb.set_footer( text = 'Спасибо за использование нашего бота!')
    emb.set_image( url = 'https://upload.wikimedia.org/wikipedia/ru/thumb/2/2a/Adventure_Time_with_Finn_%26_Jake.png/274px-Adventure_Time_with_Finn_%26_Jake.png')
    emb.set_thumbnail( url = 'https://png.pngtree.com/png-vector/20190119/ourlarge/pngtree-clock-line-filled-icon-png-image_325450.jpg')

    now_date = datetime.datetime.now()

    emb.add_field( name = 'Time', value = 'Time : {}'.format( now_date ) )

    await ctx.send( embed = emb )



    
    
#autorole
@client.event
async def on_member_join( member ):
    channel = client.get_channel( 705461507953262793 )

    role = discord.utils.get( member.guild.roles, id = 705364781753958450 )

    await member.add_roles( role )
    await channel.send( embed = discord.Embed( description = f'Пользователь {member.mention}\n{member.name}#{member.discriminator}, присоединился к нам!') )
    emb = discord.Embed( title = 'INFO', colour = discord.Color.red() )
    emb.add_field( name = 'ИНФОРМАЦИЯ',value = 'Добро пожаловать на сервер Coders_community, наш сайт http://coders-community.smors.ru/\n**ОБЯЗАТЕЛЬНО ПРОЧИТАЙТЕ ПРАВИЛА НА СЕРВЕРЕ И НАЖМИТЕ НА РЕАКЦИЮ 📖**')
    await member.send( embed = emb )

#autorole
@client.event
async def on_member_remove( member ):
    channel = client.get_channel( 740154462177591346 )
    await channel.send( embed = discord.Embed( description = f'Пользователь {member.mention}\n{member.name}#{member.discriminator},  покинул сервер') )


@clear.error
async def clear_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')

    if isinstance( error, commands.MissingPermissions ):
        await ctx.send( f'{ ctx.author.name }, у вас недостаточно прав ')

@ban.error    
async def ban_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')

    if isinstance( error, commands.MissingPermissions ):
        await ctx.send( f'{ ctx.author.name }, у вас недостаточно прав ')

@unban.error    
async def unban_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')

    if isinstance( error, commands.MissingPermissions ):
        await ctx.send( f'{ ctx.author.name }, у вас недостаточно прав ')
@kick.error    
async def kick_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')

    if isinstance( error, commands.MissingPermissions ):
        await ctx.send( f'{ ctx.author.name }, у вас недостаточно прав ')

@send_m.error    
async def send_m_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')



        
       
#join to channel
@client.command()
async def join(ctx):
    global voise
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send(f'Бот присоеденился к каналу: {channel}')

#leave from channel
@client.command()
async def leave(ctx):
    global voise
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        voice = await channel.connect()
        await ctx.send(f'Бот отключился от канала: {channel}')


#num 
@client.command( pass_context = True )
async def num( ctx ):
    await ctx.send(random.randint(1,101))
  

#text
@client.command()
@commands.has_permissions( administrator = True )
async def text(ctx, arg):
    await ctx.channel.purge( limit = 1 )
    await ctx.send(arg)
#text2
@client.command()
async def text2(ctx, arg1, arg2):
    await ctx.channel.purge( limit = 1 )
    await ctx.send('You passed {} and {}'.format(arg1, arg2))
#wordnum
@client.command()
async def wordnum(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))
#add
@client.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)


#slap
class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return '{0.author} slapped {1} because *{2}*'.format(ctx, to_slap, argument)

@client.command()
async def slap(ctx, *, reason: Slapper):
    await ctx.send(reason)

#roles
class MemberRoles(commands.MemberConverter):
    async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument)
        return [role.name for role in member.roles[1:]] # Remove everyone role!

@client.command()
async def roles(ctx, *, member: MemberRoles):
    """Tells you a member's roles."""
    await ctx.send('I see the following roles: ' + ', '.join(member))

#union
@client.command()
async def union(ctx, what: typing.Union[discord.TextChannel, discord.Member]):
    await ctx.send(what)
#slapperson
@client.command()
async def slapperson(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))

@slap.error    
async def slap_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')


@union.error    
async def union_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')

@slapperson.error    
async def slapperson_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')


@roles.error    
async def roles_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')


@add.error    
async def add_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')


@wordnum.error    
async def wordnum_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')


@text.error    
async def text_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')

@text2.error    
async def text2_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')

  

#ytn
@client.command()
async def ytn(ctx ):
    a = random.choice(['https://youtu.be/oVMjZx2D4ZI', 'https://youtu.be/T9u9nn0lscs', 'https://youtu.be/3MsvbceklK8','https://youtu.be/FCMbQVa577o','https://youtu.be/p3-pF2ms9ag','https://youtu.be/S5WkBjiUQCs','https://youtu.be/0CFby0bAsUI'])
    await ctx.send( a )
    


#emoji
@client.command()
async def emoji_random(ctx ):
    a = random.choice([':ghost:',':skull_crossbones:',':poop: ',':upside_down: ',':face_with_raised_eyebrow:',':nerd:',':face_with_monocle:',':tired_face:',':confounded:',':exploding_head:',':face_with_symbols_over_mouth:',':hot_face:',':cold_face:',':rage:',':cowboy:',':clown:',':space_invader:',':fox:',':chicken:',':penguin:',':comet:',':bow_and_arrow:',':tv:',':money_with_wings:',':gem:',':gun:',':bomb:',':firecracker:',':knife:',':toilet:',':test_tube:',':microbe:'])
    await ctx.send( a )


#coinflip
@client.command()
async def coinflip(ctx ):
    a = random.choice(['орел','решка','орел','решка','орел'])
    await ctx.send( a )

#knb
@client.command()
async def knb(ctx, member: discord.Member ):
    a = random.choice([':moyai: камень',':scissors: ножницы',':scroll: бумага'])
    v = random.choice([':moyai: камень',':scissors: ножницы',':scroll: бумага'])

    emb = discord.Embed( title = 'Камень, ножницы, бумага', colour = discord.Color.blue() )
    
    await ctx.send( embed = emb )

    emg = discord.Embed( title = f'{ member.name}', colour = discord.Color.red() )
    await ctx.send( embed = emg )

    emw = discord.Embed( title = a, colour = discord.Color.blue() )
    await ctx.send( embed = emw )

    emd = discord.Embed( title = f'{ ctx.author.name}', colour = discord.Color.red() )
    await ctx.send( embed = emd )

    emx = discord.Embed( title = v, colour = discord.Color.blue() )
    await ctx.send( embed = emx )


 
@knb.error    
async def knb_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')


#sapper
@client.command()
async def sapper(ctx):
    general = client.get_channel(724954151263404086)
    emg = discord.Embed( title = f'Game sapper\n Rules you must select a number and enter it as shown in the table below\n 1- first \n2- second\n3- third\n4- fouth\n5- fifth\n6- sixth\n7- seventh\n8- eighth\n9- ninth \ndo not forget about the prefix (-)\n\n1      2     3\n4     5     6     \n7     8     9', colour = discord.Color.red() )
    await general.send( embed = emg )
    

@client.command()    
async def first(ctx ):
    a = random.choice(['win','lose','win','lose'])
    await ctx.send( a )
    if a == 'win':
        await ctx.author.send( "if you want continue, write -nextlvls")
    if a == 'lose':
        await ctx.send( "Game over" )
        fin = random.choice(['lucky next time','try again','loser','hahaha'])
        await ctx.send( fin )

@client.command()    
async def second(ctx ):
    a = random.choice(['win','lose','win','lose'])
    await ctx.send( a )
    if a == 'win':
        await ctx.author.send( "if you want continue, write -nextlvls")
    if a == 'lose':
        await ctx.send( "Game over " )
        fin = random.choice(['lucky next time','try again','loser','hahaha'])
        await ctx.send( fin )

@client.command()    
async def third(ctx ):
    a = random.choice(['win','lose','win','lose'])
    await ctx.send( a )
    if a == 'win':
        await ctx.author.send( "if you want continue, write -nextlvls")
    if a == 'lose':
        await ctx.send( "Game over" )
        fin = random.choice(['lucky next time','try again','loser','hahaha'])
        await ctx.send( fin )


@client.command()    
async def fouth(ctx ):
    a = random.choice(['win','lose','win','lose'])
    await ctx.send( a )
    if a == 'win':
        await ctx.author.send( "if you want continue, write -nextlvls")
    if a == 'lose':
        await ctx.send( "Game over" )
        fin = random.choice(['lucky next time','try again','loser','hahaha'])
        await ctx.send( fin )

@client.command()    
async def fifth(ctx ):
    a = random.choice(['win','lose','win','lose'])
    await ctx.send( a )
    if a == 'win':
        await ctx.author.send( "if you want continue, write -nextlvls")
    if a == 'lose':
        await ctx.send( "Game over" )
        fin = random.choice(['lucky next time','try again','loser','hahaha'])
        await ctx.send( fin )

@client.command()    
async def sixth(ctx ):
    a = random.choice(['win','lose','win','lose'])
    await ctx.send( a )
    if a == 'win':
        await ctx.author.send( "if you want continue, write -nextlvls")
    if a == 'lose':
        await ctx.send( "Game over" )

@client.command()    
async def seventh(ctx ):
    a = random.choice(['win','lose','win','lose'])
    await ctx.send( a )
    if a == 'win':
        await ctx.author.send( "if you want continue, write -nextlvls")
    if a == 'lose':
        await ctx.send( "Game over" )
        fin = random.choice(['lucky next time','try again','loser','hahaha'])
        await ctx.send( fin )

@client.command()    
async def eighth(ctx ):
    a = random.choice(['win','lose','win','lose'])
    await ctx.send( a )
    if a == 'win':
        await ctx.author.send( "if you want continue, write -nextlvls")
    if a == 'lose':
        await ctx.send( "Game over" )
        fin = random.choice(['lucky next time','try again','loser','hahaha'])
        await ctx.send( fin )

@client.command()    
async def ninth(ctx ):
    a = random.choice(['win','lose','win','lose'])
    await ctx.send( a )
    if a == 'win':
        await ctx.author.send( "if you want continue, write -nextlvls")
    if a == 'lose':
        await ctx.send( "Game over" )
        fin = random.choice(['lucky next time','try again','loser','hahaha'])
        await ctx.send( fin )

 
        
@client.command()
async def nextlvls(ctx ):
    emg = discord.Embed( title = f'1      2     3\n4     5     6     \n7     8     9', colour = discord.Color.red() )
    await ctx.send( embed = emg )  


@client.command() # Попытки 5
async def угадайка(ctx):
    await ctx.message.delete()
    num = random.randint(1, 20)
    attems = 1
    msg = await ctx.send('Подождите...')
    while attems < 6:
        emb = discord.Embed(
            title = f'Попытка №{attems}',
            description= 'Угадайте число от 1 до 20'
        )
        await msg.edit(content= None, embed=emb)
        try:
            msg_o = await  client.wait_for('message', timeout= 30.0, check= lambda msg_o: msg_o.author == ctx.author)
        except asyncio.TimeoutError:
            await msg.edit(content= 'Время вышло!', embed=None)
            break
        else:
            if num == int(msg_o.content):
                emb1 = discord.Embed(
                    title= 'Вы победили!',
                    description= 'Вы угадали число!'
                )
                await msg_o.delete()
                await msg.edit(content= None, embed=emb1)
                break
            else:
                attems_h = 5 - attems
                attems = attems + 1
                if attems == 6:
                    emb2 = discord.Embed(
                        title= 'Вы проиграли!',
                        description= f'Загаданое число было : {num}'
                    )
                    await msg_o.delete()
                    await msg.edit(embed=emb2)
                    break

                emb2 = discord.Embed(
                    title= 'Неудачная попытка!',
                    description= f'Вы не угадали число у вас осталось {attems_h} попыток'
                )
                await msg.edit(content= None, embed=emb2)
                await msg_o.delete() 
                await asyncio.sleep(2)

#search
@client.command()
async def search(ctx, *, question):  # пояндексить
    # сам сайт
    url = 'https://www.bing.com/search?q=' + str(question).replace(' ', '+')
    await ctx.send(f'Кое кто не умеет пользоваться поисковиками , я сделал это за него.\n{url}')
    
    
@search.error    
async def search_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')
    
    

#youtube_search
@client.command()
async def youtube_search(ctx, *, question):  # пояндексить
    # сам сайт
    url = 'https://www.youtube.com/results?search_query=' + str(question).replace(' ', '+')
    await ctx.send(f'Так как кое кто не умеет ютубить , я сделал это за него.\n{url}')
    
    
@youtube_search.error    
async def youtube_search_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')

    if isinstance( error, commands.MissingPermissions ):
        await ctx.send( f'{ ctx.author.name }, у вас недостаточно прав ')   
  
#yandex
@client.command()
async def yandex(ctx, *, question):  # пояндексить
    # сам сайт
    url = 'https://yandex.ua/search/?lr=142&text=' + str(question).replace(' ', '%20')
    await ctx.send(f'Так как кое кто не умеет яндексить , я сделал это за него.\n{url}')
    
@yandex.error    
async def yandex_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')
      
    
    
#wiki
@client.command(pass_context = True,aliases=['вики']) #!!wiki  !!вики
async def wiki( ctx,*, amount: str):

    if not amount:
        await ctx.send("Пожалуйста, используйте такую кострукцию: `!!wiki [вики запрос]`")
    a = '_'.join(amount.split())
    await ctx.send(f'https://ru.wikipedia.org/wiki/{a}')
    
    
@wiki.error    
async def wiki_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')

 

#google
@client.command()
async def google(ctx, *, question):  # погуглить
    # сам сайт
    url = 'https://google.gik-team.com/?q=' + str(question).replace(' ', '+')
    await ctx.send(f'Так как кое кто не умеет гуглить , я сделал это за него.\n{url}')
    
    
@google.error    
async def google_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')

 

#rps
@client.command()
async def rps(ctx, *, mess):
    robot = ['Камень', 'Ножницы', 'Бумага']
    if mess == "Камень" or mess == "К" or mess == "камень" or mess == "к":
        robot_choice = random.choice(robot)
        emb = discord.Embed(title = robot_choice, colour = discord.Colour.lighter_grey())
        if robot_choice == 'Ножницы':
            emb.add_field(name = ':scissors:', value = 'Вы выиграли!')
        elif robot_choice == 'Бумага':
            emb.add_field(name = ':scroll:', value = 'Вы проиграли :с')
        else:
            emb.add_field(name = ':moyai:', value = 'Ничья!')
        await ctx.send(embed = emb)

    elif mess == "Бумага" or mess == "Б" or mess == "бумага" or mess == "б":
        robot_choice = random.choice(robot)
        emb = discord.Embed(title = robot_choice, colour = discord.Colour.lighter_grey())
        if robot_choice == 'Ножницы':
            emb.add_field(name = 'scissors:', value = 'Вы проиграли :с')
        elif robot_choice == 'Камень':
            emb.add_field(name = ':moyai:', value = 'Вы выиграли!')
        else:
            emb.add_field(name = '::scroll:', value = 'Ничья!')
        await ctx.send(embed = emb)
            
    elif mess == "Ножницы" or mess == "Н" or mess == "ножницы" or mess == "н":
        robot_choice = random.choice(robot)
        emb = discord.Embed(title = robot_choice, colour = discord.Colour.lighter_grey())
        if robot_choice == 'Бумага':
            emb.add_field(name = ':scroll:', value = 'Вы выиграли!')
        elif robot_choice == 'Камень':
            emb.add_field(name = ':moyai:', value = 'Вы проиграли :с')
        else:
            emb.add_field(name = ':scissors:', value = 'Ничья!')
        await ctx.send(embed = emb)



@rps.error    
async def rps_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')



#botinfo
@client.command( pass_context = True )
async def botinfo( ctx ):
    await ctx.channel.purge( limit = 1 )
    emt = discord.Embed(title=f"{ctx.guild.name}", description="Информация о боте **NITAGAS bot**.\n  подробнее о командах  -help\n По вопросам обращатся на сервер https://discord.gg/NfTf9JD", color = 000000)
    emt.add_field(name=f'**Меня создал:**', value="Stanislav", inline=True)  # Создает строку
    emt.add_field(name=f'**Помощь в создании:**', value="yazdrim#6779", inline=True)  # Создает строку
    emt.add_field(name=f'**Лицензия:**', value="Nitagas", inline=True)  # Создает строку
    emt.add_field(name=f'**Я написан на:**', value="Discord.py", inline=True)  # Создает строку
    emt.add_field(name=f'**Версия:**', value="1.0", inline=True)  # Создает строку
    emt.add_field(name=f'**Патч:**', value="1.0", inline=True)  # Создает строку
    emt.set_footer(text=f"© Copyright 2020 Stanislav | Все права защищены")  # создаение футера
    await ctx.send(embed=emt)


#tmute
@client.command()
@commands.has_permissions( administrator = True )
async def tmute(ctx, member: discord.Member):
    await ctx.channel.purge( limit = 1 )
    await member.edit(mute=True)


#emoji       
@client.command()
@commands.has_permissions( administrator = True )
async def emoji(ctx,id:int,reaction:str):
        await ctx.message.delete()
        message = await ctx.message.channel.fetch_message(id)
        await message.add_reaction(reaction)


#kill
@client.command()
async def kill(  ctx, member: discord.Member ):
    await ctx.send( f"{ctx.author.mention} Достает дробовик... \n https://tenor.com/view/eyebrow-raise-smile-prepared-ready-loaded-gif-15793001" )
    await asyncio.sleep( 3 )
    await ctx.send( f"{ctx.author.mention} Направляет дробовик на {member.mention}... \n https://tenor.com/view/aim-point-gun-prepared-locked-and-loaded-gif-15793489" )
    await asyncio.sleep( 2 )
    await ctx.send( f"{ctx.author.mention} Стреляет в {member.mention}... \n https://media.discordapp.net/attachments/690222948283580435/701494203607416943/tenor_3.gif" )
    await asyncio.sleep( 2 )
    await ctx.send( f"{member.mention} истекает кровью..." )
    await asyncio.sleep( 3 )
    await ctx.send( f"{member.mention} погиб..." )




#tempban
@client.command()
@commands.has_permissions( administrator = True )
async def tempban(ctx, member : discord.Member, time:int, arg:str, *, reason=None):
    await ctx.channel.purge( limit = 1 )
    if member == ctx.message.author:
        return await ctx.send("Ты не можешь забанить сам себя.")
    msgg =  f'Пользователь : {member}, забанен по причине : {reason}.'
    msgdm = f'Вы были забанены на сервере {ctx.guild.name}, по причине : {reason}.'
    if reason == None:
        msgdm = f'Вы были забанены на сервере : {ctx.guild.name}.'
    if reason == None:
        msgg =  f'Пользователь : {member}, забанен.'
    await ctx.send(msgg)  
    await member.send(msgdm)
    await ctx.guild.ban(member, reason=reason)
    if arg == "s":
        await asyncio.sleep(time)          
    elif arg == "m":
        await asyncio.sleep(time * 60)
    elif arg == "h":
        await asyncio.sleep(time * 60 * 60)
    elif arg == "d":
        await asyncio.sleep(time * 60 * 60 * 24)
    await member.unban()
    await ctx.send(f'Пользователь : {member}, разбанен.')
    await member.send(f'Вы были разбанены на сервере : {ctx.guild.name}')




#temp_add_role
@client.command()
@commands.has_permissions(administrator = True)
async def temp_add_role(ctx, amount : int, member: discord.Member = None, role: discord.Role = None):
    await ctx.channel.purge( limit = 1 )

    try:

        if member is None:

            await ctx.send(embed = discord.Embed(description = '**:grey_exclamation: Обязательно укажите: пользователя!**'))

        elif role is None:

            await ctx.send(embed = discord.Embed(description = '**:grey_exclamation: Обязательно укажите: роль!**'))

        else:

            await discord.Member.add_roles(member, role)
            await ctx.send(embed = discord.Embed(description = f'**Роль успешна выдана на {amount} секунд!**'))
            await asyncio.sleep(amount)
            await discord.Member.remove_roles(member, role)

    except:
        
        await ctx.send(embed = discord.Embed(description = f'**:exclamation: Не удалось выдать роль.**', color=0x0c0c0c))

@client.command()
@commands.has_permissions(administrator = True)
async def add_role(ctx, member: discord.Member = None, role: discord.Role = None):
    await ctx.channel.purge( limit = 1 )
    channel = client.get_channel( 738779492339941537 )
    try:
        if member is None:
            await ctx.send(embed = discord.Embed(description = '**:grey_exclamation: Обязательно укажите: пользователя!**'))
        elif role is None:
            await ctx.send(embed = discord.Embed(description = '**:grey_exclamation: Обязательно укажите: роль!**'))
        else:
            await discord.Member.add_roles(member, role)
            await ctx.send(embed = discord.Embed(description = f'**Роль успешна выдана**'))
           
    except:
        await ctx.send(embed = discord.Embed(description = f' Не удалось выдать роль.', color=0x0c0c0c))
        


#ping
@client.command() 
async def ping(ctx):
    await ctx.send(embed = discord.Embed(description = f'**:gear: Ваш пинг:** { randint( 15, 200 ) }', color=0x0c0c0c))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'**:exclamation: {ctx.author.name}, данной команды не существует.**', color=0x0c0c0c))


# Работа с ошибками мута на время



#math
@client.command()
async def math( ctx, a : int, arg, b : int ):
    try:
        if arg == '+':
            await ctx.send(embed = discord.Embed(description = f'**:bookmark_tabs: Результат:** { a + b }', color=0x0c0c0c))  

        elif arg == '-':
            await ctx.send(embed = discord.Embed(description = f'**:bookmark_tabs: Результат:** { a - b }', color=0x0c0c0c))  

        elif arg == '/':
            await ctx.send(embed = discord.Embed(description = f'**:bookmark_tabs: Результат:** { a / b }', color=0x0c0c0c))

        elif arg == '*':
            await ctx.send(embed = discord.Embed(description = f'**:bookmark_tabs: Результат:** { a * b }', color=0x0c0c0c))      

    except:       
        await ctx.send(embed = discord.Embed(description = f'**:exclamation: Произошла ошибка.**', color=0x0c0c0c))

@math.error    
async def math_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')



#voice_create
@client.command()
@commands.has_permissions(administrator = True)
async def voice_create(ctx, *, arg):
    await ctx.channel.purge( limit = 1 )
    guild = ctx.guild
    channel = await guild.create_voice_channel(f'{arg}')
    await ctx.send(embed = discord.Embed(description = f'**:microphone2: Голосовой канал "{arg}" успешно создан!**', color=0x0c0c0c))

#channel_create   
@client.command()
@commands.has_permissions(administrator = True)
async def channel_create(ctx, *, arg): 
    await ctx.channel.purge( limit = 1 )
    guild = ctx.guild
    channel = await guild.create_text_channel(f'{arg}')
    await ctx.send(embed = discord.Embed(description = f'**:keyboard: Текстовый канал "{arg}" успешно создан!**', color=0x0c0c0c))


#avatar
@client.command()
async def avatar(ctx, member : discord.Member = None):
    user = ctx.message.author if (member == None) else member
    embed = discord.Embed(title=f'Аватар пользователя {user}', color= 0x0c0c0c)
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)

# userinfo
@client.command()
async def userinfo(ctx, Member: discord.Member = None ):
    await ctx.channel.purge( limit = 1 )
    if not Member:
        Member = ctx.author
    roles = (role for role in Member.roles )
    emb = discord.Embed(title='Информация о пользователе.'.format(Member.name), description=f"Участник зашёл на сервер: {Member.joined_at.strftime('%b %#d, %Y')}\n\n "
                                                                                      f"Имя: {Member.name}\n\n"
                                                                                      f"Никнейм: {Member.nick}\n\n"
                                                                                      f"Статус: {Member.status}\n\n"
                                                                                      f"ID: {Member.id}\n\n"
                                                                                      f"Высшая роль: {Member.top_role}\n\n"
                                                                                      f"Аккаунт создан: {Member.created_at.strftime('%b %#d, %Y')}", 
                                                                                      color=0xff0000, timestamp=ctx.message.created_at)

    emb.set_thumbnail(url= Member.avatar_url)
    emb.set_footer(icon_url= Member.avatar_url)
    emb.set_footer(text='Команда вызвана: {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)


@client.command()
@commands.has_permissions(administrator = True)
async def changing_name(ctx, member: discord.Member = None, nickname: str = None):
    await ctx.channel.purge( limit = 1 )
    await ctx.send('Info')
    try:
        if member is None:
            await ctx.send(embed = discord.Embed(description = "Обязательно укажите **пользователя**!"))
        elif nickname is None:
            await ctx.send(embed = discord.Embed(description = "Обязательно укажите ник!"))
        else:
            await member.edit(nick = nickname)
            await ctx.send(embed = discord.Embed(description = f"У пользователя **{member.name}** был изменен ник на **{nickname}**"))
    except:
        await ctx.send(embed = discord.Embed(description = f"Я не могу изменить ник пользователя **{member.name}**!"))

#suggest
@client.command( pass_context = True, aliases = [ "Предложить", "предложить", "предложка", "Предложка", "Suggest" ])
@commands.has_permissions( administrator = True )
async def suggest( ctx , * , agr ):
    suggest_chanell = client.get_channel( 705461507953262793 ) #Айди канала предложки
    embed = discord.Embed(title=f"{ctx.author.name} Предложил :", description= f" {agr} \n\n")

    embed.set_thumbnail(url=ctx.guild.icon_url)

    message = await suggest_chanell.send(embed=embed)
    await message.add_reaction('✅')
    await message.add_reaction('❎')


@client.command()
async def serverinfo(ctx):
    await ctx.channel.purge( limit = 1 )
    members = ctx.guild.members
    online = len(list(filter(lambda x: x.status == discord.Status.online, members)))
    offline = len(list(filter(lambda x: x.status == discord.Status.offline, members)))
    idle = len(list(filter(lambda x: x.status == discord.Status.idle, members)))
    dnd = len(list(filter(lambda x: x.status == discord.Status.dnd, members)))
    allchannels = len(ctx.guild.channels)
    allvoice = len(ctx.guild.voice_channels)
    alltext = len(ctx.guild.text_channels)
    allroles = len(ctx.guild.roles)
    embed = discord.Embed(title=f"{ctx.guild.name}", color=0xff0000, timestamp=ctx.message.created_at)
    embed.description=(
        f":timer: Сервер создали **{ctx.guild.created_at.strftime('%A, %b %#d %Y')}**\n\n"
        f":flag_white: Регион **{ctx.guild.region}\n\nГлава сервера **{ctx.guild.owner}**\n\n"
        f":tools: Ботов на сервере: **{len([m for m in members if m.bot])}**\n\n"
        f":green_circle: Онлайн: **{online}**\n\n"
        f":black_circle: Оффлайн: **{offline}**\n\n"
        f":yellow_circle: Отошли: **{idle}**\n\n"
        f":red_circle: Не трогать: **{dnd}**\n\n"
        f":shield: Уровень верификации: **{ctx.guild.verification_level}**\n\n"
        f":musical_keyboard: Всего каналов: **{allchannels}**\n\n"
        f":loud_sound: Голосовых каналов: **{allvoice}**\n\n"
        f":keyboard: Текстовых каналов: **{alltext}**\n\n"
        f":briefcase: Всего ролей: **{allroles}**\n\n"
        f":slight_smile: Людей на сервере **{ctx.guild.member_count}\n\n"
    )

    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f"ID: {ctx.guild.id}")
    embed.set_footer(text=f"ID Пользователя: {ctx.author.id}")
    await ctx.send(embed=embed)


@client.command()
async def covid(ctx):   
    await ctx.send(f'https://www.worldometers.info/coronavirus/') 
    
#ngame 
@client.command()
async def ngame(ctx):   
    await ctx.send(f'Games\n\nугадайка- угадай число от 1 до 20\n sapper- сапер\nknb- камень, ножницы, бумага\nrps- камень, ножницы, бумага с ботом\ncoinflip- орел или решка?') 
       

#ball    
@client.command()
async def ball(ctx, arg = None):
    embe = discord.Embed( title = random.choice(['Да :8ball: ','Нет :8ball: ','Может быть','Думаю нет','Думаю да','Хорошо','Не сейчас','Позже','Сложный вопрос','Не знаю','Надо подумать','Потом','Ты шутишь?','Конечно, да!']), colour = discord.Color.red() )
    await ctx.send(embed=embe)


#search
@client.command()
async def seagoogle(ctx, *, question, args):  # пояндексить
    # сам сайт
    url = 'https://drive.google.com/drive/folders/1' + str(question).replace(' ', '+') + '?usp=sharing', 'https://drive.google.com/drive/folders/1' + str(args).replace(' ', '+') + '?usp=sharing'
    await ctx.send(f'вот\n{url}')
    
  
#search
@client.command()
async def seachgoogle(ctx, *, question):  # пояндексить
    # сам сайт
    url = 'https://drive.google.com/drive/folders/1' + str(question).replace(' ', '+') + '?usp=sharing'
    await ctx.send(f'вот\n{url}')


#link     
@client.command()
async def link(ctx, url ):
    while True: 
        r = requests.get(url)
        if r.status_code == 404:
            await ctx.message.delete()

ev_player = [''] #игроки в розыгрыше
start_ev = 0 #перемычка

#event_roles
@client.command()
async def event_roles(ctx, role: discord.Role = None, member: discord.Member = None):
    global ev_player
    global start_ev
    if role is None:
        await ctx.send('**Упомяните роль для розыгрыша.**' '\n' '`/event_roles [role]`')
        return  
    start_ev = 1
    await ctx.send(f'Администратор запустил розыгрыш роли {role.mention}. Для участия пропишите `-уч`.' '\n' f'**Розыгрыш состоится через 2 дня.**')
    await asyncio.sleep(172800)
    ev_win = r.choice(ev_player)
    member = ev_win
    await ctx.send(f'**Поздравляем {ev_win.mention}! Он выигрывает в розыгрыше и получает роль {role.mention}.**')
    await ev_win.add_roles(role)
    ev_player = ['']
    start_ev = 0

#mp
@client.command()
async def уч(ctx):
    global ev_player
    global start_ev
    author = ctx.message.author
    if start_ev == 0:
        await ctx.send('**Сейчас нету розыгрыша ролей!**')
        return
    if author in ev_player:
        await ctx.send('Вы уже приняли участие в этом розыгрыше!')
        return
    else:
        ev_player.append(author)
        print(f'Игрок {author} принял участие в розыгрыши роли.')
        await ctx.send(embed = discord.Embed(description = f'**{author.mention}, Вы успешно приняли участие в розыгрыши роли!**', color = 0xee3131))
        print('Розыгрыш роли завершен.')
#help
@client.command(pass_context = True)
async def help(ctx):
    await ctx.channel.purge(limit = 1)
    emb = discord.Embed( 
        title = 'Навигация по командам :clipboard:',
        color = 0x7aa13d
     )
    
    emb.add_field( name = '__**Информация**__', value = '''
        ***-serverinfo*** - информация о сервере
        ***-botinfo*** - информация о боte
        ***-userinfo*** - информация о пользователе
        ***-time***  
        ***-covid*** 
        ***-avatar***
        ***-ip_info ***  
        ''' )
    emb.add_field( name = '__**Игры**__', value = '''
        ***-num*** - рандомное число от 1-101
        ***-угадайка*** - угадай число от 1 до 20
        ***-sapper*** - сапер
        ***-knb*** - камень, ножницы, бумага
        ***-rps*** - камень, ножницы, бумага с ботом
        ***-coinflip*** - орел или решка?
        ***-ball*** - шар предсказаний
        ''' )
    emb.add_field( name = '__**Остальное**__', value = '''
        ***-send_m*** - отправить сообщение другому участнику через бота
        ***-ping*** - пинг
        ***-math*** - калькулятор
        ***-hello*** - Приветствие
        ***-slap*** - ударить рандомного участника
        ***-slapperson*** - ударить определенного игрока
        ***-union*** - узнать ник
        ***-roles*** - узнать роли игрока
        ***-add*** - суммировать числа
        ***-wordnum*** - количество слов в тексте
        ***-text2*** - ???
        ***-ytn*** - рандомное видео с канала Nitagas
        ***-emoji_random*** - рандомное эмоджи
        ***-kill***
        
        
        ''' )
    emb.add_field( name = '__**Поиск**__', value = '''
        ***-search*** - поиск
        ***-youtube_search*** - поиск в youtube
        ***-wiki*** - поиск в википедия
        ***-yandex*** - поиск в яндекс
        ***-google*** - поиск в гугл
        ''' )
    await ctx.author.send(embed = emb)

           
#ip_info
@client.command()
async def ip_info( ctx, arg ):
    await ctx.channel.purge(limit = 1)
    response = requests.get( f'http://ipinfo.io/{ arg }/json' )
    user_ip = response.json()[ 'ip' ]
    user_city = response.json()[ 'city' ]
    user_region = response.json()[ 'region' ]
    user_country = response.json()[ 'country' ]
    user_location = response.json()[ 'loc' ]
    user_org = response.json()[ 'org' ]
    user_timezone = response.json()[ 'timezone' ]
    global all_info
    all_info = f'```\n<INFO>\nIP : { user_ip }\nCity : { user_city }\nRegion : { user_region }\nCountry : { user_country }\nLocation : { user_location }\nOrganization : { user_org }\nTime zone : { user_timezone }```'
    await ctx.author.send( all_info )
    await ctx.send( '```NoBot » Информация отослана в Личные Сообщения!```' )

#role add
@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 728594240669745172: # ID Сообщения
        guild = client.get_guild(payload.guild_id)
        role = None

        if str(payload.emoji) == '1️⃣': # Emoji для реакций
            role = guild.get_role(728595441016373269) # ID Ролей для выдачи
        elif str(payload.emoji) == '2️⃣':
            role = guild.get_role(728595853605994558)
        elif str(payload.emoji) == '3️⃣':
            role = guild.get_role(728595568183738420)
        elif str(payload.emoji) == '4️⃣':
            role = guild.get_role(728595513489883298)
        elif str(payload.emoji) == '5️⃣':
            role = guild.get_role(728595599917580350)
        elif str(payload.emoji) == '6️⃣':
            role = guild.get_role(728595815718715423)
        elif str(payload.emoji) == '7️⃣':
            role = guild.get_role(728595715600941126)
        elif str(payload.emoji) == '8️⃣':
            role = guild.get_role(728595650639429632)
        elif str(payload.emoji) == '9️⃣':
            role = guild.get_role(736183055667953684)
        elif str(payload.emoji) == '💎':
            role = guild.get_role(736183523169534002)
        elif str(payload.emoji) == '🦅':
            role = guild.get_role(736183416885870614)
        elif str(payload.emoji) == '🟦':
            role = guild.get_role(736875237303386143)
        elif str(payload.emoji) == '📗':
            role = guild.get_role(751704160939933696)

    
        if role:
            member = guild.get_member(payload.user_id)
            if member:
                await member.add_roles(role) 

    elif payload.message_id == 745689538608758806: # ID Сообщения
        guild = client.get_guild(payload.guild_id)
        role = None

        if str(payload.emoji) == '1️⃣': # Emoji для реакций
            role = guild.get_role(745685081489801246) # ID Ролей для выдачи
        elif str(payload.emoji) == '2️⃣':
            role = guild.get_role(745685081506709674)
        elif str(payload.emoji) == '3️⃣':
            role = guild.get_role(745685081548652594)
        elif str(payload.emoji) == '4️⃣':
            role = guild.get_role(745687846576455832)
        elif str(payload.emoji) == '5️⃣':
            role = guild.get_role(751762433504313405)
	
        if role:
            member = guild.get_member(payload.user_id)
            if member:
                await member.add_roles(role) 
		
		
@client.event
async def on_guild_role_create( role ):
    channel = client.get_channel( 747764481559494686 )
    embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**A new role was created**\n{role.mention}')
    embed.set_author(name=role.guild.name, icon_url=str(role.guild.icon_url))
    embed.set_footer(text=f"Role ID: {role.id}")
    await channel.send(embed=embed)
    
@client.event
async def on_guild_role_delete( role ):
    channel = client.get_channel( 747764481559494686 )
    embed = discord.Embed(color=role.color, timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**The role** `{role.name}` **was deleted**')
    embed.set_author(name=role.guild.name, icon_url=str(role.guild.icon_url))
    embed.set_footer(text=f"Role ID: {role.id}")
    await channel.send(embed=embed)
			
@client.event
async def on_guild_name_edit(before, after):
    channel = client.get_channel( 747764481559494686 )
    embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**Guild name was changed**\n{before.name} to {after.name}')
    await channel.send(embed=embed)
				
@client.event
async def on_message_delete( message ):
    channel = client.get_channel( 747764481559494686 )
    embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**The message was delited**\n{message.content}\nAuthor {message.author.name}')
    embed.set_footer(text=f"Message ID: {message.id}")
    await channel.send(embed=embed)    

@client.event
async def on_member_edit(before, after):
    channel = client.get_channel( 747764481559494686 )
    embed = discord.Embed(color=after.author.color, timestamp=after.created_at, description=f'{after.author.mention} **changed his nick** {after.channel.mention}')
    bcontent = before.system_content[:300] + (before.system_content[300:] and '...')
    acontent = after.system_content[:300] + (after.system_content[300:] and '...')
    embed.add_field(name='Before', value=bcontent, inline=False)
    embed.add_field(name='After', value=acontent, inline=False)
    embed.set_footer(text=f"Author ID: {after.author.id}")
    await channel.send(embed=embed)
	
@client.event
async def on_member_ban(guild, member):
    channel = client.get_channel( 747764481559494686 )
    embed = discord.Embed(color=member.color if member.color != discord.Color.default() else discord.Color.red(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**{member.mention} was banned**')
    embed.set_author(name=member, icon_url=str(member.avatar_url_as(static_format='png', size=2048)))
    embed.set_footer(text=f"Member ID: {member.id}")
    await channel.send(embed=embed)

    embe = discord.Embed(color=member.color if member.color != discord.Color.default() else discord.Color.red(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**{member.mention}, вы забанены**')
    embe.set_author(name=member, icon_url=str(member.avatar_url_as(static_format='png', size=2048)))
    embe.set_footer(text=f"Guild name: {guild.name}")
    await member.send(embed=embe)

			
@client.event
async def on_member_kick(guild, member):
    channel = client.get_channel( 747764481559494686 )
    embed = discord.Embed(color=member.color if member.color != discord.Color.default() else discord.Color.red(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**{member.mention} was kicked**')
    embed.set_author(name=member, icon_url=str(member.avatar_url_as(static_format='png', size=2048)))
    embed.set_footer(text=f"Member ID: {member.id}")
    await channel.send(embed=embed)

    embe = discord.Embed(color=member.color if member.color != discord.Color.default() else discord.Color.red(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**{member.mention}, вы кикнуты**')
    embe.set_author(name=member, icon_url=str(member.avatar_url_as(static_format='png', size=2048)))
    embe.set_footer(text=f"Guild name: {guild.name}")
    await member.send(embed=embe)

@client.event
async def on_member_unban(guild, member):
    channel = client.get_channel( 747764481559494686 )
    embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**{member} was unbanned**')
    embed.set_author(name=member, icon_url=str(member.avatar_url_as(static_format='png', size=2048)))
    embed.set_footer(text=f"Member ID: {member.id}")
    await channel.send(embed=embed)

    embe = discord.Embed(color=member.color if member.color != discord.Color.default() else discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**{member.mention}, вы разбанены**')
    embe.set_author(name=member, icon_url=str(member.avatar_url_as(static_format='png', size=2048)))
    embe.set_footer(text=f"Guild name: {guild.name}")
    await member.send(embed=embe)
			

@client.event
async def on_invite_create(invite: discord.Invite):
    channel = client.get_channel( 747764481559494686 )
    embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**An invite was created**')
    embed.add_field(name='Invite Code', value=invite.code, inline=False)
    embed.add_field(name='Max Uses', value=invite.max_uses, inline=False)
    embed.add_field(name='Temporary', value=invite.temporary, inline=False)

    await channel.send(embed=embed)
   


@client.command()
@commands.has_permissions( kick_members = True )
async def tempmute(ctx, amount : int, member: discord.Member = None, * ,reason = None):
    await ctx.channel.purge( limit = 1 )
    channel = client.get_channel(747764481559494686) #Айди канала логов
    mutee_role = discord.utils.get(member.guild.roles, id = 705745998550401054) #Айди роли
    await member.add_roles( mutee_role )
    embed = discord.Embed(description = f':shield: Пользователю {member.mention} был ограничен доступ к чатам. \n📖 По причине: {reason}\n🕰️ На {amount} секунд\n🧐 Ограничил доступ {ctx.author.mention}', color=0x0c0c0c)
    embed.set_footer(text=f"ID Пользователя: {ctx.author.id}")
    await ctx.send(embed=embed)  
    await asyncio.sleep(amount)
    await member.remove_roles( mutee_role )

@client.command()
async def tm(ctx, amount : int, member: discord.Member = None, * ,reason = None):
    await ctx.send('1234567')
    role = guild.get_role('737322598240616519')
    await ctx.send('1234567')
    if role in ctx.author.roles:
        channel = client.get_channel(747764481559494686) #Айди канала логов
        mutee_role = discord.utils.get(member.guild.roles, id = 705745998550401054) #Айди роли
        await member.add_roles( mutee_role )
        embed = discord.Embed(description = f':shield: Пользователю {member.mention} был ограничен доступ к чатам. \n📖 По причине: {reason}\n🕰️ На {amount} секунд\n🧐 Ограничил доступ {ctx.author.mention}', color=0x0c0c0c)
        embed.set_footer(text=f"ID Пользователя: {ctx.author.id}")
        await ctx.send(embed=embed)  
        await asyncio.sleep(amount)
        await member.remove_roles( mutee_role )
    else:
        await ctx.send('1234567')

					
token= os.environ.get('BOT_TOKEN')
client.run( token )
