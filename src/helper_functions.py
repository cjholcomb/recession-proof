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
    return df

def import_all(years):
    df = import_one(years[0])
    for year in years[1:]:
        df = df.append(import_one(year))
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
    df['qtrid'] = df['year'] + (df['qtr']/10)
    return df

def add_dupecheck(df):
    df['industry_code'] = df['industry_code'].str.replace('-','').astype('int32')
    df['dupecheck'] = ((df['industry_code']) * 10000)+ df['qtrid']
    return df

def add_yearcheck(df):
    df['yearcheck'] = ((df['industry_code']) * 10000)+ df['year']
    return df

# def create_df_firm(df):
#     print(df.head())
#     return df.pivot_table(columns = 'qtrid', values = 'qtrly_estabs_count', index = 'industry_code', aggfunc = np.max)

def create_df_firm(df):
    return df.pivot_table(columns = 'qtrid', values = 'month3_emp_lvl', index = 'industry_code', aggfunc = np.max)
    
def create_df_empl(df):
    return df.pivot_table(columns = 'qtrid', values = 'month3_emp_lvl', index = 'industry_code', aggfunc = np.max)

def create_df_wage(df):
    return df.pivot_table(columns = 'qtrid', values = 'avg_wkly_wage', index = 'industry_code', aggfunc = np.min)

