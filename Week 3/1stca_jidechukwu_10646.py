while True:
    entry = input("Enter a number greater than 1(or 'f' to quit): ").strip()

    if entry.lower() == "f":
        break

    try:
        number = int(entry)
    except ValueError:
        print("Please enter a whole number.\n")
        continue

    if number <= 1:
        print("The number must be greater than 1. Try again.\n")
        continue

    print(f"\nMultiplication table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")
    print()
