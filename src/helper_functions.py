import pandas as pd
import matplotlib.pyplot as pyplot
import math
import scipy as scipy
import numpy as np
## pip install python-varname ##
from varname import nameof
from lookups import *
import io

###############DATAFRAME CONSTRUCTION#######################


#adds a composite variable: year and quarter in 1
def add_qtrid(df):
    df['qtrid'] = df['year'] + (df['qtr']/4)
    return df

#import one year of data to explore
def import_one(year):
    filepath = '../data/' + str(year) + '.csv'
    df = pd.read_csv(filepath, dtype = schema_dict)
    df = df.drop(drop_list, axis = 1)
    return df


#import 2007- 2014 data into a single file
def import_all(years):
    df = import_one(years[0])
    for year in years[1:]:
        df = df.append(import_one(year))
    df['industry_code'] = df['industry_code'].str.replace('31-33','31')
    df['industry_code'] = df['industry_code'].str.replace('44-45','44')
    df['industry_code'] = df['industry_code'].str.replace('48-49','48').astype('int32')
    df = add_qtrid(df)
    return df

#UNSUSED Create a timeline of # of *firms* per industry
def create_df_firm(df):
    df_firm = df.pivot_table(columns = 'qtrid', values = 'qtrly_estabs_count', index = ['industry_code', 'industry_title'], aggfunc = np.max)
    df_firm = df_firm.reset_index()
    df_firm['peak'] = max(df_firm.values[0][2:10])
    df_firm['growth'] = df_firm[2015.0] - df_firm['peak'] 
    return df_firm


#Create a timeline of # of *employees* per industry, and some derived variables (the ones we care about) 
def create_df_empl(df):
    return df.pivot_table(columns = 'qtrid', values = 'month3_emplvl', index = ['industry_code', 'industry_title'], aggfunc = np.max)
    
def derive_empl_vars(df):
    #reset the index to avoid any issues in derived variables
    df = df.reset_index()
    
    #recovery: quarter that an industry surpassed it's pre-recession peak
    df['recovery'] = (df.transpose().iloc[2:,:] > df.transpose().iloc[2:10,:].max(axis=0)).idxmax()
    
    #UNUSED nadir: Determine the lowest employement quarter for the time period
    #df['nadir'] =  df.transpose().iloc[2:,:].min(axis=0)
    # df['nadir_qtr'] = (df.transpose().iloc[2:,:] > df.transpose().iloc[2:,:].min(axis=0)).idxmin()
    
    #peak: high point *before the recession* (2007-2008), benchmark
    df['peak'] = df.transpose().iloc[2:10,:].max(axis=0)
    
    #growth: raw number of employees gained since peak
    df['growth'] = df[2015.0] - df['peak']
    
    #growth percentage: percentage of employees gained since peak
    df['growth_pcg'] = 100 * (df['growth'] / df['peak'])

    #standardizes dtypes to prevent lost data in join
    df['industry_code'] = df['industry_code'].astype('float64')

    return df

#UNUSED check the file for duplicate entries
def add_dupecheck(df):
    df['industry_code'] = df['industry_code'].str.replace('-','').astype('int32')
    df['dupecheck'] = ((df['industry_code']) * 10000)+ df['qtrid']
    return df

#UNUSED check the file for duplicate entries
def add_yearcheck(df):
    df['yearcheck'] = ((df['industry_code']) * 10000)+ df['year']
    return df

#Create a timeline of # of *average weekly wage* per industry, and some derived variables (the ones we care about) 
def create_df_wage(df):
    return df.pivot_table(columns = 'qtrid', values = 'avg_wkly_wage', index = ['industry_code', 'industry_title'], aggfunc = np.max)

def derive_wage_vars(df):
  
    #reset the index to avoid any issues in derived variables
    df = df.reset_index()
    
    #recovery: quarter that an industry surpassed it's pre-recession peak
    df['recovery'] = (df.transpose().iloc[2:,:] > df.transpose().iloc[2:10,:].max(axis=0)).idxmax()
    
    #UNUSED nadir: Determine the lowest wages quarter for the time period
    # df['nadir_qtr'] = (df.transpose().iloc[2:,:] > df.transpose().iloc[2:,:].min(axis=0)).idxmin()
    # df['nadir'] =  df.transpose().iloc[2:,:].min(axis=0)
    
    #peak: high point *before the recession* (2007-2008), benchmark
    df['peak'] = df.transpose().iloc[2:10,:].max(axis=0)
    
    #growth: raw number of weekly wages gained since peak ($)
    df['growth'] = df[2015.0] - df['peak']
    
    #growth percentage: percentage of weekly wages gained since peak
    df['growth_pcg'] = 100 * (df['growth'] / df['peak'])

    return df

#joins empl and wage tables into a single one
def join_empl_wage(df1,df2):
    df_join = df1.sort_values(by=['industry_code']).join(df2.sort_values(by=['industry_code']), lsuffix = '_wage', rsuffix = '_empl')
    #drops timeline data, retains derived variables
    df_join = df_join.drop(columns = drop_from_join, axis = 0)
    return df_join

#makes a version of the joined table with null rows dropped- used only for correlation calculations
def make_nanless(df):
    return df.dropna()

#exports all tables and info to external files
def export_info(df):
    strfile = '../data/' + str(nameof(df)) + '_info.txt'
    buffer = io.StringIO()
    df.info(buf=buffer)
    info = buffer.getvalue()
    with open(strfile, "a", encoding="utf-8") as f: 
        f.write(info)
        f.close
    strfile = str(nameof(df)) + '_desc.csv'
    print(df.describe().to_csv(strfile))
    strfile = str(nameof(df)) + '_freq.csv'
    df.to_csv(strfile)


###############DATA EXPLORATION#######################

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

