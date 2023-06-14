import discord
import responses
import os
from keepalive import keep_alive
from discord.ext import commands
from discord import app_commands

help = 'Hey! This bot was developed by Tremo and is intended to be your personal AI. Try asking a question with "$" or send a url for a summary! If you would like your inquiry answered via DM, simply start your request with a ? as well. Feel free to send Tremo feedback on his amazing Machine Learning Model.'
async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():

    bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
    
    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running!')
        try: 
          synced = await bot.tree.sync()
          print(f'Synced {len(synced)} command(s)')
        except Exception as e:
          print(e)

  
    @bot.tree.command(name='help', description='help command for bot')
    async def hello(interaction: discord.Interaction):
      await interaction.response.send_message(help, ephemeral=True)
      await on_command(interaction, 'NA', help)
      
    
    @bot.tree.command(name='summary')
    @app_commands.describe(url='send in a url to get a summary')
    async def summary(interaction: discord.Interaction, url: str):
      response = responses.run_bard(url,True)
      await interaction.response.send_message('Here is a summary of ' + url + '\n' + response)
      await on_command(interaction, summary)

    @bot.tree.command(name='question')
    @app_commands.describe(question='question to ask bot')
    async def question(interaction: discord.Interaction, question: str):
      response = responses.run_bard(question,False)
      await interaction.response.send_message(response)
      await on_command(interaction, question, response)

    
    async def on_command(interaction: discord.Interaction, prompt, response):
      # print who called the command
      print(f'{interaction.user} called {interaction.command.name} with prompt "{prompt}" in "{interaction.guild}" at {interaction.created_at.ctime()}')
      print(f'Response: {response} \n')

   
    @bot.event
    async def on_message(message):
        # if bot types
        if message.author == bot.user:
            return

        # identify who sent message
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        # for console purposes
        print(f'{username} said: "{user_message}" ({channel})')
        
  
    my_secret = os.environ['TOKEN']
    keep_alive()
    bot.run(my_secret)

    

