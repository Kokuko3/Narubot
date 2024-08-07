#!/usr/bin/env python
from os.path import exists
from pathlib import Path
import pandas as pd


from utils.utils import *

def example_sentence():
    df = pd.read_excel("~/git/Narubot/assets/vocab.xlsx")
    print(df)

example_sentence()