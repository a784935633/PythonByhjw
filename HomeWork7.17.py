#1.将摄氏温度转化为华氏温度
#C = float(input('Enter a degree in Celsius：'))
#F = (C * 1.8) + 32
#print('%.f Celsius is %0.1f Fahrenheit' %(C,F))

#2.计算圆柱体的体积
#import math
#radius,length = eval(input("Enter the radius and length of a cylinder:"))
#area = math.pi*radius*radius
#volume = area*length
#print(' The area is %.4f'%area)
#print(' The volume is %.1f'%volume)

#3.将英尺数转换为米数
#feet = float(input('Enter a value for feet:'))
#meters = feet*0.305
#print('%.1f feet is %.4f meters'%(feet,meters))

#4.计算能量
#M = eval(input('Enter the amount of water in kilograms: '))
#initialTemperature = eval(input('Enter the initial temperature：'))
#finalTemperature = eval(input('Enter the final temperature：'))
#Q = M * (finalTemperature - initialTemperature) * 4184
#print('The energy needed is {} '.format(Q))

#5.计算利息
#c,l = eval(input('Enter balance and interest rate (e.g., 3 for 3%): '))
#interest = c * (l/1200)
#print(' The interest is %.5f'%interest)

#6.加速度
#v0,v1,t = eval(input('Enter v0, v1, and t:'))
#a = (v1-v0) / t
#print('The average acceleration is %.4f'%a)

#7.复利值
#yuan = eval(input('Enter the monthly saving amount:'))
#account = 0
#for i in range (6) :
#    account = (yuan + account) * (1 + 0.00417)
#print('After the sixth month,the account value is %.2f'%account)

#8.对一个整数中的各位数字求和
#number = int(input('Enter a number between 0 and 1000:'))
#a = number % 10
#b = number // 10 % 10
#c = number // 100
#sum = a + b + c
#print('The sum of the digits is %d'%sum)
