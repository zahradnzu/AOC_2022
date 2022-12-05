def opener(file):
    tuple_list = []
    with open(file, "r") as text_file:
        for line in text_file:
            tuple_list.append(line.rstrip("\n"))
    return tuple_list

def list_returner(l):
    pair_list = []
    for pair in l:
        e1, e2 = pair.split(",")
        e1a, e1b = e1.split("-")
        e2a, e2b = e2.split("-")
        e1a = int(e1a)
        e2a = int(e2a)
        e1_pair_list = []
        e2_pair_list = []
        while int(e1b) >= e1a:
            e1_pair_list.append(int(e1a))
            e1a += 1
        while int(e2b) >= e2a:
            e2_pair_list.append(int(e2a))
            e2a += 1
        pair_list.append([e1_pair_list, e2_pair_list])
    return pair_list

def main():
    tuple_list = opener("4th_input.txt")
    pair_list = list_returner(tuple_list)
    duplicate_counter = 0
    for pair in pair_list:
        e1, e2 = pair
        for i in e1:
            ...

    print(duplicate_counter)
        





if __name__ == "__main__":
    main()