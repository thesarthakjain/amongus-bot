import discord
from discord.ext import commands
import os

token = os.environ.get('bot_token')
client = commands.Bot(command_prefix='.')
members = []                    #list of members in the game

def in_game():                  #checks whether you're playing or not
    async def predicate(ctx):
        if ctx.author in members:
            return(1)
        else:
            return(0)
    return commands.check(predicate)

def is_owner():                 #checks whether you're owner or not
    async def predicate(ctx):
        if ctx.author.id == 629276069878562817:
            return(1)
        else:
            return(0)
    return commands.check(predicate)

@client.event
async def on_ready():
    print('ready')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="thesarthakjain"))



@client.command(aliases = ['a'])
async def amongus(ctx):                 #to add yourself to a game
    if ctx.author not in members:
        try:
            await ctx.author.edit(mute = False)
        except:
            pass
        members.append(ctx.author)
        await ctx.send(f'Added {ctx.author} to the game.')
        for member in members:          #print list of players
            print(member.name)
            await ctx.send(member.name)
    else:
        members.remove(ctx.author)
        try:
            await ctx.author.edit(mute = False)
        except:
            pass
        await ctx.send(f'Removed {ctx.author} from the game.')
        for member in members:          #print list of players
            print(member.name)
            await ctx.send(member.name)


@client.command(aliases = ['m'])
@in_game()
async def mute(ctx):
    for member in members:
        try:
            await member.edit(mute = True)
        except:
            print(f"can't mute {member.name}")
    await ctx.send('Shhhhhh...')
    print('muted')


@client.command(aliases = ['um'])
@in_game()
async def unmute(ctx):
    for member in members:
        try:
            await member.edit(mute = False)
        except:
            print(f"can't unmute {member.name}")
    await ctx.send('Talk...')
    print('unmuted')


@client.command(aliases = ['list', 'l'])
async def _list(ctx):
    for member in members:          #print list of players
            print(member.name)
            await ctx.send(member.name)


@client.command(aliases = ['r'])
@is_owner()
async def remove(ctx, name = "all"):
    if name == "all":
        for member in members:
            try:    
                await member.edit(mute = False)
            except: 
                print("can't unmute")
        members.clear()
    else:
        for member in members:
            print(member.name)
            if member.name == name:
                members.remove(member)
        try:    
            await member.edit(mute = False)
        except: 
            print("can't unmute")
        for member in members:          #print list of players
            print(member.name)
            await ctx.send(member.name)

client.run(token)