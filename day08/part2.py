def visualize(data):
    layers = [data[i * 25 * 6:25 * 6 + i * 25 * 6] for i in range(100)]
    minimum = min(layers, key=lambda s: s.count("0"))
    print(minimum.count("1") * minimum.count("2"))
    for y in range(6):
        for x in range(25):
            for layer in layers:
                if layer[y * 25 + x] != "2":
                    print(layer[y * 25 + x].replace("0", " "), end="")
                    break
            else:
                print("?", end="")
        print()

with open("input.txt", "r") as f:
    data = f.read().strip()

visualize(data)
