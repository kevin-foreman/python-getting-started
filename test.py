# Converting miles to minutes and such
def mph_and_minutes_to_miles(mph, minutes):
    hours_traveled = minutes / 60.0
    miles_traveled = hours_traveled * mph
    return miles_traveled
    

miles_per_hour = float(input())
minutes_traveled = float(input())

print('Miles: {:f}'.format(mph_and_minutes_to_miles(miles_per_hour, minutes_traveled)))

# Convert C to K and back
def celsius_to_kelvin(value_celsius):
    value_kelvin = 0.0

    value_kelvin = value_celsius + 273.15
    return value_kelvin

def kelvin_to_celsius(value_kelvin):
    value_celsius = 0.0

    value_celsius = value_kelvin - 273.15
    return value_celsius

value_c = 10.0
print(value_c, 'C is', celsius_to_kelvin(value_c), 'K')

value_k = float(input())
print(value_k, 'K is', kelvin_to_celsius(value_k), 'C')

# Converting kilos to pounds
def kilo_to_pounds(kilos):
    # This statement intentionally has an error. 
    return (kilos * 2.204)
# Main part of the program starts here. Do not remove the line below.
if __name__ == '__main__':
    kilos = float(input())
    
    pounds = kilo_to_pounds(kilos)
    print(f'{pounds:.3f} lbs')
    
# Convert user input laps to miles on pre-defined course length
def laps_to_miles(user_laps):
    num_miles = user_laps * 0.25
    return num_miles

if __name__ == '__main__':
    user_laps = float(input());
    num_miles = laps_to_miles(user_laps)
    print(f'{num_miles:.2f}')