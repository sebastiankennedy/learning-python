with open('poem1.txt', 'r') as f:
    lines = f.readlines()

print(lines)

with open('poem2.txt', 'w') as f:
    for line in lines:
        if line not in ['一弦一柱思华年。\n', '只是当时已惘然。\n']:
            f.write(line)
        else:
            f.write('____________。\n')
