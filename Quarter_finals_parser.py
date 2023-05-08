from Validation import validation_check


def quarter_finals_file_parser(file_path, round_of_16_predictions):
    predictions = {}
    with open(file_path, "r") as quarter_finals:
        row_number = 0
        key_name = ""
        for row in quarter_finals:
            if row_number % 4 == 0:
                key_name = row[:4] + row[7:-1]
            if row_number % 4 == 2:
                winner = row[len(round_of_16_predictions[key_name[:4]][0]) +
                             len(round_of_16_predictions[key_name[4:]][0]) + 8:-1]
                if row[-1] != "\n":
                    winner += row[-1]
                validation_check(winner)

                if round_of_16_predictions[key_name[:4]][0] == winner:
                    runner_up = round_of_16_predictions[key_name[4:]][0]
                else:
                    runner_up = round_of_16_predictions[key_name[:4]][0]
                validation_check(runner_up)
                # predictions[key_name] = (winner, runner_up)
                predictions.update({key_name: (winner, runner_up)})

            row_number += 1

    return predictions
