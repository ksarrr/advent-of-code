with open("input.txt", "r") as moves:
    movement = {"forward" : 0, "up" : 0, "down" : 0}
    for command in moves:
        command = (command.strip("\n")).split(" ")
        movement[command[0]] = movement[command[0]] + int(command[1])
    print(movement["forward"]*(movement["down"]-movement["up"]))