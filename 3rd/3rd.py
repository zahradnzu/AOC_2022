def opener(file):
    bag_list = []
    with open(file, "r") as text_file:
        for line in text_file:
            bag_list.append(line.rstrip("\n"))
    return bag_list

def bag_splitter(bag):
    half_bag = int((len(bag)/2))
    return bag[:half_bag], bag[half_bag:]

def tuple_iterator(bag_tuples):
    duplicate_chars = []
    for bag_tuple in bag_tuples:
        comp1, comp2 = bag_tuple
        for i in comp1:
            if i in comp2 and i in comp1:
                duplicate_chars.append(i)
                break
    return duplicate_chars

def main():
    bag_list = opener("3rd_input.txt")
    bag_tuples = []
    for bag in bag_list:
        bag_tuples.append(bag_splitter(bag))
    duplicate_chars = tuple_iterator(bag_tuples)
    abc_dict = {}
    n = 1
    for i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        abc_dict[i] = n
        n += 1
    score = 0
    for item in duplicate_chars:
        score += int(abc_dict[item])
    print(score)

if __name__ == "__main__":
    main()