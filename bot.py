import os
from discord.ext import commands #importing commands and tasks from extensions
from decouple import config #used to get .env secret

bot = commands.Bot("!") #Bot invocation command

def load_cogs(bot):
    bot.load_extensions("manager")
    bot.load_extensions("tasks.dates")

    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extensions(f'commands.{cog}')

TOKEN = config("TOKEN") 
bot.run(token) #running the bot


'''
import os

for file in os.listdir('commands'):
    print(file[:-3]) #getting file name, stoping at third character from last to first
    cog = file[:-3]
    bot.load_extensions(f'commands.{cog}')
'''