""" my_set = {1, 2, 3, 4, 5}
print(my_set)

setItem = {5, 3, 1}
print(setItem) """

""" my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
print(*my_set) """

""" my_set = set([5, 8, 3, 7, 1, "h"])

print(my_set)

set_tmp = set("hello")

print(set_tmp) """

""" my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}

print(my_set | set_item)

#print(my_set.union(set_item))

#print(my_set - set_item)

#print(my_set.difference(set_item))

print(my_set.intersection(set_item)) """

""" my_set = {5, 8, 3, 7, 1, "h"}

print(my_set)

#my_set.add(9)

my_set.update([5, 9, 7, 4])

print(my_set) """

""" my_set = {5, 8, 3, 7, 1, "h"}

print(my_set)

#my_set.clear()

#my_set.remove(5)

my_set.discard(2)
print(my_set)

#remove는 없는 걸 지우면 오류/difcard는 없어도 지울 수 있음 """

""" my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}

print(my_set)

my_set.difference_update(set_item)
print(my_set) """

""" my_int = 10

print(my_int)

my_str = str(my_int)

print(my_str) """

""" my_int = 10
print(my_int)

print(my_int + 10)
my_str = str(my_int)

print(my_str)

#print(my_str + 10)

print(my_str + " hello") """

""" my_str = '10'
print(my_str)

my_int = int(my_str)
print(my_int)

print(my_int + 10)

my_int2 = int("ten")
print(my_int2) """

#사칙연산

""" a = 10
b = 3

#c = a + b
#c = a - b
#c = a / b
#c = a * b
#c = a % b     나머지
#c = a // b    몫
c = a ** b     #거듭제곱

print(c) """

""" a = 0
print(a)

a += 2
print(a)

a -= 1
print(a)

a *= 4
print(a)

a /= 2
print(a)

a **= 3
print(a) """

""" a = 10
b = 4

print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a != b) #!=은 다른 걸 찾는 연산자기 때문에 다르면 트루를 나타냄  """

#논리 연산자

""" a = 1
b = 0

print(a and b)
print(a or b)
print(not b)


x = True
y = False

print(x and y)
print(x or y)
print(not x)
print(not y) """

a = 10
b = 3

#c = a & b   AND 연산
#c = a | b   OR 연산
#c = a ^ b   XOR 연산
#c = ~ a     NOT 연산
#c = a << 2  시프트 연산
c = a >> 2   #시프트 연산

print(c)