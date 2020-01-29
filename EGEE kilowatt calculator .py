"""
EGEE Kilowatt-hour calculator 
"""
wattInput = float(input("What are the Watts? "))
hoursInput = float(input("How many hours do you use this machine a day? "))


#Find Kilowatts
kilowatts = wattInput / 1000

#Find Kilowatt-hours
kilowattHour = wattInput * hoursInput / 1000

#Print my solution 
print(f"This machine uses {kilowatts} per hour")
print(f"This machine uses {kilowattHour} a day")
