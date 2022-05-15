# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    channel = client.get_channel(810821992647360513)
    view = discord.ui.View()

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

@bot.command()
async def makeButton(ctx: commands.context,*args):
    await ctx.send('Press!', view=HogeButton(args))

client.run('OTc1MjM0NTg3NDE0Mzg4NzQ3.G-WPfP.JlhSaD82yyn4fP58KajvZgwvwgmhrvPjzNt_jA')