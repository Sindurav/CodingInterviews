def read_file(filename):
    with open(filename) as file:
        for line in file:
            nums = line.strip().split()

    file = open("output.txt", "w")
    file.write(int(nums[0])+int(nums[1]))
    file.close()


file_name = "input.txt"
read_file(file_name)
