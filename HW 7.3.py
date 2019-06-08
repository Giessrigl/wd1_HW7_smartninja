first_num = int(input("enter a number: "))
second_num = int(input("enter another number: "))
operator = input("+, -, * or / : ")

if operator == "+":
    print(first_num + second_num)

elif operator == "-":
    print(first_num - second_num)

elif operator == "*":
    print(first_num * second_num)

elif operator == "/":
    print(first_num / second_num)

else:
    print("Wrong input!")