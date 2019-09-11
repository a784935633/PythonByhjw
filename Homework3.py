# 数学方面：五角数
# def getPentagonalNumber(n):
#     count=0
#     for i in range(1,n+1):
        
#         wjs=int(i*(3*i-1)/2)
#         print(wjs,end=" " )
#         count+=1
#         if count%10==0:
#             print()
# getPentagonalNumber(100)


# 求一个整数各个数字的和
# def sumDigits(n):
#     sum=0
#     ge=0
#     while n>=10:
#         ge=n%10
#         n=int(n/10)
#         sum+=ge
#     print(n+sum)
# sumDigits(3576)


# 对三个数排序
# def displaySortedNumbers(num1,num2,num3):
#     x = [num1,num2,num3]
#     for i in range(3):
#         for j in range(2):
#             if(x[j] > x[j+1]):
#                 t = x[j]
#                 x[j] = x[j+1]
#                 x[j+1] = t
#     return x
# num1,num2,num3 = eval(input("Enter three number: "))
# x = displaySortedNumbers(num1,num2,num3)
# print("The sorted numbers are",x[0],x[1],x[2])


# 财务应用程序：计算未来投资值
# sum=0
# def futureInvestmentValue(investmentAmount,monthlyInterestRate,years):
#     global sum
#     sum = investmentAmount * (1 + monthlyInterestRate * 0.01 / 12) ** years
#     return sum
# amount = int(input("The amount invested : "))
# rate = int(input("Annual interest rate : "))
# count = 0
# print("Years Future Value")
# for i in range(1,361):
#     count += 1
#     if(count == 12):
#         print(" %d %.2f"%(i/12,futureInvestmentValue(amount,rate,i)))
#         count =0


# 显示字符
# def printChars(ch1,ch2,numberPerLine):
    
#     count=0
#     while ch1!=chr(ord(ch2)+1):
#         print(ch1,end=" ")
#         i=ord(ch1)
#         i+=1
#         ch1=chr(i)
#         count+=1
#         if count%numberPerLine==0:
#             print()
# printChars('I','Z',10)


# 一年的天数
# def numberOfDayInYear(year):
#     if year%4==0 and year%100!=0 or year%400==0:
#         print('%d年有%d天'%(year,366))
#     else :
#         print('%d年有%d天'%(year,365))

# for year in range(2010,2021):
#     numberOfDayInYear(year)


# 梅森素数
# a=[]
# for j in range(2,100):
#     for i in range(2,j):
#         if (j % i) == 0:
#             break
#     else:
#         a.append(j)
# for z in a:
#     x=2**z-1
#     while x<=31:
#         print(z,x)
#         break


# 当前时间和日期
# import time

# localtime = time.asctime(time.localtime(time.time()))
# print("本地时间为 :", localtime)


# 游戏：掷骰子
# import random
# i=random.randrange(1,7)
# j=random.randrange(1,7)
# if i+j==2 or i+j==3 or i+j==12 :
#     print('you rolled %d+%d=%d'%(i,j,i+j))
#     print('you lose')
# elif i+j==7 or i+j==11:
#     print('you rolled %d+%d=%d'%(i,j,i+j))
#     print('you win')
# else: 
#     print('you rolled %d+%d=%d'%(i,j,i+j))
#     print('point is %d'%(i+j))
#     n=i+j
#     i=random.randrange(1,7)
#     j=random.randrange(1,7)
#     for z in range(1,100):
#         if i+j==7:
#             print('you rolled %d+%d=%d'%(i,j,i+j))
#             print('you lose')
#             break
#         elif i+j==n :
#             print('you rolled %d+%d=%d'%(i,j,i+j))
#             print('you win')
#             break
#         else:
#             i=random.randrange(1,7)
#             j=random.randrange(1,7)
