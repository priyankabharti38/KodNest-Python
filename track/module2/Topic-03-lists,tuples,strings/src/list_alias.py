value_count=int(input("Enter value count: "))
original_list=[]

#read and store value in list
for i in range(value_count):
    value=int(input("Enter value: "))
    original_list.append(value)

#alias and copy
alias_list=original_list
copy_list=original_list.copy()

#read position and value for alias and copy
alias_position=int(input("Enter aslias position: "))
alias_value=int(input("Enter alias value: "))
copy_position=int(input("Enter copy position: "))
copy_value=int(input("Enter copy value: "))

#update values
alias_list[alias_position-1]=alias_value
copy_list[copy_position-1]=copy_value

#check same memory location
if original_list is alias_list:
    print("yes")

#count different valuesin original and copy list
different_count=0
for i in range(len(original_list)):
    if original_list[i]!=copy_list[i]:
        different_count+=1