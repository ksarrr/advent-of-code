with open("input.txt", "r") as bits:
    temp_read = list(map(int,bits.readline().strip("\n")))
    gamma = [x if x != 0 else (-1) for x in temp_read]
    for line in bits:
        line = line.strip("\n")
        for l in range(len(line)):
            if line[l] == "1":
                gamma[l] += 1
            else:
                gamma[l] -= 1
    gamma = [1 if x > 0 else 0 for x in gamma]
    epsilon = [0 if x > 0 else 1 for x in gamma]
    print(gamma)
    print(epsilon)
    print(int(''.join(map(str,gamma)),2)*int(''.join(map(str,epsilon)),2))