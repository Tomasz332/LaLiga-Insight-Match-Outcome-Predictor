import argparse
import pandas as pd
import numpy as np
import pickle
from datetime import datetime
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ------------------- Argument Parsing -------------------

# Set up the argument parser
parser = argparse.ArgumentParser(description="Predict match outcomes based on season data.")
parser.add_argument(
    '--csv_file',
    type=str,
    help="Path to the CSV file for predictions. If not provided, the default file is used.",
    default="2025-season-fix.csv"
)

args = parser.parse_args()
csv_file = args.csv_file

future_data = pd.read_csv("2025-season-fix.csv")

team_map = {
    'Alaves': 0, 'Las Palmas': 1, 'Real Sociedad': 2, 'Atletico Madrid': 3, 'Espanyol': 4,
    'Getafe': 5, 'Real Betis': 6, 'Real Madrid': 7, 'Villarreal': 8, 'Eibar': 9,
    'Celta Vigo': 10, 'Barcelona': 11, 'Malaga': 12, 'Deportivo La Coruna': 13,
    'Athletic Club': 14, 'Leganes': 15, 'Sevilla': 16, 'Valencia': 17, 'Levante': 18,
    'Girona': 19, 'Valladolid': 20, 'Huesca': 21, 'Rayo Vallecano': 22, 'Osasuna': 23,
    'Granada': 24, 'Mallorca': 25, 'Cadiz': 26, 'Elche': 27, 'Almeria': 28,
    'Real Oviedo': 29
}

def map_team(team):
    return team_map.get(team, len(team_map)+1)

# ------------------- Preprocessing -------------------

# Extract time components
future_data['Time'] = pd.to_datetime(future_data['Time'], format='%H:%M').dt.time
future_data['Time_dt'] = pd.to_datetime(future_data['Time'].astype(str), format='%H:%M:%S')
future_data['Hour'] = future_data['Time_dt'].dt.hour
future_data['Minute'] = future_data['Time_dt'].dt.minute
future_data['Minutes_Since_Midnight'] = future_data['Hour'] * 60 + future_data['Minute']

# Cyclical encoding of time
future_data['Time_Sin'] = np.sin(2 * np.pi * future_data['Minutes_Since_Midnight'] / 1440)
future_data['Time_Cos'] = np.cos(2 * np.pi * future_data['Minutes_Since_Midnight'] / 1440)

# Team binary encoding
future_data['Home_code'] = future_data['Home'].apply(map_team)
future_data['Away_code'] = future_data['Away'].apply(map_team)

def binary_encode(number, num_bits=5):
    return [int(bit) for bit in bin(number)[2:].zfill(num_bits)]

home_code_df = future_data['Home_code'].apply(lambda x: binary_encode(x)).apply(pd.Series)
away_code_df = future_data['Away_code'].apply(lambda x: binary_encode(x)).apply(pd.Series)

home_code_df.columns = [f'Home_code_{i}' for i in range(home_code_df.shape[1])]
away_code_df.columns = [f'Away_code_{i}' for i in range(away_code_df.shape[1])]


features_df = pd.concat([
    future_data,
    home_code_df,
    away_code_df
], axis=1)


model_inputs = features_df[[
    'Time_Sin', 'Time_Cos', 'Matchweek', 'Home_Pos',
    'Home_code_0', 'Home_code_1', 'Home_code_2', 'Home_code_3', 'Home_code_4',
    'xG_Home', 'xG_Away',
    'Away_code_0', 'Away_code_1', 'Away_code_2', 'Away_code_3', 'Away_code_4',
    'Away_Pos'
]]

# Rename to match training data column names
model_inputs = model_inputs.rename(columns={
    'Matchweek': 'Wk',
    'Home_Pos': 'Home Position',
    'Away_Pos': 'Away Position'
})

# ------------------- Load scaler and model -------------------

with open('../models/scaler', 'rb') as file:
    scaler = pickle.load(file)

with open('../models/model', 'rb') as file:
    model = pickle.load(file)

# Scale xG features
model_inputs[['xG_Home', 'xG_Away']] = scaler.transform(model_inputs[['xG_Home', 'xG_Away']])

# ------------------- Predict probabilities -------------------

probs = model.predict_proba(model_inputs)
home_win_probs = probs[:, 1]
home_not_win_probs = probs[:, 0]

# ------------------- Final Output -------------------

output_df = pd.DataFrame({
    'Matchweek': future_data['Matchweek'],
    'Home': future_data['Home'],
    'Away': future_data['Away'],
    'xG_Home': future_data['xG_Home'],
    'xG_Away': future_data['xG_Away'],
    'Home_Win_Probability': home_win_probs,
    'Home_Not_Win_Probability': home_not_win_probs
})


output_df[['Home_Win_Probability', 'Home_Not_Win_Probability']] = output_df[[
    'Home_Win_Probability', 'Home_Not_Win_Probability']].round(4)


for idx, row in output_df.iterrows():
    print(f"Matchweek {future_data.loc[idx, 'Matchweek']}")
    print(f"{row['Home']} vs {row['Away']}")
    print(f"{row['Home']} win probability: {round(row['Home_Win_Probability'] * 100, 2)}%")
    print(f"{row['Away']} win probability: {round(row['Home_Not_Win_Probability'] * 100, 2)}%\n")

