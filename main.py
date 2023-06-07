import discord
from discord.ext import commands

TOKEN = "YOUR DISCORD BOT TOKEN"

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True

# Here you can set your prefix
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("Bot connected")


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 10):
    try:
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'Deleted {amount} messages.', delete_after=5)
    except:
        await ctx.send(f'Determine the amount msg to delete. "!clear 10"', delete_after=10)

bot.run(TOKEN)
