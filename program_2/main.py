"""
Tristan Pereira
Program summary: Calculates the temperature in Fahrenheit to Kelvin.

"""
#formula to convert
def fahrenheit_to_kelvin(temp):
    return (temp + 459.67) * 5/9

#retrieve temperature from user
temp = input("Enter a temperature in fahrenheit to convert into Kelvin: ")

#check for valid type
if(temp.isnumeric()):

    #convert string to float, call our formula function and assign result
    result = fahrenheit_to_kelvin(float(temp))

    #display result
    print(f"\nresult: {result}k")
else:
    #handle error here... 
    print(f"Error, '{temp}' is not a valid temperature to convert")


