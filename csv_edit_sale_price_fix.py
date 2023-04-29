from glob import glob
import pandas as pd

# Get all csv files in the current directory
csv_files = glob('data/main_data/*.csv')
for csv_file in csv_files:
    # Read the csv file
    df = pd.read_csv(csv_file,dtype=str)
    # Fix the sale price column
    df.rename(columns={'Sale price': 'test'}, inplace=True)
    df.rename(columns={'Regular price': 'Sale price'}, inplace=True)
    df.rename(columns={'test': 'Regular price'}, inplace=True)

    rows = df[df['Regular price'] == '0']
    for index, row in rows.iterrows():
        df.at[index, 'Regular price'] = row['Sale price']
        df.at[index, 'Sale price'] = ''
    df.to_csv(csv_file, index=False)