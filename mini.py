# 직각 삼각형

""" for i in range(1, 6):
    print("*"*(i)) """
    
# 역직각삼각형

""" for i in range(5, 0, -1):
    print("*" * i) """
    
# 이등변 삼각형

""" for i in range(1, 6):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars) """
    
# n = 5 # 삼각형의 높이를 설정

""" for i in range(6, 0, -1):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars) """
    
    
# 다이아몬드

""" for i in range(1, 6):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)


for i in range(6, 0, -1):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars) """
    
# 5X5 출력

""" num = 0
line = []
for i in range(5):
    for j in range(5):
        num += 1
        line.append(num)
    print(line)
    line = [] """
    
# 세로 출력

""" # 내가 출력
line  = []
for i in range(1, 6):
    for j in range(1, 6):
        i += 5
        line.append(i - 5)
    print(line)
    line = [] """


""" # 교수님 출력
line  = []
for i in range(1, 6):
    for j in range(1, 6):
        num = ((j - 1) * 5) + i
        line.append(num)
    print(line)
    line = [] """
    
# 역순출

""" num = 26
line = []
for i in range(5):
    for j in range(5):
        num -= 1
        line.append(num)
    print(line)
    line = [] """
    
# 가위바위보 게임

""" # 참고 
import random

select = ["가위", "바위", "보"]
computer = random.choice(select)

while True:
    user = input("가위 바위 보 중에 하나를 입력하세요.> ")
    if user in select:
        break
    print("잘못된 입력입니다. 다시 입력하세요.")

print(f"컴퓨터는 {computer} 를 냈습니다.")
print(f"당신은 {user} 를 냈습니다.")

if user == "가위" and computer == "보" or \
   user == "바위" and computer == "가위" or \
   user == "보" and computer == "바위":
    print("당신이 이겼습니다.")
elif user == "가위" and computer == "가위" or \
   user == "바위" and computer == "바위" or \
   user == "보" and computer == "보":
       print("비겼습니다.")
else:
    print("당신이 졌습니다.") """


""" # 교수님 출력
import random

def get_computer_choice():
    choices = ['1', '2', '3']
    return random.choice(choices)

def determine_winner(user_choice):
    pcnum = get_computer_choice()
    print(user_choice, pcnum)
    
    if user_choice == pcnum:
        print("무승부")
        return
    elif(
    (user_choice == '1' and pcnum == '3') or
    (user_choice == '2' and pcnum == '1') or
    (user_choice == '3' and pcnum == '2')
   ):
        print("승")
        return
    else:
        print("패")
        return

print("1 : 가위")
print("2 : 바위")
print("3 : 보")
print("1~3 숫자를 입력하세요!")
chnum = input()
#pcnum = get_computer_choice()

determine_winner(chnum) """