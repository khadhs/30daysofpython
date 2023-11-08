#Write a Python program that converts a temperature in degrees Fahrenheit to degrees Celsius. The formula for conversion is: Celsius = (Fahrenheit - 32) * 5/9.
temp=int(input("Enter the temperature in Fahrenheit: "))
cel=(temp - 32) * 5/9
print(f"Temperature in Celsius {cel} degrees.")