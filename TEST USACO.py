cows_n = int(input("enter the N number of cows:"))
if cows_n > 10:
    print("too much cows")
elif cows_n < 1:
    print("too little")
else:
    cows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    cows_total = cows[:cows_n]
    d = int(input("state the distance to checkpoint:"))
    cow_speeds = {}
    speeds = []
    for cow in cows_total:
        speed = int(input("enter cow '" + cow + "' speed:"))
        cow_speeds[cow] = speed
        time = d / cow_speeds[cow]
        speeds.append(time)
        print("heres time to arrival for {cow}" + str(time))
    time_min = min(speeds)
    print("shortest time is:\n" + time_min)
