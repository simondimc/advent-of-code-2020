
# How many passwords are valid according to their policies?

def main():
    f = open("input/day_2.txt", "r")

    passwords = []

    for line in f:
        line = line.strip()
        
        passwords.append({
            "letter": line.split(" ")[1].split(":")[0],
            "min": int(line.split("-")[0]),
            "max": int(line.split("-")[1].split(" ")[0]),
            "password": line.split(": ")[1]
        })
    
    print("part 1 valid passwords:", part_1(passwords))
    print("part 2 valid passwords:", part_2(passwords))

def part_1(passwords):
    valid = 0
    for password in passwords:
        letter_count = 0

        for c in password["password"]:
            if c == password["letter"]:
                letter_count += 1

        if letter_count >= password["min"] and letter_count <= password["max"]:
            valid += 1

    return valid

def part_2(passwords):
    valid = 0
    for password in passwords:
        char1 = password["password"][password["min"] - 1]
        char2 = password["password"][password["max"] - 1]

        if char1 != char2 and (char1 == password["letter"] or char2 == password["letter"]):
            valid += 1

    return valid

if __name__ == "__main__":
    main()
