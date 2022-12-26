def calculator(prediction_0, prediction_1, prediction_2, prediction_3, prediction_4):
    group_stage_countries = {"Group A": ("Netherlands", "Senegal"),
                             "Group B": ("England", "USA"),
                             "Group C": ("Argentina", "Poland"),
                             "Group D": ("France", "Australia"),
                             "Group E": ("Japan", "Spain"),
                             "Group F": ("Morocco", "Croatia"),
                             "Group G": ("Brasil", "Switzerland"),
                             "Group H": ("Portugal", "South Korea")}

    round_of_16_countries = {"A1B2": ("Netherlands", "USA"),
                             "B1A2": ("England", "Senegal"),
                             "C1D2": ("Argentina", "Australia"),
                             "D1C2": ("France", "Poland"),
                             "E1F2": ("Japan", "Croatia"),
                             "F1E2": ("Morocco", "Spain"),
                             "G1H2": ("Brasil", "South Korea"),
                             "H1G2": ("Portugal", "Switzerland")}

    quarter_finals_countries = {"A1B2C1D2": ("Argentina", "Netherlands"),
                                "B1A2D1C2": ("France", "England"),
                                "E1F2G1H2": ("Croatia", "Brasil"),
                                "F1E2H1G2": ("Morocco", "Portugal")}

    semi_finals_countries = {"A1B2C1D2E1F2G1H2": ("Argentina", "Croatia"),
                             "B1A2D1C2F1E2H1G2": ("France", "Morocco")}

    final_countries = {"A1B2C1D2E1F2G1H2B1A2D1C2F1E2H1G2": ("Argentina", "France")}

    group_stage_points = 0
    for i, j in prediction_0.items():
        if j[0] in group_stage_countries[i]:
            group_stage_points += 1
        if j[1] in group_stage_countries[i]:
            group_stage_points += 1
        if j[0] == group_stage_countries[i][0] and j[1] == group_stage_countries[i][1]:
            group_stage_points += 1

    round_of_16_points = 0
    for i, j in prediction_1.items():
        print(prediction_1)
        if j[0] in round_of_16_countries[i]:
            round_of_16_points += 1
        if j[1] in round_of_16_countries[i]:
            round_of_16_points += 1
        if j[0] == round_of_16_countries[i][0]:
            round_of_16_points += 1
    print(round_of_16_points)
    quarter_finals_points = 0
    for i, j in prediction_2.items():
        if j[0] in quarter_finals_countries[i]:
            quarter_finals_points += 1
        if j[0] == quarter_finals_countries[i][0]:
            quarter_finals_points += 1
    print(quarter_finals_points)
    semi_finals_points = 0
    for i, j in prediction_3.items():
        if j[0] in semi_finals_countries[i]:
            semi_finals_points += 1
        if j[0] == semi_finals_countries[i][0]:
            semi_finals_points += 1
    print(semi_finals_points)
    final_points = 0
    if prediction_4["A1B2C1D2E1F2G1H2B1A2D1C2F1E2H1G2"] in final_countries["A1B2C1D2E1F2G1H2B1A2D1C2F1E2H1G2"]:
        final_points += 1
    if prediction_4["A1B2C1D2E1F2G1H2B1A2D1C2F1E2H1G2"] == final_countries[["A1B2C1D2E1F2G1H2B1A2D1C2F1E2H1G2"]]:
        final_points += 1

    return group_stage_points, round_of_16_points, quarter_finals_points, semi_finals_points, final_points
