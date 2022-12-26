from Validation import validation_check


def final_file_parser(text, semi_finals_prediction):
    winner_prediction = ""
    with open(text, "r") as final:
        row = final.readline()
        key = row[:16] + row[19:-1]
        row = final.readline()
        row = final.readline()
        winner_prediction = row[len(semi_finals_prediction[key[:16]][0]) +
                                len(semi_finals_prediction[key[16:]][0]) + 8:-1]
        if row[-1] != "\n":
            winner_prediction += row[-1]

    validation_check(winner_prediction)
    runner_up = ""
    if semi_finals_prediction[key[:16]][0] == winner_prediction:
        runner_up = semi_finals_prediction[key[:16]][0]
    else:
        runner_up = semi_finals_prediction[key[16:]][0]
    validation_check(runner_up)

    return winner_prediction, runner_up
