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
async def helping(ctx, page = 1):
    if page == 1:
        await ctx.send("All commands(page 1):\n$helping:Show all the commands.\n$hello:I just say hello:).\n$plus (number 1) (number2):Adds two numbers and i write the answer\n(write your numbers after $plus also with commands like $minus and $multiply).\nType helping 2 too see more")
    elif page == 2:
        await ctx.send("All commands(page 2):\n$minus (number 1) (number2):It dose exactly what you think\n$multiply (number 1) (number2):It wasn't added yet")
#command for $plus
@bot.command()
async def plus(ctx, l1 = 0, l2 = 0):
    await ctx.send(f"It equals:{l1 + l2}.")
#command for $minus
@bot.command()
async def minus(ctx, l1 = 1, l2 = 0):
    await ctx.send(f"It equals:{l1 - l2}")

bot.run(">INSERT TOKEN HERE<")