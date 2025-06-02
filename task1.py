try:
    with open("sample.txt", "r") as f:
        print("Reading file content:")
        c = 1
        for line in f:
            print("Lines", c, ":", line.strip())
            # print("Lines",c,":",line)
            c += 1
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")