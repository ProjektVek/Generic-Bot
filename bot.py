import datetime #importing datetime
import discord #importing discord.py library
from discord.ext import commands, tasks #importing commands and tasks from extensions
import requests #library to use api's
from decouple import config

from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound

bot = commands.Bot("!") #Bot invocation command

TOKEN = config("TOKEN") 
bot.run(token) #running the bot