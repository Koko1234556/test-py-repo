def celsius_to_fahrenheit(celsius):
   return (celsius * 9/5) + 32

celsius = float(input("Enter temperature in celsius: "))
print(f"Temperature in Fahrenheit is {celsius_to_fahrenheit(celsius)}")