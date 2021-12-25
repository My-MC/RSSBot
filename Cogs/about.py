import discord
from discord.ext import commands

class about (commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.last_member = None

    @commands.command()
    async def about(self,ctx):
        embed=discord.Embed(title="About", description="My Util Bot", color=0x4682b4)
        embed.add_field(
            name="制作者", 
            value="My#2759",
            )
        embed.add_field(
            name="ソースコード", 
            value="https://github.com/My-MC/RSSBot",
            )
        embed.add_field(
            name="使用している言語",
            value="```Python3.5.9```",
            )
        embed.add_field(
            name="使っているモジュール" ,
            value="[discord.py](https://github.com/Rapptz/discord.py) , [feedparser](https://pypi.org/project/feedparser)",
            )
        embed.set_footer(text="Created by My#2759")
        await ctx.send(embed=embed)



def setup(bot):
    return bot.add_cog(about(bot))