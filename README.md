# Discord Bot with Google's BARD and PALM API

This is a Discord bot designed to provide AI-generated responses and summaries using Google's BARD and PALM API. The bot can answer questions, provide summaries of URLs, and engage in conversations with users.

## Prerequisites

- Python 3.x
- discord.py library
- google-generativeai library

## Installation
### Getting started 
Head to ```https://discord.com/developers/applications``` and create a bot, following the instructions given on the site. Make note of the Discord bot token.
### Dependencies
Pip install the required dependencies:
   ```bash 
   pip install discord
   pip install google.generativeai
   pip install responses
   ```
### Setting up the environment variables
1. Create a .env file in the project directory.

2. Add the following environment variables to the file:
```bash
TOKEN=<Discord bot token>
bard_api=<BARD API key>
```
Replace ```bash <Discord bot token>``` with your Discord bot token and ```bash <BARD API key>``` with your BARD API key.

Make sure to keep your API keys and tokens secure and not share them publicly.

## Usage

### Customization 
1. Add custom commands in ```bash botTest.py``` with ```python @bot.tree.command(name='command_name')```
2. Modify LLM interaction in ```python responses.py``` under ```python run_bard```
3. Modify ```python keep_alive.py``` to keep the bot running on a server of your choice.

### Server
The bot as it stands runs on replit and uses a url pinging service to keep the bot running, you may modify this to host the bot on a cloud computing service of your choice. 
## Contact
Feel free to add tremo on discord or email arnavpd05@gmail.com for any further questioning.


This README provides a basic outline of the Discord bot using Google's BARD and PALM API. Feel free to modify and expand upon it to suit your specific needs.
