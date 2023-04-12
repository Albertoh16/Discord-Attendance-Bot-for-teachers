import os; import discord; import gspread
from discord.ext import commands; from datetime import date; import time
#from flask import Flask; from threading import Thread

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='-', intents=intents)
'''app = Flask('')
sa = gspread.service_account(filename="attendanceSheet.json")
sh = sa.open("Attendance Sheet")
sh.worksheet("Sheet1")

@app.route('/')
def home():
    return "I'm alive"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()'''
	
@bot.event
async def on_ready():
	print('We have logged in as ' + str(bot.user))
	for server in bot.guilds:
		for channel in server.channels:
			if str(channel.type) == 'text':
				'''await bot.get_channel(channel.id).send("Hello, I am the Class Discord Attendance Checker! Make sure that before class ends to use the -attendance command to record everybody's presence!"); break'''
	
@bot.command()
async def auto(ctx):
	lst = []
	for server in bot.guilds:
		if ctx.message.guild.id == server.id:
			name = "sheets/" + str(server) + " attendance: " + str(date.today())[5:] + "-" + str(date.today())[:4] + ".txt"
			f = open(name, "w")
			for member in ctx.message.guild.members:
				if member.voice is not None and str(member.display_name) != "Attendance Checker": lst.append(str(member.display_name) + ": PRESENT\n")
				elif member.voice is None and str(member.display_name) != "Attendance Checker": lst.append(str(member.display_name) + ": ABSENT\n")
			for i in sorted(lst): f.write(i)
			f.close(); await ctx.author.send(file=discord.File(name)); os.remove(name)

@bot.command()
async def manual(ctx, reaction):
	lst = []
	time.sleep(10)
	await bot.get_channel(ctx.message.channel.id).send(reaction.users(ctx))
#keep_alive()
bot.run(os.environ['token'])