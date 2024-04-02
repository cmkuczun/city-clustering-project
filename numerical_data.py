import pandas as pd

df = pd.read_csv('MASTER.csv')

df_numerical = df.select_dtypes(include=[np.number])

columns_to_remove = ['lat', 'lng', 'county_fips', 'pct_voters', 'pct_poverty', 
                     'pct_child_poverty', 'covid_deaths_per_100k', 'covid_case_to_death_pct', 
                     'cvap', 'foreignborn_pct', 'clf_unemploy_pct', 'lesshs_pct', 
                     'lesscollege_pct', 'lesshs_whites_pct', 'lesscollege_whites_pct']

df_final = df.select_dtypes(include=[np.number]).drop(columns=columns_to_remove, errors='ignore')

df_final.to_csv('numerical_data.csv', index=False)

# from google.colab import files
# files.download('numerical_data.csv')
