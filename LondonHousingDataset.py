import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


pd.set_option("display.width",320)
pd.set_option("display.max_columns",9)  # Shows all columns
pd.set_option("display.max_rows",None)
data = pd.read_csv(r"E:\5. London Housing Data.csv")
print(data)
print(data.count())
print(data.isnull().sum())
print(sns.heatmap(data.isnull()))
# print(plt.show())
print(data.head())
print(data.dtypes)
data.date = pd.to_datetime(data.date)
print(data.dtypes)
print(data.head())
data['year'] = data.date.dt.year
print(data)
data.insert(1, 'month', data.date.dt.month)
print(data)
data.drop(['month', 'year'], axis = 1, inplace=True)
print(data)
print(data.head())
print(data[data.no_of_crimes == 0])
print(len(data[data.no_of_crimes == 0]))
data['year'] = data.date.dt.year
print(data.head())
df1 = data[data.area == 'england']
print(df1)
print(df1.groupby('year').average_price.max())
print(df1.groupby('year').average_price.min())
print(data.groupby('year').average_price.mean())
print(data.groupby('area').no_of_crimes.max())
print(data.groupby('area').no_of_crimes.min().sort_values(ascending=True))
print(data[data.average_price < 100000].area.value_counts())