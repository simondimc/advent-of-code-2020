import math

def main():
    f = open("input/day_12.txt", "r")

    instructions = []
    for line in f:
        line = line.strip()
        command = line[0]
        argument = int(line[1:])

        instructions.append((command, argument))

    pos = move_ship(instructions)
    print("part 1:", abs(pos[0]) + abs(pos[1]))

    pos = move_by_waypoint(instructions)
    print("part 2:", abs(pos[0]) + abs(pos[1]))

def move_ship(instructions):
    pos = (0, 0)
    facing = 0

    for instruction in instructions:
        if instruction[0] == "N":
            pos = (pos[0], pos[1] + instruction[1])
        elif instruction[0] == "S":
            pos = (pos[0], pos[1] - instruction[1])
        elif instruction[0] == "E":
            pos = (pos[0] + instruction[1], pos[1])
        elif instruction[0] == "W":
            pos = (pos[0] - instruction[1], pos[1])
        elif instruction[0] == "L":
            facing = (facing + instruction[1]) % 360
        elif instruction[0] == "R":
            facing = (facing - instruction[1]) % 360
        elif instruction[0] == "F":
            if facing == 0:
                pos = (pos[0] + instruction[1], pos[1])
            elif facing == 90:
                pos = (pos[0], pos[1] + instruction[1])
            elif facing == 180:
                pos = (pos[0] - instruction[1], pos[1])
            elif facing == 270:
                pos = (pos[0], pos[1] - instruction[1])
    
    return pos

def move_by_waypoint(instructions):
    pos = (0, 0)
    waypoint = (10, 1)

    for instruction in instructions:
        if instruction[0] == "N":
            waypoint = (waypoint[0], waypoint[1] + instruction[1])
        elif instruction[0] == "S":
            waypoint = (waypoint[0], waypoint[1] - instruction[1])
        elif instruction[0] == "E":
            waypoint = (waypoint[0] + instruction[1], waypoint[1])
        elif instruction[0] == "W":
            waypoint = (waypoint[0] - instruction[1], waypoint[1])
        elif instruction[0] == "L":
            degree = instruction[1]
            radian = math.radians(degree)
            waypoint = (
                round(waypoint[0] * math.cos(radian) - waypoint[1] * math.sin(radian)),
                round(waypoint[0] * math.sin(radian) + waypoint[1] * math.cos(radian)),
            )
        elif instruction[0] == "R":
            degree = -instruction[1]
            radian = math.radians(degree)
            waypoint = (
                round(waypoint[0] * math.cos(radian) - waypoint[1] * math.sin(radian)),
                round(waypoint[0] * math.sin(radian) + waypoint[1] * math.cos(radian)),
            )
        elif instruction[0] == "F":
            pos = (pos[0] + (waypoint[0] * instruction[1]), pos[1] + (waypoint[1] * instruction[1]))
    
    return pos

if __name__ == "__main__":
    main()
