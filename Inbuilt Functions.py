antarctic_temperatures = [-25.5, -28.0, -26.3, -23.8, -27.1, -24.9, -29.2]

# Find the highest and lowest temperatures
highest_temp = max(antarctic_temperatures)
lowest_temp = min(antarctic_temperatures)

print("Highest temperature:", highest_temp, "°C")
print("Lowest temperature:", lowest_temp, "°C")

# Calculate the average temperature (rounded to 1 decimal place)
average_temp = round(sum(antarctic_temperatures) / len(antarctic_temperatures), 1)
print("Average temperature:", average_temp, "°C")
print("Type of average_temp before conversion:", type(average_temp))
average_temp = round(average_temp)
# Convert float to string
string_converted = str(average_temp)
print("Converted the float to string:", string_converted)
print("Type after conversion to string:", type(string_converted))

# Convert string to integer (drops decimal)
integer_converted = int(string_converted)
print("Converted the string to integer:", integer_converted)
print("Type after conversion to integer:", type(integer_converted))

# Find the absolute value of the coldest temperature
coldest_temp_abs = abs(lowest_temp)
print("The coldest temperature was", coldest_temp_abs, "°C below freezing.")
