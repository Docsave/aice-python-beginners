employees_per_department = 30
safety_boat = 280

complete_shares = safety_boat//employees_per_department
leftover = safety_boat%employees_per_department

print(f"Complete Share: {complete_shares}")
print(f"Leftover: {leftover}")

#checking if number is even or odd
number = 289

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

