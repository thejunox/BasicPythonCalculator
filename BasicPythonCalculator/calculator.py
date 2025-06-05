def sum_cal(num1,num2):
  return num1+num2
  
def substrac_cal(num1,num2):
  return num1-num2
  
def division_cal(num1,num2):
  return num1/num2
  
def floatdivision_cal(num1,num2):
  return num1//num2
  
def multiplication_cal(num1,num2):
  return num1*num2
  
def exponentiation_cal(num1,num2):
  return num1**num2
  
def mod_cal(num1,num2):
  return num1%num2
  
def square_root_cal(num1):
  sq = pow(num1, 0.5)
  return sq
  
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Floor Division")
print("5. Multiplication")
print("6. Exponentiation")
print("7. Modulo")
print("8. Square Root") 

choice = input("Enter your choice (1–8): ")

if choice == '8':
    num = float(input("Enter a number: "))
    print("Result:", square_root_cal(num))
else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
  

    if choice == '1':
        print("Result:", sum_cal(num1, num2))
    elif choice == '2':
        print("Result:", substrac_cal(num1, num2))
    elif choice == '3':
        print("Result:", division_cal(num1, num2))
    elif choice == '4':
        print("Result:", floatdivision_cal(num1, num2))
    elif choice == '5':
        print("Result:", multiplication_cal(num1, num2))
    elif choice == '6':
        print("Result:", exponentiation_cal(num1, num2))
    elif choice == '7':
        print("Result:", mod_cal(num1, num2))
    else:
        print("Invalid choice.")
print("Thank you for using me")

    