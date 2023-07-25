from Validation import validation_check


def final_file_parser(file_path, semi_finals_prediction):
    with open(file_path, "r") as final, open("Results of the final.txt", "r") as results:
        file_1 = final.readline()
        file_2 = results.readline()
        key_name = file_1[:16] + file_1[19:-1]
        file_1 = final.readline()
        file_2 = results.readline()
        file_1 = final.readline()
        file_2 = results.readline()

        first_country = file_1[len(semi_finals_prediction[key_name[:16]][0]) +
                               len(semi_finals_prediction[key_name[16:]][0]) + 8:-1]

        first_country += file_1[-1]
        row = file_2.split("-->")
        winner = row[-1].strip().strip("\n")
        validation_check(first_country)
        validation_check(winner)

    if semi_finals_prediction[key_name[:16]][0] == first_country:
        second_country = semi_finals_prediction[key_name[16:]][0]
    else:
        second_country = semi_finals_prediction[key_name[:16]][0]
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

    return first_country, second_country, points
