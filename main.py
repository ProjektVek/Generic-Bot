import datetime #importing datetime
import discord #importing discord.py library
from discord.ext import commands, tasks #importing commands and tasks from extensions
import requests #library to use api's

bot = commands.Bot("!") #Bot invocation command

@bot.event #on bot event
async def on_ready(): #when bot is ready
    print('Im Ready!')
    print(f'Logged as {bot.user}')
    current_time.start() #Starting task

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    """
    #Deleting bad word message
    if "palavrão" in message.content:
        await massage.channel.send(f'Por favor, {message.author.name}, não ofenda os demais usuários!')

        await message.delete()
    """

    await bot.process_commands(message)

@bot.command(name='oi') #name -> text after comment
async def say_hello(ctx): #function to say hello | ctx = context
    name = ctx.author.name

    response = "Olá, " + name

    await ctx.send(response)

#function to calculate
@bot.command(name='calcular')
async def calculate_expression(ctx, *expression): #getting context and expression // * -> creates a tuple (Join the arguments as one)
    expression = "".join(expression) #this will join all expression with "" value after each element
    response = eval(expression) #eval() -> Evaluates the final value of the expression (Use with caution, can be used to inject commands)

#currency conversion
@bot.command()
async def binance(ctx, coin, base):
    try:
        response = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}')
        data = response.json()
        price = data.get("price")

        if price:
            await ctx.send(f'O valor do par {coin}/{base} é {price}')
        else:
            await ctx.send(f'O par {coin}/{base} é inválido')
    except Exception as error:
        await ctx.send("Ops... deu algum erro!")
        print(error)

#sending a private message
@bot.command(name="segredo")
async def secret(ctx):
    try:
        await ctx.author.send("Walkthrough do Tutorial da ByLearn")
    except discord.errors.Forbidden:
        await ctx.send("Não posso te contar o segredo, habilite receber mensagens de qualquer pessoa do servidor (Opções>Privacidade)")

#getting role on reaction
@bot.command()
async def on_reaction_add(reaction, user):
    print(reaction.emoji)
    if reaction.emoji == ":thumbsup:":
        role = user.get_role(role1_id)
        await user.add_roles(role)
    elif reaction.emoji == ":poop:":
        role = user.get_role(role2_id)
        await user.add_roles(role)

#working with embeds
@bot.command(name = 'foto')
async def get_random_image(ctx):
    url_image = "https://picsum.photos/1920/1080"

    embed = discord.Embed(
        title = "Resultado da busca de imagem",
        description = "PS: a busca é totalmente aleatória",
        color = 0x0000FF
    )

    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.set_footer(text="Feito por" + bot.user.name, icon_url=bot.user.avatar_url)

    embed.add_field(name="API", value="Usamos a API do https://picsum.photos")
    embed.add_field(name="Parâmetros", value="{largura}/{altura}")
    
    embed.add_field(name="Exemplo", value=url_image, inline=False)

    embed.set_image(url=url_image)

    await ctx.send(embed=embed)

@tasks.loop(seconds=10) #ten seconds
async def current_time():
    now = datetime.datetime.now()

    now = now.strfttime("%d/%m/%Y às %H:%M:%S")

    channel = bot.get_channel("Insert ID of Channel Here")

    await channel.send ("Data atual: " + now)

token = "Defining Token"
bot.run(token) #running the bot