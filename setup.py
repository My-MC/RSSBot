from setuptools import setup

setup()

TOKEN = input("Please type your bot token : ")

w = open('./conf/token.txt','w')
w.write(TOKEN)
w.close()