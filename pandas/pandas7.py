import pandas as pd

# convert dict to pandas

data = {'000001.XSHE': {'jq_concept': [{'concept_code': 'SC0105', 'concept_name': '深股通'}, {'concept_code': 'SC0175', 'concept_name': '证金持股'}, {'concept_code': 'SC0219', 'concept_name': '转融券标的'}]}, '000002.XSHE': {'jq_concept': [{'concept_code': 'SC0091', 'concept_name': '装配式建筑'}, {'concept_code': 'SC0105', 'concept_name': '深股通'}, {'concept_code': 'SC0186', 'concept_name': 'MSCI'}, {'concept_code': 'SC0302', 'concept_name': '信创'}]}}
df = pd.DataFrame.from_dict(data)
print(df)
df.to_csv("temp.csv")