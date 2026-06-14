# We are trying ValueError in here in th try & except blocks.

try:
    num=int(input("enter any number: "))
except ValueError:
    print("Invalid input")
else:
    print(f"You entered : {num}")
    print("---Input attempt complete---")