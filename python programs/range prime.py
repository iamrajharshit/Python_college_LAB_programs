upper=int(input("Enter the upper limit"))
lower=int(input("Enter the lower limit"))

for i in range(lower, upper + 1):
   
   if i > 1:
       for i in range(2, i):
           if (i % i) == 0:
               break
       else:
           print(i)
