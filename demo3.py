# # # # # 1，获取本地计算机的IP地址
import socket
# 获取本计算机的名称
hostname = socket.gethostname()
# 获取本机IP
ip = "219.156.109.0"
print("{}".format(hostname))
print("{}".format(ip))
# # 2，根据IP地址查询地理位置
import geoip2.database
reader = geoip2.database.Reader('/Users/brycelee/Downloads/GeoLite2-City/GeoLite2-City.mmdb')
print("您的IP地理位置是：")
response = reader.city(ip)
print("地区：{}({})".format(response.continent.names["es"],response.continent.names["zh-CN"]))
print("经度：{},纬度：{}".format(response.location.longitude,response.location.latitude))
print("国家：{}({})".format(response.country.names["es"],response.country.names["zh-CN"]))
print("时区：{}".format(response.location.time_zone))
# # # 获取当前日期
# # import datetime
# # today = datetime.date.today()
# # print(today)
# # 设计计算器
# # 1，设计计算机界面
# print("\t+-*/+-*/+-*/+-*/+-*/\n\t欢迎使用Python365计算器\n\t+-*/+-*/+-*/+-*/+-*/")
# print("1、相加\t2、相减\t3、相乘\t4、相除")
# choice = input("输入你的选择(1/2/3/4):")
# # 使用多分支选择结构
# if(choice=='1'):
#     num1 = int(input("请输入第一个数字： "))
#     num2 = int(input("请输入第二个数字： "))
#     print(num1,'+',num2,'=',num1+num2 )
# elif(choice=='2'):
#     num1 = int(input("请输入第一个数字： "))
#     num2 = int(input("请输入第二个数字： "))
#     print(num1,'-',num2,'=',num1-num2 )
# elif(choice=='3'):
#     num1 = int(input("请输入第一个数字： "))
#     num2 = int(input("请输入第二个数字： "))
#     print(num1, '*', num2, '=', num1*num2)
# elif(choice=='4'):
#     num1 = int(input("请输入第一个数字： "))
#     num2 = int(input("请输入第二个数字： "))
#     print(num1, '/', num2, '=', num1 / num2)
# else:
#     print("非法输入")
#
d