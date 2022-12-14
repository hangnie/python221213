# function3.py
# 가변형식인 경우
wordlist = ["J","A","M"]
 
 #함수정의
def change(x):
    #복사본을 생성
    x1 = x[:]
    x1[0] = "H"
    print("내부:",x1)

#호출
change(wordlist)
print(wordlist)


print("--- global키워드 ---")
g = 1
def testScope(a):
    #외부에 있는 전역변수를 맵핑
    # global g
    g = 2
    return g+a

#호출
testScope(1)
print("전역변수 g:",g)
# testScope(g)


#교집합 문자를 리턴
def intersect(prelist, postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

#호출
print(intersect("HAM", "SPAM"))
