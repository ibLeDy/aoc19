def calculate_fuel(module):
    try:
        module_fuel = int(module.strip("\n")) // 3 - 2
    except AttributeError:
        module_fuel = module // 3 - 2

    return module_fuel

extra_fuel = 0

def calculate_fuel_fuel(fuel):
    global extra_fuel
    result = calculate_fuel(fuel)
    if result == 0:
        return
    elif abs(result) != result:
        return
    else:
        extra_fuel += result
        calculate_fuel_fuel(result)

with open("input.txt", "r") as f:
    modules = f.readlines()

required_fuel = 0
for module in modules:
    extra_fuel = 0
    total_fuel = calculate_fuel(module)
    calculate_fuel_fuel(total_fuel)
    required_fuel += total_fuel + extra_fuel

print(required_fuel)