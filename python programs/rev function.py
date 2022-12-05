n=int(input("Enter a number"))

def rev(n):
    revs=0
    rem=0
    while(n!=0):
        rem=n%10         #storing the last digit in variable rem 
        revs=revs*10+rem #adding the last digit in revs variable
        n//=10           #now we remove the last digit 
    return revs
print("Rev number is=",rev(n))    
