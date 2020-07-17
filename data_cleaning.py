# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 09:38:53 2020

@author: Johnson
"""


import pandas as pd


df = pd.read_csv('glassdoor_jobs.csv')




#salary parsing

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['Employer Provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']

#removing "Glassdoor est."
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K', '').replace('$',''))

min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:', ''))

df['min_salary'] =  min_hr.apply(lambda x: int(x.split('-')[0]) )
df['max_salary'] =  min_hr.apply(lambda x: int(x.split('-')[1]) )
df['avg_salary'] = (df.min_salary+df.max_salary)/2



#company name text only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)
#state field
df['job_city'] = df['Location'].apply(lambda x: x.split(',')[0])
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[-1])
print(df.job_state.value_counts())

#age of company
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis =1)
df['company_age'] = df.apply(lambda x: 0 if x.Founded == -1 else (2019 - x.Founded), axis = 1)

#parsing of job description (python,etc.)
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() else 0)
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

