print("Welcome to Love Calculator")
name1=input("Enter your name \n")
name2=input("Enter their name \n")
combinedname=name1+name2
combinedname=combinedname.lower()
t=combinedname.count("t")
r=combinedname.count("r")
u=combinedname.count("u")
e=combinedname.count("e")
truevalue=t+r+u+e
l=combinedname.count("l")
o=combinedname.count("o")
v=combinedname.count("v")
e=combinedname.count("e")
lovevalue=l+o+v+e
score=truevalue+lovevalue
if score<10 and score>90:
  print("Your score is ",score," and you go together like coke and mentos \n")
elif score>40 and score<50:
   print("Your score is ",score," and you are alright together \n")
else:
   print("Your score is ",score,"\n")
  

