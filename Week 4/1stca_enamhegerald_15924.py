while True:
    num = input("Enter a number or e to exit:")

    if num == "e":
        print("Program ended!")
        break

    num = int(num)

    if num < 1:
        print("Number should not be less than 1")
        continue

    for i in range(1,13):
        print(num, "X", i, "=", num * i)
              
