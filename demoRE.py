# demoRE.py

import re

result = re.search("[0-9]*th", " 35th")  # 숫자가 있거나 없거나 th문자열 패턴 찾기, "35th"는 data
print(result)
print(result.group())

# result = re.match("[0-9]*th", " 35th") # 숫자가 있거나 없거나 th문자열 패턴 찾기, "35th"는 data, 스페이스가 있으면 오류 정확히 찾을 문자열 조건을 넣어줘야함
# print(result)
# print(result.group())

result = re.search("apple", " this is apple")  
print(result.group())

# result = re.match("apple", " this is apple") 
# print(result.group())

# 컴파일 함수 사용
s = "Apple is big company and apple is very delicious"
#대소문자를 구분안함
c = re.compile("apple",re.I)
print(c.findall(s))

print("--- 연도 찾기 ---")
result = re.search("\d{4}","올해는 2022년")
print(result.group())
result = re.search("\d{5}","우리동네는 52300")
print(result.group())
