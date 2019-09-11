#几何学:一个五边形的面积
#import math
#r = eval(input("Enter the length from the center to a vertex:"))
#s = 2 * r * math.sin(math.pi / 5)
#area = 5 *s ** 2 / (4 * math.tan(math.pi / 5))
#print("The area of the pentagon is %.2f" %area  )


#几何学：大圆距离
#import math
#x1,y1 = eval(input("Enter point 1 (latiude and longitude) in degress: "))
#x2,y2 = eval(input("Enter point 2 (latiude and longitude) in degress: "))
#radius = 6371.01
#x11 = math.radians(x1)
#y11 = math.radians(y1)
#x22 = math.radians(x2)
#y22 = math.radians(y2)
#d = radius * math.acos(math.sin(x11) * math.sin(x22) + math.cos(x11) * math.cos(x22) * math.cos(y11-y22))
#print("The distance between the two points is %.11f km" %d)


#几何学：五角形的面积
#import math
#s = eval(input("Enter the side:"))
#area = 5 * s ** 2 / (4 * math.tan(math.pi / 5 ))
#print ("The area of the pentagon is %.14f"%area)


#几何学：一个正多边形的面积
#import math
#n = eval(input("Enter the number of sides: ")) 
#s = eval(input("Enter the side: "))
#area = n * s ** 2 / (4 * math.tan(math.pi / n ))
#print ("The area of the polygon is %.14f"%area)


#找出ASCII字符
#a = eval(input("Enter an ASCII code："))
#b = chr(a)
#print("The character is",b )


#金融应用程序：工资表
#name = input("Enter employee’s name:")
#hours = eval(input("Enter number of hours worked in a week:"))
#PayRate = eval(input("Enter hourly pay rate:"))
#federalRate = eval(input("Enter federal tax withholding rate:"))
#stateRate = eval(input("Enter  input state tax withholding rate:"))
#Federal = hours * PayRate * federalRate
#State = hours * PayRate * stateRate
#Gross = hours * PayRate
#NetPay = hours * PayRate - Federal - State
#Total = Federal + State
#print("Employee Name:",name)
#print("Hours Worked:",hours)
#print("Pay Rate:$",PayRate)
#print("GrossPay:$",Gross)
#print("Deductions:")
#print("\t Federal withholding (20.0%):$",Federal) 
#print("̲\t State withholding(9.0%):$",State)
#print("\t Total Deduction:$" ,Total)
#print("NetPay:$" ,NetPay)


#反向数字
#num = int(input("Enter an integer:"))
#i = 0
#num1 = num
#while True:
#    if num1 // 10 == 0:
#        break
#        i += 1
#        num1 = num1 // 10
#        sum = 0
#while i >= 0:
#    sum = sum + (num % 10) * (10 ** i)
#    num = num // 10
#    i = i - 1
#    print("The reversed number is :",sum)