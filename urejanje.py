import pandas as pd

podjetja = pd.read_csv("podatkiPodjetja.csv", index_col='id')

pd.options.display.max_rows = 20

podjetja.head()
