'''
* Prompt user to specify if the measurement will be in meters or feet
* Prompt user to enter length of room
* Prompt user to enter width of room
* Calculate the room area (length x width) in chosen measurement (meters or 
feet)
* If measurement was meters, convert the room area from square meters to square
feet (x 10.7639)
* If measurement was feet, convert the room area from square feet to square 
metres (/ 10.7639)
* Print the room area in their chosen measurement type, with the other 
measurement type in bracketssquare meters and square feet

### Test Cases ###
# Test Case 1
room_length_meters = 5
room_width_meters = 2
Expected output
The room's area is 10.00 square meters (107.64 square feet)

# Test Case 2
room_length_feet = 30.6
room_width_feet = 40.2
Expected output
The room's area is 1230.12 square feet (2250.73149 square meters)
'''

# Input
measurement_type = input("Please enter the measurement type as either meters"
                         " or feet, and press enter: ")
length = float(input("Please enter the room length and press "
                                 " enter: "))
width = float(input("Please enter the room width and press "
                                "enter: "))

### Algorithm ###
area = length * width

# Calculate area using other measurement type
if measurement_type == 'meters': 
    other_measurement_type = 'feet'
    converted_area = area * 10.7639
else:
    # measurement_type == 'feet':
    other_measurement_type = 'meters'
    converted_area = area / 10.7639

print(f"The room\'s area is {area:.2f} square {measurement_type} ("
      f"{converted_area:.2f} square {other_measurement_type}).")

# Tip: Can specify 2 decimal places for a float using {area_in_meters:.2f}