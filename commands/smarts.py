from discord.ext import commands

class Smarts(commands.Cog):
    '''A lot of smart commands'''
    def __init__(self, bot):
        self.bot = bot

    #function to calculate
    #bot.command -> commands.command
    @commands.command(name='calcular', help="Calcula uma expressão. Argumentos: Expressão")
    async def calculate_expression(self,ctx, *expression): #getting context and expression // * -> creates a tuple (Join the arguments as one)
        expression = "".join(expression) #this will join all expression with "" value after each element
        response = eval(expression) #eval() -> Evaluates the final value of the expression (Use with caution, can be used to inject commands)

def setup(bot): #setting bot for work
    bot.add_cog(Smarts(bot))