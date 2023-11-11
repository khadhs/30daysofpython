
#Create a program that converts a temperature in Fahrenheit to Celsius or vice versa.
#( Hint : celsius = (temperature - 32) * 5/9 ; fahrenheit = (temperature * 9/5) + 32)
temperature=int(input("Enter the temperature: "))
conversion=input("Enter 'F' to convert from celsius to fahrenheit and 'C' to convert from fahrenheit tp celsius: ")
if conversion == 'F' or conversion == 'f':
   fahrenheit = (temperature * 9/5) + 32
   print(f"Temperature is {fahrenheit:0,.2f} degree Fahrenheit.")
elif conversion=='c' or conversion == 'C':
    celsius=(temperature - 32) * 5/9
    print(f"Temperature is {celsius:0,.2f} degree Celsius.")
else:
    print("Enter either 'F or 'C'.")