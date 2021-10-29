from discord.ext import commands, tasks
import discord #importing discord.py library
import datetime #importing datetime
from tasks.tasks import current_time

from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound

class Manager(commands.Cog):
    '''Manages the bot'''

    def __init__(self,bot):
        self.bot = bot

    #bot.event -> commands.Cog.listener
    @commands.Cog.listener #on bot event
    async def on_ready(self): #when bot is ready
        print('Im Ready!')
        print(f'Logged as {self.bot.user}')
        current_time.start() #Starting task

    @commands.Cog.listener
    async def on_message(self,message):
        if message.author == self.bot.user:
            return

        """
        #Deleting bad word message
        if "palavrão" in message.content:
            await massage.channel.send(f'Por favor, {message.author.name}, não ofenda os demais usuários!')

            await message.delete()
        """

    #error treatment
    @commands.Cog.listener
    async def on_comand_error(self,ctx, error):
        if isinstance(error,MissingRequiredArgument): #if a required argument is identified
            await ctx.send('Favor enviar todos os argumentos')
        elif isinstance(error,CommandNotFound):
            await ctx.send("O comando não existe")
        else:
            raise error

def setup(bot):
    bot.add_cog(Manager(bot))