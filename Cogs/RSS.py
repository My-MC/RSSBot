import discord
from discord.ext import commands
import feedparser

# RSS配信用のURL
URL = 'https://hypixel.net/forums/off-topic.2/-/index.rss'

# 辞書型で取得
rss_dic = feedparser.parse(URL)

# entriesを摘出
main = rss_dic.entries

class RSS (commands.Cog):
    def __init__(self , bot):
        self.bot = bot
        self.last_member = None

    @commands.command()
    async def rss(self,ctx):
        for i in (reversed(main)):
            await ctx.send(i.title)
            await ctx.send(i.link)

def setup(bot):
    return bot.add_cog(RSS(bot))