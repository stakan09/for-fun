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
        super().__init__(command_prefix=commands.when_mentioned_or('$'),intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

class HogeButton(discord.ui.View):
    def __init__(self,args):
        super().__init__()

        for txt in args:
            self.add_item(HugaButton(txt))

class HugaButton(discord.ui.Button):
    def __init__(self,txt:str):
        super().__init__(label=txt,style=discord.ButtonStyle.red)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'{interaction.user.display_name}は{self.label}を押しました')

class HogeList(discord.ui.View):
    def __init__(self,args):
        super().__init__()
        self.add_item(HugaList(args))

class HugaList(discord.ui.Select):
    def __init__(self,args):

        options=[]
        for item in args:
            options.append(discord.SelectOption(label=item, description=''))
        
        super().__init__(placeholder='', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'{interaction.user.name}は{self.values[0]}を選択しました')
        
bot = CounterBot()

@bot.command()
async def makeButton(ctx: commands.context,*args):
    await ctx.send('Press!', view=HogeButton(args))

@bot.command()
async def makeList(ctx: commands.context,*args):
    await ctx.send('Press!', view=HogeList(args))

bot.run(Token)