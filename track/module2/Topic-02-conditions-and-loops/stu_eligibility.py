# Read user input

marks=int(input())
attendance=int(input())
project_status=input()

# Check the placement eligibilty

if marks>=60 and attendance>=75:
    if project_status=="yes":
        print("Eligible")

    else:("Complete Project")

else:
    print("Not Eligible")

