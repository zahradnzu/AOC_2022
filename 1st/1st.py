def main():
    elve_list = elves_list_maker("1st_input.txt")
    new_elve_list = []
    for elve in elve_list:
        calorie_count = 0
        for calorie in elve:
            try:
                calorie_count += int(calorie)
            except (ValueError, TypeError):
                new_elve_list.append(calorie_count)
                break
    
    print(max(new_elve_list))
    
    # part two
    top_three = 0
    for elve in sorted(new_elve_list, reverse=True)[0:3]:
        top_three += int(elve)
    print(top_three)

def elves_list_maker(file):
    raw_elves_list = []
    with open(file, "r") as txt_file:
        for row in txt_file:
            if row != "\n":
                row = row.strip("\n")
                raw_elves_list.append(row)
            else:
                raw_elves_list.append("---")
    converting_string = ""
    for calorie in raw_elves_list:
        if calorie != "---":
           converting_string = converting_string + calorie + ","
        else:
            converting_string = converting_string + calorie
    list_from_string = converting_string.split("---")
    elve_list = []
    for elve in list_from_string:
        elve.rstrip(",")
        elv_calories = elve.split(",")
        elve_list.append(elv_calories)
    return elve_list

if __name__ == "__main__":
    main()