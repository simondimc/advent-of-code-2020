
# How many cubes are left in the active state after the sixth cycle?

def main():
    f = open("input/day_17.txt", "r")

    lines = [line.strip() for line in f]

    
    print("part 1:", len(cubes(3, lines)))
    print("part 2:", len(cubes(4, lines)))

def cubes(dimension, lines):
    active_cubes = set()

    y = 0
    for line in lines:
        x = 0
        for v in line:
            if v == "#":
                cube = (x, y)
                for d in range(dimension - 2):
                    cube += (0,)
                active_cubes.add(cube)
            x += 1
        y += 1
    
    for c in range(6):
        activate = []
        deactivate = []

        inactive_neighbors = []
        for active_cube in active_cubes:
            active_n, inactive_n = neighbors(dimension, active_cubes, active_cube)

            if not(len(active_n) == 2 or len(active_n) == 3):
                deactivate.append(active_cube)

            for inn in inactive_n:
                inactive_neighbors.append(inn)

        for inactive_neighbor in inactive_neighbors:
            active_n, inactive_n = neighbors(dimension, active_cubes, inactive_neighbor)

            if len(active_n) == 3:
                activate.append(inactive_neighbor)

        for a in activate:
            active_cubes.add(a)
        
        for d in deactivate:
            active_cubes.remove(d)
    
    return active_cubes
    
def neighbors(dimension, active, pos):
    active_n = []
    inactive_n = []

    differs = [[] for _ in range(3**dimension)]
    i = 1
    while i <= dimension:
        diff = [-1, 0, 1]
        di = 0
        dc = 0
        for ci in range(len(differs)):
            differs[ci].append(diff[di])
            dc += 1
            if dc >= (3**(dimension - i)):
                dc = 0
                di = (di + 1) % 3
        i += 1
    
    for d in differs:
        mpos = ()
        for i, c in enumerate(pos):
            mpos += (c + d[i],)

        if mpos == pos:
            continue

        if mpos in active:
            active_n.append(mpos)
        else:
            inactive_n.append(mpos)

    return active_n, inactive_n

if __name__ == "__main__":
    main()
