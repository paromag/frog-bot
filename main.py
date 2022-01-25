import discord
from discord.ext import commands 
import json 
import requests
import io
import json
from PIL import Image, ImageFont, ImageDraw

TOKEN = 'OTEyNDI0NDI3MzczODg3NDg4.YZvvdw.FoMA7pir-alLJTp67eUZDZ6AXJ8'

bot = commands.Bot(command_prefix='/')
bot.remove_command('help')

intents = discord.Intents.default()
intents.members = True


@bot.command()
async def wink(ctx):
    response = requests.get('https://some-random-api.ml/animu/wink') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Вжык') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed 

@bot.command()
async def pat(ctx):
    response = requests.get('https://some-random-api.ml/animu/pat') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Вж') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed  
@bot.command()
async def help(ctx):
	emb = discord.Embed(color = 0xff9900, title='Команды')

	emb.add_field(name='/wink', value='Мигалка тян')
	emb.add_field(name='/pat', value='Гладилка')
	emb.add_field(name='/card', value='Гладилка')

	await ctx.send(embed=emb)
@bot.command(aliases=['me','Me','Card','card'])
async def card_user(ctx):
	await ctx.channel.purge(limit=1)
	img = Image.new('RGBA', (400, 200), '#2F3136')
	url = str(ctx.author.avatar_url)[:-10]

	response = requests.get(url, stream = True)
	response = Image.open(io.BytesIO(response.content))
	response = response.convert('RGBA')
	response = response.resize((100, 100), Image.ANTIALIAS)

	img.paste(response, (15, 15, 115, 115))

	idraw = ImageDraw.Draw(img)
	name = ctx.author.name
	tag = ctx.author.discriminator 

	headline = ImageFont.truetype('arial.ttf',size = 20)
	undertext = ImageFont.truetype('arial.ttf',size = 12)

	idraw.text((145, 15), f'{name}#{tag}', font = headline)
	idraw.text((145, 50), f'ID: {ctx.author.id}', font = undertext)

	img.save('user_card.png')



	await ctx.send(file = discord.File(fp = 'user_card.png')) 

@bot.command()
async def all(ctx):
    for Every_Member in ctx.guild.members:
        if Every_Member.bot != True:
            await Every_Member.send('Сосать доуничи')




	
	







bot.run(TOKEN)