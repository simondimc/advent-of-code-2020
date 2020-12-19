
# Part 1: Consider the validity of the nearby tickets you scanned. What is your ticket scanning error rate?
# Part 2: Once you work out which field is which, look for the six fields on your ticket that start with the word departure. What do you get if you multiply those six values together?

def main():
    f = open("input/day_16.txt", "r")

    ranges = {}

    line = f.readline().strip()
    while line != "":
        field = line.split(":")[0]
        rangee = (
            [int(v) for v in line.split(":")[1].strip().split("or")[0].strip().split("-")],
            [int(v) for v in line.split(":")[1].strip().split("or")[1].strip().split("-")]
        )
        ranges[field] = rangee
        line = f.readline().strip()
    
    f.readline()

    my_ticket = [int(v) for v in f.readline().strip().split(",")]

    f.readline()
    f.readline()

    nearby_tickets = []

    line = f.readline().strip()
    while line != "":
        nearby_tickets.append([int(v) for v in line.split(",")])
        line = f.readline().strip()
    
    # part 1

    not_valid_values = []
    not_valid_tickets = []
    for i, values in enumerate(nearby_tickets):
        valid_ticket = True
        for value in values:
            valid_value = False
            for rangee in ranges:
                if value >= ranges[rangee][0][0] and value <= ranges[rangee][0][1] or value >= ranges[rangee][1][0] and value <= ranges[rangee][1][1]:
                    valid_value = True
                    break
            if not valid_value:
                valid_ticket = False
                not_valid_values.append(value)
        if not valid_ticket:
            not_valid_tickets.append(i)
        
    print("part 1:", sum(not_valid_values))

    # part 2

    valid_tickets = []
    for i in range(len(nearby_tickets)):
        if i not in not_valid_tickets:
            valid_tickets.append(nearby_tickets[i])
    
    position_fields = [list(ranges.keys()) for _ in range(len(ranges))]
    for ticket in valid_tickets:
        for i, value in enumerate(ticket):
            to_remove = []
            for position_field in position_fields[i]:
                if not(value >= ranges[position_field][0][0] and value <= ranges[position_field][0][1] 
                    or value >= ranges[position_field][1][0] and value <= ranges[position_field][1][1]):
                    to_remove.append(position_field)
            for position_field in to_remove:
                position_fields[i].remove(position_field)

    fields_order = [None for _ in range(len(ranges))]
    ordered = 0
    while ordered < len(ranges):
        field_i = -1
        for i, position_field in enumerate(position_fields):
            if len(position_field) == 1:
                field_i = i
                break

        field = position_fields[field_i][0]
        fields_order[field_i] = field

        for i, position_field in enumerate(position_fields):
            if field in position_field:
                position_field.remove(field)
        
        ordered += 1

    departure_values = []
    for rangee in ranges:
        if rangee.startswith("departure"):
            departure_values.append(my_ticket[fields_order.index(rangee)])

    print("part 2:", multiply_list(departure_values))

def multiply_list(numbers):
    mul = 1
    for number in numbers:
        mul *= number
    return mul

if __name__ == "__main__":
    main()
