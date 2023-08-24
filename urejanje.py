import pandas as pd

podjetja = pd.read_csv("podatkiPodjetja.csv")

pd.options.display.max_rows = 20



print(podjetja.vrednost >= 3)
