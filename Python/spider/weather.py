import urllib.request
import csv
import re
# weather = {
#     "贵阳":"01010903",
#     "白云":"0101090301",
#     "开阳":"0101090303",
#     "青岛":"101120201"
# }
# city = input("请输入城市：").strip()
# cityid = weather[city]
# url = "http://www.weather.com.cn/data/cityinfo/"+str(cityid)+".html"
# data = urllib.request.urlopen(url).read().decode('utf-8')
# print(data)

# url = "http://wthrcdn.etouch.cn/weather_mini?citykey=101010100"
# data = urllib.request.urlretrieve(url=url,filename='weather',)
# with open('weather',encoding='gbk') as f:
#     datas = f.read()
#     print(datas)
#
# df = pd.read_excel('C:/Users/user/Downloads/china-city-list.xls')
# weather_city = []
# for i in df.index.values:
#     # row_data = df.ix[i['A','C']].to_dict()
#     row_data = df.loc[1]
#     weather_city.append(row_data)

weather_citys=[]
weather_city_do = {}
with open('C:/Users/user/Downloads/china-city-list.csv',encoding='utf-8') as weather:
    reader = csv.reader(weather)
    for data in reader:
        # print(data)
        weather_citys.append(data)
for weather_city in weather_citys[2:]:
    # weather_city_code = weather_city[0]
    # weather_city_name = weather_city[2]
    weather_city_do[weather_city[2]] = weather_city[0]
print("欢迎进入天气预报中心")
input_weather = input("请输入查询的天气:").strip()
while True:

    if input_weather != "quit":
        weather_code1 = weather_city_do.get(input_weather)
        weather_code2 = weather_code1[2:]
        # print(weather_code2)
        url = 'http://t.weather.sojson.com/api/weather/city/'+weather_code2
        datas = urllib.request.urlopen(url=url).read().decode('utf-8','ignore')
        # reg = '"forecast":\[\{(.*?)\]'
        data17 = ':"17",(.*?)\}'
        week1 = re.compile(data17,re.S).findall(datas)
        data18 = ':"18",(.*?)\}'
        week2 = re.compile(data18,re.S).findall(datas)
        data19 = ':"19",(.*?)\}'
        week3 = re.compile(data19,re.S).findall(datas)
        data20 = ':"20",(.*?)\}'
        week4 = re.compile(data20,re.S).findall(datas)
        data21 = ':"21",(.*?)\}'
        week5 = re.compile(data21,re.S).findall(datas)
        data22 = ':"22",(.*?)\}'
        week6 = re.compile(data22,re.S).findall(datas)
        data23 = ':"23",(.*?)\}'
        week7 = re.compile(data23,re.S).findall(datas)
        data24 = ':"24",(.*?)\}'
        week8 = re.compile(data24,re.S).findall(datas)

        print(week1)
        print(week2)
        print(week3)
        print(week4)
        print(week5)
        print(week6)
        print(week7)
        print(week8)
    else:
        break
    input_weather = input("请输入查询的天气:").strip()


















































