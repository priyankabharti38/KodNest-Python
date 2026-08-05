first_num=int(input("enter first no:"))
last_num=int(input("enter last no:"))
count=0

for i in range(first_num,last_num+1):
    if i%3==0:
        count += 1

print(f"No. divisible by 3: {count}")
        