def get_fewest_0_layer(layers):
    fewest_0 = [999, 0]
    for l in layers:
        if l.count("0") < fewest_0[0]:
            fewest_0[0] = l.count("0")
            fewest_0[1] = l
    return fewest_0[1]

def create_layers(data, layer_size):
    layers = []
    count = 0
    temp_layer = []
    for i in data:
        if count >= layer_size:
            layers.append(temp_layer.copy())
            temp_layer.clear()
            count = 0
        else:
            temp_layer.append(i)
            count += 1
    return layers

with open("input.txt", "r") as f:
    data = f.read().strip()

layer_size = 25 * 6
fewest = get_fewest_0_layer(create_layers(data, layer_size))
print(fewest.count("1") * fewest.count("2"))
