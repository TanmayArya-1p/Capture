import discord 
from discord.ext import commands
from util import *
import os
import time
from datetime import date
from capture import *
import ffmpeg
import json
from util import *
from win32api import GetSystemMetrics
from oauth_server import Authorize



valid_modes = ["STANDARD","GRAYSCALE" , "FASTPACE" , "SLOWPACE"]


client = commands.Bot(command_prefix = "!c ")
@client.event
async def on_ready():
    print("Ready to Use Capture!")


@client.command()
async def record(ctx,mode):
    if(str(ctx.author.id) == ReadUserID() and mode.upper() in valid_modes):
        r = Recorder(200.0 , (GetSystemMetrics(0), GetSystemMetrics(1)),"VP80","video.mkv" , mode=mode.upper())
        r.start()   
        while(r.running):
            pass
        time.sleep(5)
        try:
            await ctx.send(f"{ctx.author.mention} ,Captured Video:",file=discord.File("write.mp4"))
            os.remove("write.mp4")
        except:
            pass
        os.remove("video.mkv")
    else:
        await ctx.channel.send(f"{ctx.author.mention} ,`{mode}` is not a valid mode.Valid modes are : `{valid_modes}`.")

