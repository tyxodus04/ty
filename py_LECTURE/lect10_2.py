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