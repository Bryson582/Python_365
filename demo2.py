# 8月23日 Python实操
# str = 'Python 10 of 365'
# print(str[0:7])
# print(str[7:10])
# print(str[-6:-2])
# 总结一下，字符的序号有两种方向，正向递增是从0开始，
# 反向递减是从-1开始。Python常用[M:N]表示区间的选择，
# 其中不包括N的位置哦！M和N的序号有两种方向，正向递增和反向递减。
# str1 = 'PyhThon 10 Of 365'
# # 全部转换为大写
# print(str1.upper())
# # 全部转换为小写
# print(str1.lower())
# # 第一个字母转换为大写别的为小写
# print(str1.capitalize())
# # 第一个单词首字母大写
# print(str1.title())
# 好好学习，天天向上
# import math
# day_weight =0.01
# day_up = math.pow((1+day_weight),365)
# day_down = math.pow((1-day_weight),365)
# print("天天向上:{:0.2f}\n天天向下:{:0.2f}".format(day_up,day_down))
# import random # 随机数库
# str = input('请输入一个字符')
# n = random.randint(1,8)
# print(n)
# str = str.replace(str[n-1],"*")
# print("{}".format(str))
# print(random.random()) # 随机产生一个0-1的浮点数
# print(random.randint(1,100)) # 随机产生一个1-100的整数，包括1和100
# print(random.uniform(1,10)) # 随机产生一个1-10的浮点数
# x =int(input("请输入x"))
# # y =int(input("请输入y"))
# # print("交换前：x={},y={}".format(x,y))
# # x ,y=y,x
# # print("交换后：x={},y={}".format(x,y)) 此方法可以改变类型
# from wordcloud import WordCloud
# # txt = open('word.txt','r').read() #你的词库文件
# # wordcloud = WordCloud(background_color="white",width=1000, height=860, margin=2).generate(txt或者'自己喜欢的词')
# # import matplotlib.pyplot as plt
# # plt.imshow(wordcloud) #绘制词云
# # plt.axis("off") #去掉坐标轴
# # plt.show() #显示看看
# # wordcloud.to_file('word.png') #保存图片
# user_input = int(input("摄氏温度：请输入1\t\t华氏温度：请输入2"))
# if(user_input==1) :
#     c = float(input("请输入摄氏温度：\t"))
#     f = c*1.8 +32
#     print("摄氏温度:{:.0f}====>华氏温度：{:.0f}".format(c,f))
# else:
#     f= float(input("请输入华氏温度：\t"))
#     c= (f-32)/1.8
#     print("华氏温度：{:.0f}====>摄氏温度：{:.0f}".format(f,c))
# y = int(input("您14天内是否到过新冠疫区？（1代表是\t2代表否）\n"))
# if(y==1):
#     print("您的健康码"'\033[7;31m' "红色"+ '\033[0m'+ "！\n")
# if(y==2):
#     print("您的健康码"'\033[4;32m' "绿色"+ '\033[0m'+ "! \n")
import socket
# 获取计算机的名称
hostname = socket.gethostname()
# 获取本机的IP
ip = socket.gethostbyname(hostname)
import geoip2.database
reader = geoip2.database.Reader('/文件位置隐私考虑此处省略/GeoLite2-City.mmdb')
print("您的IP的地理位置是:")
# response = reader.city(ip)
# print("地区：{}({})".format(response.continent.names["es"],response.continent.names["zh-CN"]))
# print("经度：{}，纬度{}".format(response.location.longitude,response.location.latitude))
# print("国家：{}({}) ，简称:{}".format(response.country.name,response.country.names["zh-CN"], response.country.iso_code))
# print("时区：{}".format(response.location.time_zone))
# y = response.country.names["es"]
# if (y == 'China'):
#     print("您的健康码是"'\033[1;32m' "绿色"+ '\033[0m'+ "！\n")
# else:
#     print("您的健康码是"'\033[4;30;41m' "红色"+ '\033[0m'+ "！\n")