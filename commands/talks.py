from discord.ext import commands
import discord

class Talks(commands.Cog):
    ''' Talks with user '''
    def __init__(self, bot):
        self.bot = bot

    #bot.command -> commands.command
    #sending hello
    @commands.command(name='oi', help="Envia um oi (Não requer argumento)") #name -> text after comment
    async def say_hello(self,ctx): #function to say hello | ctx = context
        name = ctx.author.name

        response = "Olá, " + name

        await ctx.send(response)

    #sending a private message
    @commands.command(name="segredo", help='Envia uma mensagem no privado')
    async def secret(self,ctx):
        try:
            await ctx.author.send("Walkthrough do Tutorial da ByLearn")
        except discord.errors.Forbidden:
            await ctx.send("Não posso te contar o segredo, habilite receber mensagens de qualquer pessoa do servidor (Opções>Privacidade)")

def setup(bot): #setting bot for work
    bot.add_cog(Talks(bot))