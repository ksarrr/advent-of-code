with open("input.txt", "r") as moves:
    forward = 0
    aim = 0
    depth = 0
    for command in moves:
        command = (command.strip("\n")).split(" ")
        if command[0] == "forward":
            forward += int(command[1])
            depth += aim * int(command[1])
        elif command[0] == "down":
            aim += int(command[1])
        elif command[0] == "up":
            aim -= int(command[1])
    print(forward*depth)