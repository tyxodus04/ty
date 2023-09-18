# input

""" num = input("숫자를 입력하세요!!")
print("number", int (num)) """

# type

""" a = 12
print(type(a))

a = 12.01
print(type(a))

a = "a"
print(type(a))

a = "abcd"
print(type(a))

a = [3,2,1]
print(type(a)) """

# 행변환

""" a = "65"
# print(int(a))
# print(str(a))
# print(hex(a))  #정수를 16진수 문자열 반환
# print(oct(a))  #정수를 8진수 문자열 반환
# print((chr(a)))  #정수를 문자로 반환 하기 ASCII Code(아스키코드) 확인
print(ord("A"))  #문자를 아스키코드로 반환 하기 ASCII Code 확인 """


""" print(pow(2, 2))  #pow = 거듭제곱을 계산
print(pow(2, 6))
print(pow(3, 4))
print(3 ** 4) """

# print(divmod(10, 3)) #divmod = 나누기 몫과 나머지를 반환

# print(round(3.14))  #round = 버림하여 반환

""" a = (3, 5, 7)
b = list(a)
c = tuple(b)

print(b)
print(c)

print(type(a))
print(type(b))
print(type(c)) """



# !!! alt + shift + 방향키 위아래 하면 커서가 있는곳 위나 아래로 복사
# !!! ctrl + / 여러 줄 # 주석 처리
# !!! alt + shift + a """ """ 주석 처리



# range

""" for i in range(2,7):
    print(i) """

""" for i in range(6):
    print(i) """

""" for i in range(1, 20, 3):
    print(i) """

# max, min, sum

""" a = [3, 5, 6, 9]
print(max(a))
print(min(a))
print(sum(a)) """

# abs  #절댓값 반환

""" print(abs(-3))
print(abs(3.0))
print(abs(-3.0)) """

# sorted  #데이터 타입 내 정렬

""" a = [5, 3, 1, 9, 4]
print(sorted(a))
print(sorted(a, reverse=True)) """

# enumerate  #데이터 타입 내 인덱스와 값 반환

""" a = [5, 3, 14, False, 9, "string"]
print(enumerate(a))
print(*enumerate(a)) """

# zip  #여러 데이터 타입 내 데이터를 합쳐서 반환

""" a = [1, 2, 3]
b = [4, 5, 6]
print(zip(a, b))
print(*zip(a, b)) """

# any, all  #데이터 타입 내 요소중 True/False 인지 확인, any는 or 연산, all은 and 연산

""" a = [True, True, False]
b = [True, True, True]
print(any(a))
print(all(a))
print(all(b)) """

# format  #문자열 포맷팅 처리

""" a = 20
b = 23
c = "a 는 {}, b 는 {}, {}".format(a, b, "python")

print(c) """

""" a = 3
# print(globals())  #전역 테이블을 나타내는 딕셔너리를 반환
# print(locals())   #지역 테이블에 나타내는 딕셔너리를 반환

# print(dir(a))  #객체가 가지고 있는 모든 속성과 메서드를 반환

print(callable(a))  #객체 호출 가능여부 확인 """

# lambda 함수  #함수를 간단하게 정의하고 사용할 때 유용합니다. 하지만 너무 복잡한 함수를 만들거나 긴 함수를 만들때는 일반적인 함수를 사용하는것을 권장합니다.

""" add = lambda a, b : a + b
print(add(2, 3))
 """

""" add = lambda a, b : a + b
sub = lambda a, b : a - b
mul = lambda a, b : a * b
div = lambda a, b : a / b

print(add(2, 3))
print(sub(2, 3))
print(mul(2, 3))
print(div(2, 3)) """

# 사용자 정의

""" def add_numbers(x, y):
    return x + y

# 함수 호출

result = add_numbers(4, 5)
print(result) """

""" def greet(name):
    print(name)
    print("Hello, " + name + ". How are you?")

greet("python") """

""" def add(a, b) : 
	print(a + b)

def sub(a, b) :
	return a - b

def mul() :
	return 2 * 4

def div() :
	print(4 / 2)

add(3, 5)
print(sub(3, 5))
print(mul())
div() """

# 입력값 홀/짝수

""" def is_even(n) :
	if n % 2 == 0 :
		print("짝수")
	else :
		print("홀수")

num = input("숫자를 입력하세요 : ")

is_even(int(num)) """

# 문자열 반전

""" def reverse_string(msg):
    return msg[::-1]

in_str = input("문자열 : ")
print(reverse_string(in_str)) """

# 두 수를 입력 받아 사칙 연산

""" def add(a, b) :
    return int(a) + int(b)

def sub(a, b) :
    return int(a) - int(b)

def mul(a, b) :
    return int(a) * int(b)

def div(a, b) :
    return int(a) / int(b)

a = input("a 를 입력하세요")
b = input("b 를 입력하세요")

print("더하기 : ", add(a, b))
print("빼기 : ", sub(a, b))
print("곱하기 : ", mul(a, b))
print("나누기 : ", div(a, b)) """

""" def calc(a, b) :
    print(int(a) + int(b))
    print(int(a) - int(b))
    print(int(a) * int(b))
    print(int(a) / int(b))

a = input("a 를 입력하세요")
b = input("b 를 입력하세요")

calc(a, b) """

# 5개 수 입력

""" def sum_num(num) :
    return(sum(num))

nums = []

for i in range(1, 6) :
    inum = int(input(f"(i) 번째 숫자 입력 : "))
    nums.append(inum)

print(sum_num(nums)) """