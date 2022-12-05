n=int(input("Enter the no. of students in class"))
l_names=[]
l_rolls=[]
l_math=[]
l_ml=[]
l_ai=[]
for i in range (0,n):
    name=input("Enter the name")
    l_names.append(name)
    roll=input("Enter the roll")
    l_rolls.append(roll)
    maths_marks=int(input("Enter the maths marks"))
    l_math.append(maths_marks)
    ml_marks=int(input("Enter the ML marks"))
    l_ml.append(ml_marks)
    ai_marks=int(input("Enter the ai marks"))
    l_ai.append(ai_marks)





for j in range(0,n):
    print(l_names[j])
    print("roll no",l_rolls[j])
    print("maths marks",l_math[j])
    print("ml marks",l_ml[j])
    print("ai_marks",l_ai[j])
    total_marks=((l_math[j]+l_ml[j]+l_ai[j])/3)

    print("percentage",total_marks)
    
    if total_marks > 85:
        print("grade S")
    elif 85> total_marks >70:
        print("grade A")
    elif 70> total_marks>60:
        print("Grade B")
    elif 60>total_marks>50:
        print("Grade C")
    elif 50>total_marks>45:
        print("Grade D")
    else:
        print("Grade F Fail")
        



    
