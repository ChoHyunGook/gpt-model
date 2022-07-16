import pandas as pd

xlsx = pd.read_excel("../gpt-main/악보모음.xlsx")
xlsx.to_csv("../gpt-main/동요악보모음.csv")



