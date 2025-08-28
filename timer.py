countdown_initial = 10

print(countdown_initial)  # print initial 10 before loop starts
while countdown_initial != 0:
    countdown_initial -= 1
    print(countdown_initial)
    if countdown_initial == 5:
        print("You have reached the halfway point!")
