number=int(input())
digit_sum=0
while number>0:
    digit=number%10
    digit_sum=digit_sum+digit
    number=number//10

print(f"sum of digit: {digit_sum}")

