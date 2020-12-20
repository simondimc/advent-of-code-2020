
# Evaluate the expression on each line of the homework; what is the sum of the resulting values?

def main():
    f = open("input/day_18.txt", "r")

    expressions = [line.strip() for line in f]

    summ = 0
    for expression in expressions:
        summ += evaluate_part_1(expression)

    print("part 1:", summ)

    summ = 0
    for expression in expressions:
        summ += evaluate_part_2(expression)

    print("part 2:", summ)

def evaluate_part_1(expression):
    expression = expression[::-1]

    return evaluate_recursive_part_1(expression)

def evaluate_recursive_part_1(expression):
    add_index = expression.find("+")
    mul_index = expression.find("*")
    brc_index = expression.find(")")

    if add_index == -1 and mul_index == -1 and brc_index == -1:
        return int(expression)

    comp_list = []
    if add_index != -1:
        comp_list.append(add_index)
    if mul_index != -1:
        comp_list.append(mul_index)
    if brc_index != -1:
        comp_list.append(brc_index)

    closest = min(comp_list)

    if add_index == closest:
        n1 = expression.split("+", 1)[0].strip()
        n2 = expression.split("+", 1)[1].strip()
        return int(n1) + evaluate_recursive_part_1(n2)
    elif mul_index == closest:
        n1 = expression.split("*", 1)[0].strip()
        n2 = expression.split("*", 1)[1].strip()
        return int(n1) * evaluate_recursive_part_1(n2)
    else:
        brc_c = 1
        n1 = ""
        for c in expression[1:]:
            if c == ")":
                brc_c += 1
            elif c == "(":
                brc_c -= 1
            if brc_c == 0:
                break
            n1 += c
        n2 = expression.split(")" + n1 + "(", 1)[1].strip()
        n1c = evaluate_recursive_part_1(n1)
        return evaluate_recursive_part_1(str(n1c) + " " + n2)

def evaluate_part_2(expression):
    return evaluate_recursive_part_2(expression)

def evaluate_recursive_part_2(expression):
    print(expression)
    add_index = expression.find("+")
    mul_index = expression.find("*")
    brc_index = expression.find("(")

    if add_index == -1 and mul_index == -1 and brc_index == -1:
        return int(expression)

    if brc_index != -1:
        brc_c = 1
        n1 = ""
        for c in expression[expression.index("(") + 1:]:
            if c == "(":
                brc_c += 1
            elif c == ")":
                brc_c -= 1
            if brc_c == 0:
                break
            n1 += c
        n21 = expression.split("(" + n1 + ")", 1)[0].strip()
        n22 = expression.split("(" + n1 + ")", 1)[1].strip()
        n1c = evaluate_recursive_part_2(n1)
        return evaluate_recursive_part_2(n21 + " " + str(n1c) + " " + n22)

    if mul_index != -1:
        n1 = expression.split("*", 1)[0].strip()
        n2 = expression.split("*", 1)[1].strip()
        return evaluate_recursive_part_2(n1) * evaluate_recursive_part_2(n2)
    
    if add_index != -1:
        n1 = expression.split("+", 1)[0].strip()
        n2 = expression.split("+", 1)[1].strip()
        return evaluate_recursive_part_2(n1) + evaluate_recursive_part_2(n2)

if __name__ == "__main__":
    main()
