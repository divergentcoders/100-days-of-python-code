row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? \n")
column=int(position[0])
row=int(position[1])
selectedrow=map[row-1]
selectedrow[column-1]="X"
print(f"{row1}\n{row2}\n{row3}")
