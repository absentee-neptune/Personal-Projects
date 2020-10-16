speed = int(input("Your speed in mph: "))
distance = float(input("Enter your distance in miles: "))
print("Enter your choice of format for time")
choice = input("decimal hours (D) or hours and minutes (M): ")
print()
if choice == "D" or choice == "d":
    time = distance/speed
    print("At", speed, "mph, it will take")
    print(time, "hours to travel", distance, "miles.")
else:
    time = distance/speed
    hours = int(time)
    minutes = int((time - hours)*60)
    print("At", speed, "mph, it will take")
    print(hours, "hours and", minutes, "minutes to travel",\
    distance, "miles.")
input("\n\nPress the Enter key to exit")

