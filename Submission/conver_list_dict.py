X = [['A', 'B', 'C'], ['A', 'B', 'D'],['W','X'],['W','Y','Z']]
d = {}

for path in X:
    current_level = d
    for part in path:
        if part not in current_level:
            current_level[part] = {}
        current_level = current_level[part]

print(d)