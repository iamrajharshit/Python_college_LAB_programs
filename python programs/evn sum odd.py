n=int(input("Enter the n number"))
n_number=[]
evensum=0
oddsum=0
for i in range (0,n):
    
    numbers=int(input("Enter the numbers"))
    n_number.append(numbers)
    
    
for i in range (0,n):
    if n_number[i]/2:
        evensum=evensum+n_number[i]
    else:
        oddsum=oddsum+n_number[i]

print("even sum=",evensum)
print("odd sum=",oddsum)
