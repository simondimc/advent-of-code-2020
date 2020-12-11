
# Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?

def main():
    f = open("input/day_11.txt", "r")

    seats = []
    for line in f:
        line = line.strip()
        seats_row = []
        for c in line:
            seats_row.append(c)
        seats.append(seats_row)

    print("part 1:", simulate_until_no_change(seats, adjacent_occupied_seats, 4))
    print("part 2:", simulate_until_no_change(seats, see_line_occupied_seats, 5))

def simulate_until_no_change(seats, occupied_seats_function, visible_occupied_threshold):
    updated_seats = update_seats(seats, 1, occupied_seats_function, visible_occupied_threshold)
    while updated_seats != seats:
        seats = updated_seats
        updated_seats = update_seats(seats, 1, occupied_seats_function, visible_occupied_threshold)
    
    count_occupied = 0
    for r in seats:
        for seat in r:
            if seat == "#":
                count_occupied += 1
    
    return count_occupied

def update_seats(seats, n, occupied_seats_function, visible_occupied_threshold):
    for _ in range(n):
        i = 0
        updated_seats = [[0 for c in range(len(seats[r]))] for r in range(len(seats))]
        while i < len(seats):
            j = 0
            while j < len(seats[i]):
                if seats[i][j] == "L" and occupied_seats_function(seats, i, j) == 0:
                    updated_seats[i][j] = "#"
                elif seats[i][j] == "#" and occupied_seats_function(seats, i, j) >= visible_occupied_threshold:
                    updated_seats[i][j] = "L"
                else:
                    updated_seats[i][j] = seats[i][j]
                j += 1
            i += 1
        seats = updated_seats
    
    return seats

def adjacent_occupied_seats(seats, i, j):
    count = 0

    if j-1 >= 0 and seats[i][j-1] == "#":
        count += 1
    if j+1 < len(seats[i]) and seats[i][j+1] == "#":
        count += 1

    if i-1 >= 0 and j-1 >= 0 and seats[i-1][j-1] == "#":
        count += 1
    if i-1 >= 0 and seats[i-1][j] == "#":
        count += 1
    if i-1 >= 0 and j+1 < len(seats[i-1]) and seats[i-1][j+1] == "#":
        count += 1

    if i+1 < len(seats) and j-1 >= 0 and seats[i+1][j-1] == "#":
        count += 1
    if i+1 < len(seats) and seats[i+1][j] == "#":
        count += 1
    if i+1 < len(seats) and j+1 < len(seats[i+1]) and seats[i+1][j+1] == "#":
        count += 1
    
    return count

def see_line_occupied_seats(seats, i, j):

    def in_loop_check(value):
        if value == "L":
            return True, 0
        elif value == "#":
            return True, 1
        return False, 0
    
    count = 0

    di = i-1
    while di >= 0:
        b, c = in_loop_check(seats[di][j])
        count += c
        if b: break
        di -= 1
    
    di = i+1
    while di < len(seats):
        b, c = in_loop_check(seats[di][j])
        count += c
        if b: break
        di += 1
    
    dj = j-1
    while dj >= 0:
        b, c = in_loop_check(seats[i][dj])
        count += c
        if b: break
        dj -= 1
    
    dj = j+1
    while dj < len(seats[i]):
        b, c = in_loop_check(seats[i][dj])
        count += c
        if b: break
        dj += 1
    
    di = i-1
    dj = j-1
    while di >= 0 and dj >= 0:
        b, c = in_loop_check(seats[di][dj])
        count += c
        if b: break
        di -= 1
        dj -= 1
    
    di = i-1
    dj = j+1
    while di >= 0 and dj < len(seats[di]):
        b, c = in_loop_check(seats[di][dj])
        count += c
        if b: break
        di -= 1
        dj += 1
    
    di = i+1
    dj = j-1
    while di < len(seats) and dj >= 0:
        b, c = in_loop_check(seats[di][dj])
        count += c
        if b: break
        di += 1
        dj -= 1
    
    di = i+1
    dj = j+1
    while di < len(seats) and dj < len(seats[di]):
        b, c = in_loop_check(seats[di][dj])
        count += c
        if b: break
        di += 1
        dj += 1

    return count

if __name__ == "__main__":
    main()
