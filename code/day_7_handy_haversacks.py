
# Part 1: How many bag colors can eventually contain at least one shiny gold bag?
# Part 2: How many individual bags are required inside your single shiny gold bag?

def main():
    f = open("input/day_7.txt", "r")

    bags = {}

    for line in f:
        line = line.strip()
        bag = line.split(" bag")[0]
        contain = line.split("contain ")[1]
        bags_in_bag = []
        if contain != "no other bags.":
            for bag_in_bag in contain.split(","):
                bag_in_bag = bag_in_bag.strip()
                number = int(bag_in_bag.split(" ")[0])
                name = " ".join(bag_in_bag.split(" ")[1:]).split(" bag")[0]
                bags_in_bag.append((number, name))
        bags[bag] = bags_in_bag

    print("part 1:", contain_at_least_one(bags, "shiny gold"))
    print("part 2:", inside_a_bag(bags, "shiny gold"))

def contain_at_least_one(bags, target):
    count = 0
    for bag in bags:
        if bag != target and contain_at_least_one_recursive(bags, bag, target):
            count += 1

    return count

def contain_at_least_one_recursive(bags, bag, target):
    for number, name in bags[bag]:
        if name == target:
            return True

    for number, name in bags[bag]:
        if contain_at_least_one_recursive(bags, name, target):
            return True
    
    return False

def inside_a_bag(bags, target):
    count = 0

    for number, name in bags[target]:
        count += number
        for _ in range(number):
            count += inside_a_bag(bags, name)
    
    return count

if __name__ == "__main__":
    main()
