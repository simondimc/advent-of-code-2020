import math

# Part 1: What is the highest seat ID on a boarding pass?
# Part 2: What is the ID of your seat?

def main():
    f = open("input/day_5.txt", "r")

    seats = [line.strip() for line in f]

    seats_ids = []
    for seat in seats:
        row_info = seat[:7]
        column_info = seat[7:]
        row = binary_space_partitioning(row_info, (0, 127), ("F", "B"))
        column = binary_space_partitioning(column_info, (0, 7), ("L", "R"))
        seat_id = row * 8 + column
        seats_ids.append(seat_id)
    
    print("part 1:", max(seats_ids))

    seats_ids.sort()
    
    my_seat_id = -1
    i = 0
    j = 1
    while j < len(seats_ids):
        if seats_ids[i] + 2 == seats_ids[j]:
            my_seat_id = seats_ids[i] + 1
            break
        i += 1
        j += 1

    print("part 2:", my_seat_id)

def binary_space_partitioning(sequence, rangee, alphabet):
    for char in sequence:
        half = math.floor((rangee[1] - rangee[0]) / 2)
        if char == alphabet[0]:
            rangee = (rangee[0], rangee[0] + half)
        elif char == alphabet[1]:
            rangee = (rangee[1] - half, rangee[1])
    
    return rangee[0]

if __name__ == "__main__":
    main()
