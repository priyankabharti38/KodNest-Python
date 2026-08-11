def display(name, hours, days):
    print(f"welcome: {name}!")
    total=hours*days
    print(f"Total study hours: {total}")



name=input()
hours=int(input())
days=int(input())
display(name,hours,days)
