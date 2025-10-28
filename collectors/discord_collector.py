import discord

TOKEN = "your_discord_bot_token"
client = discord.Client()

messages = []

@client.event
async def on_message(message):
    if not message.author.bot:
        messages.append({
        "platform": "discord",
        "user": str(message.author),
        "timestamp": str(message.created_at),
        "text": message.content,
        "url": f"https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}"
    })