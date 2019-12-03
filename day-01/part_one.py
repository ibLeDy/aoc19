with open("input.txt", "r") as f:
    modules = f.readlines()

required_fuel = 0
for module in modules:
    module_fuel = int(module.strip("\n")) // 3 - 2
    required_fuel += module_fuel

print(required_fuel)
