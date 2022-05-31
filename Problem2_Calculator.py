print ("Type the number for the chosen operation")
print ("Numbers in decimal form (float) are possible")
print ("1, Addition")
print ("2, Subtraction")
print ("3, Multiplication")
print ("4, Division")

Chosen_operation = input('Input Operation: ')
x = float(input("Input the first number: "))
y = float(input("Input the second number: "))

if Chosen_operation == '1':
  #Function for Addition
  print(x + y)
elif Chosen_operation == '2':
  #Function for Subtraction
  print(x - y)
elif Chosen_operation == '3':
  #Function for Multiplication
  print (x * y)
elif Chosen_operation == '4':
  #Function for Division
  print (x / y)
else:
  print('Error, Try Again')



# Note to self:
# Make sure that the inputs for this kind of program are in float(Decimals) or 
# in interger(whole numbers) so that it doesn't end up like 2 + 3 = 23.0
# 
