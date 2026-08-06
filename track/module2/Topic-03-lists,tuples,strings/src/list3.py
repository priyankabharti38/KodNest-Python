# collect total count
score_count=int(input("enter count:"))
scores=[]

# read and store element in list
for i in range(score_count):
    score=int(input("enter score: "))
    scores.append(score)
    
search_score=int(input("enter target score: "))

# calculate total, highest, lowest manually
total=0
highest_mark=0
lowest_mark=0

for i in scores:
    total+=i
    if i>highest_mark:
        highest_mark=i
    elif i<lowest_mark:
        lowest_mark=i

# display result
print(f"Total:{total}")
print(f"Highest:{highest_mark}")
print(f"Lowest:{lowest_mark}")

# search for target score
if search_score in scores:
    print("Found")

else:
    print("Not Found")

