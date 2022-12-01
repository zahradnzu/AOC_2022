def main():
    elves_list = elves_list_maker("1st.txt")
    elv_str = ""
    for calorie in elves_list:
        if calorie != "---":
            elv_str = elv_str + calorie + ","
        else:
            elv_str = elv_str + calorie
    print(elv_str)

def elves_list_maker(file):
    elves_list = []
    with open(file, "r") as txt_file:
        for row in txt_file:
            if row != "\n":
                row = row.strip("\n")
                elves_list.append(row)
            else:
                elves_list.append("---")
    return elves_list


if __name__ == "__main__":
    main()