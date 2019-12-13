import collections

with open("input.txt", "r") as f:
    start_s, end_s = map(int, f.read().split("-"))
    start, end = int(start_s), int(end_s)

def compute_result():
    count = 0
    for num in range(start, end):
        num_s = str(num)

        if len(num_s) != 6:
            continue

        if not (
            ord(num_s[0]) <= ord(num_s[1]) <= ord(num_s[2]) <=
            ord(num_s[3]) <= ord(num_s[4]) <= ord(num_s[5])
        ):
            continue

        valid = False
        prev = num_s[0]
        for c in num_s[1:]:
            if c == prev:
                valid = True
            prev = c

        if not valid:
            continue

        valid2 = False
        counter = collections.Counter(num_s)
        for _, n in counter.most_common():
            if n == 2:
                valid2 = True
                print(num_s)

        if not valid2:
            continue

        count += 1
    return count

result = compute_result()
print(result)
