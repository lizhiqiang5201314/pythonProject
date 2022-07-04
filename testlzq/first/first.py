# print("hello Python!")
# print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
# bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
# a,b,c=1,2,3
# print(a,b,c)
# a=b=c=1
# print(a,b,c)
# a=12
# print(id(a))
# a=a+1
# print(id(a))
# a=[1,2,3]
# print(id(a))
# a="1"
# b=[1,2,3]
# print(type(a),type(b))
# s="pythonabcdes"
# print(s[0:8:2])
# print(s[-1])
# a="pythonpostman"
# a=a.replace("好","坏")  #变量的替换函数
# print(a)
# a=a.count("n") #统计字符数量
# print(a)
# print(a)
# name="李武"
# age=25
# sex="女"
# print("李总是谁:%s" %name,"他多大:%d" %age,"你性别:%s" %sex)
# print("你是谁",name,age,sex)
# print("我叫{a},我今年{b},我是一个{c}生".format(a=name,b= age,c=sex))
# print("你叫什么: %s %d %s" %(name,age,sex))
#
# a=input()
# print(a)
# a=[111,222,[333,444,[555,666,[777,888,[999]]]]]
# print(a[2][2][2][2][0])
# a=[1,2,3,4,5]
# a[1]=1
# print(a)
# a.insert(-1,5)
# a.append("mysql")
# print(a)
# for i in a :
#     print(i,end="个")
#     print(i)
# a=["1","2","nm"]
# print(max(a))
# a=(1,2,3)
# # a[1]=0
# print(a)
# a={"name":"李武","age":"25"}
# a["name"]="ll"
# print(a["name"])


# for i in range(5): #循环输入输出语句
#   a=input("请输入") #循环输入输出语句
#   print(a)         #循环输入输出语句

# n = 5
# while n > 0:
#     n = n-1
#     if n == 2:
#         break
#     print(n)
# print('循环结束。')
# print(n)

# n = 7
# while n>0 :
#     n=n-1
#     if n==2 :
#         break
#     print(n)
# print('循环结束。')
#
# for letter in 'Runoob':  # 第一个实例
#     if letter == 'b':
#         break
#     print('当前字母为 :', letter)
#
# var = 10  # 第二个实例
# while var > 0:
#     print('当期变量值为 :', var)
#     var = var - 1
#     if var == 5:
#         break
#
# print("Good bye!")

# a={1,2,3,3,3}
# print(a)

# age=int(input("请输入你的年龄:"))
# while age<18 :
#     print("小心凣凣找你！")
#     age=int(input("请再次输入你的年龄:"))
#     if age>=18 :
#         break
# print(age,"岁,你很安全！")

# for i in range(10) :
#     print(i+1,end=" ")
#
# a=1;b=0
# while a<=100 :
#     if a%2==0 :
#         b+=a
#     a+=1
# print(b)

# a=250
# while 1 :
#     try :
#         b=int(input("请猜数:"))
#         if b>a :
#             print("很遗憾，猜大了!")
#         elif b<a :
#             print("很遗憾，猜小了！")
#         else :
#             print("猜对了！")
#             break
#     except :
#         print("输入错误，请重新输入！")



# a=[1,2,3,4,5,6,7,8,9,10]
# for i in a :
#     if i==4 :
#         continue
#     print(i)

for i in range(1,10) :
    for j in range(1,10) :
        if  j<= i:
            print("%d*%d=%d" %(i,j,i*j),end=" ")
    print()

# a={"特朗普":"2b","普京":"nb","安倍":"sb"}
# b=[]
# for i,j in a.items():
#     b.append(i)
#     b.append(j)
#     print(i,j)
# print(b)

# 输出商品列表，用户输入序号，显示用户选中的商品
#     商品 li = ["手机", "电脑", '鼠标垫', '游艇']
# 要求：1：页面显示 序号 + 商品名称，如：
#       	1 手机
# 	   	2 电脑
#      		 …
#      2： 用户输入选择的商品序号，然后打印商品名称
#      3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
#      4：用户输入Q或者q，退出程序。

# li = ["1.手机", "2.电脑", '3.鼠标垫', '4.游艇','q.退出']
# a=0
# for x in li:
#     print(x)
# while 1 :
#     a.int(input("请输入指令:"))
# if a = 2 :
#     print("")
#
#
#
#     print("输入有误，请重新输入")

# li = ["1.手机", "2.电脑", '3.鼠标垫', '4.游艇','q.退出']
# for i in li :
#     print(i)
# while 1 :
#         b=input("请输入购买指令:")
#         if b=='1' :
#             print("手机")
#         elif b=='2' :
#             print("电脑！")
#         elif b=='3' :
#             print("鼠标垫")
#         elif b=='4' :
#             print("游艇")
#         elif b=='q':
#             print("退出成功！")
#             break
#         else :
#             print("输入错误，请重新输入！")


# ps=123456
# while 1 :
#     password=int(input("请输入密码:"))
#     if password!=ps :
#         password=int(input("密码错误，您还有两次机会！\n请输入密码:"))
#         if password != ps:
#             password = int(input("密码错误，您还有一次机会！\n请输入密码:"))
#             if password !=ps:
#                 print("三次密码都输入错误，强制退出系统!")
#                 break
#             elif password==ps :
#                 print("输入正确进入柜台系统!")
#                 break
#         elif password==ps :
#             print("输入正确进入柜台系统!")
#             break
#     elif password==ps :
#         print("输入正确进入柜台系统!")
#         break
#
# yue=20000
# li = ["1.存款", "2.取款", '3.退卡', ]
# for i in li :
#         print(i)
# while 1 :
#         b=input("请输入指令:")
#         if b=='1' :
#             c = int(input("请输入存款金额:"))
#             yue+=c
#             print("存款成功！您当前余额为：",yue)
#         elif b=='2' :
#             c = int(input("请输入取款金额:"))
#             yue-=c
#             print("取款成功！您当前余额为：", yue)
#         elif b=='3':
#             print("退出成功！")
#             break
#         else :
#             print("输入错误，请重新输入！")
#
# class Student():
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score
#     def showstudentinfo(self):
#         print("姓名:%s,成绩:%d"%(self.name,self.score))
# aa=Student("小明",90)
# aa.showstudentinfo()
#
# class Str(Student):
#     def __init__(self,name,score):
#         super(Str,self).__init__(name,score)
#     def sleep(self):
#             super(Str,self).showstudentinfo()
#             print("成功调用父类方法")
# tt=Str("李四",98)
# tt.sleep()


# class Dog():
#     def __init__(self,name,age,sex):
#         self.age=age
#         self.sex=sex
#         self.name=name
#     def shuijiao(self):
#         print("姓名:%s,年龄:%d,性别:%s" % (self.name, self.age,self.sex))
#         print("会睡觉")
#     def huipao(self):
#         print("姓名:%s,年龄:%d,性别:%s" % (self.name, self.age,self.sex))
#         print("会跑")
#     def eat(self):
#         print("姓名:%s,年龄:%d,性别:%s" % (self.name, self.age,self.sex))
#         print("会吃饭")
# aa=Dog("李武",2,"母")
# bb=Dog("武哥",20,"雌伏")
# aa.shuijiao()
# bb.huipao()
# bb.eat()
#
# class dog(Dog):
#     def huipao(self):
#         print("会撒尿")
# cc=dog("李武",2,"母")
# cc.huipao()
# cc.eat()
# with open(r"D:niubi.txt","r",encoding="utf-8") as f:
#     a=f.read()
    # b=f.readline()
    # c=f.readlines()
    # print(a)v222
# with open(r"D:niubi.txt","a",encoding="utf-8") as f:
#     f.write("傻不拉几\n深刻的回家看了")

# import json #导入json模块
# data={"name":"李武","age":18,"sex":"男"} #定义字典数据
# print(data)
# print(type(data)) #输出字典里面的元素
# a=json.dumps(data,ensure_ascii=False) #将字典python数据转换为json数据
# print(a)
# print(type(a)) #输出转换后的数据类型
#
# workbook =xed open workbookirun:mou.xlsxn
# sheet2= workbook.sheet_by_name("登录数据")
#






























