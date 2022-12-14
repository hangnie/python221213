# function 2.py
def setValue(newValue) :
    # 지역변수
    x = newValue
    print(x)

#호출
retValue = setValue(5)
print(retValue)

# 함수 정의
def swap(x,y):
    return y,x

# 호출
print(swap(3,4))

print("--- 불변형식 ---")
a = 1.2
print( id(a))
a = 2.3
print( id(a))

print("--- 가변형식 ---")
lst = [1,2,3]
print( id(lst))
lst.append(4)
print( id(lst))

print("--- 이름을 해석하는 순서 ---")
# 함수정의
def func1(a):
    x = 1
    return x+a

#호출
print(func1(1))

# 함수정의
x = 5
def func2(a):
    return x+a

#호출
print(func2(1)) 

