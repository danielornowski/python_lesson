unit = input("Is this temperature in Celsius or Fahrenheit (C/F)")
temp = float(input("Enter the tamperature: "))

if unit == "C":
    temp = round((temp * 9) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9)
    print(f"The temperature in Celsius is: {temp}°C")
else:
    print('Invalid unit')