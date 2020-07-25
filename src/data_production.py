import pandas as pd
import matplotlib.pyplot as plt
import math
import scipy as scipy
from scipy.stats import norm
import numpy as np
import seaborn as sb
from varname import nameof
import io
from helper_functions import *
from lookups import *


#form the dataframes
df = import_all(recession_years)
df_wage = create_df_wage(df)
df_wage = derive_wage_vars(df_wage)
df_empl = create_df_empl(df)
df_empl = derive_empl_vars(df_empl)
df_join = join_empl_wage(df_wage, df_empl)
#print(df_join.info())
# print(df_join.describe())
# print(df_join.head(20))
# print(df_join.describe())

# Grab the top performers from generation 5 (Other generations commented out)

df_wage[(df_wage['industry_code'] > 100000)& (df_wage[2015.0] > 0)].sort_values(by = ['growth_pcg']).dropna().tail(10).to_csv('data/top_5_wagegrowth.csv')
# df_wage[(df_wage['industry_code'] > 10000) & (df_wage['industry_code'] < 100000)& (df_wage[2015.0] > 0)].sort_values(by = ['growth_pcg']).dropna().tail(5).to_csv('top_5_wagegrowth.csv', mode = 'a', header= False)
# df_wage[(df_wage['industry_code'] > 1000) & (df_wage['industry_code'] < 10000)& (df_wage[2015.0] > 0)].sort_values(by = ['growth_pcg']).dropna().tail(5).to_csv('top_5_wagegrowth.csv', mode = 'a', header= False)
# df_wage[(df_wage['industry_code'] > 100) & (df_wage['industry_code'] < 1000)& (df_wage[2015.0] > 0)].sort_values(by = ['growth_pcg']).dropna().tail(5).to_csv('top_5_wagegrowth.csv', mode = 'a', header= False)
# df_wage[(df_wage['industry_code'] > 10) & (df_wage['industry_code'] < 100)& (df_wage[2015.0] > 0)].sort_values(by = ['growth_pcg']).dropna().tail(3).to_csv('top_5_wagegrowth.csv', mode = 'a', header= False)

df_empl[(df_empl['industry_code'] > 100000)& (df_empl[2015.0] > 0)].sort_values(by = ['growth_pcg']).dropna().tail(10).to_csv('data/top_5_emplgrowth.csv')
# df_empl[(df_empl['industry_code'] > 10000) & (df_empl['industry_code'] < 100000)& (df_empl[2015.0] > 0)].sort_values(by = ['growth_pcg']).dropna().tail(5).to_csv('top_5_emplgrowth.csv', mode = 'a', header= False)
# df_empl[(df_empl['industry_code'] > 1000) & (df_empl['industry_code'] < 10000)& (df_empl[2015.0] > 0)].sort_values(by = ['growth_pcg']).dropna().tail(5).to_csv('top_5_emplgrowth.csv', mode = 'a', header= False)
# df_empl[(df_empl['industry_code'] > 100) & (df_empl['industry_code'] < 1000)& (df_empl[2015.0] > 0)].sort_values(by = ['growth_pcg']).dropna().tail(5).to_csv('top_5_emplgrowth.csv', mode = 'a', header= False)
# df_empl[(df_empl['industry_code'] > 10) & (df_empl['industry_code'] < 100)& (df_empl[2015.0] > 0)].sort_values(by = ['growth_pcg']).dropna().tail(3).to_csv('top_5_emplgrowth.csv', mode = 'a', header= False)














