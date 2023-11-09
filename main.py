# Initialize variables for highest, lowest, and sum of temperatures
highest_temp = float('-inf')
lowest_temp = float('inf')
total_temp = 0

# Loop through the specified time range (8am to 6pm)
for hour in range(8, 7 + 12, 2):
    # Prompt the user to enter the temperature for the current hour
    temperature_str = input(f"Enter {hour}am temp: ")

    # Extract the numerical temperature value and convert it to an integer
    temperature = int(temperature_str[:-1])

    # Update highest and lowest temperatures
    if temperature > highest_temp:
        highest_temp = temperature
    if temperature < lowest_temp:
        lowest_temp = temperature

    # Add the temperature to the total
    total_temp += temperature

# Calculate the average temperature
average_temp = total_temp / 7

# Print the results
print(f"Highest Temp: {highest_temp}C")
print(f"Lowest Temp:   {lowest_temp}C")
print(f"Average Temp: {average_temp:.1f}C")
