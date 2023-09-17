import json
import pandas as pd


def numberAbove2Exec(answer: dict):
    """
    将question、wrong_instance、right_instance字段中的number3、number4...进行替换
    """

    instance = answer["instance"].split()

    for i in range(3, len(instance)):
        replace_str = "number" + str(i)
        answer["question"] = answer["question"].replace(replace_str, instance[i])
        answer["right_instance" if "right_instance" in answer else "wrong_instance"] = answer[
            "right_instance" if "right_instance" in answer else "wrong_instance"].replace(
            replace_str, instance[i])

    return answer


df1 = pd.read_json("./test.json")

dd = {}
for idx in df1.columns.values:
    n = len(df1[idx][0]["instance"].split())
    if n > 3:
        ll = []
        for i in df1.index.values:
            ll.append(numberAbove2Exec(df1[idx][i]))
        dd[str(idx)] = ll

json_dd = json.dumps(dd)

with open('num_test.json', 'w') as f:
    f.write(json_dd)
