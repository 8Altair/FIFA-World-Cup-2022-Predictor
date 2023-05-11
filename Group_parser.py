def validation_check(group, country_1, country_2):
    groups = {"Group A": ("Ecuador", "Netherlands", "Qatar", "Senegal"),
              "Group B": ("England", "Iran", "USA", "Wales"),
              "Group C": ("Argentina", "Mexico", "Poland", "Saudi Arabia"),
              "Group D": ("Australia", "Denmark", "France", "Tunisia"),
              "Group E": ("Costa Rica", "Germany", "Japan", "Spain"),
              "Group F": ("Belgium", "Canada", "Croatia", "Morocco"),
              "Group G": ("Brasil", "Cameroon", "Serbia", "Switzerland"),
              "Group H": ("Ghana", "Portugal", "South Korea", "Uruguay")}

    if group in groups:
        ongoing_group = groups[group]
        if country_1 not in ongoing_group or country_2 not in ongoing_group:
            print("Invalid country given!")
            exit(1)
    else:
        print("Invalid group given!")
        exit(-1)


def group_stage_file_parser(file_path):
    predictions = {}
    with open(file_path, "r") as group_stage, open("Rezultati grupe.txt", "r") as results:
        row_number = 0
        key_part_one = "Group "
        key_part_two = chr(ord("A") - 1)
        group_name = ""
        first_country = ""

        for row_1, row_2 in zip(group_stage, results):
            if row_number % 5 == 0:
                key_part_two = chr(ord(key_part_two) + 1)
                group_name = key_part_one + key_part_two
            if row_number % 5 == 2:
                first_country = row_1[3:-1]
            if row_number % 5 == 3:
                second_country = row_1[3:-1]
                if row_1[-1] != "\n":
                    second_country += row_1[-1]
                validation_check(group_name, first_country, second_country)
                predictions[group_name] = (first_country, second_country)
            row_number += 1

    return predictions
