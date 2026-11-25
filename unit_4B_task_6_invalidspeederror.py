class InvalidSpeedError(Exception):
    pass

speed = float(input("Enter vehicle speed (km/h): "))

try:
    if speed < 0 or speed > 120:
        raise InvalidSpeedError("Speed must be between 0 and 120 km/h")
    else:
        print("Valid speed:", speed, "km/h")

except InvalidSpeedError as e:
    print("Error:", e)