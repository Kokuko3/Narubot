import itertools
from os.path import exists
from pathlib import Path

from discord.ext import commands
from discord import app_commands
import pandas as pd

from utils.utils import *

async def setup(bot:commands.Bot):
    await bot.add_cog(StudentCommands(bot))

class StudentCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="example", description="Generate a sentence in either hiragana or katakana using current vocab words (and Kanji!!!)") 
    async def example(self, interaction:discord.Interaction):
        """Generate a sentence in either hiragana or katakana using current vocab words (and Kanji!!!)
        First overwrite kanji.csv and vocab.csv with the data from quizlet and merge them into one csv. 
        Then, grab all grammer points from the excel spreadsheet and add to csv. Prompt user for either 
        hirigana or katakana sentence. Send the csv and user choice to a chatgpt api call to ask for 
        an example sentence of these points

        Outputs:
            Example sentence for the user
        """
        df = pd.read_csv("~/git/Narubot/assets/vocab.csv")
        message = str(df)
        await interaction.response.send_message(message)
        