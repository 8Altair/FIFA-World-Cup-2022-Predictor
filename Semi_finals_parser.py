from Validation import validation_check


def semi_finals_file_parser(text, quarter_finals_predictions):
    predictions = {}
    with open(text, "r") as semi_finals:
        row_number = 0
        key = ""
        for row in semi_finals:
            if row_number % 4 == 0:
                key = row[:8] + row[11:-1]
            if row_number % 4 == 2:
                winner = row[len(quarter_finals_predictions[key[:8]][0]) +
                             len(quarter_finals_predictions[key[8:]][0]) + 8:-1]

                if row[-1] != "\n":
                    winner += row[-1]
                winner = winner.strip()
                validation_check(winner)

                runner_up = ""
                if quarter_finals_predictions[key[:8]][0] == winner:
                    runner_up = quarter_finals_predictions[key[8:]][0]
                else:
                    runner_up = quarter_finals_predictions[key[:8]][0]
                validation_check(runner_up)
                predictions[key] = (winner, runner_up)

            row_number += 1

    return predictions
