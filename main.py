# インストールしたライブラリを読み込む
import discord
from discord.ext import commands
import logging
import yaml

#logの設定

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='Logs/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#fileの読み書き
with open("./conf/token.yml","r") as f:
    x = yaml.safe_load(f)
    if x["token"] == None:
        ww = input("Didn't set token.Please write here : ")
        yw = { 'title': 'TOKEN', 'token': f"{ww}"}
        with open("./conf/token.yml" , "w") as w:
            yaml.dump(yw, w, encoding='utf-8', allow_unicode=True)
            TOKEN = ww
    else:
        TOKEN = x["token"]


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
