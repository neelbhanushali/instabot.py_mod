#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import sys

from src import InstaBot

import pandas as pd

df = pd.read_csv('acc.csv', header = 0)

media_id = 1753858169015406083
# media_id = sys.argv[1]
# run python like.py 1753858169015406083

for i, row in enumerate(df.values):
	bot = InstaBot(df.iloc[i].ig, df.iloc[i].igpw)


	bot.like(media_id)
	bot.logout()