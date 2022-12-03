def opener(file):
    with open(file, "r") as text_file:
        bag_list = []
        for line in text_file:
            bag_list.append(line.rstrip("\n"))
        return bag_list

def main():
    bag_list = opener("3rd_input.txt")

if __name__ == "__main__":
    main()