# 입력 암호화

""" import getpass

# pw = getpass.getpass("Pass : ")
pw = input("Pass :")
print(pw) """

# 해시 알고리즘

""" import hashlib

hl = hashlib.sha256()
# target = "hello"
# target = "hi"
# target = "world"
# target = "python"
# target = "media"
# target = "media proram"
# target = "1234567890"
target = "to be or not to be, That is a question!"

hl.update(target.encode("utf-8"))
print(hl.hexdigest())
# print(hl.digest()) """

# keccak256

""" import Crypto.Hash.keccak as kek

# target = "hello"
# target = "hi"
# target = "world"
# target = "python"
# target = "media"
# target = "media proram"
# target = "1234567890"

target = "to be or not to be, That is a question!"

kksh = kek.new(digest_bits=256)
kksh.update(target.encode("utf-8"))

# print(kksh.digest())
print(kksh.hexdigest()) """

# 입력키 변환

""" import getpass
import hashlib

pw = getpass.getpass("Pass: ")
print(pw)

hl = hashlib.sha256()

hl.update(pw.encode("utf-8"))
print(hl.digest())
print(hl.hexdigest()) """

# 암호 파일 저장

""" import hashlib
import os

def pwInsert():
    if os.path.exists('pw.txt'):
        pw = input('insert pass :')
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        with open('pw.txt', 'r') as fp:
            return hs.hexdigest() == fp.read()
    else:
        return True
    
if pwInsert():
     pw = input('new pass :')
     with open('pw.txt', 'w') as fp:
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        fp.write(hs.hexdigest())
else:
    print("not allow password") """
    
# 시스템 정보

""" import platform as pf

pn = pf.uname()
print(pn)

pm = pf.machine()
print(pm)

pp = pf.processor()
print(pp)

ps = pf.system()
print(ps) """

# 웹정보 읽기

""" import urllib.request as ur

url = 'https://www.google.com'

# res = urllib.request.urlopen(url)
res = ur.urlopen(url)

web = res.read()

with open("ul.html", "wb") as fp:
    fp.write(web)
    
# print(web.decode('utf-8'))
print(web) """

# 웹정도 읽기2

""" import http.client as hc

# url = "https://www.google.com"
# url = "www.google.com"
# url = "www.daum.net"
url = "v.daum.net"
# conn = http.client.HTTPSConnection(url)
conn = hc.HTTPSConnection(url)
# conn.request("GET", "/")
conn.request("GET", "/v/20231103063908539")

r = conn.getresponse()

with open("ulcl.html", "wb") as fp:
    fp.write(r.read())
    
conn.close()

print(r) """

# 웹정보 읽기3

""" import requests

url = "https://www.google.com"
res = requests.get(url)
web = res.content

with open("ulrp.html", "wb") as fp:
    fp.write(web)
    
print(web) """

# 싱글스레드

""" import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

start = time.time()
for i in range(3) :
    counter(f"num{i}")
    
end = time.time()

# print("sigle end")
print("single end", end - start) """

# 멀티스레드

""" import threading as td
import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

thread1 = td.Thread(target=counter, args=("1num",))
thread2 = td.Thread(target=counter, args=("2num", ))
thread3 = td.Thread(target=counter, args=("3num", ))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
end = time.time()

print("multi end", end - start) """

# 병렬처리

""" import multiprocessing as mp
import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

if __name__ == "__main__":
    process1 = mp.Process(target=counter, args=("1num",))
    process2 = mp.Process(target=counter, args=("2num",))
    process3 = mp.Process(target=counter, args=("3num",))

    start = time.time()

    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()
    end = time.time()

    print("proc-end", end-start) """

# main 실행

""" def main() :
    print("hello world")

def run() :
    print("hello python")

if __name__ == "__main__":
    # run()
    main() """
    
# 비동기 처리 1

""" import asyncio
import time

async def worker1():
    for i in range(1, 6):
        print(f"Task 1: Step {i}")
        await asyncio.sleep(1)

async def worker2():
    for i in range(1, 4):
        print(f"Task 2: Step {i}")
        await asyncio.sleep(2)
        
async def main():
    
    task_1 = asyncio.create_task(worker1())
    task_2 = asyncio.create_task(worker2())
    
    print("start task")
    start = time.time()
    await task_1
    await task_2
    end = time.time()
    print("end-", end-start)
    print("end task")
    
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main()) """
    
# 비동기 처리 2

""" import asyncio
import random as rd
import time

async def tester(name):
    snum = rd.randint(10, 20)
    print(f"{name} - {snum}")
    for i in range(snum):
        await asyncio.sleep(1)
        print(f"{name} - {snum} - {i}")
        
    print(f"end of {name}")
    
async def main():
    task1 = asyncio.create_task(tester("1test"))
    
    task2 = asyncio.create_task(tester("2test"))
    
    task3 = asyncio.create_task(tester("3test"))
    
    print("start")
    start = time.time()
    await task1
    await task2
    await task3
    end = time.time()
    print("end", end-start)
    
if __name__ == '__main__':
    asyncio.run(main()) """
    
# 스케쥴 처리

""" import time
import sched

start = time.time()

def tester(name):
    print(f"start-time {time.time() - start}")
    for i in range(3):
        print(f"{name} - {i}")
        
    print(f"end of {name}")

def run():
    s = sched.scheduler()
    s.enter(5, 1, tester, ('1num',))
    s.enter(5, 1, tester, ('4num',))
    s.enter(3, 1, tester, ('2num',))
    s.enter(7, 1, tester, ('3num',))
    s.run()

if __name__ == "__main__":
    run()
    # main()
    print("end") """
    
# 문자열 비교

""" import diff_match_patch.diff_match_patch as dm

origin = "To be or not to be, That is a question!"
copyed = "To be and not to be, That is a question!"

dmp = dm()
diff = dmp.diff_main(origin, copyed)
print(diff)
dmp.diff_cleanupSemantic(diff)

for d in diff:
    print(d) """
    
# faker 임의 데이터

""" from faker import Faker as fk

# temp = fk()
temp = fk("ko-KR")
print(temp.name())

# temp = fk("ko-KR")
print(temp.name() + "\n" + 
	temp.address() + "\n" + 
	temp.postcode() + "\n" + 
	temp.company() + "\n" + 
	temp.job() + "\n" + 
	temp.phone_number() + "\n" + 
	temp.email() + "\n" + 
	temp.user_name() + "\n" + 
	temp.ipv4_private() + "\n" + 
	temp.ipv4_public() + "\n" + 
	temp.catch_phrase() + "\n" + 
	temp.color_name() + "\n") """
 
# foker - csv 파일 저장

""" from faker import Faker as fk

# temp = fk()
temp = fk("ko-KR")
print(temp.name())

# with open("fktemp.txt", "w", newline='') as f:
with open("fktemp.csv", "w", newline='') as f:
    for i in range(30):
        f.write(temp.name() + "," + 
	        temp.address() + "," + 
	        temp.postcode() + "," + 
	        temp.company() + "," + 
	        temp.job() + "," + 
	        temp.phone_number() + "," + 
	        temp.email() + "," + 
	        temp.user_name() + "," + 
	        temp.ipv4_private() + "," + 
	        temp.ipv4_public() + "," + 
	        temp.catch_phrase() + "," + 
	        temp.color_name() + "\n") """
         
# 시스템 명령어 사용

""" import subprocess as sp

# res = sp.run(["cmd", "/c", "dir"], capture_output=True)
# res = sp.run(["cmd", "/c", "dir"], capture_output=False)
res = sp.run(["cmd", "/c", "ipconfig", "/all"], capture_output=False)
# res = sp.run(["cmd", "/c", "ipconfig", "/all"], capture_output=True)
print(res) """

# 에러처리

""" import traceback as td

def tester():
    # return 1/0
    return 1

def caller():
    tester()

def main():
    try:
        caller()
        
    # except ZeroDivisionError:
    #    print("zde error")
        
    except ValueError:
        print("ve error")
        
    except Exception as ex:
        print("ex error", ex)
        
    else:
        print("ok")
        
    finally:
        print("end") """