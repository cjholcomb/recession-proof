#Which industries can weather a recession?

An attempt to discern what industries fared the best in retaining jobs and maintaining wages through the 2007 recession.

# Overview

We are currently in one of the worst recessions in living memory. The COVID-19 pandemic has hobbled the American economy, with layoffs putting millions of Americans in precarious financial positions. Firms have collapsed or gone dark, education is being (temporarily?) reworked to be online-only. Jobless Americans are currently using their idle time to gain new marketable skills so they can reenter an extremely competitive workforce.

Job training is the solution to any and all "skills mismatch" problems in the labor market, or so our policy-makers believe. There are government-funded programs to help workers learn new skills. Americans looking to add to their skill sets can borrow to pay for education or reach into their own pockets. The decision of *what* new skills to learn, however, is left to individual workers.

This project is an attempt to describe the employment numbers from the last recession. I intend to compare the employment numbers across industries, to see which industries are the "safest" bets for workers to invest their resources into joining.

# Assumptions

* The BLS data in question is accurate (duh).
* Inflation will be ignored (for now).
* We will concern ourselves only with job counts, not population counts or pro0portions of jobs to working-age/capable Americans.
* Average wage in each industry (the only available data) is generalizable to the working population.

# Questions

* What were the most "resilient" industries? Which industries had the shortest period between job losses and recovery to their pre-recession numbers?
  * Apply this same question to the number of establishments in each industry.
* Were there any industries that remained constant in their job numbers throughout the recession?
* Which industries had the most dramatic shifts in wages across the recession? Which were devalued (lower average wage) and which increased in value?
* How did the job numbers change for each industry as a percentage of total American jobs?

## Stretch Goals

1. How did wages fare when adjusted for inflation?
2. Which region(s) were the highest recovery/growth areas for the most resilient industries? (I know you want maps, Land)
3. Are there any familiar trends in the *current* (Q1-Q2 2020) recession?

# Dataset

I will be using data from the U.S. Bureau of Labor Statistics' Quarterly Census of Employment and Wages. Data exists as far back as 1990 (for the current questionnaire), however we will only concern ourselves with the months between Q1 2007 (the "official" start of the recession) to Q4 2014 (The year in which the American economy achieved the same overall job numbers as when the recession began).

The below image illustrates the length and severity of the 2007 recession:

![recession_chart](ScariestJan2017.PNG)

## File too large!

I started with the *full* dataset from the BLS website (Found here:https://data.bls.gov/cew/data/files/2007/csv/2007_qtrly_singlefile.zip). The compressed file was approximately 500 megs, and uncompressed to 2.2 gigs. And that was only for one year.

I spent a good portion of a day trying to spin up an AWS instance. When that ultimately failed, I messaged a friend with an incredibly powerful gaming/streaming machine at his disposal. He allowed me to remote into the machine and open up the file to take a look- and the file was orders of magnitude too detailed for my purposes. It contained a line for every US County (~3,100) and industry (~2,600) *combinations*, times 4 since these results are quarterly. I only need one of those dimensions (industry) so I started fresh, grabbing the full data by area. That download is split into hundreds of files for different counties and states, but it contains a file for the entire US, which is a much more reasonable dataset. I quickly grabbed that file for every year in question (2007-2014).

Next came the task of getting all these files into a format that I wanted. I wrote some dictionaries and lists (stored in lookups.py) collect the schemas and the data I wanted to keep, so I could functionize the importing process and ensure repeatability. I wrote functions to import a single file, convert to the correct schema, and then drop unneeded columns. Then I added a function to pull all files into a single dataset. And I found myself working with a reasonable 150k rows of data, as opposed to the 251,280,000 the other path would have given me. This has the downside of removing location as a possible independent variable to explore, but tweaking the lookup tables would allow me to easily repeat all of my steps to to an area-based analysis instead of an industry one.

## Dataset Metadata:

 #   Column              Non-Null Count   Dtype    Description
---  ------              --------------   -----    -----------
 0   industry_code       149772 non-null  int32    Numeric code for industry
 1   agglvl_code         149772 non-null  object   Aggregation Level of Industry
 2   year                149772 non-null  int64    4 digit Year
 3   qtr                 149772 non-null  int64    1 digit quarter
 4   industry_title      149772 non-null  object   Full name of each industry
 5   agglvl_title        149772 non-null  object   Full description of aggregation level
 6   qtrly_estabs_count  149772 non-null  int64    Full count of firms in each industry operation for that quarter
 7   month1_emplvl       149772 non-null  int64    Count of total employees in industry for month 1 of the qtr
 8   month2_emplvl       149772 non-null  int64    Count of total employees in industry for month 2 of the qtr
 9   month3_emplvl       149772 non-null  int64    Count of total employees in industry for month 1 of the qtr 
 10  total_qtrly_wages   149772 non-null  int64    Total wages earned in that industry for the quarter (whole dollars)
 11  avg_wkly_wage       149772 non-null  int64    Average wage for employees in the industry
 12  qtrid               149772 non-null  float64  Composit of year and qtr [(year + qtr) * 4]
 
 This table provides the raw data that will generate the variables I really care about: growth over the time period in both wages and employment, when the industry "peaked" in the early years of the recession, and when the industry recovered. I transformed the data into two seperate timeline tables, tracking the employment and wage numnbers over the relevant quarters. In each table I computed the relevant derived vairables, then joined both the employee and wage timeline tables, dropping the time series and retaining only the derived variables.
 
 #   Column               Non-Null Count  Dtype    Description  
---  ------               --------------  -----    -----------
 0   industry_code        2447 non-null   int64    Numeric code for industry
 1   industry_title       2447 non-null   object   Full name of each industry
 2   recovery_wage        2447 non-null   float64  Quarter in which wages surpassed pre-recession peak
 3   peak_wage            2363 non-null   float64  Pre-recession peak wages
 4   growth_wage          2160 non-null   float64  2014q4 wages - peak_wage
 5   growth_pcg_wage      2160 non-null   float64  100 * ( growth_wage / peak_wage )
 6   recovery_empl        2447 non-null   float64  Quarter in which employment surpassed
 7   peak_empl            2363 non-null   float64  Pre- recession peak employment
 8   growth_empl          2160 non-null   float64  2014q4 employment - peak_empl
 9   growth_pcg_empl      2160 non-null   float64  100* ( growth_empl / peak_empl )
 
 Now that I have the data I want, it's time for some top-level exploration.
 
 ## A note on industry codes:
 
 The QCEW data contains five layers of aggregation
 





It was time to create three sub-tables to get at what I really cared about. I made a composite column (year + quarter) and then pivoted the table three times. Once for total establishments, once for total employment, and once for average wages. This gave me a timeline of all 32 quarters of data across all industries.

 There were quite a few industries that seemed to pop up more than once in the data. Clearly some of them are aggregate measures of several more rows of data, possibly including rows with the same industry name. The data nerd in me wanted to discern how those aggregate rows are comprised, but my goal is to provide information for jobless Americans, not to fully account that the sum of everything adds up. In those cases, I took the maximum values of each unique industry for both establishments and employment. For wages, I went with the minimum. Again, this is from the perspective of a job seeker, and given we don't know how much overlap is in each row of data, means, quartiles, and medians are not reliable. Minimums is the more conservative measure, which, as a job seeker myself, I'd be more likely to place bets on than the max.

 Next steps:

 Compute "peak" month from 2007 - 2008 column.
 Compute recovery time in quarters: quarters between peak month in 07-08 until the number surpassed the peak.
 Compute "growth"- difference between peak and recovery 
