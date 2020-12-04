import re

# Count the number of valid passports.

def main():
    f = open("input/day_4.txt", "r")

    passwords_fields = []

    fields = {}
    for line in f:
        line = line.strip()
        if line == "":
            passwords_fields.append(fields)
            fields = {}
        else:
            line_fields = line.split(" ")
            for line_field in line_fields:
                field = line_field.split(":")[0]
                value = line_field.split(":")[1]
                fields[field] = value
    passwords_fields.append(fields)
    
    optional = ["cid"]

    part_1_valid = 0
    part_2_valid = 0
    for password_fields in passwords_fields:
        keys = list(password_fields.keys())
        required_keys = [key for key in keys if key not in optional]
        
        if len(required_keys) == 7:
            part_1_valid += 1

            byr = re.match("^[0-9]{4}$", password_fields["byr"])
            if not (byr is not None and int(byr.group()) >= 1920 and int(byr.group()) <= 2002):
                continue

            iyr = re.match("^[0-9]{4}$", password_fields["iyr"])
            if not (iyr is not None and int(iyr.group()) >= 2010 and int(iyr.group()) <= 2020):
                continue

            eyr = re.match("^[0-9]{4}$", password_fields["eyr"])
            if not (eyr is not None and int(eyr.group()) >= 2020 and int(eyr.group()) <= 2030):
                continue

            hgt = re.match("^[0-9]+(cm|in)$", password_fields["hgt"])
            if hgt is not None:
                if (hgt.group()[-2:] == "cm" and not (int(hgt.group()[:-2]) >= 150 and int(hgt.group()[:-2]) <= 193)):
                    continue
                elif (hgt.group()[-2:] == "in" and not (int(hgt.group()[:-2]) >= 59 and int(hgt.group()[:-2]) <= 76)):
                    continue
            else:
                continue

            hcl = re.match("^#[0-9a-f]{6}$", password_fields["hcl"])
            if hcl is None:
                continue

            if password_fields["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                continue
            
            pid = re.match("^[0-9]{9}$", password_fields["pid"])
            if pid is None:
                continue

            part_2_valid += 1


    print("part 1:", part_1_valid)
    print("part 2:", part_2_valid)

if __name__ == "__main__":
    main()
