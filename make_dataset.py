import pandas as pd
import json

df = pd.read_csv("poke.csv", encoding="shift-jis")
data = []
for _, item in df.iterrows():
    output_str = "{0}のタイプは、{1}".format(item["名前"], item["タイプ1"])
    if (pd.isnull(item["タイプ2"]) == False):
        output_str += "と{0}".format(item["タイプ2"])
    output_str += "です。"
    data.append({"input": "{0}のタイプを教えてください".format(item["名前"]), "output": output_str})
    data.append({"input": "{0}のタイプは何ですか？".format(item["名前"]), "output": output_str})
    data.append({"input": "{0}のタイプ".format(item["名前"]), "output": output_str})
    
with open("dataset.json", "wt") as f:
    json.dump(data, f, ensure_ascii=False)