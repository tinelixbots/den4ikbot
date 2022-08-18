# Den4ik Bot
# Created by tretdm (aka. tinelix) at 2022-08-18 from Den4ik
# Repo: https://github.com/den4ikbot/den4ikbot
# Based on Microbot Discord bot: https://github.com/tinelix/microbot.
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher.

import os
from dotenv import load_dotenv # loading environment variables module, for install 'pip install python-dotenv'
dotenv_path = os.path.join('../', '.env')

tokens = {
    'discord_api': os.environ['DISCORD_TOKEN'],    # Discord API token from system environment
}

config = {
    'name': 'Den4ik Bot',
    'version': '0.0.1',
    'version_date': '2022-08-18',
    'prefix': '+',
    'accent_def': 0x33b5e5,
    'accent_err': 0xff4444,
    'owner_id': 951845579502280725, # Bot developer ID
    'bugs_ch': 0,  # To show a bug report in the console, set the value to 0
}

links = {
    'invite': 'https://discord.com/api/oauth2/authorize?client_id=1009762625158127636&permissions=2147862592&scope=bot',
    'support': '',
    'website': '',
    'repo': 'https://github.com/den4ikbot/den4ikbot',
}
