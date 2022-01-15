from setuptools import setup
import os

setup()

path1 = "./conf/token-origin.yml"
path2 = "./conf/token.yml"
os.rename(path1 , path2)