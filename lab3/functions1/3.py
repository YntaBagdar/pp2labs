def solve(numheads, numlegs):
    #ns = 'No solutions!'
    for i in range(numheads + 1):
        j = numheads - i
        if 2 * i + 4 * j == numlegs:
            return i, j
    #return ns, ns


if __name__ == "__main__":
    num_heads = 35
    num_legs = 94

    solutions = solve(num_heads, num_legs)
    print(solutions)


