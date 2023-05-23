from Final_parser import final_file_parser as ffp
from Group_parser import group_stage_file_parser as gsfp
from Quarter_finals_parser import quarter_finals_file_parser as qffp
from Round_of_16_parser import round_of_16_file_parser as ro16fp
from Semi_finals_parser import semi_finals_file_parser as sffp

if __name__ == '__main__':
    matrix_of_file_names = (("Dino/Dino - predikcija grupe.txt", "Dino/Dino - predikcija osmine finala.txt",
                             "Dino/Dino - predikcija četvrtine finala.txt", "Dino/Dino - predikcija polufinala.txt",
                             "Dino/Dino - predikcija finala.txt"),
                            ("Faris/Faris - predikcija grupe.txt", "Faris/Faris - predikcija osmine finala.txt",
                             "Faris/Faris - predikcija četvrtine finala.txt", "Faris/Faris - predikcija polufinala.txt",
                             "Faris/Faris - predikcija finala.txt"),
                            ("Kristijan/Kristijan - predikcija grupe.txt",
                             "Kristijan/Kristijan - predikcija osmine finala.txt",
                             "Kristijan/Kristijan - predikcija četvrtine finala.txt",
                             "Kristijan/Kristijan - predikcija polufinala.txt",
                             "Kristijan/Kristijan - predikcija finala.txt"),
                            ("Miran/Miran - predikcija grupe.txt", "Miran/Miran - predikcija osmine finala.txt",
                             "Miran/Miran - predikcija četvrtine finala.txt", "Miran/Miran - predikcija polufinala.txt",
                             "Miran/Miran - predikcija finala.txt"),
                            ("Tin/Tin - predikcija grupe.txt", "Tin/Tin - predikcija osmine finala.txt",
                             "Tin/Tin - predikcija četvrtine finala.txt", "Tin/Tin - predikcija polufinala.txt",
                             "Tin/Tin - predikcija finala.txt"),
                            )

    all_points = []
    for person in matrix_of_file_names:
        points = []
        print(f"\n{person[0][0]}'s prediction:\n")
        group_stage_prediction = gsfp(person[0])
        points.append([p[2] for p in group_stage_prediction.values()])
        # print(group_stage_prediction, points)
        round_of_16_prediction = ro16fp(person[1], group_stage_prediction)
        # print(round_of_16_prediction)
        quarter_finals_prediction = qffp(person[2], round_of_16_prediction)
        # print(quarter_finals_prediction)
        semi_finals_prediction = sffp(person[3], quarter_finals_prediction)
        # print(semi_finals_prediction)
        final_prediction = ffp(person[4], semi_finals_prediction)
        # print(final_prediction)

        all_points.append(points)
