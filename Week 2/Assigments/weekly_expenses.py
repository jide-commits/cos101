# Calculates student weekly expenses

student_name = input("Enter student name: ")
daily_transport_cost = float(input(" Enter daily transport cost: "))
daily_feeding_cost = float(input(" Enter daily feeding cost: "))
number_of_days_on_campus = int(input(" Enter number of days on campus: "))
cost_of_other_expenses = float(input(" Enter cost of other expenses: "))

if daily_transport_cost < 0:
    print("Cannot Process, Input a positive value")

if daily_feeding_cost < 0:
    print("Cannot process. Input a positive value")

if number_of_days_on_campus < 0:
    print("Cannot Process, Input a positive value")

if cost_of_other_expenses < 0:
    print("Cannot Process, Input a positive value")



total_transport = daily_transport_cost * number_of_days_on_campus
total_feeding = daily_feeding_cost * number_of_days_on_campus
weekly_total = total_transport + total_feeding + cost_of_other_expenses

print("student name:", student_name)
print(f"daily transport cost: NGN { daily_transport_cost:.2f}")
print(f"daily feeding cost: NGN { daily_feeding_cost:.2f}")
print(f"cost of other expenses: NGN { cost_of_other_expenses:.2f}")
print(f"total transport: NGN { total_transport:.2f}")
print(f"total feeding: NGN { total_feeding:.2f}")
print(f"weekly total: NGN { weekly_total:.2f}")

    
                              
