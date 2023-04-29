from glob import glob
import pandas as pd

# Get all csv files in the current directory
csv_files = glob('data/main_data/*.csv')
output = 'data/final_upload_data/marged.csv'
mdf = pd.DataFrame()
dfs = []
for csv_file in csv_files:
    # Read the csv file
    df = pd.read_csv(csv_file,dtype=str)
    dfs.append(df)
mdf = pd.concat(dfs)
mdf.to_csv(output, index=False)