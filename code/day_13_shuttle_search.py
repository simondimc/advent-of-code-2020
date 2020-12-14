import sys
import math

# Part 1: What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus?
# Part 2: What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list?

def main():
    f = open("input/day_13.txt", "r")
    
    earliest_depart = int(f.readline().strip())
    bus_ids = []
    for i, bus_id in enumerate(f.readline().strip().split(",")):
        if bus_id != "x":
            bus_ids.append((i, int(bus_id)))

    print("part 1:", earliest_bus(earliest_depart, bus_ids))
    print("part 2:", earliest_offset(bus_ids))
    

def earliest_bus(earliest_depart, bus_ids):
    closest_bus_id = -1
    closest_time = float('inf')
    for bus_id in bus_ids:
        d = math.ceil(earliest_depart / bus_id[1])
        if bus_id[1] * d - earliest_depart < closest_time:
            closest_time = bus_id[1] * d - earliest_depart
            closest_bus_id = bus_id[1]
    
    return closest_bus_id * closest_time

def earliest_offset(bus_ids):
    t = 0

    i = 1
    lcm = 1
    while i < len(bus_ids):
        lcm *= bus_ids[i - 1][1]
        while (t + bus_ids[i][0]) % bus_ids[i][1] != 0:
            t += lcm
        i += 1

    return t

if __name__ == "__main__":
    main()
