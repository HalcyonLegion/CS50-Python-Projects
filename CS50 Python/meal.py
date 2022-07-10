#Ask for Input - a Time, and then have the program tell you which meal you should eat. Needs to be 24h format, and include no meal time response too
#times are 7 to 8 breakfast time, 12 to 13 lunch time, and 18 to 19 dinner time
#times should be greater than/equal to >= the first one and less than/equal to the second one <=

def main():
    what_time = input("What time is it? ")
    time = convert(what_time)
    if time >= 7 and time <= 8:
        print("breakfast time")
    if time >= 12 and time <= 13:
        print("lunch time")
    if time >= 18 and time <= 19:
        print("dinner time")

#because the input is going to be 7:30 i.e. hours and minutes seperated by a : then we can split as hours, minutes
def convert(time):
    hours, minutes = time.split(":")
    in_min = float(minutes) / 60
    return float(hours) + in_min


if __name__ == "__main__":
    main()