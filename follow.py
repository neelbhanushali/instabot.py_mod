#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

from src import InstaBot

import pandas as pd

df = pd.read_csv('acc.csv', header = 0)

user_id = 4139561924

for i, row in enumerate(df.values):
	bot = InstaBot(df.iloc[i].ig, df.iloc[i].igpw)


	bot.follow(user_id)
	bot.logout()