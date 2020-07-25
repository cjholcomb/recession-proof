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
from data_production import *

#Some basic timelines
# plot_industries(df_wage, [101, 102], 'Wage Growth: Top Level','Year', 'Averge Weekly Wage')
# plot_industries(df_wage, range(1011, 1020), 'Wage Growth: Goods Production','Year', 'Averge Weekly Wage')
# plot_industries(df_wage, range(1020, 1030), 'Wage Growth: Services','Year', 'Averge Weekly Wage')

plot_industries(df_empl, [101, 102], 'Employment Growth: Top Level','Year', 'Total Jobs')
plot_industries(df_empl, range(1011, 1020), 'Employment Growth: Goods Production','Year', 'Total Jobs')
plot_industries(df_empl, range(1020, 1030), 'Employment Growth: Services','Year', 'Total Jobs')

#Top Performers Timelines

plot_industries(df_wage, [81130,221122,561440,453991,323111,621330,561320,515112,113210], 'Top Ten Wage Growth Industries (Gen5)','Year', 'Averge Weekly Wage')
plot_industries(df_wage, [621491, 812113, 485119, 111191, 519130, 923140, 454111, 483112, 624120], 'Top Ten Employment Growth Industries (Gen5)','Year', 'Quarterly Employment')

# sb.set()
# fig, ax = plt.subplots()
# x = df_join[df_join['industry_code_wage'] > 100000]['growth_pcg_wage']
# ax = sb.distplot(x, fit = norm, kde = False, color = 'c')
# ax.set_title('Wage Growth Distribution')
# ax.set_xlabel('Percentage Growth')
# ax.set_ylabel('Occurance')
# plt.show()

# fig, ax = plt.subplots()
# sb.set()
# x = df_join[(df_join['industry_code_wage'] > 10000) & (df_join['growth_pcg_empl'] < 300 )]['growth_pcg_empl']
# ax = sb.distplot(x, fit = norm, kde = False, color = 'y')
# ax.set_title('Employment Growth Distribution')
# ax.set_xlabel('Percentage Growth')
# ax.set_ylabel('Occurance')
# plt.show()

# fig, ax = plt.subplots()
# sb.set()
# x = df_join[(df_join['industry_code_wage'] > 10000) & (df_join['recovery_wage'] >= 2009)]['recovery_wage']
# ax = sb.distplot(x, kde = True, color = 'm')
# ax.set_title('Wage Recovery Distribution')
# ax.set_xlabel('Percentage Growth')
# ax.set_ylabel('Occurance')
# plt.show()

# fig, ax = plt.subplots()
# sb.set()
# x = df_join[(df_join['industry_code_wage'] > 10000) & (df_join['recovery_empl'] >= 2009)]['recovery_empl']
# ax = sb.distplot(x, kde = True, color = 'g')
# ax.set_title('Employment Recovery Distribution')
# ax.set_xlabel('Percentage Growth')
# ax.set_ylabel('Occurance')
# plt.show()

