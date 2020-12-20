
# How many messages completely match rule 0?

def main():
    f = open("input/day_19.txt", "r")

    rules = {}
    
    line = f.readline().strip()
    while line != "":
        rid = line.split(":")[0]
        rule = line.split(":")[1].replace('"', "").split("|")

        for i in range(len(rule)):
            rs = rule[i].strip().split(" ")
            rule[i] = rs
        rules[rid] = rule

        line = f.readline().strip()

    messages = [line.strip() for line in f]

    # part 1

    summ = 0
    for message in messages:
        ok, res_messages = match_rule(message, rules)
        if ok and len([message for message in res_messages if message == ""]):
            summ += 1
    
    print("part 1:", summ)

    # part 2

    rules["8"] = [["42"], ["42", "8"]]
    rules["11"] = [["42", "31"], ["42", "11", "31"]]

    summ = 0
    for message in messages:
        ok, res_messages = match_rule(message, rules)
        if ok and len([message for message in res_messages if message == ""]):
            summ += 1
    
    print("part 2:", summ)
    
def match_rule(message, rules):
    return match_rule_recursive(message, "0", rules)

def match_rule_recursive(message, rid, rules):
    if rid not in rules:
        return message[0] == rid, [message[1:]]

    or_rule = rules[rid]
    or_result = [None for _ in range(len(or_rule))]
    i = 0
    while i < len(or_rule):
        and_rule = or_rule[i]
        j = 0
        and_message = [message]
        while j < len(and_rule):
            k = 0
            message_result = []
            while k < len(and_message):
                if len(and_message[k]) > 0:
                    ok, child_message = match_rule_recursive(and_message[k], and_rule[j], rules)
                    if ok:
                        for cm in child_message:
                            message_result.append(cm)
                k += 1
            and_message = message_result
            j += 1
        if len(and_message) > 0:
            or_result[i] = and_message
        i += 1
    
    or_result = [or_r for or_r in or_result if or_r != None]
    orr_result = []
    for orr in or_result:
        orr_result += orr

    return len(orr_result) > 0, orr_result

if __name__ == "__main__":
    main()
