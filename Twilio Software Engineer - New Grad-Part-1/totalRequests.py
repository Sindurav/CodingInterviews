from collections import defaultdict


def read_file(filename):
    host2req = defaultdict(int)
    with open(filename) as file:
        for line in file:
            line_list = line.split()
            host2req[line_list[0]] += 1

    file = open("records_"+filename, "w")
    for host in host2req:
        file.write(host+" "+str(host2req[host])+"\n")
    file.close()


file_name = input()
read_file(file_name)