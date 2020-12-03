
def main():
    f = open("input/day_3.txt", "r")

    tree_map = [line.strip() for line in f]

    r11 = traverse_slope(tree_map, 1, 1)
    r31 = traverse_slope(tree_map, 3, 1)
    r51 = traverse_slope(tree_map, 5, 1)
    r71 = traverse_slope(tree_map, 7, 1)
    r12 = traverse_slope(tree_map, 1, 2)

    print("1, 1:", r11)
    print("3, 1:", r31)
    print("5, 1:", r51)
    print("7, 1:", r71)
    print("1, 2:", r12)

    print(r11 * r31 * r51 * r71 * r12)

def traverse_slope(tree_map, right, down):
    position = {"x": 0, "y": 0}

    trees = 0
    while position["y"] < len(tree_map):
        if tree_map[position["y"]][position["x"]] == "#":
            trees += 1
            
        position["x"] = (position["x"] + right) % len(tree_map[position["y"]])
        position["y"] += down
    
    return trees

if __name__ == "__main__":
    main()
