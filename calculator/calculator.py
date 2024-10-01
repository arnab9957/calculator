def  addition(num1,num2) :
     result = num1+num2 
     print("{0}+{1}={2}" . format(num1,num2,result))
def  substraction(num1,num2) :
     result = num1-num2
     print("{0}-{1}={2}" . format(num1,num2,result))
def  multplication(num1,num2) :
     result = num1*num2
     print("{0}*{1}={2}" . format(num1,num2,result))
def   division(num1,num2) :
    if num2==0.0 :
      print ("Divisible by 0 is not possible..")
    else :
       result = num1/num2
       print("{0}/{1}={2}". format(num1,num2,result))
while True :
 print("Enter 1 for addition : ")
 print("Enter 2 for substraction : ")
 print("Enter 3 for multplication : ")
 print("Enter 4 for division : ")
 print("Enter q or Q for Exit : ")
 choise = input ("Enter your choice :")
 if choise == 'q' or choise =='Q' :
  break
 num1 = float(input("Enter first number : "))
 num2 = float(input("Enter second number : "))
 if choise =='1':
  addition(num1,num2)
 elif choise == '2' :
  substraction (num1,num2)
 elif choise == '3' :
  multplication (num1,num2)
 elif choise == '4':
  division (num1,num2) 
 else : 
  print("Invalid choise..")