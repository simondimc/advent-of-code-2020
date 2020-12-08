
# Part 1: Immediately before any instruction is executed a second time, what value is in the accumulator?
# Part 2: Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?

def main():
    f = open("input/day_8.txt", "r")

    instructions = []
    for line in f:
        line = line.strip()
        operation = line.split(" ")[0]
        argument = int(line.split(" ")[1])
        instructions.append({
            "operation": operation,
            "argument": argument
        })
    
    print("Part 1:", accumulator_value_at_loop(instructions))
    print("Part 2:", fix_and_get_accumulator_value(instructions))

def accumulator_value_at_loop(instructions):
    loops, sequence, accumulator = run_instructions(instructions)

    if loops:
        return accumulator
    
    return None

def fix_and_get_accumulator_value(instructions):
    loops, sequence, accumulator = run_instructions(instructions)
    if loops:
        for instruction in reversed(sequence):
            if instruction["operation"] == "jmp":
                instructions[instruction["index"]]["operation"] = "nop"

                loops, sequence, accumulator = run_instructions(instructions)
                if not loops:
                    return accumulator
                
                instructions[instruction["index"]]["operation"] = "jmp"

            elif instruction["operation"] == "nop":
                instructions[instruction["index"]]["operation"] = "jmp"

                loops, sequence, accumulator = run_instructions(instructions)
                if not loops:
                    return accumulator

                instructions[instruction["index"]]["operation"] = "nop"
    
    return accumulator

def run_instructions(instructions):
    sequence = []
    accumulator = 0

    seen_instructions = []
    instruction = 0

    while instruction not in seen_instructions:
        if instruction > len(instructions) - 1:
            return False, sequence, accumulator

        sequence.append({
            "index": instruction,
            "operation": instructions[instruction]["operation"],
            "argument": instructions[instruction]["argument"]
        })
        seen_instructions.append(instruction)

        operation = instructions[instruction]["operation"]
        argument = instructions[instruction]["argument"]

        if operation == "acc":
            accumulator += argument
            instruction += 1
        elif operation == "jmp":
            instruction += argument
        elif operation == "nop":
            instruction += 1

    return True, sequence, accumulator

if __name__ == "__main__":
    main()
