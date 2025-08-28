age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age. Please enter a non-negative number.")
elif age < 12:
    print("Child ticket")
elif 12 <= age <= 64:
    print("Adult ticket")
else:
    print("Senior ticket")
