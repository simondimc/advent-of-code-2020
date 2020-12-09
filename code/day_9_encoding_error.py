
# Part 1: What is the first number that is not the sum of two of the 25 numbers before it?
# Part 2: Find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1. Add together the smallest and largest number in this contiguous range.

def main():
    f = open("input/day_9.txt", "r")

    numbers = [int(line.strip()) for line in f]

    print("part 1:", number_not_sum(numbers))
    print("part 2:", encryption_weakness(numbers))

def number_not_sum(numbers):
    i = 25
    while check_sum(numbers[i-25:i], numbers[i]):
        i += 1
    
    return numbers[i]

def check_sum(numbers, number):
    i = 0
    while i < len(numbers):
        j = i + 1
        while j < len(numbers):
            if numbers[i] + numbers[j] == number:
                return True
            j += 1
        i += 1
    
    return False

def encryption_weakness(numbers):    
    c_set = contiguous_set(numbers, number_not_sum(numbers))
    
    return min(c_set) + max(c_set)

def contiguous_set(numbers, number):
    i = 0
    while i < len(numbers):
        if numbers[i] == number:
            i += 1
            continue

        j = i
        c_set = []
        while sum(c_set) + numbers[i] < number:
            c_set.append(numbers[j])
            j += 1
        if sum(c_set) == number:
            return c_set
        i += 1

    return None

if __name__ == "__main__":
    main()
