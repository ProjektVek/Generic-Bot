from discord.ext import commands

class Reactions(commands.Cog):
    ''' Works with Reactions '''
    def __init__(self, bot):
        self.bot = bot

    #Events -> commands.Cog.listener
    @commands.Cog.listener
    async def on_reaction_add(self ,reaction, user):
        print(reaction.emoji)
        if reaction.emoji == ":thumbsup:":
            role = user.get_role(role1_id)
            await user.add_roles(role)
        elif reaction.emoji == ":poop:":
            role = user.get_role(role2_id)
            await user.add_roles(role)

def setup(bot): #setting bot for work
    bot.add_cog(Reactions(bot))