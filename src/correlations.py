import scipy.stats as sp

from helper_functions import *
from lookups import *
from data_production import *


df_nanless = df_join.dropna()

print(sp.pearsonr(df_join['recovery_wage'],df_join['recovery_empl']))

print(sp.pearsonr(df_nanless['recovery_wage'],df_nanless['growth_pcg_empl'].dropna()))

print(sp.pearsonr(df_nanless['growth_pcg_wage'],df_nanless['growth_pcg_empl']))

print(sp.pearsonr(df_nanless['growth_pcg_wage'],df_nanless['recovery_empl']))

print(sp.pearsonr(df_nanless['recovery_wage'],df_nanless['growth_pcg_wage']))

print(sp.pearsonr(df_nanless['recovery_empl'],df_nanless['growth_pcg_empl']))