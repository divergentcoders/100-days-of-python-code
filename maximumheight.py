sc=int(input("Enter how many students height u want to enter \n"))
height=[]
for i in  range(sc):
  ele=int(input("enter the height of students \n"))
  height.append(ele)
maxi=0
for h in height:
  if h>maxi:
    maxi=h
print("the greatest height is \n",maxi)
