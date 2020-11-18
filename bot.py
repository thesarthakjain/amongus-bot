import discord
from discord.ext import commands
import os

token = os.environ.get('bot_token')
client = commands.Bot(command_prefix='.')
members = []

def in_game():
        async def predicate(ctx):
            if ctx.author in members:
                return (1)
            else:
                return (0)
        return commands.check(predicate)

@client.event
async def on_ready():
    print('ready')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="thesarthakjain"))

@client.command()
async def amongus(ctx):
    if ctx.author not in members:
        members.append(ctx.author)
        await ctx.send(f'Added {ctx.author} to the game.')
        print(members)
    else:
        members.remove(ctx.author)
        await ctx.author.edit(mute = False)
        await ctx.send(f'Removed {ctx.author} from the game.')
        print(members)

@client.command()
@in_game()
async def mute(ctx):
    for member in members:
        await member.edit(mute = True)
    await ctx.send('Shhhhhh...')

@client.command()
@in_game()
async def unmute(ctx):
    for member in members:
        await member.edit(mute = False)
    await ctx.send('Talk...')

@client.command(aliases = ['list'])
async def _list(ctx):
    for member in members:
        await ctx.send(member.name)
        print(member.name)

client.run(token)