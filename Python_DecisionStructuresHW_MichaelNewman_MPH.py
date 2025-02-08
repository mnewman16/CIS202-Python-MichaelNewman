distance = float(input("How many miles will you travel?"))
speed_limit = float(input("Enter the speed limit in MPH"))
speed = float(input("How fast will you drive in MPH"))

time = distance / speed_limit
speed_time = distance / speed

minutes_per_hour = 60

speed_time_min = speed_time*minutes_per_hour
time_min = time*minutes_per_hour

if speed > speed_limit:
    saved_time = time_min - speed_time_min
else:
    print("You didn't save any time, but you drove safe!")

print(f'Time taken at speed limit {time_min:.2f} minutes')
print(f'Time taken at at your speed {speed_time_min:.2f} minutes')
print(f'Time saved in minutes: {saved_time:.2f}')
