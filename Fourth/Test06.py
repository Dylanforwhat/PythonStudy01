import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
map_dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}
df_mapped = df.applymap(lambda x: map_dict.get(x))
print(df_mapped)