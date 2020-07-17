# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 21:17:19 2020

@author: Johnson
"""


import scraper as gs
import pandas as pd 




df =  gs.get_jobs("data scientist", 15, False, 15)
df