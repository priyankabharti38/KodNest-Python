marks=int(input())

# calculate grade
if marks>100 or marks<0:
    print("Invalid Input")
if marks>=90:
    print("Grade: A")

if marks>=75:
    print("Grade: B")

if marks>=60:
    print("Grade: C")

if marks>=40:
    print("Grade: D")

else:
    print("Grade: F")
