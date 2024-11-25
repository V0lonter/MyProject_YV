import pandas as pd

df = pd.read_csv("C:\\Users\\finko\\Desktop\\університет\\комп'ютерні науки\\Практичні\\pract-19\\start.csv")

df.columns = ['City1', 'City2']

print("Температура в першому місті:")
print(df['City1'])

print("\nТемпература в другому місті:")
print(df['City2'])