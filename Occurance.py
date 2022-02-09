arr = [1, 2, 3, 2, 1]
duplicate = []

for j in arr:
    x = 0
    for i in arr:
        if i not in duplicate:
            x+=1
            if x>1 or x==2 :
                duplicate.append(i)
                x = 0
print("Output:",duplicate[0])


