import discord
from discord.ext import commands
import feedparser

class RSS (commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.last_member = None

    @commands.command()
    async def rss(self,ctx,url):
        rss_dic = feedparser.parse(url)
        main = rss_dic.entries
        for i in (reversed(main)):
            embed=discord.Embed(title=i.title, description=i.link, color=0x00008b)
            embed.set_footer(text=i.published)
            await ctx.send(embed=embed)

def setup(bot):
    return bot.add_cog(RSS(bot))