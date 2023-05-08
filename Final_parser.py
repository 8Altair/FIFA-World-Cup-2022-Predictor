from Validation import validation_check


def final_file_parser(file_path, semi_finals_prediction):
    with open(file_path, "r") as final:
        row = final.readline()
        key_name = row[:16] + row[19:-1]
        row = final.readline()
        row = final.readline()
        winner_prediction = row[len(semi_finals_prediction[key_name[:16]][0]) +
                                len(semi_finals_prediction[key_name[16:]][0]) + 8:-1]
        winner_prediction += row[-1]

    validation_check(winner_prediction)
    if semi_finals_prediction[key_name[:16]][0] == winner_prediction:
        runner_up = semi_finals_prediction[key_name[16:]][0]
    else:
        runner_up = semi_finals_prediction[key_name[:16]][0]
    validation_check(runner_up)

    return winner_prediction, runner_up
