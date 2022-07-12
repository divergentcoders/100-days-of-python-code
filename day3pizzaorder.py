print("Welcome to Python Pizza Delivery")
size=input("Enter the size of pizza u want S for small size, M for medium size,L for large size \n")
peperconi=input("Do u want peperconi Y for yes, N for no \n")
extracheese=input("Do u want extra cheese Y for yes, N for no \n")
bill=0;
if size=='S' and peperconi=='Y' and extracheese=='Y':
  bill=15+2+1
elif size=='S' and peperconi=='Y' and extracheese=='N':
  bill=15+2
elif size=='S' and peperconi=='N' and extracheese=='N':
  bill=15
elif size=='S' and peperconi=='N' and extracheese=='Y':
  bill=15+1
elif size=='M' and peperconi=='Y' and extracheese=='Y':
  bill=20+3+1
elif  size=='M' and peperconi=='Y' and extracheese=='N':
  bill=20+3
elif  size=='M' and peperconi=='N' and extracheese=='N':
  bill=20
elif  size=='M' and peperconi=='N' and extracheese=='Y':
  bill=20+1
elif size=='L' and peperconi=='Y' and extracheese=='Y':
  bill=25+3+1
elif  size=='L' and peperconi=='Y' and extracheese=='N':
  bill=25+3
elif  size=='L' and peperconi=='N' and extracheese=='N':
  bill=25
elif  size=='L' and peperconi=='N 'and extracheese=='Y':
  bill=25+1
print(bill)
  
