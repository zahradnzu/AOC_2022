def opener(file):
    with open(file, "r") as text_file:
        pair_list = []
        for line in text_file:
            pair_list.append(line.rstrip("\n"))
        return pair_list

def main():
    print(score(opener("2nd_input.txt")))

def score(l: list):
    my_choice = 0
    match_result = 0
    enemy_dict = {"A":1, "B":2, "C":3}
    ally_dict = {"X":1, "Y":2, "Z":3}
    for pair in l:
        my_choice += ally_dict[pair[2]]
        if ally_dict[pair[2]] == enemy_dict[pair[0]]:
            match_result += 3
        elif ally_dict[pair[2]] == 1 and enemy_dict[pair[0]] == 3:
            match_result += 6
        elif ally_dict[pair[2]] == enemy_dict[pair[0]] + 1:
            match_result += 6
    score_result = my_choice + match_result
    return score_result

if __name__ == "__main__":
    main()