 c=[["White","Black"],["Black", "White"]]  
input[0]

code="abcdefgh"
code.index(input[0])
row_pos=int(code.index(input[0]))+1
col_pos=int(input[-1])
(row_pos+col_pos)%2

cell=input("Enter a cell label:")
col_pos=int(code.index(input[0]))+1
row_pos=int(input[-1])
pos=row_pos+col_pos
if pos%2==1:
    print("The cell is white")
else:
    print("The cell is black")
