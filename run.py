# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 21:17:19 2020

@author: Johnson
"""


import scraper as gs
import pandas as pd 

path = "C:/Users/Johnson/Documents/GitHub/Data Science Projects/ds_salary_proj/chromedriver"


df =  gs.get_jobs("data scientist", 15, False, path, 15)
df