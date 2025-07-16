"""
Tristan Pereira
Program summary: Calculates the volume of a prism

Note: With this program I decided to play around with the language a bit. There are a few approaches
to building this program. For example, I could have assigned each variable independently
using multiple input() functions. However this could be repetitive, I thought it would be cool to do it by
iterating through a list of parameters taken directly from a function signature. It's a little
messier, but very modular. I read about the inspect module directly from the python docs here:
 https://docs.python.org/3/library/inspect.html#inspect.signature
"""
#import necessary modules, inspect to get function sig
from inspect import signature
#region Implementation
def calculate_trapezoidal_prism_volume(length, height, base_width, top_width):
    return length * height * ((base_width + top_width) / 2 )

def reduce_measurement(percentage, measurements):
     #create and return a list with the modified values
     return [value * (1 - percentage/100) for value in measurements]

#return a string of params from a given function 
def signature_to_string(func):
    sig = signature(func)
    return [param for param in sig.parameters]

func = signature_to_string(calculate_trapezoidal_prism_volume)
#print results, reduces repitition
def print_(list_of_values):
    LENGTH = len(list_of_values)
    for i in range(LENGTH):
            print(f"{list_of_values[i]}", end='')
    print("\n")

#initialize list 
param_list =[]

#get measurements for a given function
def get_measurements(values, func):
    for i in range(len(func)):
        while True:
            user_input = input(f"{func[i]}: ")
            #catch invalid entries, step up from program_2 when I used isnumeric() 
            try:
                value = float(user_input)
                values.append(value)
                break
            except ValueError:
                print("Invalid value entered, try again.")
    return values
#endregion
#[ Main program logic ]
def main():
    print("To calculate trapezoid volume enter the following values\n")
    v = get_measurements(param_list, func)
    print(f"Volume: {calculate_trapezoidal_prism_volume(*v)}")
    print_(f"Measurements: {v}")
    v = reduce_measurement(25, v)
    print_(f"Reduced measurements: {v}")
    v = calculate_trapezoidal_prism_volume(*v)
    print_(f"Volume with reduced measurements: {v}")

main()

#region Prototype (what got me started)
# #initialize list
# print("To calculate trapezoid volume enter the following values\n")
# for i in range(len(func)):
#     #cast to int then attach value to list to be computed
#     param_list.append(int(input(f"{func[i]}: ")))
# print(f"Result: {calculate_trapezoidal_prism_volume(*param_list)}")

# #increment for each param
# # for i in range(PARAM_COUNT):
# #     #get user input for corresponding args
# #     v = input(f"{param_str_args[i]}:")
#endregion





