import discord

from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix=settings['prefix'])
bot.remove_command('help')


@bot.event
async def on_ready():
    print('Bot connected')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('твоём очке пальчиком'))


@bot.command(aliases=['онлайн'])
async def online(ctx, t=None):
    while t:
        players_list = parse_main()
        await ctx.send(f'{players_list}')
    else:
        await ctx.send(f'Бот закончил свою работу')


@bot.command(aliases=['стоп'])
async def online(ctx):
    return online(False)


bot.run(settings['token'])
