def analyze_student(name, marks, experience=0):
    average=sum(marks) /len(marks)
    if average>=60:
        status ='ready'
    else:
        status='need practice'

    return name, average, status, experience

name, average, status, experience=analyze_student("Asha", [70,80,90])
print("Name:", name)
print("Average", average)
print("Status:", status)
print("Experience:", experience)
