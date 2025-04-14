import discord
from discord.ext import commands
from config import TOKEN
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}! You can send a game logo image and i can tell its name!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'./images/{file_name}')
            result = get_class("./kerasmodel.h5", "./labels_txt", f'./images/{file_name}')[0]

            if result == "FIFA\n":
                await ctx.send("This game is FIFA. Click this link to learn more: https://tr.wikipedia.org/wiki/EA_Sports_FC_25")
            if result == "Fortnite\n":
                await ctx.send("This game is Fortnite. Click this link to learn more: https://tr.wikipedia.org/wiki/Fortnite")
            if result == "LoL\n":
                await ctx.send("This game is League of Legends. Click this link to learn more: https://en.wikipedia.org/wiki/League_of_Legends")
            if result == "Minecraft\n":
                await ctx.send("This game is Minecraft. Click this link to learn more: https://tr.wikipedia.org/wiki/Minecraft   (dev note: chicken jockey)")
            if result == "Valorant\n":
                await ctx.send("This game is Valorant. Click this link to learn more: https://tr.wikipedia.org/wiki/Valorant")

            await ctx.send(f"Saved the image to ./images/{file_name}")
    else:
        await ctx.send("You forgot to upload the image")

bot.run("TOKEN")