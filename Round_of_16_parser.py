from Validation import validation_check


def round_of_16_file_parser(text, group_predictions):
    predictions = {}
    with open(text, "r") as round_of_16:
        row_number = 0
        key = ""
        for row in round_of_16:
            if row_number % 4 == 0:
                key = row[:2] + row[5:-1]
            if row_number % 4 == 2:
                winner = row[len(group_predictions["Group " + key[0]][0]) +
                             len(group_predictions["Group " + key[2]][1]) + 8:-1]

                if row[-1] != "\n":
                    winner += row[-1]
                validation_check(winner)

                runner_up = ""
                if group_predictions["Group " + key[0]][0] == winner:
                    runner_up = group_predictions["Group " + key[2]][1]
                else:
                    runner_up = group_predictions["Group " + key[0]][0]
                validation_check(runner_up)
                predictions[key] = (winner, runner_up)

            row_number += 1

    return predictions
