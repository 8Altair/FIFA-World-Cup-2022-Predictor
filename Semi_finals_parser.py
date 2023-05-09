from Validation import validation_check


def semi_finals_file_parser(file_path, quarter_finals_predictions):
    predictions = {}
    with open(file_path, "r") as semi_finals:
        row_number = 0
        key_name = ""
        for row in semi_finals:
            if row_number % 4 == 0:
                key_name = row[:8] + row[11:-1]
            if row_number % 4 == 2:
                winner = row[len(quarter_finals_predictions[key_name[:8]][0]) +
                             len(quarter_finals_predictions[key_name[8:]][0]) + 8:-1]

                if row[-1] != "\n":
                    winner += row[-1]
                validation_check(winner)

                if quarter_finals_predictions[key_name[:8]][0] == winner:
                    runner_up = quarter_finals_predictions[key_name[8:]][0]
                else:
                    runner_up = quarter_finals_predictions[key_name[:8]][0]
                validation_check(runner_up)
                predictions[key_name] = (winner, runner_up)

            row_number += 1

    return predictions
