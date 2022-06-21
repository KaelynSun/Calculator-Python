Boolean_check = True

while Boolean_check:
  print ("Type the number for the chosen operation")
  print ("Numbers in decimal form (float) are possible")
  print ("1: Addition")
  print ("2: Subtraction")
  print ("3: Multiplication")
  print ("4: Division")
  print ("5: Exponentiation")
  print ("6: Modulo")
  print ("7: Integer Division")  
  Chosen_operation = input('Input Operation: ')

  while Chosen_operation not in ('1', '2', '3', '4','5','6','7'):
    Chosen_operation = input('Please input another operation number: ')
  
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
  elif Chosen_operation == '5':
    print(x**y)
  elif Chosen_operation == '6':
    print(x % y)
  elif Chosen_operation == '7':
    print(x//y)

  Another_operation = input("Do you want to calculate again? (yes/no): ")
  if Another_operation == 'yes':
    Boolean_check = True
  elif AnotherOperation == 'no':
   Boolean_check = False  

# Note to self:
# Make sure that the inputs for this kind of program are in float(Decimals) or 
# in interger(whole numbers) so that it doesn't end up like 2 + 3 = 23.0
# 
