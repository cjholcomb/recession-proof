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
# print(df_join.info())
# print(df_join.describe())
# print(df_join.head(20))
# print(df_join.describe())

# fig, ax = plt.subplots()
# x = make_nanless(df_join['growth_pcg_wage'])
# mean = x.mean()
# std = x.std
# # y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
# #      np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
# ax.hist(x, bins = 100, density = 1)
# ax.set_xlabel =('Percentage Wage Growth from Peak')
# ax.set_ylabel =('Frequency')
# ax.set_title = ('Wage Growth Distribution')
# plt.show()

fig, ax = plt.subplots()
sb.set()
x = df_join['growth_pcg_wage']
ax = sb.distplot(x, fit = norm, kde = False, color = 'c')
ax.set_title('Wage Growth Distribution')
ax.set_xlabel('Percentage Growth')
ax.set_ylabel('Occurance')
plt.show()

fig, ax = plt.subplots()
sb.set()
x = df_join[df_join['growth_pcg_empl'] < 300]['growth_pcg_empl']
ax = sb.distplot(x, fit = norm, kde = False, color = 'y')
ax.set_title('Employment Growth Distribution')
ax.set_xlabel('Percentage Growth')
ax.set_ylabel('Occurance')
plt.show()

fig, ax = plt.subplots()
sb.set()
x = df_join[df_join['recovery_wage'] > 2009]['recovery_wage']
ax = sb.distplot(x, kde = True, color = 'm')
ax.set_title('Wage Recovery Distribution')
ax.set_xlabel('Percentage Growth')
ax.set_ylabel('Occurance')
plt.show()

fig, ax = plt.subplots()
sb.set()
x = df_join[df_join['recovery_empl'] > 2009]['recovery_empl']
ax = sb.distplot(x, kde = True, color = 'g')
ax.set_title('Employment Recovery Distribution')
ax.set_xlabel('Percentage Growth')
ax.set_ylabel('Occurance')
plt.show()


df_wage[(df_wage['industry_code'] > 100000)& (df_wage[2015.0] > 0)].sort_values(by = ['growth_pcg']).dropna().head(10)







