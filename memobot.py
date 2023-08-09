import os
import discord
from discord.ext import commands

os.environ['SSL_CERT_FILE'] = '/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/certifi/cacert.pem'

intents = discord.Intents.default()
intents.message_content = True  # Enable message content in intents
intents.presences = True  # Enable presence intent
intents.members = True    # Enable server members intent

bot = commands.Bot(command_prefix='!', intents=intents)

# Dictionary to store saved messages categorized by topics
saved_messages = {}

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def save(ctx, topic: str, *, message: str):
    """
    Command to save a message with a given topic.
    Usage: !save <topic> <message>
    """
    if topic.lower() not in saved_messages:
        saved_messages[topic.lower()] = []
    saved_messages[topic.lower()].append(message)
    await ctx.send(f'Message saved under topic "{topic}"!')

@bot.command()
async def show(ctx, topic: str):
    """
    Command to show saved messages for a given topic.
    Usage: !show <topic>
    """
    topic = topic.lower()
    if topic in saved_messages:
        messages = saved_messages[topic]
        if messages:
            response = '\n'.join(messages)
        else:
            response = f'No messages found for topic "{topic}"'
    else:
        response = f'No messages found for topic "{topic}"'
    await ctx.send(response)

@bot.command()
async def categories(ctx):
    """
    Command to list all available categories (topics).
    Usage: !categories
    """
    categories = ', '.join(saved_messages.keys())
    if categories:
        await ctx.send(f'Available categories: {categories}')
    else:
        await ctx.send('No categories found.')

@bot.command()
async def delete(ctx, topic: str):
    """
    Command to delete a specific topic and its saved messages.
    Usage: !delete <topic>
    """
    topic = topic.lower()
    if topic in saved_messages:
        del saved_messages[topic]
        await ctx.send(f'Topic "{topic}" and its messages have been deleted.')
    else:
        await ctx.send(f'No messages found for topic "{topic}"')

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('MTEzNzc5MDY2MzIzMzEzMDUxOQ.GYXUib.Dd7SKq0gHAPjtX8itDyfveHfEVKWqr0Yyb7jLI')
