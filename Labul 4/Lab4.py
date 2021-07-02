import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("test.csv")
print(df['AL'])
df['AL'].fillna(888, inplace=True)
print(df.describe())
print(df.mean())

df['AT'].plot(kind='hist')
plt.show()
df.plot(kind='scatter', x='AT', y='BE')
plt.show()
print(df.corr())
a = {'a':3}

print(pd.DataFrame(a))
