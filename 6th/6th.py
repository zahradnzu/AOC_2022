import re

def opener(file):
    with open(file, "r") as text_input:
        for line in text_input:
            return str(line)

def main():
    text = opener("6th_input")
    s_index = 0
    for s in text:
        try:
            if s in text[(s_index + 1):(s_index + 4)] or text[(s_index + 1)] in text[(s_index + 2):(s_index + 4)] or text[(s_index + 2)] == text[(s_index + 3)]:
                s_index += 1
                continue
            else:
                print((s_index + 4))
        except IndexError:
            break
        
if __name__ == "__main__":
    main()