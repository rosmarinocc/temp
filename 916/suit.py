import pandas as pd
import json
import re
import random


def doCorrect(critic: pd.Series):
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

    num_str_list_needrand = list(set(num_str_list_total).difference(set(num_str_list_used)))

    for num_str in num_str_list_needrand:
        loc = int(num_str[-1])
        numbers.insert(loc, float(random.randint(1, 100)))

    for idx, num in enumerate(numbers):
        body_instance = body.replace(("numbers" + str(idx)), num)
        linear_instance = linear_formula.replace(("numbers" + str(idx)), num)


# random_int = random.randint(1, 100)
# print(random_int)
#
# num_ins = len(critic["Numbers"])
#
# # Linear_Formula 纠错
# p = re.compile(r".*?(number\d).*?")
# linear_formula = critic["Linear_Formula"]
# num_str_list = re.findall(p, linear_formula)
# for j, num_str in enumerate(num_str_list):
#     linear_formula = linear_formula.replace(num_str, ("number" + str(j)))
#
# critic["Linear_Formula"] = linear_formula

# # 数值回代
# body = critic["Body"]
# linear_formula = critic["Linear_Formula"]
# for i in range(num_ins):
#


df1 = pd.read_json("./1.json")
for idx in df1.index.values:
    doCorrect(df1.loc[idx])
#
#

# ss = "#0: subtract ( number0, number3 ) |  EOS"
# pattern_num = re.compile(r".*?(number\d).*?")
# res = re.findall(pattern_num, ss)
# print(res)

# num_ins = 2
#
# num_str_list = ['number0', 'number3']
# linear_formula = "#0: subtract ( number0, number3 ) |  EOS"
#
# for j, num_str in enumerate(num_str_list):
#     linear_formula = linear_formula.replace(num_str, ("number" + str(j)))
# print(linear_formula)

num_str_list_total = ["number1", "number2", "number3", "number4"]
num_str_list_used = ["number2", "number4"]

list1 = [50, 100, 200, 394892]
a = list(set(num_str_list_total).difference(set(num_str_list_used)))
print(a)

list1.insert(2, random.randint(1, 100))
list1.insert(4, random.randint(1, 100))

print(list1)

a = "halloe word"
b = a.replace("world", "cat")
print(b)
