# Multiplication Table For a Number
multiplier = int(input("Enter a number: "))

print()
print(f" MULTIPLICATION TABLE FOR {multiplier}")
    
for number in range (1, 13):
    result = multiplier * number
    print(f"{multiplier} x {number} = {result}")
