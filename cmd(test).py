while True:
    cmd = input()
    parts = cmd.split()
    if parts[0] == "sum" :
        print(int(parts[1]) + int(parts[2]))
    elif parts[0] == "sub" :
        print(int(parts[1]) - int(parts[2]))
    elif parts[0] == "mul" :
        print(int(parts[1]) - int(parts[2]))
    elif parts[0] == "div" :
        print(int(parts[1] - int(parts[2])))
    elif parts[0] == "end" :
        break
    else :
        print("invalid command")