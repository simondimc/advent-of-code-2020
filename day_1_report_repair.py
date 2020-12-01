
# What is the product of the n entries that sum to 2020?

def main():
    f = open("input/day_1.txt", "r")

    entries = [int(line.strip()) for line in f]

    print("2 entries:")
    solution = find_n_sum(2, entries, 2020)
    print_solution(solution)

    print("3 entries:")
    solution = find_n_sum(3, entries, 2020)
    print_solution(solution)

    print("6 entries:")
    solution = find_n_sum(6, entries, 2020)
    print_solution(solution)

def print_solution(solution):
    if solution == None:
        print("not found")
    else:
        print(solution)
        print("sum:", sum(solution))
        print("product:", multiply_list(solution))

def find_n_sum(n, numbers, looking_for):
    numbers.sort(reverse=True)

    return find_n_sum_recursive(n, numbers, looking_for)

def find_n_sum_recursive(n, numbers, looking_for):
    if n == 1:
        for number in reversed(numbers):
            if number > looking_for:
                return None
            elif number == looking_for:
                return [number]
    else:
        for i, number in enumerate(numbers):
            if number < looking_for and n > 0:
                solution = find_n_sum_recursive(n - 1, numbers[i + 1:], looking_for - number)
                if solution != None:
                    solution = [number] + solution
                    return solution

    return None

def multiply_list(numbers):
    mul = 1
    for number in numbers:
        mul *= number
    return mul

if __name__ == "__main__":
    main()
