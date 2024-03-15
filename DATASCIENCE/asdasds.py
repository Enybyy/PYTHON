# import pandas as pd
# import pickle
# from scipy.stats import poisson


# dict_table = pickle.load(open('Dictionaries/dict_groups', 'rb'))
# df_historical_data = pd.read_csv('Database/df_clean_worldcups.csv')
# df_fixture = pd.read_csv('Database/df_clean_worldcup_2022.csv')


# df_home = df_historical_data[['Local_Team', 'Local_Goals', 'Away_Goals']]
# df_away = df_historical_data[['Away_Team', 'Local_Goals', 'Away_Goals']]

# df_home = df_home.rename(columns={
#                          'Local_Team': 'Team', 'Local_Goals': 'GoalsScored', 'Away_Goals': 'GoalsConceded'})
# df_away = df_away.rename(columns={
#                          'Away_Team': 'Team', 'Local_Goals': 'GoalsConceded', 'Away_Goals': 'GoalsScored'})

# df_team_strength = pd.concat(
#     [df_home, df_away], ignore_index=True).groupby(['Team']).mean()
# print(df_team_strength)


import pandas as pd
import pickle
from scipy.stats import poisson

# READ & LOAD
dict_groups = pickle.load(open('Dictionaries/dict_groups', 'rb'))
df_clean_worldcups = pd.read_csv('Database/df_clean_worldcups.csv')
df_clean_worldcup_2022 = pd.read_csv('Database/df_clean_worldcup_2022.csv')

# for group_key in dict_groups:
#     dict_groups[group_key]['Pts'] = dict_groups[group_key]['Pts'].astype(float)

for group_key in dict_groups:
    print(f"Tipos de datos para el grupo {group_key}:")
    print(dict_groups[group_key].dtypes)
    print()
