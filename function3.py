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

print("--- 함수의 기본인자값 ---")
#함수의 기본인자값
def times(a=10, b=20):
    return a*b

#호출
print( times())
print( times(5))
print( times(5,6))

# 키워드인자(파라메터명을 명시)
print("--- 키워드인자(파라메터명을 명시) ---")
def connectURI(server,port):
    strURL = "http://" + server + ":" + port
    return strURL
    
#호출
print( connectURI("credu.com","80"))
print( connectURI(port="8080", server="credu.com"))

# 가변적인 경우(가변인자 *)
print("\n--- 가변적인 경우(가변인자 *) ---")
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

#호출
print( union ("HAM","EGG"))
print( union ("HAM","EGG","SPAM"))


# 정의되지 않은 인자(필수와 옵션이 같이 있는 경우 **)
print("\n--- 정의되지 않은 인자(필수와 옵션이 같이 있는 경우 **) ---")
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" +port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL

# 호출
print (userURIBuilder("credu.com","80", id="kim", passwd="1234"))
print (userURIBuilder("credu.com","80", id="kim", passwd="1234", age="30"))


# 간단하게 함수를 정의하는 문법:람다함수
# 입력을 받아서 : 뒤에서 처리
print("\n--- 간단하게 함수를 정의하는 문법:람다함수 ---")
g = lambda x,y:x*y  # 원래는 def times(x,y): return x*y 로 해야하는 것을 한줄로 작성
print(g(3,4))
print(g(5,6))
# 일회성으로 사용하고 버리기
print((lambda x:x*x)(3))
print(globals())



