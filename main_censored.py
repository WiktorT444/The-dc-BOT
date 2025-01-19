import discord
from discord.ext import commands
#intents for bot
intents = discord.Intents.default()
intents.message_content = True
#var for bot and command prefix    v   You can change it here
bot = commands.Bot(command_prefix='$', intents=intents)
#Who you logged in as?
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
#commands
#command for $hello
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello;)I am {bot.user} use $help to see all commands.")
#command for $help1
@bot.command()
async def help1(ctx):
    await ctx.send("All commands:\n$help:Show all the commands.\n$hello:I just say hello:).\n$plus:Adds two numbers and i write the answer(write your numbers after $plus also with commands like $minus and $multiply).\n$minus:It dose exactly what you think(not added yet)\n$multiply:It wasn't added yet")
#command for $plus
@bot.command()
async def plus(ctx, l1 = 0, l2 = 0):
    await ctx.send(f"It equals:{l1 + l2}.")

bot.run(">INSERT TOKEN HERE<")