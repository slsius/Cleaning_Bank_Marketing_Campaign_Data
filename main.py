import pandas as pd
import numpy as np

# Start coding here...
#read data file
file_name = 'bank_marketing.csv'
data = pd.read_csv(file_name)

#[job] replace '.' to '-'
data['job'] = data['job'].str.replace('.','_')

#[education] Change "." to "_" and "unknown" to np.NaN
data['education'] = data['education'].str.replace('.','_')
data.loc[data['education'] == 'unknown', 'education'] = np.nan

#data['credit_default'] Convert to boolean data type: 1 if "yes", otherwise 0.
credit_default_equ = data['credit_default'] == 'yes'
data.loc[credit_default_equ, 'credit_default'] = 1
data.loc[~credit_default_equ, 'credit_default'] = 0
data['credit_default'] = data['credit_default'].astype('bool')

#mortgage Convert to boolean data type:1 if "yes", otherwise 0
mortgage_equ = data['mortgage'] == 'yes'
data.loc[mortgage_equ, 'mortgage'] = 1
data.loc[~mortgage_equ, 'mortgage'] = 0
data['mortgage'] = data['mortgage'].astype('bool')

#define client csv header
client_header = ['client_id','age','job','marital','education','credit_default','mortgage']

#export client.csv
data[client_header].to_csv('client.csv',index=False)

#previous_outcome Convert to boolean data type:1 if "success", otherwise 0.
outcome_mapping = {'success': 1, 'nonexistent': 0, 'failure':0}
data['previous_outcome'] = df['previous_outcome'].map(outcome_mapping).astype(bool)
#previous_outcome_equ = data['previous_outcome'] == 'success'
#data.loc[previous_outcome_equ,'previous_outcome'] == 1
#data.loc[~previous_outcome_equ,'previous_outcome'] == 0
#data['previous_outcome'] = data['previous_outcome'].astype('bool')

#campaign_outcome Convert to boolean data type:1 if "yes", otherwise 0.
mapping = {'yes': 1, 'no': 0}
data['campaign_outcome'] = df['campaign_outcome'].map(mapping).astype(bool)
#data['campaign_outcome'] = data['campaign_outcome'].str.lower().map
#campaign_outcome_equ = data['campaign_outcome'] == 'yes'
#data.loc[campaign_outcome_equ,'campaign_outcome'] == 1
#data.loc[~campaign_outcome_equ,'campaign_outcome'] == 0
#data['campaign_outcome'] = data['campaign_outcome'].astype('bool')

#last_contact_date Create from a combination of day, month, and a newly created year column (which should have a value of 2022);Format = "YYYY-MM-DD"
data['year'] = 2022
month_mapping = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}
data['month'] = data['month'].str.lower().map(month_mapping)
data['last_contact_date'] = pd.to_datetime(df[['year', 'month', 'day']], errors='coerce')

#define campaign csv header
campaign_header = ['client_id','number_contacts','contact_duration','previous_campaign_contacts','previous_outcome','campaign_outcome','last_contact_date']

#export economic.csv
data[campaign_header].to_csv('campaign.csv',index=False)

#define economic header
econ_header = ['client_id','cons_price_idx','euribor_three_months']

#export econ csv
data[econ_header].to_csv('economics.csv',index=False)
