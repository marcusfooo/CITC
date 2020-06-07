while True:
  operation = int(input("Enter your operation\n1)+\n2)-\n3)*\n4)/\n"))

  no1 = int(input("Enter the first number: "))
  no2 = int(input("Enter the second number: "))


  if operation == 1:
    answer = no1 + no2
    print("The equation is %s + %s = %s" %(no1, no2, answer))

  elif operation == 2:
    answer = no1 - no2
    print("The equation is %s - %s = %s" %(no1, no2, answer))

  elif operation == 3:
    answer = no1 * no2
    print("The equation is %s * %s = %s" %(no1, no2, answer))

  elif operation == 4:
    answer = no1 / no2
    print("The equation is %s / %s = %s" %(no1, no2, answer))