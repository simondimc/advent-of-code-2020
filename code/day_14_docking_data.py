
# Execute the initialization program. What is the sum of all values left in memory after it completes?

def main():
    f = open("input/day_14.txt", "r")

    instructions = []
    for line in f:
        line = line.strip()

        if line[0:4] == "mask":
            instructions.append((
                "mask", 
                line.split("=")[1].strip()
            ))
        elif line[0:3] == "mem":
            instructions.append((
                "mem", 
                int(line.split("[")[1].split("]")[0]),
                int(line.split("=")[1].strip())
            ))
    
    mem1 = {}
    mem2 = {}
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

    for instruction in instructions:
        if instruction[0] == "mask":
            mask = instruction[1]
        elif instruction[0] == "mem":
            mem1[instruction[1]] = value_after_mask(instruction[2], mask)

            addresses = addresses_after_mask(instruction[1], mask)
            for address in addresses:
                mem2[address] = instruction[2]

    summ1 = 0
    for address in mem1:
        summ1 += mem1[address]

    summ2 = 0
    for address in mem2:
        summ2 += mem2[address]

    print("part 1:", summ1)
    print("part 2:", summ2)

def value_after_mask(value, mask):
    value_m = value_mask(value)
    
    cm = ""
    for vm, m in zip(value_m, mask):
        if m != "X":
            vm = m
        cm += vm

    return mask_value(cm)

def addresses_after_mask(address, mask):
    address_m = value_mask(address)

    cm = ""
    nox = 0
    for dm, m in zip(address_m, mask):
        if m == "0":
            cm += dm
        elif m == "1":
            cm += "1"
        elif m == "X":
            cm += "X"
            nox += 1

    addresses = ["" for _ in range(2**nox)]

    x = 2**nox / 2
    for bit in cm:
        if bit != "X":
            for i in range(len(addresses)):
                addresses[i] += bit
        else:
            xi = 0
            b = "0"
            for i in range(len(addresses)):
                if xi >= x:
                    b = "0" if b == "1" else "1"
                    xi = 0

                addresses[i] += b
                xi += 1

            x /= 2
    
    for i in range(len(addresses)):
        addresses[i] = mask_value(addresses[i])

    return addresses

def value_mask(value):
    mask = ""
    v = 2**35
    while v >= 1:
        if value >= v:
            mask += "1"
            value -= v
        else:
            mask += "0"
        v /= 2
    return mask

def mask_value(mask):
    value = 0
    v = 2**35
    for m in mask:        
        if m == "1":
            value += v
        v /= 2
    return int(value)

if __name__ == "__main__":
    main()
