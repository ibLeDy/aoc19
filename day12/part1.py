from typing import NamedTuple
import re


VECTOR_RE = re.compile(r'-?\d+')


class Vector(NamedTuple):
    x: int
    y: int
    z: int

    def add(self, other):
        return self._replace(
            x=self.x + other.x,
            y=self.y + other.y,
            z=self.z + other.z,
        )

class Moon(NamedTuple):
    pos: Vector
    vel: Vector


with open("input.txt", "r") as f:
    data = f.read().splitlines()

moons = []
for d in data:
    x, y, z = VECTOR_RE.findall(d)
    moons.append(Moon(Vector(int(x), int(y), int(z)), Vector(0, 0, 0)))

for _ in range(1000):
    for i, moon in enumerate(moons):
        vel_x, vel_y, vel_z = moon.vel
        for next_moon in moons:
            if next_moon is moon:
                continue
            if next_moon.pos.x > moon.pos.x:
                vel_x += 1
            elif next_moon.pos.x < moon.pos.x:
                vel_x -= 1
            if next_moon.pos.y > moon.pos.y:
                vel_y += 1
            elif next_moon.pos.y < moon.pos.y:
                vel_y -= 1
            if next_moon.pos.z > moon.pos.z:
                vel_z += 1
            elif next_moon.pos.z < moon.pos.z:
                vel_z -= 1

        moons[i] = moon._replace(vel=Vector(vel_x, vel_y, vel_z))

    for i, moon in enumerate(moons):
        moons[i] = moon._replace(pos=moon.pos.add(moon.vel))

print(sum(
    sum(abs(p) for p in moon.pos) * sum(abs(v) for v in moon.vel)
    for moon in moons
))
