import FinanceDataReader as fdr
# pip install Finance-DataReader
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests as rq

# 막대그래프
""" # x_years = ['2020', '2021', '2022']
# y_data = [100, 400, 900]
# clr = ["C2", "lime", "#57ADCC"]

# plt.bar(x_years, y_data)

# 문양 채우기
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="/")

# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="//")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="///")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="////")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="/////")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="//////")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="///////")

# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\\\")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\\\\\")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\\\\\\\")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\\\\\\\\\")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\\\\\\\\\\\")

# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="++")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="+++")

# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="*")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="o")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="oo")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="x")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="xx")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch=".")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="..")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="...") """

# 산점도 그래프
""" x = 1
y = 1

plt.scatter(1, 1)
plt.scatter(x+1, y+1)
plt.scatter(x+2, y+1)
plt.scatter(x+3, y+1)
plt.scatter(x+3, y+2)
plt.scatter(x+3, y+3)
plt.scatter(x+3, y+4)
plt.scatter(x+4, y+1)
plt.scatter(x+4, y+2)
plt.scatter(x+4, y+3)
plt.scatter(x+4, y+4)


# 크기, 색상 변경     # {x}{y}{포인트크기}{색상설정}{투명}
plt.scatter(x+1.5, y+1.5, 100, "C1")
plt.scatter(x+2.5, y+1.5, 150, "red")
plt.scatter(x+3.5, y+1.5, 200, 4)

plt.scatter(x+4.5, y+1.5, 200, "C6", alpha=0.5)

# plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="Spectral")
# plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="Blue")
# plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="viridis")
# plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="inferno")
# plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="plasma")
# plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="magma")
# plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="cividis")
# plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="spring")
# plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="flag")
plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="winter")

plt.colorbar()

plt.show() """

# 히스토그램 - 도수 분표(분표별 출력)

""" import numpy as np

rn = np.random.randint(1, 30, size=20)
print(rn)

# 라벨 설정
# plt.hist(rn,  bins=10, label="def") 



plt.hist(rn, bins=20)

# 투명도 설정
# plt.hist(rn,  bins=10, label="def", alpha=0.5)

# 그래프 스타일 설정
plt.hist(rn, bins=10, label="def", alpha=0.5, histtype="step")
# plt.hist(rn, bins=10, label="def", alpha=0.5, histtype="stepfilled")
# plt.hist(rn, bins=10, label="def", alpha=0.5, histtype="barstacked")


plt.legend()
plt.show() """

# 파이 차트
""" rate = [30, 40, 20, 10]
labels = ["Alpha", "Beta", "Gamma", "Delta"]

# plt.pie(rate)

# 라벨 표시
# plt.pie(rate, labels=labels)

# 퍼센트 표시
# plt.pie(rate, labels=labels, autopct='%.1d%%')
# plt.pie(rate, labels=labels, autopct='%d%%')
# plt.pie(rate, labels=labels, autopct='%.1f%%')
# plt.pie(rate, labels=labels, autopct='%.3f%%')

# 시작 각도 설정 a-b-c-d
# plt.pie(rate, labels=labels, autopct='%.1f%%')
# plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=0)
# plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=90)
# plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=270)

# 시작 방향 설정
#              시계방향으로 시작
# plt.pie(rate, labels=labels, autopct='%.1f%%', counterclock=False)
# plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=0, counterclock=False)
# plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False)
# plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=180, counterclock=False)
# plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=270, counterclock=False)

# 공백 설정
# plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[1, 1, 1, 1])
# plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0, 0, 0, 0])
# plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0.1, 0.1, 0.1, 0.1])
# plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0, 0.1, 0, 0.1])
# plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0, 0.1, 0, 0])
# plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0, 0.5, 0, 0])

plt.show() """

# 패널 스타일 설정
""" # print(plt.style.available) # 사용가능한 스타일 키

# plt.style.use("bmh")
# plt.style.use("ggplot")
# plt.style.use("classic")
# plt.style.use("Solarize_Light2")
# plt.style.use("dark_background")
# plt.style.use("fast")

plt.plot([2,3,6,7,10], [1,4,5,8,9])
plt.show() """

# 포맷 설정
""" # plt.rcParams['figure.figsize'] = (1, 2)
# plt.rcParams['figure.figsize'] = (4, 3)

# plt.rcParams['font.size'] = 15
# plt.rcParams['font.size'] = 20

# plt.rcParams['lines.linewidth'] = 5
# plt.rcParams['lines.linewidth'] = 50

# plt.rcParams['lines.linestyle'] = "-"
# plt.rcParams['lines.linestyle'] = "--"

# 위 눈금 설정
# plt.rcParams['xtick.top'] = True

# 오른 눈금 설정
# plt.rcParams['ytick.right'] = True

# 안쪽으로 눈금 설정
# plt.rcParams['xtick.direction'] = 'in'
# plt.rcParams['ytick.direction'] = 'in'

# 눈금 길이
# plt.rcParams['ytick.major.size'] = 12

# 세부 눈금
# plt.rcParams['xtick.minor.visible'] = True

plt.plot([2,3,6,7,10], [1,4,5,8,9])
plt.show() """

# 객체 활용
""" fig, ax = plt.subplots()
# [왼, 밑, 두께, 높이]
# ax = fig.add_axes([0, 0, 0, 0])
# ax = fig.add_axes([1, 1, 0, 0])
# ax = fig.add_axes([1, 1, 1, 1])

plt.show() """

# 다중 행열 구성
""" # fig, ax = plt.subplots(1, 1)
# fig, ax = plt.subplots(1, 2)
# fig, ax = plt.subplots(2, 1)
# fig, ax = plt.subplots(2, 2)
# fig, ax = plt.subplots(3, 2)
# fig, ax = plt.subplots(3, 3)

# plt.tight_layout()
plt.show() """

# 다중 객체 그래프 구성
""" x = [1,4,5,8,9]
y1 = [2,3,6,7,10]

# fig, ax = plt.subplots(2, 2)
# fig, ax = plt.subplots(2, 2, sharex=True)
# fig, ax = plt.subplots(2, 2, sharey=True)
# fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)

# ax[0][0].plot(x, y1)
# ax[0][1].plot(x, y1)
# ax[1][0].plot(x, y1)
# ax[1][1].plot(x, y1)

plt.show() """

# y축 동시 표시
""" x = [1,4,5,8,9]

y1 = [2,3,6,7,10]
# y2 = [10,8,6,4,2]
y2 = [100,80,60,40,20]

fig, ax1 = plt.subplots()
ax1.set_xlabel("X-Data")
ax1.set_ylabel("Y1")
ax1.plot(x, y1, color="C1", label="y1 Data")
ax1.legend(loc="upper right")

ax2 = ax1.twinx()
ax2.set_ylabel("Y2")
ax2.plot(x, y2, color="C3", label="y2 Data")
ax2.legend(loc="lower left")

plt.show() """

# 이종 그래프 출력
""" x = [1,4,5,8,9]
y1 = [2,3,6,7,10]
y2 = [2,3,6,7,10]

fig, ax1 = plt.subplots()

ax1.plot(x, y1, "-o", color="C1", label="XData")
ax1.set_xlabel("X")
ax1.set_ylabel("Ydata")
ax1.legend(loc="upper left")

ax2 = ax1.twinx()
ax2.bar(x, y2, color="C2", label="YData")
ax2.set_ylabel("Y2data")
ax2.legend(loc="lower left")

plt.show() """
# label을 쓰기 위해선 legend가 필요함

# 다중 그래프
""" x1 = [2,3,6,7,10]
x2 = [1,4,5,8,9]

y1 = [1,4,5,8,9]
y2 = [2,4,6,8,10]

# 전체 로우, 전체 컬럼, 인덱스
# plt.subplot(2, 1, 1)    # 1set
# plt.subplot(1, 2, 1)    # 2set
# plt.subplot(3, 1, 1)    # 3set
plt.subplot(2, 2, 1)    # 4set
plt.plot(x1, y1, "o-")

plt.title("X1 Graph")
plt.xlabel("x-data")
plt.ylabel("y-data")

# 스타일 지정
plt.style.use("bmh")

# plt.subplot(2, 1, 2)    # 1set
# plt.subplot(1, 2, 2)    # 2set
# plt.subplot(3, 1, 2)    # 3set
plt.subplot(2, 2, 2)    # 4set
plt.plot(x2, y2, ".-")

# 스타일 지정
plt.style.use("ggplot")
# plt.subplot(3, 1, 3)    # 3set
plt.subplot(2, 2, 3)    # 4set
plt.plot(x1, y1, ".-")
plt.plot(x2, y2, ".-")

plt.title("X3 Graph")
plt.xlabel("x3-data")
plt.ylabel("y3-data")

# 스타일 지정
plt.style.use("classic")

plt.subplot(2, 2, 4)    # 4set
plt.plot(x1, y2, ".-")
plt.plot(x2, y1, ".-")

plt.title("X4 Graph")
plt.xlabel("x4-data")
plt.ylabel("y4-data")

# 스타일 지정
plt.style.use("Solarize_Light2")
plt.tight_layout()

# 이미지 저장
# plt.savefig("data/imggg.jpg")
# plt.savefig("data/imgg.png")

plt.show() """

# 다중 막대그래프
""" x_years = ["2020", "2021", "2022"]
y_data = [100, 400, 900]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
# fig, ((ax1, ax3), (ax2, ax4)) = plt.subplots(2, 2)
ax1.bar(x_years, y_data)
ax2.bar(x_years, y_data)
ax3.bar(x_years, y_data)
ax4.bar(x_years, y_data)

ax1.bar(x_years, y_data, color="aquamarine", edgecolor="black", hatch="/")
ax2.bar(x_years, y_data, color="salmon", edgecolor="black", hatch="\\")
ax3.bar(x_years, y_data, color="navajowhite", edgecolor="black", hatch="+")
ax4.bar(x_years, y_data, color="lightskyblue", edgecolor="black", hatch="*")

plt.tight_layout()

plt.show() """

# seaborn 상관관계
""" # pip install plotly
tips = sns.load_dataset("tips")
print(tips)
# 산점도와 선형 희귀 선 표시
sns.regplot(x="total_bill", y="tip", data=tips)

plt.show() """

# 지표별 상관관계 출력
""" tips = sns.load_dataset("tips")
print(tips)

# plt.figure(figcize(10, 6))

sns.barplot(x="day", y="tip", data=tips)
# sns.barplot(x="day", y="total_bill", data=tips, palette="viridis")
# sns.barplot(x="tip", y="total_bill", data=tips)
# sns.barplot(x="sex", y="total_bill", data=tips)
# sns.barplot(x="sex", y="tip", data=tips)
# sns.barplot(x="smoker", y="total_bill", data=tips)
# sns.barplot(x="smoker", y="tip", data=tips)
# sns.barplot(x="time", y="total_bill", data=tips)

plt.title("Average Tips")
plt.xlabel("x")
plt.ylabel("Average")

plt.show() """

# 타이타닉 예제
""" titanic = sns.load_dataset("titanic")

sns.barplot(x="sex", y="survived", hue="pclass", data=titanic)
plt.show() """

""" titanic = sns.load_dataset("titanic")
print(titanic)

# 탑승클래스별 인원구성
# sns.countplot(x="class", hue="who", data=titanic)

# 클래스별 생존자
# sns.countplot(x="class", hue="alive", data=titanic)

# 성별별 생존자
# sns.countplot(x="sex", hue="alive", data=titanic)

# 싱글 여행자별 인원구성
# sns.countplot(x="alone", hue="who", data=titanic)

# 탑승지별 생존자의 클래스 구별
# sns.barplot(x="embark_town", y="survived", hue="pclass", data=titanic)
# sns.barplot(x="sex", y="survived", hue="pclass", data=titanic)

plt.show() """

# 주식
""" df = fdr.DataReader("KS11")
df0 = df.loc["2023"]

print(df0)

# df0["Open"].plot()
# df0["High"].plot()
# df0["Low"].plot()
# df0["Close"].plot()

plt.grid(True)
plt.show() """

# 코스피/다우 지수 비교
""" dow = fdr.DataReader("DJI", "2010-06-01")
kospi = fdr.DataReader("KS11", "2010-06-01")

# plt.figure(figsie=(7, 7))

# 각 지수별 종가 기준 그래프 출력
# plt.plot(dow.index, dow.Close, "r--", label="Dow")
# plt.plot(kospi.index, kospi.Close, "b", label="KOSPI")

# 최고가 기준
# plt.plot(dow.index, dow.High, "r--", label="Dow")
# plt.plot(kospi.index, kospi.High, "b", label="KOSPI")

# 해당 날짜 기준 증가 상승율, 상대 수익율 계산
d = (dow.Close / dow.Close.loc["2010-06-01"]) * 100
k = (kospi.Close / kospi.Close.loc["2010-06-01"]) * 100
plt.plot(d.index, d, "r--", label="Dow")
plt.plot(k.index, k, "b", label="KOSPI")

plt.grid(True)

plt.legend()
plt.show() """

# 국내 특정 주가
import requests
from datetime import datetime
from matplotlib import dates as mdates
from bs4 import BeautifulSoup as bs

""" headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

# url = "https://finance.naver.com/item/sise_day.nhn?code=005930" # 삼성전자
url = "https://finance.naver.com/item/sise_day.nhn?code=068270" # 셀트리온

res = rq.get(url, headers=headers)
html = bs(res.text, "html.parser")
html_table = html.select("table")
table = pd.read_html(str(html_table))
print(table)

df_list = []

# 페이지 수 동적으로 결정
page = 1
for page in range(1, 10):
    page_url = f"{url}&page={page}"
    print(page_url)

    response = requests.get(page_url, headers=headers)
    html = bs(response.text, "html.parser")
    html_table = html.select("table")
    table = pd.read_html(str(html_table))

    if not table[0].empty:
        df_list.append(table[0].dropna())
        page += 1
    else:
        break
    
# print(df_list)

# 리스트에 담긴 DataFrame을 한 번에 연결
df = pd.concat(df_list, ignore_index=True)

df = df.dropna()
df = df.iloc[0:30]
df = df.sort_values(by="날짜")

plt.figure(figsize=(15, 5))
plt.title("Target (close)")
plt.xticks(rotation=45)
plt.plot(df["날짜"], df["종가"], "co-")
plt.grid(color="gray", linestyle="--")
plt.show() """

# nasdaq
""" import yfinance as yf

# ticker = "AAPL" # 애플 주식 예시
ticker = "MSFT" # MS 주식 예시
start_date = "2022-01-01"
end_date = "2023-12-02"

data = yf.download(ticker, start=start_date, end=end_date)

# 시각화
plt.figure(figsize=(12, 6))
plt.plot(data["Close"], label="Close Price")

# 50일 평균
data["MA_50"] = data["Close"].rolling(window=50).mean()

# 200일 평균
data["MA_200"] = data["Close"].rolling(window=200).mean()

plt.plot(data["MA_50"], label="50-day Mean Average")
plt.plot(data["MA_200"], label="200-day Mean Average")

plt.title("Stock Price")
plt.xlabel("Data")
plt.ylabel("Price($)")
plt.legend()
plt.show """

""" url = "https://www.worldometers.info/world-population/population-by-country/"
response = requests.get(url)
soup = bs(response.text, "html.parser")

# 국가 및 인구 데이터 추출
countries = []
populations = []

rows = soup.select("#example2 tbody tr")
for row in rows:
    columns = row.select("td")
    country = columns[1].get_text(strip=True)
    population = int(columns[2].get_text(strip=True).replace(",", ""))
    
    countries.append(country)
    populations.append(population)
    
# 상위 10개 국가 시각화
top_countries = countries[:10]
top_populations = populations[:10]

plt.figure(figsize=(12, 6))
plt.barh(top_countries[::-1], top_populations[::-1], color="skyblue")
plt.xlabel("Population")
plt.title("Top 10")
plt.show() """