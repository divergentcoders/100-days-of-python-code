year=int(input("enter a year"))
if year%4==0:
  if year%100==0:
    if year%400==0:
      print("the entered year is a leap year \n")
    else:
      print("the entered year is not a leap year \n")
  else:
    print("the entered year is a leap year \n")
else:
  print("the entered year is not a leap year \n")
