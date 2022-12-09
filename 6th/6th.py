import re

def opener(file):
    with open(file, "r") as text_input:
        for line in text_input:
            return str(line)

def main():
    text = opener("6th_input")
    s_index = 3
    for s in text[3:]:
        try:
            if text[s_index] != text[(s_index - 1)] and text[s_index] != text[(s_index - 2)] and text[s_index] != text[(s_index - 3)] and text[s_index] != text[(s_index - 4)]:
                print(s_index + 1)
                break
            else:
                s_index += 1
        except IndexError:
            continue


if __name__ == "__main__":
    main()