# インストールしたライブラリを読み込む
import discord
from discord.ext import commands
import logging

#logの設定

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='Logs/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#fileの読み書き
r = open('./conf/token.txt')
r_str = r.readline()
r.close()

# 自分のBOTのtokenの定義
TOKEN = r_str

# 接続に必要なオブジェクトを生成
bot = commands.Bot(command_prefix="!")

# 起動時に動作する処理
@bot.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('='*44)
    print('ログインしました')
    print('-'*44)
    print("TOKEN  =  " + TOKEN)
    print('='*44)

bot.load_extension("Cogs.RSS")
bot.load_extension("Cogs.about")
bot.run(TOKEN)


