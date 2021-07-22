import os
import radio_functions as rf
import discord
from discord.ext import commands

            
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="Vote du serveur", url="https://www.twitch.tv/zamanite/"))
    print('My Ready is Body')
@client.event
async def on_message(message):
    # Create voice channel for user
    if str(message.channel) == "spam" and message.content == "!create":
        if (message.author.VoiceState.channel == None):
            channel = client.get_channel()
            await channel.send("Vous devez etre connecte en vocal")
            
            
    # ----------------------------------
    # Modify a message and anonymyze it
    #
    # To avoid the spam and saying stupid 
    # things there is a logging possibility
    # ----------------------------------
    elif str(message.channel) == "spam" and message.content != "":
        channel = client.get_channel(os.environ['CHANNEL_SENDING'])
        # Logging the message sent
        channeladmin = client.get_channel(os.environ['CHANNEL_ADMIN'])
        radiomsg = rf.cricri(rf.obscure(message.content))
        await message.channel.purge(limit=1)
        await channel.send(radiomsg)
        await channeladmin.send(message.author)
        
    if str(message.channel) == "discussion-code" and str(message.author.id) == os.environ['BOT_ID']:
        channel = client.get_channel(os.environ['CHANNEL_ADMIN'])
        await channel.send(message.id)

client.run(os.environ['BOT_TOKEN'])
