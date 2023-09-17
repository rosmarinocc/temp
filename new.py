import re

pattern4 = re.compile(r"((-?\d+)(.\d+)?)")

s = "我的好嘛是范德萨打发1.314吗，的萨芬就卡了123434.3，你是2300.5"

print(re.findall(pattern4, s)[-1][0])
