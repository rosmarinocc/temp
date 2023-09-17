import json

import pandas as pd
import re

# 标准化回答结尾


df1 = pd.read_json("./test.json")


def finalAnswerExec(answer: dict):
    """
    将gpt_wrong、gpt_right结尾句处理成 ‘so, the final answer is xxx .’ 的形式

    case1：
    "final_answer": 6.222222222222222

    case2:
    "answer": 504.0

    case3:
    So, the final answer is 13000.0 dollars.

    case4: 更复杂的例子
    which is 12.0. 36.0 + 12.0 = 48.0 \n So, Karen picks up 48.0 cases of 12.0 boxes from the cookie mom.

    """
    analysis = answer["gpt_wrong" if "gpt_wrong" in answer else "gpt_right"]
    # try:  # 非json

    # pattern1 = re.compile(r"\"final_answer\"\s*:\s*((-?\d+)(.\d+)?)")
    pattern1 = re.compile(r"\"final_answer\"\s*:.*?((-?\d+)(.\d+)?)")
    # pattern2 = re.compile(r"\"answer\"\s*:\s*((-?\d+)(.\d+)?)")
    pattern2 = re.compile(r"\"answer\"\s*:.*?((-?\d+)(.\d+)?)")
    # pattern3 = re.compile(r"so\s*,\s*the\s*final\s*answer\s*is\s*((-?d+)(.d+)?)", re.IGNORECASE)
    pattern3 = re.compile(r"=\s*((-?\d+)(.\d+)?)\s*So", re.IGNORECASE)
    # print(analysis)
    try:
        if "\"final_answer\"" in analysis:
            final_value = re.search(pattern1, analysis).group(1)
            analysis = analysis + f"so, the final answer is {final_value}.\n"
        elif "\"answer\"" in analysis:
            final_value = re.search(pattern2, analysis).group(1)
            analysis = analysis + f"so, the final answer is {final_value}.\n"
        elif "So" in analysis or "so" in analysis:
            final_value = re.search(pattern3, analysis).group(1)
            analysis = analysis + f"so, the final answer is {final_value}.\n"
    except:
        print("Error")
        print(analysis)
    print(analysis)


# analysis = answer["gpt_wrong" if "gpt_wrong" in answer else "gpt_right"]
# # analysis=eval(analysis)
# analysis_str = ""
#
# answer_pattern = re.compile(r"so\s*,\s*the\s*final\s*answer\s*is", re.IGNORECASE)  # final-answer处理
# punc_pattern = re.compile(r"\.\s*$")  # 标点处理
# for k, v in analysis.items():
#     if "answer" in k:
#         # 一种情况,"so,the final answer"包含在前文
#         if re.search(answer_pattern, analysis_str) is None:
#             analysis_str = analysis_str + f"so,the final answer is {v} "
#         # 标点处理
#         analysis_str = (analysis_str.strip() + "\n") if re.search(punc_pattern, analysis_str) \
#             else (analysis_str.strip() + ".\n")
#     else:
#         analysis_str = analysis_str + f"{k}:{v}\n"


def numberAbove2Exec(answer: dict):
    """
    将question、wrong_instance、right_instance字段中的number3、number4...进行替换
    """
    question = answer["question"]
    instance = answer["instance"].split()
    instance2replace = answer["right_instance" if "right_instance" in answer else "wrong_instance"]

    for i in range(3, len(instance)):
        replace_str = "number" + str(i)
        question = question.replace(replace_str, instance[i])
        instance2replace = instance2replace.replace(replace_str, instance[i])


# for i in range(1,8):
#     for j in range(3):
#         finalAnswerExec(df1[i][j])
#
# pattern2 = re.compile(r"\"answer\"\s*:\s*((-?\d+)(.\d+)?)")
# a = """{
#   "analysis": "Step 1: Subtract the annual interest rate of 3.0% from the initial deposit of $70.0 to find the interest earned per year. 70.0 - 3.0 = 67.0\nStep 2: Multiply the interest earned per year by the number of years, 2.5, to find the total interest earned. 67.0 * 2.5 = 167.5\nStep 3: Multiply the total interest earned by 0.01 to convert it from a percentage to dollars. 167.5 * 0.01 = 1.675\n\nTherefore, you would earn $1.675 in simple interest in 2.5 years.",
#   "answer": 1.675
# }"""
#
# print(re.match(pattern2, a))
# print(re.search(pattern2, a))
# t=re.search(pattern2,a).group(1


# for i in range(1, 8):
#     for j in range(3):
#         answer = df1[i][j]["gpt_wrong" if "gpt_wrong" in df1[i][j] else "gpt_right"]
#
#         try:
#             analy_dict = json.loads(answer)
#         except:
#             print(answer)
#             # {analysis: step 1: Add ... So, you have 12.0 balloons in total.}
#             p = re.compile(r"{.analysis\s*:\s*", re.IGNORECASE)
#             answer=re.sub(p, answer, "\"analysis:\"")
#             print(answer)
#             analy_dict = json.loads(answer)
#             print(analy_dict)


a = """{analysis: step 1: Add the number of cupcake packages Maggi had, which is 3.0, to the number of cupcakes in each package, which is 4.0. 3.0 + 4.0 = 7.0
step 2: Subtract the number of cupcakes Maggi ate, which is 5.0, from the total number of cupcakes obtained in step 1. This will give you the number of cupcakes left. 7.0 - 5.0 = 2.0
so, the final answer is 2.0.
}
"""

p = re.compile(r"analysis\s*:\s*(.*)}", re.S)

print(re.search(p, a).group(1))

