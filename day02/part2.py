import random

with open("input.txt", "r") as f:
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

result = [0]
while result[0] != 19690720:
    modified = program.copy()
    modified[1] = random.randint(0, 99)
    modified[2] = random.randint(0, 99)
    result = run_program(modified)

print(100 * result[1] + result[2])
