with open("input.txt", "r") as measurements:
    prev_depth = int(measurements.readline().strip("\n"))
    # print(str(prev_depth)+" N/A")
    increased = 0
    for depth in measurements:
        depth = int(depth.strip("\n"))
        if depth > prev_depth:
            increased += 1
            # print(str(depth)+" increased")
        # else:
        #     print(str(depth)+" decreased")
        prev_depth = depth
    print(increased) 