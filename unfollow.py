#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import sys

from src import InstaBot

import pandas as pd

df = pd.read_csv('acc.csv', header = 0)

user_id = 4139561924
# user_id = sys.argv[1]
# run python unfollow.py 4139561924

for i, row in enumerate(df.values):
	bot = InstaBot(df.iloc[i].ig, df.iloc[i].igpw)


	bot.unfollow(user_id)
	bot.logout()