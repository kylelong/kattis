ann = input().strip()
ben = input().strip()

i = j = 0
res = []

while i < len(ann) and j < len(ben):
    if ann[i] < ben[j]:
        res.append(ann[i])
        i += 1
    elif ben[j] < ann[i]:
        res.append(ben[j])
        j += 1
    else:
        res.append(ann[i])
        res.append(ben[j])
        i += 1
        j += 1
        
res.extend(ann[i:])
res.extend(ben[j:])

print(''.join(res))