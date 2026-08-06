# total student count
student_count=int(input("Enter total count:"))

# creating list
marks= []

# read and store value in list
for i in range(student_count):
    mark= int(input("Enter mark:"))
    marks.append(mark)
   

# update the mark in list
position=int(input("Enter position:"))
updated_number=int(input("Enter new mark:"))
passing_mark=int(input("Enter passing mark:"))

marks[position-1]=updated_number

# calculate total, average, highest, lowest
total=0
average=0
highest_mark=0
lowest_mark=0
passed_count=0


total=sum(marks)
average=total/student_count
highest_mark=max(marks)
lowest_mark=min(marks)

# count passed student
for i in marks:
    if i>=passing_mark:
        passed_count+=1

# display all results
print(f"Total marks:{total}")
print(f"Average marks:{average}")
print(f"Highest Mark:{highest_mark}")
print(f"Lowest Mark:{lowest_mark}")
print(f"Passed Count:{passed_count}")