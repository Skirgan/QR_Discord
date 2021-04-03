import discord
import qrcode
from discord.ext import commands
bot = commands.Bot(command_prefix='!') # Вместо ! может быть любые символы

@bot.command()
async def шифр(ctx, *, text):
    qrim = qrcode.make(text)
    qrim.save('qrcode.png')
    with open('qrcode.png', 'rb') as f:
        picture = discord.File(f)
    embed = discord.Embed(title='',colour=discord.Colour.light_gray())
    embed.add_field(name=f'Шифровка в QR',value=f'**Зашифровано**: `{text}`')
    embed.set_image(url="attachment://qrcode.png")
    await ctx.send(file=discord.File('qrcode.png'),embed=embed)

bot.run('Токен')
