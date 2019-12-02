with open("input.txt") as f:
    program = list(map(int, f.read().split(",")))

steps = 4

def run_program(p):
    for i in range(0, len(p), 4):
        if p[i] == 1:
            p[p[i + 3]] = p[p[i + 1]] + p[p[i + 2]]
        elif p[i] == 2:
            p[p[i + 3]] = p[p[i + 1]] * p[p[i + 2]]
        elif p[i] == 99:
            return p

result = run_program(program)
print(result[0])
