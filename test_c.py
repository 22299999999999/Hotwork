with open("data.txt") as f:
    while True:
        line = f.readline()
        if line:
            print(line)
            print("hello python")
        else:
            break
