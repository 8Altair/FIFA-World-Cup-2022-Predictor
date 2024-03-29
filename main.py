from tabulate import tabulate

from Final_parser import final_file_parser as ffp
from Group_parser import group_stage_file_parser as gsfp
from Quarter_finals_parser import quarter_finals_file_parser as qffp
from Round_of_16_parser import round_of_16_file_parser as ro16fp
from Semi_finals_parser import semi_finals_file_parser as sffp

if __name__ == '__main__':
    matrix_of_file_names = (("Player1/Player1 - group prediction.txt", "Player1/Player1 - round of 16 prediction.txt",
                             "Player1/Player1 - quarter final prediction.txt",
                             "Player1/Player1 - semi final prediction.txt", "Player1/Player1 - final prediction.txt"),
                            ("Player2/Player2 - group prediction.txt", "Player2/Player2 - round of 16 prediction.txt",
                             "Player2/Player2 - quarter final prediction.txt",
                             "Player2/Player2 - semi final prediction.txt",
                             "Player2/Player2 - final prediction.txt"),
                            )

    all_points = []
    for person in matrix_of_file_names:
        points = []
        group_stage_prediction = gsfp(person[0])
        points.append([p[2] for p in group_stage_prediction.values()])

        round_of_16_prediction = ro16fp(person[1], group_stage_prediction)
        points.append([p[2] for p in round_of_16_prediction.values()])

        quarter_finals_prediction = qffp(person[2], round_of_16_prediction)
        points.append([p[2] for p in quarter_finals_prediction.values()])

        semi_finals_prediction = sffp(person[3], quarter_finals_prediction)
        points.append([p[2] for p in semi_finals_prediction.values()])

        final_prediction = ffp(person[4], semi_finals_prediction)
        points.append(final_prediction[2])

        all_points.append(points)

    headers = ["Player", "Stage", "Points in Phase", "Total Points"]
    table = []

    for idx, person in enumerate(matrix_of_file_names):
        name = person[0].split('/')[0]  # Get the player's name
        total_points = sum(
            [sum(p) if isinstance(p, list) else p for p in all_points[idx]])  # Sum of all points earned by the player
        stages = ["Group Stage", "Round of 16", "Quarter Finals", "Semi Finals",
                  "Finals"]  # The stages of the competition

        for i, stage in enumerate(stages):
            if i != len(stages) - 1:
                table.append([name, stage, ", ".join(map(str, all_points[idx][i])), sum(all_points[idx][i])])
            else:
                # For the final stage, the point data is stored as an integer instead of a list
                table.append([name, stage, all_points[idx][i], all_points[idx][i]])

        # Add the total points row
        table.append([name, "Total", "", total_points])

    # Creating a table with headers.
    table_string = tabulate(table, headers, tablefmt="fancy_grid")
    # Open the file in write mode ('w')
    with open("Table.txt", "w", encoding="utf-8") as f:
        # Write the table string to the file
        f.write(table_string)
    print(table_string)  # Print the table
