with open("input.txt", "r") as read_bits:
    bits = read_bits.read().split("\n")
    bits.sort()
    temp_bits = bits
    position = 0
    while len(temp_bits) > 1:
        # print(temp_bits)
        ones = 0
        for line in range(len(temp_bits)):
            if temp_bits[line][position] == "1":
                ones += 1
        # print(ones)
        if ones >= len(temp_bits)/2:
            temp_bits = temp_bits[len(temp_bits)-ones:]
        else:
            temp_bits = temp_bits[:len(temp_bits)-ones]
        position += 1
    # print(temp_bits)
    oxygen = int(''.join(map(str,temp_bits)),2)
    temp_bits = bits
    position = 0
    while len(temp_bits) > 1:
        # print(temp_bits)
        ones = 0
        for line in range(len(temp_bits)):
            if temp_bits[line][position] == "1":
                ones += 1
        # print(ones)
        if ones >= len(temp_bits)/2:
            temp_bits = temp_bits[:len(temp_bits)-ones]
        else:
            temp_bits = temp_bits[len(temp_bits)-ones:]
        position += 1
    # print(temp_bits)
    co2 = int(''.join(map(str,temp_bits)),2)
    print(oxygen)
    print(co2)
    print(oxygen*co2)