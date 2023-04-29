from glob import glob
import pandas as pd
inp = 'data/final_upload_data/marged.csv'
out = 'data/final_upload_data/marged_price_publish.csv'
df = pd.read_csv(inp,dtype=str)
df = df.drop_duplicates(subset=['SKU'])
df['Published'] = '1'
df.to_csv(out, index=False,columns=['SKU','Published','Sale price','Regular price'])