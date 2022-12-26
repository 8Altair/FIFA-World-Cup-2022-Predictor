from Validation import validation_check


def quarter_finals_file_parser(text, round_of_16_predictions):
    predictions = {}
    with open(text, "r") as quarter_finals:
        row_number = 0
        key = ""
        for row in quarter_finals:
            if row_number % 4 == 0:
                key = row[:4] + row[7:-1]
            if row_number % 4 == 2:
                winner = row[len(round_of_16_predictions[key[:4]][0]) +
                             len(round_of_16_predictions[key[4:]][0]) + 8:-1]

                if row[-1] != "\n":
                    winner += row[-1]
                validation_check(winner)

                runner_up = ""
                if round_of_16_predictions[key[:4]][0] == winner:
                    runner_up = round_of_16_predictions[key[4:]][0]
                else:
                    runner_up = round_of_16_predictions[key[:4]][0]
                validation_check(runner_up)
                predictions[key] = (winner, runner_up)

            row_number += 1

    return predictions
