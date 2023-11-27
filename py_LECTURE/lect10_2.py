""" import pandas as pd

folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target)

from faker import Faker as fk
import os

# temp = fk()
temp = fk("ko-KR")
print(temp.name())

folder = "data/"
if not os.path.isdir(folder):
    os.mkdir(folder)

with open(folder + "fktemp.csv", "w", encoding='utf8') as f :
    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")

with open(folder + "fktemp.csv", "a", newline='', encoding='utf8') as f :
    for i in range(30) :
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
        
""" import pandas as pd

folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target)

# print(df.name == "윤아름")
# print(df.company == "박이박")

# temp = df[df.postcode > 70000]
# print(temp)

# res = df[df.color == "Maroon"].head(1)
# print(res)

# res = df[df.postcode > 70000][["name", "postcode", "color"]]
# print(res)
# print(res.count)

# temp = df.postcode.mean()
# temp = df.postcode.sum()
# print(temp)

# temp = df[df.color=="Maroon"].postcode.mean()
# print(temp)

# temp = df[df.color=="Maroon"].postcode.sum()
# print(temp)

# temp = df[df.postcode > df.postcode.mean()][["name", "postcode"]]
# temp = df[df.postcode > df.postcode.mean()]
# print(temp)

# temp = df.company.isnull()   # ---------
# for el in temp :
#     if el == True :
#         print(el)

# temp = df.company.empty
# temp = df[df.company.isnull()]["name", "postcode"]   # ---------
# print(temp)

# temp = df[(df.color == "Maroon")]
# temp = df[~(df.color == "Maroon")]
# temp = df[~(df.color == "Maroon")][["name"]]   # ---------
# print(temp.count())
# print(temp.color.count())
# print(temp)

# temp = df[(df.color == "Maroon") & (df.postcode > 70000)]
# temp = df[(df.color == "Maroon") | (df.postcode > 70000)]
# temp = df[(df.color == "Maroon") | (df.postcode > 70000)][["name"]]
# print(temp)

# temp = df.sort_values("postcode")
# temp = df.sort_values("postcode", "ascending=False")   # ---------
# temp = df.sort_values("name", ascending=True)
# print(temp) """



# pivot, 데이터 재배열

""" import pandas as pd

col = ['Machine','Country','Price','Brand']
data = [['TV','Korea',1000,'A'],
        ['TV','Japan',1300,'B'],
        ['TV','China',300,'C'],
        ['PC','Korea',2000,'A'],
        ['PC','Japan',3000,'E'],
        ['PC','China',450,'F']]
df = pd.DataFrame(data=data, columns=col)
print(df)

print("\n------------------------------\n")
# print(df.pivot(index='Machine',columns='Country',values='Price'))
# print(df.pivot(index='Brand',columns='Machine',values='Price'))
# print(df.pivot(index='Country',columns='Machine',values='Price'))
# print(df.pivot(index='Price',columns='Brand',values='Machine')) """

# rank 매기기

""" import pandas as pd

folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target) """
""" df["aver"] = df.postcode.rank(method="average")
# print(df[["postcode", "aver"]])

df["dense"] = df.postcode.rank(method="dense")
# print(df[["postcode", "dense"]])

df["first"] = df.postcode.rank(method="first")
# print(df[["postcode", "first"]])

df["min"] = df.postcode.rank(method="min")
# print(df[["postcode", "min"]])

# df["max"] = df.postcode.rank(method="min", ascending=False)
df["max"] = df.postcode.rank(method="max")
# print(df[["postcode", ",max"]])

print(df[["postcode", "max", "min", "first", "dense", "aver"]]) """

# 전치 컬럼=로우변환
# print(df.transpose())

# 누적 계산
# print(df["postcode"].expanding().sum())
# print(df["postcode"].expanding())

# 내림차순 기준
# print(df.postcode.idxmax(axis=0)) # 가장 작은 수
# print(df.postcode.idxmin(axis=0)) # 가장 큰 수

# empty 추가
# print(df.empty)
# print(df.postcode.empty)

# 검색
# print(df.isin([53770]))
# print(df.isin(["김하윤"]))

# print(df.isin([53770, 67238]))

# print(df.isin([53770, 67238, "김하윤"]))

# 기간 계산

""" # period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
dt = {"col1":[1,2,3,4,5,6],"col2":period}
idx = ["row1","row2","row3","row4","row5","row6"]
pf = pd.DataFrame(data=dt, index=idx)
print(pf) """

# 인덱스 시간 - 간격 생성

""" # i = pd.date_range("2023-11-10", periods=10, freq="1H")
i = pd.date_range("2023-11-10", periods=10, freq="3H")
df = pd.DataFrame({"col1":[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)

# print("\n---------------------------\n")
# 특정시간 찾기
# print(df.at_time("09:00"))
# print(df.at_time("03:00"))

# print("\n---------------------------\n")
# 범위 찾기
# print(df.between_time(start_time="12:00", end_time="00:00"))
# print(df.between_time(start_time="03:00", end_time="09:00"))

# x일 간격 생성 - 기간별 찾기
i = pd.date_range("2023-11-10", periods=10, freq="3D")
# i = pd.date_range("2023-11-10", periods=10, freq="5D")
df = pd.DataFrame({'col1':[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)

# print(df.first("5D"))

print(df.first("7D"))

print(df.last("7D")) """



""" # pip install Finance-DataReader
import FinanceDataReader as fdr

# ksp = fdr.DataReader("KS11", "2023")
ksp = fdr.DataReader("KS11", "2001")
print(ksp)
print("\n---------------------------\n")

# 최고가
# res = ksp["High"].max()
# print(res)

# res = ksp["High"].idxmax()
# print(res)

# 최저가
# res = ksp["Low"].min()
# print(res)

# res = ksp["Low"].idxmin()
# print(res)

# 최고가
# res = ksp["Volume"].nlargest(n=5)
# res = ksp["Volume"].nlargest(n=10)
# print(res)

# 최저가
# res = ksp["Volume"].nsmallest(n=5)
# res = ksp["Close"].nsmallest(n=5)
# res = ksp["Close"].nlagest(n=5)
# print(res)

# 3000 최초일
# cond = ksp["Close"] >= 3000
# cond = ksp["Close"] >= 2000
# res = ksp[cond].index[0]
# print(res)

# 위 값 참조 처리

# res = ksp["Volume"] > ksp["Volume"].shift()
# print(res)

ksp["up"] =  ksp["Volume"] > ksp["Volume"].shift()
# print(ksp)

# res = ksp["up"] != ksp["up"].shift().cumsum()
# print(res)

ksp["grp"] = (ksp["up"] != ksp["up"].shift()).cumsum()
# print(ksp)

# 연속 증가값 확인
ksp["up_cnt"] = ksp["grp"].groupby(ksp["grp"].values).cumcount() + 1
# print(ksp)

# 연속 상승값 확인
res = ksp["up_cnt"].max())
print(res) """

# 변환

""" import pandas as pd

target = "./data/apt.csv"

df = pd.read_csv(target, encoding="CP949")

df.to_csv("./data/conv_apt.csv", encoding="utf8")

print(df.head) """

""" import pandas as pd

df = pd.read_csv("./data/conv_apt.csv", index_col=0)

print(df.head())

# 컬럼명 바꾸기
print("\n---------------------------\n")
df = df.rename(columns={"분양가격(제곱미터)":"분양가"})
# print(df)
# 컬럼 타입변경
# print(df.dtypes) 

df["분양가"] = df["분양가"].convert_dtypes()
# print(df.dtypes)

# array 변환
# arr = df.to_numpy()
# print(arr)
# print(arr[2])
# print(len(arr))

# 요약정보
# print(df.describe())

# 축변환하기
# print(df.transpose())
# print("\n---------------------------\n")
# print(df.T.head())

# 정렬
# res = df.sort_values(by="지역명")[:5]
# print(res)

# res = df.sort_values(by="지역명")
# res = df.sort_values("지역명")
# res = df.sort_values("지역명", ascending=True)
res = df.sort_values("지역명", ascending=False)
# print(res.head(10))
# print(res.head())

# res = df.sort_values(by="연도")
# res = df.sort_values(by="분양가")
res = df.sort_values(by="연도")[10:20]
# print(res)
# print(res.head())

# 컬럼이름 출력
# res = df["지역명"][:5]
# res = df[["지역명", "연도"]]
# res = df[["지역명", "연도", "분양가"]]
res = df[["지역명", "연도", "분양가"]][:7]
# res = df[["지역명", "연도"]][:5]
# print(res)

# print("\n---------------------------\n")
# res = df.loc[:, ["지역명", "연도", "분양가"]][:5]
# res = df.loc[:][:5]
#res = df.loc[:][:]
# res = df.iloc[1]
# print(res)

# res = df.loc[:6, ["지역명", "연도"]]
# res = df.loc[:6, ["지역명", "연도"]][:3]
res = df.loc[:6, ["지역명", "연도"]][3:]
# res = df.loc[6:, ["지역명", "연도"]][:7]
# print(res)

# 필터 출력
# res = df.loc[df["지역명"]=="강원"]
# res = df.loc[df["연도"] > 2020]
# res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]]
# res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]][:10]
res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]][-10:]
# print(res)

# 인덱스 지정 선택
df0 = df.copy()
# print(df0)

# print("\n---------------------------\n")
# res = df.iloc[2]
res = df.iloc[2][2]
# print(res)

# 인덱스 필터
res = df[df.index > 3560]
# print(res)

# 필터
# res  = df[df.연도 == 2023]
res  = df[df.월 == 3]
# print(res)

# 비트연산 필터
# res = df[(df.연도 == 2023) & (df.지역명 == "서울")]
# res = df[(df.연도 == 2023) & (df.지역명 == "서울") & (df.월 == 6)]
# print(res)

# 컬럼 추가

# columns=list(df.columns)
# print(columns + "컬럼")

# df1 = df.reindex(index=df.index[:7], columns=list(df.columns) + ["extra"])
df1 = df.reindex(columns=list(df.columns) + ["extra"])
# print(df)
# print("\n---------------------------\n")
# print(df1)

print("\n---------------------------\n")
# df1.loc[:6, "extra"] = "0"
# df1.loc[:4, "extra"] = False
# print(df1)

# 복사
df2 = df1.copy()

# Nan 행 제거
# res = df2.dropna(how="any")
# res = df2.fillna(value="1234")
res = df2.fillna(value="1234", inplace=True)
# print(df2)
# print("\n---------------------------\n")
# res = df2.dropna(how="any", inplace=True)
# print(res)

# print("\n---------------------------\n")
# print(df2)

# Nan 데이터 출력
# res = pd.isna(df1)
# res = pd.isna(df)
# res = pd.isna(df0)
# res = pd.isna(df2)
# print(res)

# 데이터 종류별 출력
# res = df["연도"].value_counts()
# res = df["지역명"].value_counts()
# res = df["월"].value_counts()
# res = df.월.value_counts()
# print(res)

# 그룹핑
# res = df.groupby(["지역명", "연도", "월"]).sum()
# res = df.groupby(["지역명", "연도", "월"]).all()
# print(res)

res = df.groupby(["지역명", "연도", "월"])["분양가"].agg("sum")
print(res) """