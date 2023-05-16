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
        winner = ""

        for file_1, file_2 in zip(group_stage, results):
            if row_number % 5 == 0:
                key_part_two = chr(ord(key_part_two) + 1)
                group_name = key_part_one + key_part_two
            if row_number % 5 == 2:
                first_country = file_1[3:-1]
                winner = file_2[3:-1]
            if row_number % 5 == 3:
                second_country = file_1[3:-1]
                runner_up = file_2[3:-1]
                if file_1[-1] != "\n":
                    second_country += file_1[-1]
                    runner_up += file_2[-1]

                validation_check(group_name, first_country, second_country)
                validation_check(group_name, winner, runner_up)

                points = 0
                if first_country == winner:
                    points += 1
                    if second_country == runner_up:
                        points += 2
                elif second_country == winner:
                    points += 1
                    if first_country == runner_up:
                        points += 1
                elif first_country == runner_up or second_country == runner_up:
                    points += 1

                predictions[group_name] = (first_country, second_country, points)
            row_number += 1

    return predictions
