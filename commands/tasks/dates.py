from discord.ext import commands,tasks
import datetime

class Dates(commands.Cog):
    ''' Works with Dates '''
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.current_time.start()

    @tasks.loop(seconds=10) #ten seconds
    async def current_time(self):
        now = datetime.datetime.now()

        now = now.strfttime("%d/%m/%Y às %H:%M:%S")

        channel = self.bot.get_channel("Insert ID of Channel Here")

        await channel.send ("Data atual: " + now)



def setup(bot): #setting bot for work
    bot.add_cog(Dates(bot))