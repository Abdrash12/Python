#Temprature Converter
celcius_temprature = []
fahrenheit_temprature = []
count = int(input("How many readings do you want to convert?"))
for i in range(count):
    temp = float(input("Enter the Tempratures: "))
    celcius_temprature.append(temp)
for celcius in celcius_temprature:
    fahrenheit_temprature.append((celcius * 9/5) + 32)
print("Temprature in Celcius: ", celcius_temprature)
print("Temprature in Farenheit: ", fahrenheit_temprature)
                                                                                                              