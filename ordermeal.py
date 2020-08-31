# 点菜小程序
menu_list = [ "糖醋排骨","水煮鱼","大盘鸡","拌黄瓜","萝卜炒肉","土豆丝"] # 菜品目录
price = [48, 58,38, 12 , 45 ,15 ] # 菜品价格
order_price = 0 # 菜品单价
order_list = [] # 已点菜品
count = 0 # 计算总价
k = 0 # 餐品数目
n = 0
seat_list = [2,2,2,4,4,4,6,6,6] # 每桌的座位数
sitdown_list = [] # 存放已经被坐了的座位号
guest_list =[] # 存放就餐人数量
print("**************欢迎光临大连工业大学小菜馆**************")
x = int(input("请问您几位: "))
guest_list.append(x)
for y in seat_list:
    n += 1
    if y >= x:
        sitdown_list.append(seat_list.index(y))
        seat_list.remove(y)
        print("您的座位是{}号桌".format(sitdown_list))
        break
if n != seat_list.index(y) + 1:
    print("对不起，本餐厅没有合适的座位。")
else:
    print("请您参考下列菜单菜品价格进行点菜")
    print("Python 365 菜品\n",menu_list)
    print("Python 365 菜单价格\n",price)
    print("***************如完成点菜请输入N,如需要取消已点菜品请输入C***************")
    server = input('请输入菜品进行点餐: ')
    def order_1(menu_list, order_list,server1):
        order_list.append(server1)
        print('已经点购菜名：{}'.format(order_list))
        a = menu_list.index(server1)
        return(a)
    while ( server != 'N'):
        if (server != 'C'):
            k+=1
            order_price = order_1(menu_list, order_list, server)
            print("***************如完成点菜请输入N,如需要取消已点菜品请输入C***************")
            server = input('请输入菜品进行点餐: ')
            count += price[order_price]
        else:
            if (k==0):
                print("!!!您还未点任何菜品!!!")
                server = input('请输入菜品进行点餐: ')
            else:
                cancle = input('请输入要取消的菜品: ')
                b = menu_list.index(cancle)
                order_list.remove(cancle)
                count -= price[b]
                k -=1
                print("***************如完成点菜请输入N,如需要取消已点菜品请输入C***************")
                server = input('请输入菜品进行点餐: ')
    print("一共点了{0}道菜品，共计{1}元".format(k,count))
    while True:
        fee = float(input("您支付的金额是："))
        if float(fee) < float(count):
            print("***************您支付的金额不足***************")
            continue
        else:
            print("您支付了{}元,找您{}元".format(count, fee - count))
            break