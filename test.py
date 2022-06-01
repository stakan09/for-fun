from discord.ext import commands
import discord
import sys

sys.path.append(".\discord_token")
import discord_token as dscrd

Token=dscrd.discToken

from urllib.parse import quote_plus

intents = discord.Intents.all()

##superは部分共通の操作を記述するときに使う。特殊の操作はsuperを呼び出した後に書く。
class CounterBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('##'),intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

bot = CounterBot()

@bot.command()
async def log(ctx, arg1,arg2,*args):
    await ctx.send('Training:{} Weights:{} Reps:{}'.format(arg1,arg2,args))


bot.run(Token) 