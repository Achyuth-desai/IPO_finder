import pandas as pd
data_new = pd.read_csv("~/Achyuth/web scraping/new.csv",sep=",", index_col=None).drop(columns="Unnamed: 9")
data_old = pd.read_csv("~/Achyuth/web scraping/old.csv", sep=",", index_col=None)
df_new = pd.DataFrame(data_new)
df_old = pd.DataFrame(data_old)
df_diff = df_new.merge(df_old,indicator=True, how='outer').loc[lambda x : x['_merge']=='left_only']
df_diff.to_csv('hehe.csv', index=False, encoding='utf-8')
#df_diff = df_new.compare(df_old)
#print(df_old)
#print(df_new)
#print("NEW DATA : \n",data_new)
#print("OLD DATA : \n",data_old)