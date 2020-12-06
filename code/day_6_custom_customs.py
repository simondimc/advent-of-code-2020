
# Part 1: For each group, count the number of questions to which anyone answered "yes".
# Part 2: For each group, count the number of questions to which everyone answered "yes".

def main():
    f = open("input/day_6.txt", "r")

    groups_answers = []

    group_answers = []
    for line in f:
        line = line.strip()
        if line == "":
            groups_answers.append(group_answers)
            group_answers = []
        else:
            person_answers = []
            for line_answer in line:
                person_answers.append(line_answer)
            group_answers.append(person_answers)
    groups_answers.append(group_answers)

    print("part 1:", anyone(groups_answers))
    print("part 2:", everyone(groups_answers))

def anyone(groups_answers):
    summ = 0
    for group_answers in groups_answers:
        answers = []
        for person_answers in group_answers:
            for person_answer in person_answers:
                if person_answer not in answers:
                    answers.append(person_answer)
        
        summ += len(answers)

    return summ

def everyone(groups_answers):
    summ = 0
    for group_answers in groups_answers:
        answers = []
        first = True
        for person_answers in group_answers:
            if first:
                answers = person_answers
                first = False
            else:
                intersection = []
                for person_answer in person_answers:
                    if person_answer in answers:
                        intersection.append(person_answer)
                answers = intersection

        summ += len(answers)

    return summ

if __name__ == "__main__":
    main()
