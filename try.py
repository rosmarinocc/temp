import json
import re
#
# with open("/data/haixiahan/Data/Math/evaluation/han_critic_test_replace.json", "r", encoding='utf-8') as f:
#     data = json.load(f)

# for critic in data:
#     p = re.compile(r"((-?\d+)(.\d+)?)")
#     l1 = re.findall(p, critic["Equation"])
#     l2 = re.findall(p, critic["Linear_Instance"])


s1 = "( 26.0 - 9.0 )"
s2 =  "#0: subtract ( 26.0, 9.0 ) |  EOS"

p = re.compile(r"[^#]((-?\d+)(.\d+)?)")
l1 = [x[0] for x in re.findall(p, s1)]
l2 =[x[0] for x in  re.findall(p, s2)]
print(l1)
print(l2)
print(l1==l2)

# json_str = json.dumps(data, indent=4, ensure_ascii=False)
# with open("/data/haixiahan/Data/Math/evaluation/han_critic_test_replace.json", "w", encoding='utf-8') as json_file:
#     json_file.write(json_str)



l=["number1","number3","number0"]
l2=sorted(l)
print(l2)