import pandas as pd
import matplotlib.pyplot as pyplot
import math
import scipy as scipy
import numpy as np
from varname import nameof

schema_dict = { 'area_fips':str,
                'own_code':str,
                'industry_code':str,
                'agglvl_code':str,
                'size_code':str,
                'year':int,
                'qtr':int,
                'disclosure_code':str,
                'area_title':str,
                'own_title':str,
                'industry_title':str,
                'agglvl_title':str,
                'size_title':str,
                'qtrly_estabs':int,
                'month1_emplvl':int,
                'month2_emplvl':int,
                'month3_emplvl':int,
                'total_qtrly_wages':int,
                'taxable_qtrly_wages':int,
                'qtrly_contributions':int,
                'avg_wkly_wage':int,
                'lq_disclosure_code':str,
                'lq_qtrly_estabs':float,
                'lq_month1_emplvl':float,
                'lq_month1_emplv2':float,
                'lq_month1_emplv3':float,
                'lq_total_qtrly_wages':float,
                'lq_taxable_qtrly_wages':float,
                'lq_qrtly_contributions':float,
                'oty_disclosure_code':str,
                'oty_qtrly_estabs':int,
                'oty_qtrly_estabs_pct_chg':float,
                'oty_month1_emplvl_chg':int,
                'oty_month1_emplvl_pct_chg':float,
                'oty_month2_emplv_chg':int,
                'oty_month2_emplvl_pct_chg':float,
                'oty_month3_emplvl_chg':int,
                'oty_month3_emplvl_pct_chg':float,
                'oty_total_qtrly_wages_chg':int,
                'oty_total_qtrly_wages_pct_chg':float,
                'oty_taxable_qtrly_wages_chg':int,
                'oty_taxable_qtrly_wages_pct_chg':float,
                'oty_qrtly_contributions_chg':int,
                'oty_qrtly_contributions_pct_chg':float,
                'oty_avg_wkly_wage_chg':int,
                'oty_avg_wkly_wage_pct_chg':float}

schema_dict_nested = {str:
                ['area_fips',
                'own_code',
                'industry_code',
                'agglvl_code',
                'size_code',
                'disclosure_code',
                'area_title',
                'own_title',
                'industry_title',
                'agglvl_title',
                'size_title',
                'lq_disclosure_code',
                'oty_disclosure_code'],
                int:
                ['qtrly_estabs',
                'month1_emplvl',
                'month2_emplvl',
                'month3_emplvl',
                'total_qtrly_wages',
                'taxable_qtrly_wages',
                'qtrly_contributions',
                'avg_wkly_wage',
                'oty_qtrly_estabs',
                'oty_month1_emplvl_chg',
                'oty_month2_emplv_chg',
                'oty_month3_emplvl_chg',
                'oty_total_qtrly_wages_chg',
                'oty_taxable_qtrly_wages_chg',
                'oty_qrtly_contributions_chg',
                'oty_avg_wkly_wage_chg'],
                float:
                ['lq_qtrly_estabs',
                'lq_month1_emplvl',
                'lq_month1_emplv2',
                'lq_month1_emplv3',
                'lq_total_qtrly_wages',
                'lq_taxable_qtrly_wages',
                'lq_qrtly_contributions',
                'oty_qtrly_estabs_count_chg',
                'oty_qtrly_estabs_count_pct_chg',
                'oty_month1_emplvl_pct_chg',
                'oty_month2_emplvl_pct_chg',
                'oty_month3_emplvl_pct_chg',
                'oty_total_qtrly_wages_pct_chg',
                'oty_taxable_qtrly_wages_pct_chg',
                'oty_qrtly_contributions_pct_chg',
                'oty_avg_wkly_wage_pct_chg']}

drop_list = ['area_fips',
                'own_code',
                'industry_code',
                'agglvl_code',
                'size_code',
                'disclosure_code',
                'area_title',
                'own_title',
                'agglvl_title',
                'size_title',
                'lq_disclosure_code',
                'oty_disclosure_code',
                'oty_month1_emplvl_chg',
                'oty_month2_emplvl_chg',
                'oty_month3_emplvl_chg',
                'oty_total_qtrly_wages_chg',
                'oty_taxable_qtrly_wages_chg',
                'oty_qtrly_contributions_chg',
                'oty_avg_wkly_wage_chg',
                'lq_qtrly_estabs_count',
                'lq_month1_emplvl',
                'lq_month2_emplvl',
                'lq_month3_emplvl',
                'lq_total_qtrly_wages',
                'lq_taxable_qtrly_wages',
                'lq_qtrly_contributions',
                'oty_qtrly_estabs_count_chg',
                'oty_qtrly_estabs_count_pct_chg',
                'oty_month1_emplvl_pct',
                'oty_month2_emplvl_pct',
                'oty_month3_emplvl_pct',
                'oty_total_qtrly_wages_pct',
                'oty_taxable_qtrly_wages_chg',
                'oty_qtrly_contributions_pct',
                'oty_avg_wkly_wage_pct',
                'oty_taxable_qtrly_wages_chg.1',
                'lq_avg_wkly_wage',
                'taxable_qtrly_wages']

recession_years = [ '2007'
                    '2008',
                   '2009',
                   '2010',
                   '2011',
                   '2012',
                   '2013',
                   '2014']

columns_list =  ['area_fips',
                'own_code',
                'industry_code',
                'agglvl_code',
                'size_code',
                'year',
                'qtr',
                'disclosure_code',
                'area_title',
                'own_title',
                'industry_title',
                'agglvl_title',
                'size_title',
                'qtrly_estabs',
                'month1_emplvl',
                'month2_emplvl',
                'month3_emplvl',
                'total_qtrly_wages',
                'taxable_qtrly_wages',
                'qtrly_contributions',
                'avg_wkly_wage',
                'lq_disclosure_code',
                'lq_qtrly_estabs',
                'lq_month1_emplvl',
                'lq_month1_emplv2',
                'lq_month1_emplv3',
                'lq_total_qtrly_wages',
                'lq_taxable_qtrly_wages',
                'lq_qrtly_contributions',
                'oty_disclosure_code',
                'oty_qtrly_estabs',
                'oty_qtrly_estabs_pct_chg',
                'oty_month1_emplvl_chg',
                'oty_month1_emplvl_pct_chg',
                'oty_month2_emplv_chg',
                'oty_month2_emplvl_pct_chg',
                'oty_month3_emplvl_chg',
                'oty_month3_emplvl_pct_chg',
                'oty_total_qtrly_wages_chg',
                'oty_total_qtrly_wages_pct_chg',
                'oty_taxable_qtrly_wages_chg',
                'oty_taxable_qtrly_wages_pct_chg',
                'oty_qrtly_contributions_chg',
                'oty_qrtly_contributions_pct_chg',
                'oty_avg_wkly_wage_chg',
                'oty_avg_wkly_wage_pct_chg']

def import_one(year):
    filepath = 'data/' + str(year) + '.csv'
    df = pd.read_csv(filepath, dtype = schema_dict)
    df = df.drop(drop_list, axis = 1)
    return df

def import_all(years):
    df = pd.Dataframe(columns = columns_list, dtype = schema_dict)
    df = df.drop(drop_list, axis =1)
    for year in years
        df = df.append(import_one(year))
    return df

def export_info(df):
    strfile = str(nameof(df)) + '_desc.txt'
    file = file.open(strfile)
    file.write(df.info())
    file.write(df.describe())
    file.write(df['industry_title'].value_counts())
    file.close()



# def import_all(years):
#     lst = []
#     for year in years:
#         filepath = 'data/' + str(year) + '.csv'
        # lst.append(exec('scew' + str(year) +'_df = pd.read_csv(filepath, dtype = schema_dict)'))


