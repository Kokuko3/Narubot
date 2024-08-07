import itertools
from os.path import exists
from pathlib import Path

from discord.ext import commands
from discord import app_commands

from utils.utils import *

class StudentCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description="Generate a sentence in either hiragana or katakana using current vocab words (and Kanji!!!)") 
    async def example(self, interaction:discord.Interaction):
        """Generate a sentence in either hiragana or katakana using current vocab words (and Kanji!!!)
        First overwrite kanji.csv and vocab.csv with the data from quizlet and merge them into one csv. 
        Then, grab all grammer points from the excel spreadsheet and add to csv. Prompt user for either 
        hirigana or katakana sentence. Send the csv and user choice to a chatgpt api call to ask for 
        an example sentence of these points

        Outputs:
            Example sentence for the user
        """