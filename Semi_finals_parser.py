from Validation import validation_check


def semi_finals_file_parser(file_path, quarter_finals_predictions):
    predictions = {}
    with open(file_path, "r") as semi_finals, open("Rezultati polufinala.txt", "r") as results:
        row_number = 0
        key_name = ""

        for file_1, file_2 in zip(semi_finals, results):
            if row_number % 4 == 0:
                key_name = file_1[:8] + file_1[11:-1]
            if row_number % 4 == 2:
                first_country = file_1[len(quarter_finals_predictions[key_name[:8]][0]) +
                                       len(quarter_finals_predictions[key_name[8:]][0]) + 8:-1]

                row = file_2.split("-->")
                winner = row[-1].strip().strip("\n")

                if file_1[-1] != "\n":
                    first_country += file_1[-1]
                validation_check(first_country)
                validation_check(winner)

                if quarter_finals_predictions[key_name[:8]][0] == first_country:
                    second_country = quarter_finals_predictions[key_name[8:]][0]
                else:
                    second_country = quarter_finals_predictions[key_name[:8]][0]
                validation_check(second_country)

                if row[0].split("v")[0][:-1] == winner:
                    loser = row[0].split("v")[1][1:-1]
                else:
                    loser = row[0].split("v")[0][:-1]
                validation_check(loser)

                points = 0
                if first_country == winner or second_country == winner:
                    points += 1
                if second_country == loser or first_country == loser:
                    points += 1

                predictions[key_name] = (first_country, second_country, points)
            row_number += 1

    return predictions
