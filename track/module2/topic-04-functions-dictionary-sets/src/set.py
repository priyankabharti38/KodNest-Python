numbers={10,20,30,40,60,60}
number2={50,10,90,80}



numbers.add(20)
numbers.add(70)
numbers.remove(10)
numbers.discard(50)

unique_set=set(numbers)

union_set=numbers|number2
intersection_set=numbers & number2
difference_set=numbers-number2

print("length of numbers:", len(numbers))
print("Student set:", numbers)
print("Union:", union_set)
print("intersection:",intersection_set)
print("Difference:",difference_set)
