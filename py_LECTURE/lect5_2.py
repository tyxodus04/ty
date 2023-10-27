#file exist

""" import os

fp = "filemod.py"
# fp = "temp1.txt"
#file = open(fp, "w")

if os.path.exists(fp) :
	print("ok")
    file = open("temp.txt", "a")
    
else :
	print("error")
    file = open("temp.txt", "w") """
 
#file.close()

# exception file read

""" import os

fp = "temp.txt"

if os.path.exists(fp) :
    f = open(fp, "r")
    for line in f:
        print(line)
else :
    f = open(fp, "w")
    for i in range(100):
        f.write(str(i) + "\n")
	#print("error")
 
f.close() """

# 파일 삭제

""" import os

fp = "new.txt"

f = open(fp, "w")
f.close()

os.remove(fp)
print("complete") """

# dir 출력

""" import os

def dir_print(p) :
	files = os.listdir(p)
	for f in files :
		print(f)

fp = "new.txt"

f = open(fp, "w")
f.close()

dir_print("./")

os.remove(fp)
print("-------------------------\n\n")
dir_print("./") """

# 파일명 변경

""" import os

fp = "new.txt"

f = open(fp, "w")
# f.close

os.rename(fp, "new1.txt")
print("complete") """

# 재배열 예외처리

""" import os

fp = "new.txt"
tp = "new1.txt"

f = open(fp, "w")
f.close

if os.path.exists(tp):
    print("exist, same name file")
    os.remove(tp)
else:
    os.rename(fp, "new1.txt")
    print("complete") """
    
# 파일명 변경 확인

""" import os

def dir_print(p) :
	files = os.listdir(p)
	for f in files :
		print(f)
  
fp = "new.txt"
tp = "new1.txt"

f = open(fp, "w")
f.close

dir_print("./")
print("\n==========================")

if os.path.exists(tp):
    os.remove(tp)
    dir_print("./")
    print("exist, same name file")
else:
    os.rename(fp, "new1.txt")
    dir_print("./")
    print("complete") """
    
# with

""" # f = open("temp.txt", "r")
with open("temp.txt", "r") as f:
    print(f.read())
    
    # for i in range(110):
    #     res = f.readline()
    #     print(res) """