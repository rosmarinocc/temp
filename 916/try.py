import pandas as pd
import json
import re
import random


def doCorrect(critic: dict):
    """
    将"Body"和"Linear_Formula"字段中的numberX进行实例代入，
    创建新字段"Body_Instance"和"Linear_Instance"
    """
    body = critic["Body"]
    linear_formula = critic["Linear_Formula"]
    numbers = critic["Numbers"]

    p = re.compile(r".*?(number\d).*?")
    num_str_list_total = re.findall(p, body)
    num_str_list_used = re.findall(p, linear_formula)

    num_str_list_needrand = sorted(list(set(num_str_list_total).difference(set(num_str_list_used))))

    for num_str in num_str_list_needrand:
        # 如果先插入的位置为4，超出了3会默认插在最后一位导致bug
        loc = int(num_str[-1])
        numbers.insert(loc, float(random.randint(1, 100)))

    for idx, num in enumerate(numbers):
        body = body.replace(("number" + str(idx)), str(num))
        linear_formula = linear_formula.replace(("number" + str(idx)), str(num))

    return {"Numbers": numbers, "Body_Instance": body, "Linear_Instance": linear_formula}


with open("./1.json", "r", encoding='utf-8') as f:
    data = json.load(f)

for critic in data:
    res = doCorrect(critic)
    critic["Numbers"] = res["Numbers"]
    critic["Body_Instance"] = res["Body_Instance"]
    critic["Linear_Instance"] = res["Linear_Instance"]

json_str = json.dumps(data, indent=4, ensure_ascii=False)
with open("./3.json", "w", encoding='utf-8') as json_file:
    json_file.write(json_str)
