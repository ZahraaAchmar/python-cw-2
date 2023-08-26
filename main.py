my_name = input("enter your name:")
my_age =  input("enter your age:")
print (f"My name is {my_name} and I am {my_age} years old")
first_number =  int (input("enter the first number:"))
secound_number = int (input("enter the secound number:"))
operation = input ("enter the operation:")
if operation == "+":
    print (first_number + secound_number)
elif operation == "-":
    print (first_number - secound_number)
elif operation == "*":
    print (first_number * secound_number)
elif operation == "/":
    print (first_number / secound_number)
else:
    print("the operation is not valid")

bus_capacity = 69
people_inbus = int (input("how many ppl are there in the bus?:"))
ppl_whoare_waiting = int (input("how many ppl are waiting?:"))
empty_seats = bus_capacity - people_inbus
if empty_seats>ppl_whoare_waiting :
    print(f"join the bus there is {empty_seats} more")
elif empty_seats<=ppl_whoare_waiting :
    print("the bus is full")