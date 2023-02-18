import discord
import os

token = "MTA3NjQ4NzkyNjc4OTE4NTYyNg.GvjbEv.GC4DuOmt-nJeqvduNGBSDYJ3PIc_x7HHEjxUXs"
client = discord.Client(intents=discord.Intents.default())
@client.event
async def on_ready():
    print("로그인되었습니다!")
    print(client.user.name)
    print(client.user.id)
    print("============================")

client.event
async def on_message(message):
   if message.content == '핑':
        await message.channel.send('퐁')

   if message.content == "?":
        embed=discord.Embed(color=0xff00, title="제목", description="설명", timestamp=message.created_at)
        await message.channel.send(embed=embed)

client.run(token)
