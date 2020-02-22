print("Hello, This program will calculate you speed distance or time as long as at least two of these values are known.")
print("Please enter your first variable choice, speed, distance or time.")
choice=input()
if choice == "speed":
    print("What is the speed in mph?")
    speed=int(input())
elif choice == "distance":
    print("What is the distance in miles?")
    dist=int(input())
elif choice == "time":
    print("What is the time in hours?")
    time=int(input())
else:
    print("Incorrect entry, exiting.")
    exit()
print("Please select a second variable, speed, distance or time.")
choice2=input()
if choice2 == choice:
    print("You have already selected that variable, exiting")
    exit()
elif choice2 == "speed":
    print("What is the speed in mph?")
    speed=int(input())
elif choice2 == "distance":
    print("What is the distance in miles?")
    dist=int(input())
elif choice2 == "time":
    print("What is the time in hours?")
    time=int(input())
else:
    print("That was not a valid selection")
    exit()
if (choice == "speed" and choice2 == "distance") or (choice == "distance" and choice2 == "speed"):
    print("The time taken is "+str(dist/speed)+" hours")
if (choice == "distance" and choice2 == "time") or (choice == "time" and choice2 == "distance"):
    print("The speed is "+str(dist/time)+" mph")
if (choice == "speed" and choice2 == "time") or (choice == "time" and choice2 == "speed"):
    print("The distance is "+str(speed*time)+" miles")
 