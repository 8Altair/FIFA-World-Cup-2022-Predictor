def validation_check(country):
    countries = ("Ecuador", "Netherlands", "Qatar", "Senegal", "England", "Iran", "USA", "Wales",
                 "Argentina", "Mexico", "Poland", "Saudi Arabia", "Australia", "Denmark", "France", "Tunisia",
                 "Costa Rica", "Germany", "Japan", "Spain", "Belgium", "Canada", "Croatia", "Morocco",
                 "Brasil", "Cameroon", "Serbia", "Switzerland", "Ghana", "Portugal", "South Korea", "Uruguay")

    if country not in countries:
        print("Invalid country given:", country)
        exit(1)
