windows_size = 3

with open("input.txt", "r") as measurements:
    depths = [None for i in range(windows_size-1)]
    for i in range(windows_size-1):
        depths[i] = int(measurements.readline().strip("\n"))
    increased = 0
    temp_depth = int(measurements.readline().strip("\n"))
    prev_depths = sum(depths) + temp_depth
    print(str(sum(depths)+temp_depth)+" N/A")
    for i in range(1,windows_size-1):
        depths[i-1]=depths[i]
    depths[-1] = temp_depth
    for depth in measurements:
        depth = int(depth)
        # print(prev_depths)
        # print(depths+[depth])
        if (sum(depths)+depth) > prev_depths:
            increased += 1
            print(str(sum(depths)+depth)+" increased")
        elif (sum(depths)+depth) == prev_depths:
            print(str(sum(depths)+depth)+" no change")
        else:
            print(str(sum(depths)+depth)+" decreased")
        prev_depths = sum(depths)+depth
        for i in range(1,windows_size-1):
            depths[i-1]=depths[i]
        depths[-1]=depth
    print(increased)