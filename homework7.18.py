
#解一元二次方程
# import math
# a,b,c = map(float,input("Enter a, b, c：").split(","))
# jisuan = b*b-4*a*c
# if jisuan >0:
#   r1=(-b+math.sqrt(b*b-4*a*c))/ 2*a
#   r2=(-b-math.sqrt(b*b-4*a*c))/ 2*a
#   print("The roots are  {}  and {}  ".format(r1,r2))
# elif jisuan == 0:
#   r1=(-b+math.sqrt(b*b-4*a*c))/ 2*a
#   print("The roots is {} ".format(r1))
# else:
#   print("The equation has no real roots")


#学习加法
# import random
# res1=random.randrange(0,99)
# print('第一个随机数',res1)
# res2=random.randrange(0,99)
# print('第二个随机数',res2)
# he=int(input('请输入以上两个随机数之和:'))
# if he==(res1+res2):
#     print('程序报告结果为真')
# else:
#     print('程序报告结果为假')


#找未来数据
# today=int(input("Enter today's day:"))
# wl=int(input('Enter the number of days slapsed since today:'))
# s=(today+wl)%7
# if today==0 :
#     xq='Sunday'
# elif today==1 :
#     xq='Monday'
# elif today==2 :
#     xq='Tuesday'
# elif today==3 :
#     xq='Wednesday'
# elif today==4 :
#     xq='Thursday'
# elif today==5 :
#     xq='Friday'
# elif today==6 :
#     xq='Saturday'

# if  s==0:
#     xt='Sunday'
# elif  s==1:
#     xt='Monday'
# elif  s==2:
#     xt='Tuesday'
# elif  s==3:
#     xt='Wednesday'
# elif  s==4:
#     xt='Thursday'
# elif  s==5:
#     xt='Friday'
# elif  s==6:
#     xt='Saturday'
# print('Today is %s and the fulture day day is %s'%(xq,xt))


#对三个整数排序
# num1,num2,num3=map(int,input('请输入三个数字：').split(' '))
# if num1>num2 and num2>num3 :
#     print(num3,num2,num1)
# elif num1>num2 and num2<num3 and num3<num1:
#     print(num2,num3,num1)
# elif num1<num2 and num2>num3 and num3<num1:
#     print(num3,num1,num2)
# elif num1<num2 and num2>num3 and num3>num1:
#     print(num1,num3,num2)
# elif num1<num2 and num2<num3 and num3>num1:
#     print(num1,num2,num3)
# else :
#     print(num2,num1,num3)


#金融方面：比较价钱
# m1,p1=map(float,input('Enter weigth and price for packet 1:').split(' '))
# m2,p2=map(float,input('Enter weigth and price for packet 2:').split(' '))
# s1=p1/m1
# s2=p2/m2

# if s1<s2:
#     print('Packet 1 has the better price.')
# else:
#     print('Packet 2 has the better price.')


#找出一个月中的天数
# y,n=map(int,input('请输入月份和年：').split(' '))
# if n%4==0 and n%100!=0 or n%400==0 :
#     print('%d 年一月份有29天'%n)
# else :
#     if y==1:
#         print('%d 年一月份有31天'%n)
#     elif y==2:
#         print('%d 年二月份有28天'%n)
#     elif y==3:
#         print('%d 年三月份有31天'%n)
#     elif y==4:
#         print('%d 年四月份有30天'%n)
#     elif y==5:
#         print('%d 年五月份有31天'%n)
#     elif y==6:
#         print('%d 年六月份有30天'%n)
#     elif y==7:
#         print('%d 年七月份有31天'%n)
#     elif y==8:
#         print('%d 年八月份有31天'%n)
#     elif y==9:
#         print('%d 年九月份有30天'%n)
#     elif y==10:
#         print('%d 年十月份有31天'%n)
#     elif y==11:
#         print('%d 年十一月份有30天'%n)
#     elif y==12:
#         print('%d 年十二月份有31天'%n)


# 游戏：头或尾
# import numpy as np
# cc=str(input('猜测：'))
# res=np.random.choice(['正面','反面'])
# if cc=='正面':
#     print('实际是：',res)
#     if res=='正面':
#         print('猜对了')
#     else :
#         print('猜错了')
# else:
#     print('实际是：',res)
#     if res=='正面':
#         print('猜错了')
#     else :
#         print('猜对了')


# 游戏：剪刀石头布
# import random
# computer = random.randint(0,2)
# user = int(input("scissor(0),rock(1),paper(2):"))
# if computer == 0:
#     com_gesture = "scissors"
# elif computer == 1:
#     com_gesture = "rock"
# else:
#     com_gesture = "paper"
# print(com_gesture)
# if user == 0:
#     user_gesture = "scissors"
# elif user == 1:
#     user_gesture = "rock"
# else:
#     user_gesture = "paper"

# if computer == user:
#     print("The computer is %s. You are %s too.It is a draw"%(com_gesture,user_gesture))
# elif user == 0 and computer == 2:
#     print("The computer is %s. You are %s.You won"%(com_gesture,user_gesture))
# elif user == 1 and computer == 0:
#     print("The computer is %s. You are %s.You won"%(com_gesture,user_gesture))
# elif user == 2 and computer == 1:
#     print("The computer is %s. You are %s.You won"%(com_gesture,user_gesture))
# else:
#     print("The computer is %s. You are %s.You lose"%(com_gesture,user_gesture))


# 科学问题：一周的星期几
# year=int(input('Enter year:(e.g..2008):'))
# mouth=int(input('Enter month:1-12:'))
# day=int(input('Ener the day of the month:1-31 :'))
# j=int(year/100)
# k=year%100
# if mouth==1 or mouth==2:
#     year-=1
#     mouth+=12
#     j=int(year/100)
#     k=year%100
#     h=(day+(26*(mouth+1)/10)+k+(k/4)+(j/4)+5*j)%7
    
# else:
#     j=int(year/100)
#     k=year%100
#     h=(day+(26*(mouth+1)/10)+k+(k/4)+(j/4)+5*j)%7

# if h==0 :
#         print('Day of the week is Saturday')
# elif h==1 :
#         print('Day of the week is Sunday')
# elif h==2 :
#         print('Day of the week is Monday')
# elif h==3 :
#         print('Day of the week is Tuesday')
# elif h==4 :
#         print('Day of the week is Wednesday')
# elif h==5 :
#         print('Day of the week is Thursday')
# else :
#         print('Day of the week is Friday')


# 游戏：选出一张牌
# import numpy as np
# res1 = np.random.choice(['Ace','2','3','4','5','6','7','8','9','10','jack','Queen','King'])
# res2 = np.random.choice(['梅花','红桃','方块','黑桃'])
# print('the card you picked is the {} of {}'.format(res1,res2))


# 回文数
# num=int(input('Enter a three digit integer:'))
# bai=int(num/100)
# shi=int((num/10)%10)
# ge=num%10
# if bai==ge :
#     print('%d is a palindrome'%num)
# else :
#     print('%d is not a palindrome'%num)


# 计算三角形的周长
# b1,b2,b3=map(float,input('Enter three edges:').split(' '))
# count1,count2,count3=False,False,False
# if b1+b2>b3:
#     count1=True
#     if b1+b3>b2:
#         count2=True
#         if b2+b3>b1 :
#             count3=True
# if count1 and count2 and count3 :
#     print('The perineter is ',b1+b2+b3)
# else :
#     print('非法输入！')