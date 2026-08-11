skills=[]
for i in range(5):
    skill=input("enter skills:")
    skills.append(skill)

skill_record=tuple(skills)
print("Tuple:",skill_record)
print("First three skills:",skill_record[:3])
print("Last two skills:",skill_record[-2:])
print("Alternate:",skill_record[::2])
print("Reverse:",skill_record[::-1])
