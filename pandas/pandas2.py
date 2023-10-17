import pandas as pd
import numpy as np
print("---------------------------------------------- select data -------------------------------------------")
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A', 'B', 'C', 'D'])
print("------------ df ------------")
print(df)
print("df['A']")
print(df['A'])
print("df.B")
print(df.B)

print("------------------------------")
print(df[0:3])
print(df['20130102':'20130104'])
print(df['2013-01-02':'2013-01-04'])
print("------------ select by label: loc ------------------")
print(df.loc['20130102'])
print("------------")
print(df.loc[:,['A','B']])
print("------------")
print(df.loc['20130102',['A','B']])

print("------------ select by position: iloc ------------------")
print("------df------")
print(df)
print("-----df.iloc[3]-------")
print(df.iloc[3])
print("-----df.iloc[3, 1]-------")
print(df.iloc[3, 1])
print("------df.iloc[3:5, 1:3]------")
print(df.iloc[3:5, 1:3])
print("------df.iloc[[1,3,5], 1:3]------")
print(df.iloc[[1,3,5], 1:3])

print("------------ mixed selection: ix ------------------")
print("------df------")
print(df)
print("------------")
#AttributeError: 'DataFrame' object has no attribute 'ix'
#print(df.ix[:3, ['A', 'C']])
print(df.iloc[:3, [0, 2]])
print("----- Boolean indexing -------")
print(df)
print(df[df.A > 8])
print("---------------------------------------------- set data -------------------------------------------")
print(df)
df.iloc[2, 2] = 1111
df.loc['20130101', 'B'] = 22222
# df[df.A > 12] = 0
#df.A[df.A > 12] = 0
df.B[df.A >= 12] = 0
#df.B[df.B > 12] = 0
#df['F'] = np.nan
df['E'] = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130101', periods=6))
print(df)

print("---------------------------------------------- handle NaN -------------------------------------------")
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
print(df)
# how = {'any', 'all'}
#print(df.dropna(axis=0, how="any"))
#print(df.dropna(axis=1, how="any"))
#print(df.fillna(value=0))
print(df.isnull())
print("------------")
print(np.any(df.isnull()) == True)

