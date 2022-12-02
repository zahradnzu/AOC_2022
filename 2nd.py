def opener(file):
    with open(file, "r") as text_file:
        return text_file

def main():
    input = opener("2nd_input.txt")
    for line in input:
        print(line)

if __name__ == "__main__":
    main()