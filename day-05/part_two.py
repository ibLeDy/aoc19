with open("input.txt", "r") as f:
    program = [int(part) for part in f.read().strip().split(",")]

def run(program):
    def param_mode(instr, idx):
        mode = instr // (10 ** (idx + 1)) % 10
        if mode == 0:
            return program[program[count + idx]]
        elif mode == 1:
            return program[count + idx]
        else:
            raise NotImplementedError(mode)

    count = 0
    while count < len(program):
        instr = program[count]
        opc = instr % 100
        if opc == 99:
            return program
        elif opc == 1:
            program[program[count + 3]] = param_mode(instr, 1) + param_mode(instr, 2)
            count += 4
        elif opc == 2:
            program[program[count + 3]] = param_mode(instr, 1) * param_mode(instr, 2)
            count += 4
        elif opc == 3:
            program[program[count + 1]] = 5  # hardcoded
            count += 2
        elif opc == 4:
            print(param_mode(instr, 1))
            count += 2
        elif opc == 5:
            if param_mode(instr, 1):
                count = param_mode(instr, 2)
            else:
                count += 3
        elif opc == 6:
            if not param_mode(instr, 1):
                count = param_mode(instr, 2)
            else:
                count += 3
        elif opc == 7:
            if param_mode(instr, 1) < param_mode(instr, 2):
                program[program[count + 3]] = 1
            else:
                program[program[count + 3]] = 0
            count += 4
        elif opc == 8:
            if param_mode(instr, 1) == param_mode(instr, 2):
                program[program[count + 3]] = 1
            else:
                program[program[count + 3]] = 0
            count += 4
        else:
            raise AssertionError(f"wut {program} {count}")
    raise AssertionError(f"wat {program} {count}")

result = run(program)
# print(result)
