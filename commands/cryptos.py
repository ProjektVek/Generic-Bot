from discord.ext import commands
import requests

class Cryptos(commands.Cog):
    ''' Works with Cryptocurrency '''
    def __init__(self, bot): #class constructor
        self.bot = bot

    #currency conversion
    #bot.command -> commands.command
    @commands.command(help='Verifica o preço de um par na binance. Não requer argumento')
    async def binance(self,ctx, coin, base):
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

def setup(bot): #setting bot for work
    bot.add_cog(Cryptos(bot))