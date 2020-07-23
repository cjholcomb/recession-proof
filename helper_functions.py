import pandas as pd
import matplotlib.pyplot as pyplot
import math
import scipy as scipy
import numpy as np
from varname import nameof
from src.lookups import *

def import_one(year):
    filepath = 'data/' + str(year) + '.csv'
    df = pd.read_csv(filepath, dtype = schema_dict)
    df = df.drop(drop_list, axis = 1)
    df['industry_code'] = df['industry_code'].str.replace('31-33','31')
    df['industry_code'] = df['industry_code'].str.replace('44-45','44')
    df['industry_code'] = df['industry_code'].str.replace('48-49','48').astype('int32')
    df = add_qtrid(df)
    return df

def import_all(years):
    df = import_one(years[0])
    for year in years[1:]:
        df = df.append(import_one(year))
    df['industry_code'] = df['industry_code'].str.replace('31-33','31')
    df['industry_code'] = df['industry_code'].str.replace('44-45','44')
    df['industry_code'] = df['industry_code'].str.replace('48-49','48').astype('int32')
    df = add_qtrid(df)
    return df

def export_info(df):
    strfile = str(nameof(df)) + '_info.txt'
    buffer = io.StringIO()
    df.info(buf=buffer)
    info = buffer.getvalue()
    with open(strfile, "a", encoding="utf-8") as f: 
        f.write(info)
        f.close
    strfile = str(nameof(df)) + '_desc.csv'
    print(df.describe().to_csv(strfile))
    strfile = str(nameof(df)) + '_freq.csv'
    print(df['industry_title'].value_counts().to_csv(strfile))

def add_qtrid(df):
    df['qtrid'] = df['year'] + (df['qtr']/4)
    return df

def add_dupecheck(df):
    df['industry_code'] = df['industry_code'].str.replace('-','').astype('int32')
    df['dupecheck'] = ((df['industry_code']) * 10000)+ df['qtrid']
    return df

def add_yearcheck(df):
    df['yearcheck'] = ((df['industry_code']) * 10000)+ df['year']
    return df

def create_df_firm(df):
    df_firm = df.pivot_table(columns = 'qtrid', values = 'qtrly_estabs_count', index = ['industry_code', 'industry_title'], aggfunc = np.max)
    df_firm = df_firm.reset_index()
    return df_firm
    
def create_df_empl(df):
    df_empl = df.pivot_table(columns = 'qtrid', values = 'qtrly_estabs_count', index = ['industry_code', 'industry_title'], aggfunc = np.max)
    df_empl = df_empl.reset_index()
    return dfempl

def create_df_wage(df):
    df_wage = df.pivot_table(columns = 'qtrid', values = 'avg_wkly_wage', index = ['industry_code', 'industry_title'], aggfunc = np.min)
    df_wage = df_wage.reset_index()


def plot_industries(df, lst):
    fig, ax = plt.subplots()
    x = df.columns.values[2:]
    for indus in lst:
        if indus in all_industries.keys():
            y = df[df['industry_code'] == indus].values[0][2:]
            label = df[df['industry_code'] == indus].values[0][1]
            ax.plot(x,y,label = label)
    ax.legend(bbox_to_anchor = (1,1), fancybox = True)
    plt.show();

def peaks(industry_code):
    empl_peak = max(df_empl[df_empl['industry_code'] == industry_code].values[0][2:10])
    firm_peak = max(df_firm[df_empl['industry_code'] == industry_code].values[0][2:10])
    wage_peak = max(df_wage[df_empl['industry_code'] == industry_code].values[0][2:10])
    return empl_peak, firm_peak, wage_peak

def growth(industry_code):
    empl_peak, firm_peak, wage_peak = peaks(industry_code)
    df_temp = df_empl[df_empl['industry_code'] == industry_code]
    empl_growth = df_temp.iloc[0,33] - empl_peak 
    df_temp = df_firm[df_firm['industry_code'] == industry_code]
    firm_growth = df_temp.iloc[0,33] - firm_peak
    df_temp = df_wage[df_wage['industry_code'] == industry_code]
    wage_growth = df_temp.iloc[0,33] - wage_peak
    return empl_growth, firm_growth, wage_growth

