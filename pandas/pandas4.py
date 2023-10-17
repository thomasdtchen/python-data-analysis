import pandas as pd
left=pd.DataFrame({'key':['K0', 'K1', 'K2', 'K3'],
                   'A':['A0', 'A1', 'A2', 'A3'],
                   'B':['B0', 'B1', 'B2', 'B3']})
print(left)
right=pd.DataFrame({'key':['K0', 'K1', 'K2', 'K3'],
                   'C':['C0', 'C1', 'C2', 'C3'],
                   'D':['D0', 'D1', 'D2', 'D3']})
print(right)
res=pd.merge(left, right, on='key')
print(res)
print("-------------------------------------------------")
left=pd.DataFrame({'A':['A0', 'A1', 'A2', 'A3'],
                   'B':['B0', 'B1', 'B2', 'B3'],
                    'key1':['K0', 'K0', 'K1', 'K2'],
                    'key2':['K0', 'K1', 'K0', 'K1']})
right=pd.DataFrame({'key1':['K0', 'K1', 'K1', 'K2'],
                    'key2':['K0', 'K0', 'K0', 'K0'],
                    'C':['C0', 'C1', 'C2', 'C3'],
                    'D':['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
# how = ['left', 'right', 'outer', 'inner']
#print(pd.merge(left, right, on=['key1', 'key2'], how='inner'))
#print(pd.merge(left, right, on=['key1', 'key2'], how='right'))
#print(pd.merge(left, right, on=['key1', 'key2'], how='left'))
#print(pd.merge(left, right, on=['key1', 'key2'], how='outer', indicator=True))

print(pd.merge(left, right, left_index=True, right_index=True, how='outer', indicator="indicator"))

print("------------------------------------------------------------------")
boys = pd.DataFrame({'k':['K0','K1','K2'], 'age':[1,2,3]})
girls = pd.DataFrame({'k':['K0','K0','K3'], 'age':[4,5,6]})
print(boys)
print(girls)
print(pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner'))