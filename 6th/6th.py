import re

def opener(file):
    with open(file, "r") as text_input:
        for line in text_input:
            return str(line)

def main():
    text = opener("6th_input")
    s = re.search(r"[a-z]{4}", text)
    for string in text:
        s = re.search(r".*[a-z]{4}", text)
        print(s.group())


    # for s in text:
    #     if s != text[(s_index - 1)] and text[(s_index - 1)] != text[(s_index - 2)] and text[(s_index - 2)] != text[(s_index - 3)] and text[(s_index - 3)] != text[(s_index - 4)]:
    #         print(text[(s_index - 4):(s_index)])
    #         break
    #     else:
    #         s_index += 1

if __name__ == "__main__":
    main()