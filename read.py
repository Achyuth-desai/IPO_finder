import pandas as pd 

df1 = pd.read_csv('file.csv',index_col=0)
df2 = pd.read_csv('file1.csv',index_col=0)

df = pd.concat([df1,df2])
df = df.reset_index(drop=True)
df_gpby = df.groupby(list(df.columns))

idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1]

df.reindex(idx)

df.to_csv('result.csv')