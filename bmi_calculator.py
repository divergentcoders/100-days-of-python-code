height=float(input("enter your height \n"))
weight=float(input("enter your weight \n"))
bmi=round(weight/height**2)
if bmi<18:
  print("you are underweight \n")
elif bmi>=18 and bmi<25:
  print("you have a normal weight \n")
elif bmi>=25 and bmi<30:
  print("you are overweight \n")
elif bmi>=30 and bmi<35:
  print("you are obese \n")
else:
  print("you are clinically obese \n")

  
