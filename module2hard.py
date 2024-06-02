def parol(a):
    parol_1 = []
    if a>=3 and a<=20:
        for j in range(20, 0, -1):
            for k in range(1, 20):
                if a%(j+k)==0 and j>k:
                    parol_1.append(k)
                    parol_1.append(j)

    result = ''.join(str(h) for h in parol_1) # самая сложная строка для меня
    return result
print(parol(11))