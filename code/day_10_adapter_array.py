
# Part 1: What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
# Part 2: What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?

def main():
    f = open("input/day_10.txt", "r")

    adapters = [int(line.strip()) for line in f]

    jd = jolt_differences(adapters)
    print("part 1:", jd[0] * jd[2])
    print("part 2:", count_distinct_arrangements(adapters))

def jolt_differences(adapters):
    jd = [0, 0, 0]

    jolt = 0
    adapters.sort()

    for aj in adapters:
        diff = aj - jolt
        jd[diff - 1] += 1
        jolt = aj

    jd[2] += 1

    return jd

def count_distinct_arrangements(adapters):
    adapters.sort()
    adapters = [0] + adapters

    mem, count = count_distinct_arrangements_recursive(adapters, {})

    return count

def count_distinct_arrangements_recursive(adapters, mem):
    if len(adapters) == 1:
        return mem, 1

    count = 0
    c = adapters[0]
    ni = 1
    while ni < len(adapters) and adapters[ni] - c <= 3:
        if adapters[ni] in mem:
            count += mem[adapters[ni]]
        else:
            mem, child_count = count_distinct_arrangements_recursive(adapters[ni:], mem)
            count += child_count
            mem[adapters[ni]] = child_count
        
        ni += 1

    return mem, count
    
if __name__ == "__main__":
    main()
