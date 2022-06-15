import get_data
import relation
import pandas as pd
import create_kg
data_path = 'data/data1.txt'
with open(data_path,'r',encoding="utf-8") as f:
    data = f.read().split("。")
# print(data)
kg_dic = {
    "郝哲族":[],
    "描述":[],
    "关系":[]
}
print("下面开始生成三元组结构化数据")
for i in data:
    try:
        ret = relation.srl_AtoA(i)#每个列表包含若干个三元组
    except Exception as e:
        print(e)
    if ret:
        l = len(ret)
        for j in range(l):
            kg_dic["郝哲族"].append(ret[j][0])
            kg_dic["描述"].append(ret[j][1])
            kg_dic["关系"].append(ret[j][2])
print(kg_dic)  
df = pd.DataFrame(kg_dic)
print(df)
df.to_excel(data_path[:-4]+".xlsx")
create_kg.create_kg(df)
