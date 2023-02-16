import os

import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import responses
import youtubeSearch as YT
import youtube_dl

async def send_message(message, user_message, is_private = False):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    TOKEN = 'MTA3NTYxNjc2NDk2MjAxMzI1Nw.Grd6_w.tVO1k5Wuai5wTvMQ6UsRq7Q0r5JEdSckviqSo8'
    client = commands.Bot(command_prefix = '-', intents=intents)

    @client.event
    async def on_ready():
        print('------------------------------')
        print(f'{client.user} is now running!')
        print('------------------------------')

    @client.command(name='play', aliases=['p'], pass_context = True)
    async def play(ctx, *, search_term:str = None):
        if ctx.author.voice:
            voice = None
            if search_term == None:
                await ctx.send('No song specified.')
                return
            if not ctx.voice_client:
                channel = ctx.message.author.voice.channel
                voice = await channel.connect()
            else:
                voice = ctx.guild.voice_client
            
            url = YT.singleSearch(search_term)
            server = ctx.message.server
            voice_client = client.voice_clients(server)
            player = await voice_client.

            source = FFmpegPCMAudio('song.mp3')
            voice.play(source)
        else:
            await ctx.send('You must be in a voice channel to play a song!')
            return

    @client.command(pass_context = True)
    async def leave(ctx):
        if ctx.voice_client:
            await ctx.guild.voice_client.disconnect()
        else:
            await ctx.send("I'm not in a voice channel!")

    @client.command(pass_context = True)
    async def pause(ctx):
        voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send('No audio playing...')

    @client.command(pass_context = True)
    async def resume(ctx):
        voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send('No audio paused...')

    @client.command(pass_context = True)
    async def stop(ctx):
        voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
        voice.stop()

    client.run(TOKEN)