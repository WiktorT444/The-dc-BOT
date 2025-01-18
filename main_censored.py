import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello;)")

@bot.command()
async def help(ctx):
    await ctx.send("All commands:\n$help:Show all the commands.\n$hello:I just say hello:).\n$plus:Adds two numbers and i write the answer(not added yet).\n$minus:It dose exactly what you think(not added yet)\n$multiply:It wasn't added yet")


bot.run(">INSERT TOKEN HERE<")