score=int(input("enter your score (0-100)"))
if score < 0 or score > 100:
    print("Score must be between 0 and 100:")

if(score>=90):
    print("Grade A")
elif(score>80):
    print("Grade B")
elif(score>=70):
    print("Grade C")
elif(score>=60):
    print("Grade D")
else:
    print("Grade E")

print("enter your score")
