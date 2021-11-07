# インストールした discord.py等のライブラリを読み込む
import discord
from discord.ext import commands
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='Logs/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# 自分のBOTのtokenの定義
TOKEN = 'Please type your token'

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

# メッセージ受信時に動作する処理
@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

    await bot.process_commands(message)

bot.load_extension("Cogs.RSS")
bot.run(TOKEN)


