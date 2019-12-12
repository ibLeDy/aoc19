from typing import NamedTuple

class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Velocity:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

with open("input.txt", "r") as f:
    data = f.read().strip().splitlines()

moons = ["io", "europa", "ganymede", "callisto"]

scan = {}
for i, moon in enumerate(moons):
    x, y, z = [int(p.split("=")[-1]) for p in data[i].strip("<>").split(", ")]
    scan[moon] = [Position(x, y, x), Velocity(0, 0, 0)]

for moon in scan:
    x = [1 if v[0].x < scan[moon][0].x else 0 for k, v in scan.items() if k != moon and v[0].x != scan[moon][0].x]
    y = [1 if v[0].y < scan[moon][0].y else 0 for k, v in scan.items() if k != moon and v[0].y != scan[moon][0].y]
    z = [1 if v[0].z < scan[moon][0].z else 0 for k, v in scan.items() if k != moon and v[0].z != scan[moon][0].z]  

    for i in x:
        if i == 1:
            scan[moon][1].x += 1
        elif i == 0:
            scan[moon][1].x -= 1

    for i in y:
        if i == 1:
            scan[moon][1].y += 1
        elif i == 0:
            scan[moon][1].y -= 1

    for i in z:
        if i == 1:
            scan[moon][1].z += 1
        elif i == 0:
            scan[moon][1].z -= 1


for moon in scan:
    print((scan[moon][0].x, scan[moon][0].y, scan[moon][0].z),
           (scan[moon][1].x, scan[moon][1].y, scan[moon][1].z))


# steps = {}
# steps[count] = 
# steps = {
#     0: {
#         "positions": positions,
#         "velocities": velocities
#     } 
# }