from Validation import validation_check


def round_of_16_file_parser(file_path, group_predictions):
    predictions = {}
    with open(file_path, "r") as round_of_16, open("Rezultati osmine finala.txt", "r") as results:
        row_number = 0
        key_name = ""
        first_country = ""
        winner = ""

        for file_1, file_2 in zip(round_of_16, results):
            if row_number % 4 == 0:
                key_name = file_1[:2] + file_1[5:-1]
            if row_number % 4 == 2:
                first_country = file_1[len(group_predictions["Group " + key_name[0]][0]) +
                                       len(group_predictions["Group " + key_name[2]][1]) + 8:-1]
                winner = file_2[len(group_predictions["Group " + key_name[0]][0]) +
                                len(group_predictions["Group " + key_name[2]][1]) + 8:-1]

                if file_1[-1] != "\n":
                    first_country += file_1[-1]
                validation_check(first_country)
                if file_2[-1] != "\n":
                    winner += file_2[-1]
                validation_check(winner)
                # Kako napraviti?
                if group_predictions["Group " + key_name[0]][0] == first_country:
                    second_country = group_predictions["Group " + key_name[2]][1]
                else:
                    second_country = group_predictions["Group " + key_name[0]][0]
                validation_check(second_country)

                if group_predictions["Group " + key_name[0]][0] == winner:
                    loser = group_predictions["Group " + key_name[2]][1]
                else:
                    loser = group_predictions["Group " + key_name[0]][0]
                validation_check(loser)

                points = 0
                if first_country == winner or second_country == winner:
                    points += 1
                if second_country == loser or first_country == loser:
                    points += 1

                predictions[key_name] = (winner, loser, points)
            row_number += 1

    return predictions
