
# Given your starting numbers, what will be the nth number spoken?

def main():
    f = open("input/day_15.txt", "r")

    numbers = [int(c) for c in f.readline().split(",")]

    spoken = {}
    for i, n in enumerate(numbers):
        spoken[n] = i + 1
    numbers.append(0)

    print("part 1:", nth_spoken(2020, numbers, spoken))
    print("part 2:", nth_spoken(30000000, numbers, spoken))

def nth_spoken(n, numbers, spoken):
    while len(numbers) < n:
        last_spoken = numbers[-1]
        if last_spoken not in spoken:
            numbers.append(0)
            spoken[last_spoken] = len(numbers) - 1
        else:
            numbers.append(len(numbers) - spoken[last_spoken])
            spoken[last_spoken] = len(numbers) - 1

    return numbers[-1]

if __name__ == "__main__":
    main()
