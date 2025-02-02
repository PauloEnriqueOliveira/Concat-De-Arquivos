import pandas as pd
import glob
import os

path = 'Caminho com diversas bases para leitura'

path_csv = glob.glob(os.path.join(path, "*.csv"))

dfs = []

for arquivo in path_csv:
    df = pd.read_csv(arquivo) 
    dfs.append(df)

df_conc = pd.concat(dfs, ignore_index=True)

df_conc
