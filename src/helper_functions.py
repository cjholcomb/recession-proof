def schema_convert(df):
    schema_dict = {'A':str, 'B':int,'C':float,}
    df = pd.DataFrame({'A':['area_fips','own_code','industry_code','agglvl_code','size_code','year','qtr','disclosure_code','area_title','own_title','industry_title','agglvl_title','size_title','lq_disclosure_code','oty_disclosure_code'],'B':['qtrly_estabs_count','month1_emplvl','month2_emplvl','month3_emplvl','total_qtrly_wages', 'taxable_qtrly_wages','qtrly_contributions','avg_weekly_wage','oty_qtrly_estabs_count_chg','oty_month1_emplvl_chg','oty_month2_emplvl_chg','oty_month3_emplvl_chg','oty_total_qtrly_wages_chg','oty_taxable_qtrly_wages_chg','oty_qtrly_contributions_chg','oty_avg_wkly_wage_chg',],'C':['lq_qtrly_estabs_count','lq_month1_emplvl','lq_month2_emplvl','lq_month3_emplvl','lq_total_qtrly_wages','lq_taxable_qtrly_wages','lq_qtrly_contributions','lq_avg_wkly_wage','oty_qtrly_estabs_count_pct_chg','oty_month1_emplvl_pct_chg','oty_month3_emplvl_pct_chg','oty_month2_emplvl_pct_chg','oty_total_qtrly_wages_pct_chg','oty_taxable_qtrly_wages_pct_chg','oty_qtrly_contributions_pct_chg','oty_avg_wkly_wage_pct_chg']})
    for col, col_type in schema_dict.items():
        df[col] = df[col].astype(col_type)
    return df