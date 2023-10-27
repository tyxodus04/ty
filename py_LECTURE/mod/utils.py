import math
import random
from datetime import datetime as dt
import os

def mt_sqrt(x):
    return math.sqrt(x)

def mt_sinpi():
    return math.sin(math.pi / 2)

def mt_elog():
    return math.log(math.e)

def mt_exp(x):
    return math.exp(x)

def mt_pi():
    return math.pi

def rd_int(x, y):
    return random.randrange(x, y)

def rd_list(this):
    return random.choice(this)

def rd_rd():
    return random.random()

def rd_normalvariate():
    return random.normalvariate(0.1)

def get_dtnow():
    return dt.now()

def cvt_time2str(objtime):
    return dt.strptime(objtime, "%Y-%m-%d")

#def cvt_str2time(Strtime):
    return dt.strftime("%Y-%a-%d")

def cvt_str2time():
    obj = dt.now
    return obj.strftime("%Y-%m-%d")

# 특정 시간대의 현재 시간 출력
# from pytz import timezone
#import timezone
# tz = timezone('Asla/Seoul)
#tz = timezone('UTC')
#print("timezon : ", dt.now(tz))

# 문자열을 날짜로 변환
""" date_string = '2021-07-08'
date_object = dt.strptime(date_string, '%Y-%m-%d')
print(date_object)

# 날짜를 문자열로 변환
date_object = dt.now()
date_String = date_object.strftime('%Y-%m-%d')
print(date_string) """

def get_curdir():
    return os.getcwd()

""" # 현재 작업 디렉토리 출력
print(os.getcwd())

# 디렉토리 변경
os.chdir('../')
# 변경된 디렉토리 출력
print(os.getcwd())

# 파일 목록 출력
print(os.listdir())

# 디렉토리 생성
os.mkdir('new_directory')
print(os.listdir())

# 디렉토리 삭제
os.rmdir('new_directory')
print(os.listdir()) """

def os_mkdir(pname):
    return os.mkdir(pname)